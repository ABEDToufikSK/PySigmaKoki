# SIGMAKOKI Controller Python Library

Welcome to the SIGMAKOKI Controller Python Library, designed to empower developers with a powerful Python interface for controlling SIGMAKOKI stages and controllers using pySerial. This library has been meticulously crafted to cater to a wide range of applications, including measurement systems, robotics, and beyond. With support for control modes (SHOT, HIT & FC), diverse stage types (linear, rotation & gonio), precision division settings, and units (nanometer, micrometer, millimeter & degree), along with comprehensive status monitoring and stage stroke management, you'll find everything you need to take control of your SIGMAKOKI equipment.

## Features

- **Control Modes**: This library covers all control modes, including SHOT, HIT, and FC, allowing you to choose the mode that suits your application.

- **Stage Types**: It supports various stage types, including linear, rotation, and gonio stages.

- **Division Settings**: You can configure the division settings to achieve precise control of your stages.

- **Units**: Control your stages with different units such as nanometer, micrometer, millimeter, and degree, ensuring flexibility in your applications.

- **Status Monitoring**: Easily monitor the status of your stages, ensuring smooth operation and diagnostics.

- **Stage Strokes**: This library provides support for stage strokes, enabling you to set and manage stage limits effectively.

- **More**

## Installation

To install the SIGMAKOKI Controller Python Library, you can use pip:

```bash
pip install sigmakoki-controller
```

## Controller/Stage model

To begin exploring the library's capabilities, refer to our documentation and sample code examples.
TODO

## Usage

Here's a basic example of how to use this library to control a SIGMAKOKI stage:

- **Controller**: SHOT-304GS
- **Stage**: XYStage HPS60-20X  

```python
# Import the required module
from SIGMAKOKI.SK_SHOT import StageControlShot

# Function to get the stage position by axis in mm
def getPosition(axis):
    while con.IsBusy == True:
        position = con.GetPositionMillimeter(axis)  # Get the position in millimeters
        print(f"StageNo {axis} , {position}")  # Print the position
        con.UpdateStatus()
        if con.IsBusy == False:
            position = con.GetPositionMillimeter(axis)
            print(f"StageNo {axis} , {position}")# Print the position
            break

# Function to get positions of all stages in mm
def getAllPosition():
    while con.IsBusy == True:
        for i in range(1, con.AxisNum + 1):
            position = con.GetPositionMillimeter(i)  # Get the position for each axis
            print(f"StageNo {i} , {position}")# Print the position
        con.UpdateStatus()
        if con.IsBusy == False:
            for i in range(1, con.AxisNum + 1):
                position = con.GetPositionMillimeter(i)
                print(f"StageNo {i} , {position}")# Print the position
            break

if __name__ == "__main__":
    port = 'com8'  # Define the COM port, adjust as needed

    # Create an instance of StageControlShot with the specified parameters
    con = StageControlShot(port, "SHOT-304GS", StageControlShot.BaudRateclass.BR_9600)

    # set full step for axis 1 & 2
    con.SetFullStepInMicrometer(1, 2)
    con.SetFullStepInMicrometer(2, 2)
    con.SetResolution(1, 2)
    con.SetResolution(2, 2)

    # Set speed and acceleration for all stages
    value = [5, 5, 5, 4]
    acc = [50, 50, 50, 50]
    con.SetSpeedAllMillimeter(value, acc)

    # Return mechnical origin for all axis   
    con.ReturnMechanicalOriginAll()
    con.UpdateStatus()
    getAllPosition()

    # linear interpolation axis 1, axis 2 
    con.LinearInterpolationMillimeter(2, 2)
    con.UpdateStatus()
    getAllPosition()

    speed = [0, 0, 0, 0]
    for i in range(4):
        speed[i] = con.GetSpeedMillimeter(i+1)  # Get speed for each axis
    print(speed)

    # Absolute drive for axis 1
    for i in range(20):
        con.AbsoluteDriveSingleMillimeter(1, 1 + i * 1)
        con.UpdateStatus()
        getPosition(1)

    # Absolute drive for axis 2
    for i in range(20):
        con.AbsoluteDriveSingleMillimeter(2, 1 + i * 1)
        con.UpdateStatus()
        getPosition(2)

    # Relative drive for axis 1
    for i in range(5):
        con.RelativeDriveSingleMicrometer(1, -2000)
        con.UpdateStatus()
        getPosition(1)

    # Relative drive for axis 2
    for i in range(5):
        con.RelativeDriveSingleMicrometer(2, -2000)
        con.UpdateStatus()
        getPosition(2)

    # Absolute Abs for axis 2
    con.AbsoluteDriveSinglePulse(2, 1000)    
    con.UpdateStatus()
    getPosition(2)

    # retrun logical for all axis
    con.ReturnLogicalOriginAll()
    con.UpdateStatus()
    getAllPosition()

    # Accessing private variable (mangling) and public properties
    print(con._StageControlShot__last_error_message)
    print(con.LastErrorMessage)

    print("Program End")
```

We're thrilled to have you on board and look forward to seeing how you'll leverage the SIGMAKOKI Controller Python Library for your projects. Enjoy exploring the world of precision control and measurement!

If you have any questions, feedback, or contributions, please don't hesitate to reach out to us. Your insights and ideas are invaluable as we continue to enhance this library for the developer community.

## SIGMAKOKI | Precision in Motion

Visit our website: <www.sigmakoki.com>
