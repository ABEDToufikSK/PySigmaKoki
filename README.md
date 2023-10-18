# SIGMAKOKI Controller Python Library

## Summary

Welcome to the SIGMAKOKI Controller Python Library, designed to empower developers with a powerful Python interface for controlling SIGMAKOKI stages and controllers using [pySerial](https://github.com/pyserial/pyserial). This library has been meticulously crafted to cater to a wide range of applications, including measurement systems, robotics, and beyond. With support for control modes (SHOT, HIT, FC), diverse stage types (linear, rotation, gonio), precision division settings, and units (nanometer, micrometer, millimeter, degree), along with comprehensive status monitoring and stage stroke management, you'll find everything you need to take control of your SIGMAKOKI equipment.

## Features

- **Control Modes**: This library covers all control modes, including SHOT, HIT, and FC, allowing you to choose the mode that suits your application.

- **Stage Types**: It supports various stage types, including linear, rotation, and gonio stages.

- **Division Settings**: You have the ability to finely tune division settings, enabling precise control of your stages to meet your exact requirements.

- **Units**: Control your stages with different units such as nanometer, micrometer, millimeter, and degree, ensuring flexibility in your applications.

- **Status Monitoring**: Easily monitor the status of your stages, ensuring smooth operation and diagnostics.

- **Stage Strokes**: This library provides support for stage strokes, enabling you to set and manage stage limits effectively.

- **More**: Explore additional features, including software limits, jog commands, and more, by delving into the library for comprehensive details.  

## Installation

To install the SIGMAKOKI Controller Python Library, you can use pip:

```bash
pip install sigmakoki-controller
```

<div style="page-break-before: always;"
></div>

## Controller/Stage model

| [SHOT-302/304GS](https://jp.optosigma.com/en_jp/shot-302gs.html) | [SHOT-702H](https://jp.optosigma.com/en_jp/shot-702h.html) | [SHRC-203](https://jp.optosigma.com/en_jp/shrc-203.html) |[GIP-101](https://jp.optosigma.com/en_jp/gip-101b.html)|
| :-: | :-: | :-: | :-: |
| Controller | Controller | Controller | Controller |
| ![img1](Materials/SHOT-302.jpg) | ![img2](Materials/shot-702h.jpg) | ![img3](Materials/shrc-203.jpg) | ![img4](Materials/gip-101.jpg) |
| [[USER-M]](https://jp.optosigma.com/html/en_jp/software/motorize/manual_en/SHOT-302GS_304GS.pdf) | [[USER-M]](https://jp.optosigma.com/html/en_jp/software/motorize/manual_en/SHOT-702_EN.pdf) |[[USER-M]](https://jp.optosigma.com/html/en/page_pdf/SHRC-203.pdf) |[USER-M](https://jp.optosigma.com/html/en_jp/software/motorize/manual_en/GIP-101_en.pdf) |
| Linear Stages | Rotation Stages | Goniometer Stages | With Scale |
| ![img1](Materials/OSMSseries.jpg) | ![img2](Materials/OSMS-YAWseries.jpg) | ![img3](Materials/OSMS-gonio.jpg) | ![img4](Materials/OSMS(CS)20-(X).jpg) |
| [[GUIDE]](https://jp.optosigma.com/en_jp/motorized-stages/stepping-motor-stages/linear-motorized-stages.html) | [[GUIDE]](https://jp.optosigma.com/en_jp/motorized-stages/stepping-motor-stages/rotation-motorized-stages.html) |[[GUIDE]](https://jp.optosigma.com/en_jp/motorized-stages/stepping-motor-stages/goniometer-motorized-stages.html) |[Guide](https://jp.optosigma.com/en_jp/motorized-stages/stepping-motor-stages/with-scale.html) |

To begin exploring the library's capabilities, refer to our documentation and sample code examples.

- **Sample code SHOT-304GS**: [How to use this library to control SHOT-304GS](#shot-304gs-controller-usage)

- **Sample code SHOT-302GS_SHOT-702**:[How to use this library to control SHOT-302GS](#shot-302gs_shot-702-controllers-usage)

### **Note**

Before using the SK library, there are several essential considerations.

- Configure the right parameters for your stages to ensure precise program management.
- Each stage comes with specific motor attributes, including step angle and pulses per rotation.
- Consider the mechanical properties, such as lead screw and pitch, for accurate control.
- Some stages, like OSMS-ZF, involve gearing details that you should be aware of.
- Take into account division specifications, including resolution (Full/Half), to fine-tune your control settings.
- A deep understanding of these stage details will enable you to write more effective code and achieve precise control over Sigma Koki Controllers and Stages.

<div style="page-break-before: always;"
></div>

### **SHOT-304GS Controller Usage**

Here's a basic example of how to use this library to control a SIGMAKOKI stage:

- **Controller**: SHOT-304GS
- **Stage**: XYStage HPS60-20X  

```python
import os, sys
import time
# add the parent directory of the current file to the Python module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the required module    JP:  必要なモジュール・インポート  
from SIGMAKOKI.SK_SHOT import StageControlShot

if __name__ == "__main__":
    port = 'com8'  # Define the COM port, adjust as needed

    # Create an instance of StageControlShot with the specified parameters 
    # JP:指定されたパラメータでStageControlShotのインスタンスを作成
    Controlleur = StageControlShot(port, "SHOT-304GS", StageControlShot.BaudRateClass.BR_9600)
    
    if Controlleur.IsComConnected():
        print("Serial Comport is Connected")
    else:
        print(Controlleur.LastErrorMessage+ " [Serial Comport is Not Open]")
        sys.exit()

    # set full step for axis 1 & 2   JP: 軸1および軸2の線形補間
    Controlleur.SetFullStepInMicrometer(1, 2)
    Controlleur.SetFullStepInMicrometer(2, 2)
    Controlleur.SetResolution(1, 2)
    Controlleur.SetResolution(2, 2)

    # Set speed and acceleration for all stages  JP: すべてのステージの速度と加速度を設定
    value = [5, 5, 5, 4]
    acc = [50, 50, 50, 50]
    Controlleur.SetSpeedAllMillimeter(value, acc)
```

>**You can find further continuation within the program by exploring** [Shot-304GS](tests/test_SHOT-304GS.py)

<div style="page-break-before: always;"
></div>

### **SHOT-302GS_SHOT-702 Controllers Usage**

Here's a basic example of how to use this library to control a SIGMAKOKI stage:

- **Controller**: SHOT-302GS
- **Stage**: XYStage HPS60-20X  

```python
import os, sys
import time
# add the parent directory of the current file to the Python module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the required module    JP:  必要なモジュール・インポート
from SIGMAKOKI.SK_SHOT import StageControlShot

if __name__ == "__main__":
    port = 'com8'  # Define the COM port, adjust as needed

    # Create an instance of StageControlShot with the specified parameters 
    # JP:指定されたパラメータでStageControlShotのインスタンスを作成
    Controller = StageControlShot(port, "SHOT-702 / SHOT-302GS", StageControlShot.BaudRateClass.BR_9600)#please set to BaudRateClass.BR_38400 in case of SHOT-702 
    
    if Controller.IsComConnected():
        print("Serial Comport is Connected")
    else:
        print(Controller.LastErrorMessage+ " [Serial Comport is Not Open]")
        sys.exit()

    # set full step for axis 1 & 2   JP: 軸1および軸2の線形補間
    Controller.SetFullStepInMicrometer(1, 2)
    Controller.SetFullStepInMicrometer(2, 2)
    Controller.SetResolution(1, 2)
    Controller.SetResolution(2, 2)

    # Set speed and acceleration for all stages  JP: すべてのステージの速度と加速度を設定
    value = [5, 5]
    acc = [50, 50]
    Controller.SetSpeedAllMillimeter(value, acc)
```

>**You can find further continuation within the program by exploring** [Shot-302GS](tests/test_SHOT-302GS_SHOT-702.py)

<div style="page-break-before: always;"
></div>

## SIGMAKOKI | Precision in Motion

We're thrilled to have you on board and look forward to seeing how you'll leverage the SIGMAKOKI Controller Python Library for your projects. Enjoy exploring the world of precision control and measurement!

If you have any questions, feedback, or contributions, please don't hesitate to reach out to us. Your insights and ideas are invaluable as we continue to enhance this library for the developer community.

Visit our website: <www.sigmakoki.com>
