# Qtest-Python
Qtest Python Version

# Installation
For quick environmental configuration, we recommend installing Anaconda on your machine. The Anaconda installation can be found [Conda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

Mac OS and Linux: After successful installation of Anaconda, open the terminal, navigate to Qtest folder and run:
```
conda env create --file environment.yml
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


## Coordinate Section
### Add Base coordinates
- Automatic generation
  - Click 'Auto', enter the number of gamble in the pop-up window
  - Generated coordinates are shown in the column 'Coordinate'
- Load from file
  - Click 'Load', select the file (*.csv, *.excel)
  - Coordinates are shown in the column 'Coordinate' and the number of coordinate is shown in the 'Number of Coordinates' box
- Add coordinate one by one
  - Put the number of coordinates in the 'Number of Coordinates' box by putting number directly or using spin 
  - Check 'Set' box, the empty boxes are shown under the column '1'
  - You can now put the coordinate name by editing the boxes directly

### Add/Delete coordinates
- Add additional coordinate by 'Add' button
- Delete coordinate by 'Delete' button

### Lock coordinates
- After the edition is done, check the 'lock' box
- After locking the coordinate, the number of coordinates is used for following operations
- The number of coordinates cannot be modified unless you click 'clear' to reset it to zero

### Save coordinates
- Click 'Save' button and select the target path to store the coordinates shown in the main window
- Please save the coordinates before checking 'Lock'. Otherwise, nan value is stored


## Theory Section
### Add Base Theory
- Vertex Mode
  - Check 'Vertex' box, and you will see the 'Coordinates' above the grey column
  - Click 'Add' to add columns. The first row is used for theory name, and following rows are for the value (0/1)
  - You can also click 'Auto' and select 0 or 1 for each vertex
  - Click 'Check' to make sure all the valus are between 0 and 1. (not neccessary for the other two mode)
  
- Intensity Mode
  - Check 'Intensity' box, and you will see the 'instance' above the grey column
  - Click 'Add' to add columns. The first row is used for theory name, and following rows are for the intensity (not limited to [0,1]).
  - Click 'Calculate Intensity Order' button, you will see the coordinates are ordered by their intensity value in the right window
  
- Alternatives Mode
  - Check 'Alternative' box and the coordinates are ordered
  - Click 'Begin' to input a new inequation
  - Click 'Add to Left' or 'Add to Right' to add probability to left/right side
  - Click 'End' to see the inequation in right window 
  
- Load from File
  - Vertex Mode and Intensity Mode support 'Load' from files directly. But you can only load it before clicking 'Lock'

### Add/Delete theory
- Click the 'Add' button for a new column and put your data
- Click the column you want to delete but make sure the column is not empty before deleting it
  
### Lock theories
- Click the 'Lock' button, and you will see the theory names in the grey row

### Save theories
- Click 'Save' button and select the target path to store the theory shown in the right window
- Please save the theory before checking 'Lock'. Otherwise, nan value is stored

