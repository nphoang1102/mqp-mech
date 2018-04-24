# MQP Yale's Open Hand Iteration 0

The files under folder _ReflexOne Finger_ is assembly of finger model of Reflex One (source from **_RightHand Robotics_**). This model is also used for subsequent iterations for interference check.

The files in this folder are:
- Motor models: AX12 (with removed back cover) and XL320.
- Mounting models for motors.
- Gear models: to create new gear models with different dimension, make a copy of _Gear.SLDPRT_ and modify to desired dimension.
- Base models for hand: top plate and bottom plate.
- Assembly test models:
  - Model to verify position of gears and motors.
  - Model of AX12 motor with pulley attached.
  - Model of full assembly to check interference.
- Python script:
  - To create list of gear dimensions and related torque reduction ratio then export to _Gear Measurements.xlsx_.
  - May use database software to find desired torque reduction ratio with related gear dimensions by importing data from _Gear Measurements.xlsx_.

The purpose of iteration 0:
- Test the mechanism: gear train.
- Verify how well the 3D printed parts assembled together.
- Verify how well the details of parts were printed.

Everything in this folder requires SolidWork 2018, Microsoft Excel, and Word Editor (or PyCharm for the Python script) to open and view.
