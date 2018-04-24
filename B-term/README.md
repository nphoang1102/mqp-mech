# MQP Yale's Open Hand Iteration 1 & 2

###### ReflexOne Finger
The file in this folder is assembly of finger model of Reflex One (source from *_RightHand Robotics_*). 

###### Prototype 1
The files in this folder are for iteration 1 model: 
  - Change in close distance between two front fingers.
  - Introduce new gear type - two stage gear, to reduce number of gears thus reduce total base size.

The files are:
  - Motor models: AX12 (with removed back cover) and XL320.
  - Mounting models for motors.
  - Gear models.
  - Base models for hand: top plate and bottom plate.
  - Assembly test models: 
    - Model to verify position of gears and motors.
    - Model of AX12 motor with pulley attached.
    - Model of full assembly to check interference.
  - Excel file of ratio calculations generated from Python script in A-term folder.
    - May use database software to find desired torque reduction ratio with related gear dimensions by importing data from _Ratio Calculation.xlsx_.
  - Archive file of STL files for 3D printing.

The purpose of iteration 1:
  - Test the new design of two front finger gears with controlled glove
  
###### Prototype 1 Fixes (Not Prototype 2 Yet)
The files in this folder are fixes for iteration 1 model to make it performs better and smoother.
The files are the same as in _Prototype 1_ folder with adjusted changes in each file.

###### Prototype 2
The files in this folder are for iteration 2 model:
  - Change in distance of two front fingers to avoid interference of two finger knuckles.
  - Change in base shape for aesthetic purpose.

The file types are the same as in _Prototype 1_ folder with addition of a separated folder for STL files.
The file types are re-named for searching purpose:
  - *gear_A*: types of gear.
  - *mount_A*: types of mount.
  - *base_A*: types of base.
  - *test_A*: types of testing models.

Everything in this folder requires SolidWork 2018, Microsoft Excel, and Word Editor (or PyCharm for the Python script) to open and view.
