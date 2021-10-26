# MULT_CON multinomial model with linear inequality constraints
#    [X,L,W,P,MSG] = mult_con(M,A,B,N,RSTATE,OPT_TOL)
#
#   M contains the data. It has to be a cell array, where each cell 
#   corresponds to a multinomial random variable. Each cell is a row vector
#   containing the count for each category in the corresponding variable.
#   Example:
#      M = { [12,8]; [10,5,15] };
#   creates a binomial and a trinomial variable, with 20 and 30 observations
#   respectively.
#   Note that each vector of length k defines (k-1) parameters for the
#   corresponding distribution.
#   [Python] Use 2D array instead M

#   A is a matrix and B is a column vector, specifying the inequality
#   constraints in the form of AX <= B.
#   Note that X is formed by concatenating each parameter vector 
#   in the order specified in M.
#   [Python] A, B 2-D array

#   N (optional) is the number of iterations for the Silvapulle algorithm.
#   The default value is 10,000.
#
#   RSTATE is optional. If specified, the random number generators will
#   be set to the given value (a scalar non-negative integer). This can
#   be used to create repeatable results.
#   
#   OPT_TOL (optional) is a (positive scalar) upper bound for first-order
#   optimality measure when finding the maximum likelihood estimator. 
#   Smaller OPT_TOL ensures more accurate estimator but may not be
#   attained. The default value of 1e-10 should work fine.
#
#   PROGRESS is optional. It should be a non-empty text string for progress bar.
#
# Outputs:
#   
#   X is the maximum likelihood solution (within the feasible region).
#   
#   L is the log-likelihood ratio (i.e. the test statistic).
#
#   W is a vector containing the Chi-bar squared weights.
#   
#   P is the p value for the hypothesis test.
#
#   MSG contains warning messages (if any) that have been generated. It is
#   a cell array of strings:
#       'conv' - maximum-likelihood estimator failed to converge
#       'dim'  - non-full rank polytope warning
#       
#
# Example (2 binomials):
#
#       M={ [5,5]; [6,4] }; 
#       A=[1,-1; 1,1; -1,0];
#       B=[0; 1; 0];
#       [X,L,W,P]=mult_con(M,A,B);
#
# Author: Houxiang Ji <hj14@illinois.edu>
# Status: Verified

import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint, Bounds

def get_q(m):
    tol = 1e-6
    n = m.shape[0] # number of data points/rows
    q = []

    for i in range(n):
        row_sum = np.sum(m[i])
        theta = m[i]/row_sum
        if (np.sum(theta>tol) > 0 or np.sum(theta>1-tol) > 0):
            median = np.ones(len(theta)) / len(theta)
            dir = median - theta
            theta = theta + tol * dir/np.linalg.norm(dir)
        q = np.concatenate((q, theta[:-1]))
    return q

def get_equality_constraints(m,q):
    n = m.shape[0]
    p_len = q.shape[0]
    A = np.zeros((n,p_len+n))
    B = np.ones((n,1))
    s_idx = 0

    for i in range(n):
        e_idx = s_idx + len(m[i]) - 2
        A[i][s_idx:e_idx+1] =1 
        A[i][p_len + i] = 1
        s_idx = e_idx + 1
    return A,B

def get_ext_q(m):
    tol = 1e-6
    n = m.shape[0] # number of data points/rows
    q = []
    q2 = np.zeros(n)

    for i in range(n):
        row_sum = np.sum(m[i])
        theta = m[i]/row_sum
        if (np.sum(theta>tol) > 0 or np.sum(theta>1-tol) > 0):
            median = np.ones(len(theta)) / len(theta)
            dir = median - theta
            theta = theta + tol * dir/np.linalg.norm(dir)
        q = np.concatenate((q, theta[:-1]))
        q2[i] = theta[-1]
    
    result = np.concatenate((q,q2))
    
    return result
    # return np.expand_dims(result, axis=0)

# object function to optimize
def costFunc(x, m):
    n = m.shape[0]
    p_len = len(x) - n
    L = 0
    st_idx = 0

    for i in range(n):
        ed_idx = st_idx + len(m[i]) - 2
        param = np.concatenate((x[st_idx:ed_idx+1],x[p_len+i:p_len+i+1]))
        L = L - np.dot(m[i], np.log(param).T)
        st_idx = ed_idx + 1
    res = float(L)
    return res

# def costFunc(x, m):
#     m = m.reshape(10,)
#     res = float(sum(m+x))
#     return res

def neglog_L_fast(x, m):
    n = m.shape[0]
    p_len = len(x) - n
    G = np.zeros_like(x)
    L = 0
    st_idx = 0

    for i in range(n):
        ed_idx = st_idx + len(m[i]) - 2
        param = np.concatenate((x[st_idx:ed_idx+1],x[p_len+i:p_len+i+1]))
        L = L - np.dot(m[i], np.log(param).T)
        G[st_idx:ed_idx+1] = (-1*m[i]/param)[:-1]
        G[p_len+i] = (-1*m[i]/param)[-1]
        st_idx = ed_idx + 1
    return L,G


# keep the same interface, ignore random number generator setting
# return value: x, L, w, p
def mult_con(m,A,b,N=10000,rstate=0,opt_tolerance=1e-10,progress=[]):
    n_done = np.array([0,0])
    
    # test trivial condition
    # q (1, dimension)
    q = get_q(m)
    # careful about the logic here
    if(not np.any(np.dot(A,q.T) > b)):
        print('All inequalities satisfied')
        x = q
        L = 0
        w = []
        p = 1
        return x,L,w,p

    eA, eB = get_equality_constraints(m,q)
    print(eA.shape, eB.shape)
    tol = 1e-10
    tolfun = opt_tolerance
    x = get_ext_q(m)
    
    # x = fmincon(fun,x0,A,b,Aeq,beq,lb,ub,nonlcon,options)
    # MATLAB is efficient (fmincon function) but the problem needs to be differentiable
    # https://github.com/byuflowlab/pyfmincon
    # https://github.com/ewiger/mlab
    # object function: neglog_L_fast(x,m)
    # nonlinear constraint: Ax <=b, Aeq x = beq, lb<=x<=ub
    
    lb = np.ones_like(x)*1e-6
    ub = np.ones_like(x)*(1-1e-6)
    A = np.concatenate((A, np.zeros((A.shape[0], m.shape[0]))), axis = 1)
    Aeq = eA
    beq = eB.flatten()
    print(A.shape, x.shape, Aeq.shape, beq.shape, lb.shape, ub.shape)

    # constraint1 = NonlinearConstraint(A, lb=np.inf, ub=b)
    constraint2 = LinearConstraint(Aeq, lb=beq, ub=beq)
    # cons = (constraint1, constraint2)
    bounds = Bounds(lb, ub)
    result = minimize(costFunc, x0 = x, args=(m),
                        method='trust-constr',
                        options = {'xtol':tol, 'gtol':tolfun},
                        constraints = constraint2, bounds = bounds, tol = tol)
    print(result)







    