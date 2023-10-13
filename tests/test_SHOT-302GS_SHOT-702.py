# add the parent directory of the current file to the Python module
import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the required module    JP:  必要なモジュール・インポート
from SIGMAKOKI.SK_SHOT import StageControlShot

# Function to get the stage position by axis in mm          JP: 各軸の位置（mm単位）を取得する関数
def getPosition(axis, timeout=10): # timeout 10second
    start_time = time.time()
    while Controller.IsBusy and (time.time() - start_time) < timeout:
        position = Controller.GetPositionMillimeter(axis)  # Get the position in millimeters
        print(f"StageNo {axis} , {position}")  # Print the position
        Controller.UpdateStatus()

    if not Controller.IsBusy:
        position = Controller.GetPositionMillimeter(axis)
        print(f"StageNo {axis} , {position}")
    else:
        print("Timeout reached. Exiting loop.")

# Function to get positions of all stages in mm             JP: すべてのステージの位置（mm単位）を取得する関数
def getAllPosition(timeout=10): # timeout 10second
    start_time = time.time()
    while Controller.IsBusy and (time.time() - start_time) < timeout:
        positions = [Controller.GetPositionMillimeter(i) for i in range(1, Controller.AxisNum + 1)]  # Get positions for all axes
        for i, position in enumerate(positions, start=1):
            print(f"StageNo {i} , {position}")
        Controller.UpdateStatus()

    if not Controller.IsBusy:
        positions = [Controller.GetPositionMillimeter(i) for i in range(1, Controller.AxisNum + 1)]
        for i, position in enumerate(positions, start=1):
            print(f"StageNo {i} , {position}")
    else:
        print("Timeout reached. Exiting loop.")

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

    # Return mechnical origin for all axis   JP: すべての軸の機械原点に戻る
    if Controller.ReturnMechanicalOriginAll():
        if Controller.UpdateStatus():
            getAllPosition()

    print(Controller.LastErrorMessage)

    # linear interpolation axis 1, axis 2    JP: 軸1および軸2の線形補間
    if Controller.LinearInterpolationMillimeter(2, 2):
        if Controller.UpdateStatus():
            getAllPosition()

    speed = [0, 0]
    for i in range(2):
        speed[i] = Controller.GetSpeedMillimeter(i+1)  # Get speed for each axis JP: # 各軸の速度を取得
    print(speed)

    # Absolute drive for axis 1   JP: 軸1の絶対移動
    for i in range(20):
        Controller.AbsoluteDriveSingleMillimeter(1, 1 + i * 1)
        Controller.UpdateStatus()
        getPosition(1)

    # Absolute drive for axis 2    JP: 軸2の絶対移動
    for i in range(20):
        Controller.AbsoluteDriveSingleMillimeter(2, 1 + i * 1)
        Controller.UpdateStatus()
        getPosition(2)

    # Relative drive for axis 1    JP: 軸1の相対移動
    for i in range(5):
        Controller.RelativeDriveSingleMicrometer(1, -2000)
        Controller.UpdateStatus()
        getPosition(1)

    # Relative drive for axis 2    JP: 軸2の相対移動
    for i in range(5):
        Controller.RelativeDriveSingleMicrometer(2, -2000)
        Controller.UpdateStatus()
        getPosition(2)

    # Absolute Abs for axis 2      JP: 軸2の絶対移動
    Controller.AbsoluteDriveSinglePulse(2, 1000)    
    Controller.UpdateStatus()
    getPosition(2)
    print(Controller.LastErrorMessage)

    # retrun logical for all axis  JP: すべての軸の論理原点に戻る
    Controller.ReturnLogicalOriginAll()
    Controller.UpdateStatus()
    getAllPosition()

    # Accessing private variable (mangling) and public properties
    print(Controller._StageControlShot__last_error_message)
    print(Controller.LastErrorMessage)

    print("Program End")