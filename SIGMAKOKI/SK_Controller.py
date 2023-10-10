import serial

class StageControlBase:
    def __init__(self):
        pass
#region properties

#region Define properties here (use Python's property decorator)
    @property
    def ControllerModel(self):
        pass

    @property
    def AxisNum(self):
        pass

    @property
    def IsBusy(self):
        pass

    @property
    def SendCommand(self):
        pass

    @property
    def RecieveCommand(self):
        pass

    @property
    def StatusLogFlag(self):
        pass

    @property
    def DriveLogFlag(self):
        pass

    @property
    def LastErrorMessage(self):
        pass
#endregion

#region Communication-related properties
    @property
    def PortName(self):
        pass  # COM port name

    @property
    def PortNumber(self):
        pass  # COM port number

    @property
    def BaudRate(self):
        pass  # Baud rate

    @property
    def WriteTimeOut(self):
        pass  # Write timeout

    @property
    def ReadTimeOut(self):
        pass  # Read timeout

    @property
    def DataBits(self):
        pass  # Data bits

    @property
    def Parity(self)-> serial.PARITY_NONE:
        pass  # Parity

    @property
    def StopBits(self)-> serial.STOPBITS_ONE:
        pass  # Stop bits

    @property
    def HandShake(self):
        pass  # Handshake

    @property
    def Delimiter(self):
        pass  # Delimiter

    @property
    def IsOpen(self):
        pass  # COM port state (Open/Close)
#endregion

#endregion

#region methods

#region "Functions for getting/setting properties of axis class"

    def GetPositionPulse(self, axisnum):
        pass  # Get position value in pulses

    def GetPositionNanometer(self, axisnum):
        pass  # Get position value in nanometers

    def GetPositionMicrometer(self, axisnum):
        pass  # Get position value in micrometers

    def GetPositionMillimeter(self, axisnum):
        pass  # Get position value in millimeters

    def GetPositionDegree(self, axisnum):
        pass  # Get position value in degrees

    def GetPulseToNanometer(self, axisnum):
        pass  # Convert pulses to nanometers

    def GetPulseToMicrometer(self, axisnum):
        pass  # Convert pulses to micrometers

    def GetPulseToMillimeter(self, axisnum):
        pass  # Convert pulses to millimeters

    def GetPulseToDegree(self, axisnum):
        pass  # Convert pulses to degrees

    def SetPulseToNanometer(self, axisnum, value):
        pass  # Set pulse-to-nanometer conversion value

    def GetLimitSignal(self, axisnum):
        pass  # Get limit detection signal

    def GetSpeedPulse(self, axisnum):
        pass  # Get speed value in pulses

    def GetSpeedNanometer(self, axisnum):
        pass  # Get speed value in nanometers

    def GetSpeedMicrometer(self, axisnum):
        pass  # Get speed value in micrometers

    # Set speed value in millimeters
    def SetSpeedMillimeter(self, axisnum, value):
        pass

    # Set speed value in degrees
    def SetSpeedDegree(self, axisnum, value):
        pass

    # Get acceleration time in milliseconds
    def GetAccelTime(self, axisnum):
        pass

    # Set acceleration time in milliseconds
    def SetAccelTime(self, axisnum, value):
        pass

    # Get maximum stroke limit in pulses
    def GetStrokeLimitMaxPulse(self, axisnum):
        pass

    # Get maximum stroke limit in nanometers
    def GetStrokeLimitMaxNanometer(self, axisnum):
        pass

    # Get maximum stroke limit in micrometers
    def GetStrokeLimitMaxMicrometer(self, axisnum):
        pass

    # Get maximum stroke limit in millimeters
    def GetStrokeLimitMaxMillimeter(self, axisnum):
        pass

    # Get maximum stroke limit in degrees
    def GetStrokeLimitMaxDegree(self, axisnum):
        pass

    # Set maximum stroke limit in pulses
    def SetStrokeLimitMaxPulse(self, axisnum, value):
        pass

    # Set maximum stroke limit in nanometers
    def SetStrokeLimitMaxNanometer(self, axisnum, value):
        pass

    # Set maximum stroke limit in micrometers
    def SetStrokeLimitMaxMicrometer(self, axisnum, value):
        pass

    # Set maximum stroke limit in millimeters
    def SetStrokeLimitMaxMillimeter(self, axisnum, value):
        pass

    # Set maximum stroke limit in degrees
    def SetStrokeLimitMaxDegree(self, axisnum, value):
        pass

    # Get minimum stroke limit in pulses
    def GetStrokeLimitMinPulse(self, axisnum):
        pass

    # Get minimum stroke limit in nanometers
    def GetStrokeLimitMinNanometer(self, axisnum):
        pass

    # Get minimum stroke limit in micrometers
    def GetStrokeLimitMinMicrometer(self, axisnum):
        pass

    # Get minimum stroke limit in millimeters
    def GetStrokeLimitMinMillimeter(self, axisnum):
        pass

    # Get minimum stroke limit in degrees
    def GetStrokeLimitMinDegree(self, axisnum):
        pass

    # Set minimum stroke limit in pulses
    def SetStrokeLimitMinPulse(self, axisnum, value):
        pass

    # Set minimum stroke limit in nanometers
    def SetStrokeLimitMinNanometer(self, axisnum, value):
        pass

    # Set minimum stroke limit in micrometers
    def SetStrokeLimitMinMicrometer(self, axisnum, value):
        pass

    # Set minimum stroke limit in millimeters
    def SetStrokeLimitMinMillimeter(self, axisnum, value):
        pass

    # Set minimum stroke limit in degrees
    def SetStrokeLimitMinDegree(self, axisnum, value):
        pass

    # Get offset from mechanical origin in pulses
    def GetOffsetMoriginPulse(self, axisnum):
        pass

    # Get offset from mechanical origin in nanometers
    def GetOffsetMoriginNanometer(self, axisnum):
        pass

    # Get offset from mechanical origin in micrometers
    def GetOffsetMoriginMicrometer(self, axisnum):
        pass

    # Get offset from mechanical origin in millimeters
    def GetOffsetMoriginMillimeter(self, axisnum):
        pass

    # Get offset from mechanical origin in degrees
    def GetOffsetMoriginDegree(self, axisnum):
        pass

    # Set offset to mechanical origin in pulses
    def SetOffsetMoriginPulse(self, axisnum, value):
        pass

    # Set offset to mechanical origin in nanometers
    def SetOffsetMoriginNanometer(self, axisnum, value):
        pass

    # Set offset to mechanical origin in micrometers
    def SetOffsetMoriginMicrometer(self, axisnum, value):
        pass

    # Set offset to mechanical origin in millimeters
    def SetOffsetMoriginMillimeter(self, axisnum, value):
        pass

    # Set offset to mechanical origin in degrees
    def SetOffsetMoriginDegree(self, axisnum, value):
        pass
#endregion

#region Define other methods, properties, and fields as needed

    def ConnectCom(self):
        pass

    def OpenSerialPort(self):
        pass

    def CloseSerialPort(self):
        pass
#endregion

#region Functions for Control Commands
    # Get status update
    def UpdateStatus(self):
        pass

    # Get positioning status (Busy/Ready)
    def PositioningStatus(self):
        pass

    # Return to mechanical origin for a single axis
    def ReturnMechanicalOriginSingle(self, axisnum):
        pass

    # Return to mechanical origin for all axes
    def ReturnMechanicalOriginAll(self):
        pass

    # Return to logical origin for a single axis
    def ReturnLogicalOriginSingle(self, axisnum):
        pass

    # Return to logical origin for all axes
    def ReturnLogicalOriginAll(self):
        pass

    # Set logical origin for a single axis
    def SetLogicalOriginSingle(self, axisnum):
        pass

    # Set logical origin for all axes
    def SetLogicalOriginAll(self):
        pass

    # Stop drive for a single axis
    def StopDriveSingle(self, axisnum):
        pass

    # Stop drive for all axes
    def StopDriveAll(self):
        pass

    # Emergency stop
    def EmergencyStop(self):
        pass

    # Absolute drive for a single axis in pulses
    def AbsoluteDriveSinglePulse(self, axisnum, target):
        pass

    # Absolute drive for a single axis in nanometers
    def AbsoluteDriveSingleNanometer(self, axisnum, target):
        pass

    # Absolute drive for a single axis in micrometers
    def AbsoluteDriveSingleMicrometer(self, axisnum, target):
        pass

    # Absolute drive for a single axis in millimeters
    def AbsoluteDriveSingleMillimeter(self, axisnum, target):
        pass

    # Absolute drive for a single axis in degrees
    def AbsoluteDriveSingleDegree(self, axisnum, target):
        pass

    # Absolute drive functions for all axes
    def AbsoluteDriveAllPulse(target):        
        pass

    # Absolute drive for all axes in nanometers.
    def AbsoluteDriveAllNanometer(target):
        pass

    # Absolute drive for all axes in micrometers.
    def AbsoluteDriveAllMicrometer(target):
        pass

    # Absolute drive for all axes in millimeters.
    def AbsoluteDriveAllMillimeter(target):
        pass

    # Absolute drive for all axes in degrees.
    def AbsoluteDriveAllDegree(target):
        pass

    # Relative drive functions for single axis
    def RelativeDriveSinglePulse(axisnum, pitch):
        pass

    # Relative drive for a single axis in nanometers.
    def RelativeDriveSingleNanometer(axisnum, pitch):
       pass

    # Relative drive for a single axis in micrometers.
    def RelativeDriveSingleMicrometer(axisnum, pitch):
        pass

    # Relative drive for a single axis in millimeters.
    def RelativeDriveSingleMillimeter(axisnum, pitch):
        pass

    # Relative drive for a single axis in degrees.
    def RelativeDriveSingleDegree(axisnum, pitch):
        pass

    # Relative drive functions for all axes
    def RelativeDriveAllPulse(pitch):
       pass

    # Relative drive functions for all axes in nanometers
    def RelativeDriveAllNanometer(pitch):
        pass

    # Relative drive functions for all axes in micrometers
    def RelativeDriveAllMicrometer(pitch):        
        pass

    # Relative drive functions for all axes in millimeters
    def RelativeDriveAllMillimeter(pitch):
        pass

    # Relative drive functions for all axes in degrees
    def RelativeDriveAllDegree(pitch):
        pass

    # JOG drive functions for single and all axes
    def JOGDriveSingle(axisnum, plusflag):
        pass

    def JOGDriveAll(plusflag):
        pass

    # Set speed functions for single and all axes
    def SetSpeedSinglePulse(axisnum, value, act):
        pass

    # Set speed for a single axis in nanometers.
    def SetSpeedSingleNanometer(axisnum, value, act):
        pass

    # Set speed for a single axis in micrometers.
    def SetSpeedSingleMicrometer(axisnum, value, act):
        pass

    # Set speed for a single axis in millimeters.
    def SetSpeedSingleMillimeter(axisnum, value, act):
        pass

    # Set speed for a single axis in degrees.
    def SetSpeedSingleDegree(axisnum, value, act):
        pass

    # Set speed for all axes in pulse units.
    def SetSpeedAllPulse(value, act):
        pass

    # Set speed for all axes in nanometers.
    def SetSpeedAllNanometer(value, act):
        pass

    # Set speed for all axes in micrometers.
    def SetSpeedAllMicrometer(value, act):
        pass

    # Set speed for all axes in mm.
    def SetSpeedAllMillimeter(value, act):
        pass

    # Set speed for all axes in degrees.
    def SetSpeedAllDegree(value, act):
        pass

    # Linear interpolation functions for 2 axes with pulses
    def LinearInterpolationPulse(move_x, move_y):
        pass

    # Linear interpolation drive for 2 axes in nanometers.
    def LinearInterpolationNanometer(move_x, move_y):
        pass

    # Linear interpolation drive for 2 axes in micrometers.
    def LinearInterpolationMicrometer(move_x, move_y):
        pass

    # Linear interpolation drive for 2 axes in mm.
    def LinearInterpolationMillimeter(move_x, move_y):
        pass

    # Set resolution function
    def SetResolution(axisnum, value):
        pass

    # Generic command function
    def GenericCommand(sendcom):
        pass
#endregion

#endregion 