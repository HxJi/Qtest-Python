# Qtest-Python
Qtest Python Version

# Installation
For quick environmental configuration, we recommend installing Anaconda on your machine. The Anaconda installation can be found [Conda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

Mac OS and Linux: After successful installation of Anaconda, open the terminal, navigate to Qtest folder and run:
```
conda env create --file qtest_env.yml
```
The environment configuratioin would take several minutes and after the installation, you can check the environments by run:
```
conda env list
```
Please make sure you can see the environment named qtest. You can set the enviroment name by changing the *qtest_env.yml*. If the enviroment is shown, please run the following instructions to run Qtest.
```
conda activate qtest
python qtest.py
```
