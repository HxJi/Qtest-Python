# Refer to freq_test_super.m file in Qtest-2.1
# FREQ_TEST_SUPER performs theory-level frequentist test for the
# supermajority probability specification.
#    RES=freq_test_super(M,V,LAMBDA,N,RSTATE)
   
#    M is the data matrix, where each row gives the outcome of a binomial
#    test. For example, for a 3-dimensional case, with 20 observations per
#    dimensions, M could be [8,12; 7,13; 11,9]

#    V is a vertex matrix, where each row corresponds to one vertex. The
#    vertex coordinates can be anywhere from 0 to 1. An example set of
#    vertices in 3-dimensional space: [1,0,1; 1,1,0.5; 0.1,0.1,0.1]

#    LAMBDA is the supermajority level. It should be from 0.5 to 1. If
#    LAMBDA is a scalar then all vertices use this same level. Otherwise,
#    LAMBDA can be a vector whose length equals the number of vertices,
#    and each component specifies the level for the corresponding vertex.

#    N (optional) is the number of iterations for the Silvapulle algorithm.
#    The default value is 10,000.

#    RSTATE is optional. If specified, the random number generators will
#    be set to the given value (a scalar non-negative integer). This can
#    be used to create repeatable results. Default: 0.

#    CACHE is optional. It can either be a path name for the cache file, or
#    an existing cache object. If a path name is specified and the file does
#    not exist it will be created as a new cache file.

#  Outputs:

#    RES is a structure containing various test results, including results
#    for individual vertices and theory-level results.
#    Vertex-level results:
#        p: p-value of each vertex
#        p_cached: 1 if cached result is used
#        p_time: computation time (in seconds)
#    Theory-level results:
#        max_p: maximum p-value over all vertices
#        time: overall time (in seconds)
#        params: input parameters for this analysis

# Author: Houxiang Ji <hj14@illinois.edu>
# Status: Not Verified

import time
import numpy as np
from mult_con import mult_con

def freq_test_super(data, vertex, sup, iter=10000, rstate=0):
    start = time.time()
    result = dict()
    vertex_time = []

    dimension = data.shape[0]
    vert_num = vertex.shape[0] # number of vertex
    A = np.concatenate((np.identity(dimension), -1 * np.identity(dimension)), axis = 0)

    # scalar value instead of vector
    if len(sup) == 1:
        sup = np.ones(vert_num) * sup
    
    for i in range(vert_num):
        time_vertex = time.time()
        d = 0.5 * (1-sup[i])
        ex_u = np.maximum(d-vertex[i], 0)
        ex_l = np.maximum(vertex[i]+d-1, 0)
        B1 = np.minimum(vertex[i]+d+ex_u, 1)
        B2 = np.maximum(vertex[i]-d-ex_l, 0) * -1
        B = np.concatenate((B1,B2), axis = 0)
        # disable cache for now
        _,_,_,p = mult_con(data,A,B,iter,rstate)
        vertex_time.append(time.time() - time_vertex)

    # p is the hypothesis test value for 
    result['p_value'] = p
    result['p_max'] = max(p)
    result['runtime'] = time.time() - start
    result['runtime_vertex'] = vertex_time

    return result

m = np.array([[8,12], [7,13], [11,9], [2,18], [5,15]])
v = np.array([[1,0,1,0,1],[1,1,0.5,0,1],[0.1,0.1,0.1,0,1]])
sup = np.array([0.6])

freq_test_super(m,v,sup)





