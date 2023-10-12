import serial
import time
from .SK_Controller import StageControlBase
from .clsStageAxisSHOT import clsStageAxisSHOT
#// ステージ制御クラス…対象機：GIP-101, SHOT-702, SHOT-302GS, SHOT-304GS

# SHOT class
class StageControlShot(StageControlBase):
    
#region Constructor
    def __init__(self,portNumber="COM1", controller= "SHOT-702 / SHOT-302GS", bRate=9600):
        """
        Initialize a new instance of the StageController class.

        Args:
            ports (SerialPort): The SerialPort object for communication.
        """
        if self.OpenSerialPort(portNumber, controller, bRate):
        
            self.__controller_model = controller

            if self.__controller_model == "GIP-101":
                self.__axis_count = 1
            elif self.__controller_model == "SHOT-702 / SHOT-302GS":
                self.__axis_count = 2
            elif self.__controller_model == "SHOT-304GS":
                self.__axis_count = 4
            else:
                self.__axis_count = self.AXIS_COUNT_DEFAULT

            self.__axis = [clsStageAxisSHOT() for _ in range(self.__axis_count)]
            self.comports.timeout = self.READ_TIMEOUT_DEFAULT
            self.comports.write_timeout = self.WRITE_TIMEOUT_DEFAULT
            self.__portNo = portNumber
            self.__busy_flag = self.BUSY_FLAG_DEFAULT
            self.__send_command = self.SEND_COMMAND_DEFAULT
            self.__receive_command = self.RECIEVE_COMMAND_DEFAULT
            self.__last_error_message = ""      
        else:
            self.__last_error_message =+ ", please serial comport "   
#endregion  

#region members & data
    #BaudRate class (Enumerations)
    class BaudRateclass:
            BR_2400 = 2400
            BR_4800 = 4800
            BR_9600 = 9600
            BR_19200 = 19200
            BR_38400 = 38400

    # Default Values(Stage Parameters)
    CONTROLLER_MODEL_DEFAULT = "SHOT-302GS"
    AXIS_COUNT_DEFAULT = 2
    BUSY_FLAG_DEFAULT = False
    SEND_COMMAND_DEFAULT = ""
    RECIEVE_COMMAND_DEFAULT = ""

    # Serial Port Settings
    PORT_NAME_DEFAULT = "COM1"
    BAUDRATE_DEFAULT = BaudRateclass.BR_9600
    WRITE_TIMEOUT_DEFAULT = 10
    READ_TIMEOUT_DEFAULT = 10
    DATABITS_DEFAULT = 8
    PARITY_DEFAULT = serial.PARITY_NONE
    STOPBITS_DEFAULT = serial.STOPBITS_ONE
    HANDSHAKE_DEFAULT = "rts/cts"
    DELIMITER_DEFAULT = "\r\n"
    RECCOM_OK = b"OK\r\n" 
    RECCOM_NG = b"NG\r\n"
#endregion

#region Define properties stages (use Python's property decorator)
# Controller Model Property
    @property
    def ControllerModel(self):
        """
        Get or set the controller model.

        Returns:
            str: The controller model.
        """
        return self.__controller_model

    @ControllerModel.setter
    def ControllerModel(self, value):
        """
        Set the controller model.

        Args:
            value (str): The controller model to set.
        """
        self.__controller_model = value

    # Axis Number Property
    @property
    def AxisNum(self):
        """
        Get or set the number of control axes.

        Returns:
            int: The number of control axes.
        """
        return self.__axis_count

    @AxisNum.setter
    def AxisNum(self, value):
        """
        Set the number of control axes.

        Args:
            value (int): The number of control axes to set.
        """
        self.__axis_count = value

    # Busy Flag Property
    @property
    def IsBusy(self):
        """
        Get the positioning status.

        Returns:
            bool: True if busy, False if ready.
        """
        return self.__busy_flag

    # Send Command Property
    @property
    def SendCommand(self):
        """
        Get the send command.

        Returns:
            str: The send command.
        """
        return self.__send_command

    # Receive Command Property
    @property
    def ReceiveCommand(self):
        """
        Get the receive command.

        Returns:
            str: The receive command.
        """
        return self.__receive_command

    # Last Error Message Property
    @property
    def LastErrorMessage(self):
        """
        Get the last error message.

        Returns:
            str: The last error message.
        """
        return self.__last_error_message

    #endregion

#region Communication Properties
    # COM Port Name
    @property
    def PortName(self):
        """
        COM port name
        """
        return self.comports.port

    @PortName.setter
    def PortName(self, value):
        """
        Set the comport name

        Args:
            value (str): The port name 
        """
        if value is None:
            self.comports.port = "COM1"
        else:
            self.comports.port = value

    # COM Port Number
    @property
    def PortNumber(self):
        """
        Gets the COM port number.

        Returns:
        str: The COM port number.
        """
        return self.comports.portstr

    @PortNumber.setter
    def PortNumber(self, value):
        """
        Sets the COM port number.

        Args:
        value (int): The COM port number to set.

        Returns:
        None
        """
        self.comports.portstr = "COM" + str(value)

    # Baud Rate
    @property
    def BaudRate(self):
        """
        Gets the Baud rate for communication.

        Returns:
        int: The Baud rate.
        """
        return self.comports.baudrate

    @BaudRate.setter
    def BaudRate(self, value):
        """
        Sets the Baud rate for communication.

        Args:
        value (int): The Baud rate to set.

        Returns:
        None
        """
        self.comports.baudrate = value

    # Write Timeout
    @property
    def WriteTimeOut(self):
        """
        Gets the write timeout.

        Returns:
        int: The write timeout.
        """
        return self.comports.write_timeout

    @WriteTimeOut.setter
    def WriteTimeOut(self, value):
        """
        Sets the write timeout.

        Args:
        value (int): The write timeout to set.

        Returns:
        None
        """
        self.comports.write_timeout = value

    # Read Timeout
    @property
    def ReadTimeOut(self):
        """
        Gets the read timeout.

        Returns:
        int: The read timeout.
        """
        return self.comports.timeout

    @ReadTimeOut.setter
    def ReadTimeOut(self, value):
        """
        Sets the read timeout.

        Args:
        value (int): The read timeout to set.

        Returns:
        None
        """
        self.comports.timeout = value

    # Data Bits
    @property
    def DataBits(self):
        """
        Gets the data bits.

        Returns:
        int: The data bits.
        """
        return self.comports.bytesize

    @DataBits.setter
    def DataBits(self, value):
        """
        Sets the data bits.

        Args:
        value (int): The data bits to set.

        Returns:
        None
        """
        self.comports.bytesize = value

    # Parity
    @property
    def Parity(self):
        """
        Gets the parity setting for communication.

        Returns:
        str: The parity setting.
        """
        return self.comports.parity

    @Parity.setter
    def Parity(self, value):
        """
        Sets the parity setting for communication.

        Args:
        value (str): The parity setting to set.

        Returns:
        None
        """
        self.comports.parity = value

    # Stop Bits
    @property
    def StopBits(self):
        """
        Gets the stop bits for communication.

        Returns:
        float: The stop bits.
        """
        return self.comports.stopbits

    @StopBits.setter
    def StopBits(self, value):
        """
        Sets the stop bits for communication.

        Args:
        value (float): The stop bits to set.

        Returns:
        None
        """
        self.comports.stopbits = value

    # Handshake
    @property
    def HandShake(self):
        """
        Gets the flow control (handshake) setting.

        Returns:
        bool: The flow control (handshake) setting.
        """
        return self.comports.rtscts

    @HandShake.setter
    def HandShake(self, value:bool):
        """
        Sets the flow control (handshake) setting.

        Args:
        value (bool): The flow control (handshake) setting to set.

        Returns:
        None
        """
        self.comports.rtscts = value

    # Is COM Port Open
    @property
    def IsOpen(self):
        """
        Gets the state of the COM port (open or closed).

        Returns:
        bool: True if the COM port is open, False if it's closed.
        """
        return self.comports.is_open
    
    #endregion

#region method [Axis Class Property Access Functions]

    # get position in pulse
    def GetPositionPulse(self, axisnum):
        """
        Gets the current position of the specified axis in pulse units.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            int: The current position of the specified axis in pulse units.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionPulse
        else:
            return 0

    # get position in nanometer
    def GetPositionNanometer(self, axisnum):
        """
        Gets the current position of the specified axis in nanometer units.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            int: The current position of the specified axis in nanometer units.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionNanometer
        else:
            return 0

    # get position in micrometer
    def GetPositionMicrometer(self, axisnum):
        """
        Gets the current position of the specified axis in micrometer units.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in micrometer units.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionMicrometer
        else:
            return 0.0

    # get position in mm
    def GetPositionMillimeter(self, axisnum):
        """
        Gets the current position of the specified axis in millimeter units.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in millimeter units.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionMillimeter
        else:
            return 0.0

    # get position in degree
    def GetPositionDegree(self, axisnum):
        """
        Gets the current position of the specified axis in degrees.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in degrees.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionDegree
        else:
            return 0.0

    # get limit
    def GetLimitSignal(self, axisnum):
        """
        Gets the limit signal state of the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the limit signal state.

        Returns:
            int: The limit signal state of the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].LimitState
        else:
            return 0

    # get position pulse to nanomter
    def GetPulseToNanometer(self, axisnum):
        """
        Gets the conversion factor from pulse units to nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the conversion factor.

        Returns:
            float: The conversion factor from pulse units to nanometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PulseToNanometer
        else:
            return 0
        
    # Get position in micrometers
    def GetPositionMicrometer(self, axisnum):
        """
        Gets the current position of the specified axis in micrometers.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in micrometers.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionMicrometer
        else:
            return 0.0

    # Get position in millimeters
    def GetPositionMillimeter(self, axisnum):
        """
        Gets the current position of the specified axis in millimeters.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in millimeters.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionMillimeter
        else:
            return 0.0

    # Get position in degrees
    def GetPositionDegree(self, axisnum):
        """
        Gets the current position of the specified axis in degrees.

        Args:
            axisnum (int): The axis number for which to retrieve the position.

        Returns:
            float: The current position of the specified axis in degrees.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PositionDegree
        else:
            return 0.0

    # Get limit signal
    def GetLimitSignal(self, axisnum):
        """
        Gets the limit signal state of the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the limit signal state.

        Returns:
            int: The limit signal state of the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].LimitState
        else:
            return 0

    # Get the nanometer equivalent of pulse value
    def GetPulseToNanometer(self, axisnum):
        """
        Gets the conversion factor from pulse units to nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the conversion factor.

        Returns:
            float: The conversion factor from pulse units to nanometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PulseToNanometer
        else:
            return 0

    # Set the nanometer equivalent of pulse value
    def SetPulseToNanometer(self, axisnum, value):
        """
        Sets the conversion factor from pulse units to nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the conversion factor.
            value (float): The conversion factor from pulse units to nanometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].PulseToNanometer = value

    # Get the micrometer equivalent of pulse value
    def GetPulseToMicrometer(self, axisnum):
        """
        Gets the conversion factor from pulse units to micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the conversion factor.

        Returns:
            float: The conversion factor from pulse units to micrometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PulseToMicrometer
        else:
            return 0.0

    # Get the millimeter equivalent of pulse value
    def GetPulseToMillimeter(self, axisnum):
        """
        Gets the conversion factor from pulse units to millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the conversion factor.

        Returns:
            float: The conversion factor from pulse units to millimeters for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PulseToMillimeter
        else:
            return 0.0

    # Get the degree equivalent of pulse value
    def GetPulseToDegree(self, axisnum):
        """
        Gets the conversion factor from pulse units to degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the conversion factor.

        Returns:
            float: The conversion factor from pulse units to degrees for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].PulseToDegree
        else:
            return 0.0

    # Get offset in pulse
    def GetOffsetMoriginPulse(self, axisnum):
        """
        Gets the offset in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the offset.

        Returns:
            int: The offset in pulse units for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].OffsetMoriginPulse
        else:
            return 0

    # Get offset in nanometers
    def GetOffsetMoriginNanometer(self, axisnum):
        """
        Gets the offset in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the offset.

        Returns:
            float: The offset in nanometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].OffsetMoriginNanometer
        else:
            return 0

    # Get offset in micrometers
    def GetOffsetMoriginMicrometer(self, axisnum):
        """
        Gets the offset in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the offset.

        Returns:
            float: The offset in micrometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].OffsetMoriginMicrometer
        else:
            return 0.0

    # Get offset in millimeters
    def GetOffsetMoriginMillimeter(self, axisnum):
        """
        Gets the offset in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the offset.

        Returns:
            float: The offset in millimeters for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].OffsetMoriginMillimeter
        else:
            return 0.0

    # Get offset in degrees
    def GetOffsetMoriginDegree(self, axisnum):
        """
        Gets the offset in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the offset.

        Returns:
            float: The offset in degrees for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].OffsetMoriginDegree
        else:
            return 0.0

    # Set offset in pulse
    def SetOffsetMoriginPulse(self, axisnum, value):
        """
        Sets the offset in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the offset.
            value (int): The offset in pulse units.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].OffsetMoriginPulse = value

    # Set offset in nanometers
    def SetOffsetMoriginNanometer(self, axisnum, value):
        """
        Sets the offset in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the offset.
            value (float): The offset in nanometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].OffsetMoriginNanometer = value

    # Set offset in micrometers
    def SetOffsetMoriginMicrometer(self, axisnum, value):
        """
        Sets the offset in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the offset.
            value (float): The offset in micrometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].OffsetMoriginMicrometer = value

    # Set offset in millimeters
    def SetOffsetMoriginMillimeter(self, axisnum, value):
        """
        Sets the offset in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the offset.
            value (float): The offset in millimeters.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].OffsetMoriginMillimeter = value

    # Set offset in degrees
    def SetOffsetMoriginDegree(self, axisnum, value):
        """
        Sets the offset in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the offset.
            value (float): The offset in degrees.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].OffsetMoriginDegree = value

    # Get upper stroke limit in pulse
    def GetStrokeLimitMaxPulse(self, axisnum):
        """
        Gets the upper stroke limit in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the upper stroke limit.

        Returns:
            int: The upper stroke limit in pulse units for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MaxStrokePulse
        else:
            return 0

    # Get upper stroke limit in nanometers
    def GetStrokeLimitMaxNanometer(self, axisnum):
        """
        Gets the upper stroke limit in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the upper stroke limit.

        Returns:
            float: The upper stroke limit in nanometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MaxStrokeNanometer
        else:
            return 0

    # Get upper stroke limit in micrometers
    def GetStrokeLimitMaxMicrometer(self, axisnum):
        """
        Gets the upper stroke limit in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the upper stroke limit.

        Returns:
            float: The upper stroke limit in micrometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MaxStrokeMicrometer
        else:
            return 0.0

    # Get upper stroke limit in millimeters
    def GetStrokeLimitMaxMillimeter(self, axisnum):
        """
        Gets the upper stroke limit in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the upper stroke limit.

        Returns:
            float: The upper stroke limit in millimeters for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MaxStrokeMillimeter
        else:
            return 0.0

    # Get upper stroke limit in degrees
    def GetStrokeLimitMaxDegree(self, axisnum):
        """
        Gets the upper stroke limit in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the upper stroke limit.

        Returns:
            float: The upper stroke limit in degrees for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MaxStrokeDegree
        else:
            return 0.0

    # Get lower stroke limit in pulse
    def GetStrokeLimitMinPulse(self, axisnum):
        """
        Gets the lower stroke limit in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the lower stroke limit.

        Returns:
            int: The lower stroke limit in pulse units for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MinStrokePulse
        else:
            return 0

    # Get lower stroke limit in nanometers
    def GetStrokeLimitMinNanometer(self, axisnum):
        """
        Gets the lower stroke limit in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the lower stroke limit.

        Returns:
            float: The lower stroke limit in nanometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MinStrokeNanometer
        else:
            return 0

    # Get lower stroke limit in micrometers
    def GetStrokeLimitMinMicrometer(self, axisnum):
        """
        Gets the lower stroke limit in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the lower stroke limit.

        Returns:
            float: The lower stroke limit in micrometers for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MinStrokeMicrometer
        else:
            return 0.0

    # Get lower stroke limit in millimeters
    def GetStrokeLimitMinMillimeter(self, axisnum):
        """
        Gets the lower stroke limit in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the lower stroke limit.

        Returns:
            float: The lower stroke limit in millimeters for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MinStrokeMillimeter
        else:
            return 0.0

    # Get lower stroke limit in degrees
    def GetStrokeLimitMinDegree(self, axisnum):
        """
        Gets the lower stroke limit in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the lower stroke limit.

        Returns:
            float: The lower stroke limit in degrees for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].MinStrokeDegree
        else:
            return 0.0

    # Set upper stroke limit in pulse
    def SetStrokeLimitMaxPulse(self, axisnum, value):
        """
        Sets the upper stroke limit in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the upper stroke limit.
            value (int): The upper stroke limit in pulse units.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MaxStrokePulse = value

    # Set upper stroke limit in nanometers
    def SetStrokeLimitMaxNanometer(self, axisnum, value):
        """
        Sets the upper stroke limit in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the upper stroke limit.
            value (float): The upper stroke limit in nanometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MaxStrokeNanometer = value

    # Set upper stroke limit in micrometers
    def SetStrokeLimitMaxMicrometer(self, axisnum, value):
        """
        Sets the upper stroke limit in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the upper stroke limit.
            value (float): The upper stroke limit in micrometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MaxStrokeMicrometer = value

    # Set upper stroke limit in millimeters
    def SetStrokeLimitMaxMillimeter(self, axisnum, value):
        """
        Sets the upper stroke limit in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the upper stroke limit.
            value (float): The upper stroke limit in millimeters.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MaxStrokeMillimeter = value

    # Set upper stroke limit in degrees
    def SetStrokeLimitMaxDegree(self, axisnum, value):
        """
        Sets the upper stroke limit in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the upper stroke limit.
            value (float): The upper stroke limit in degrees.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MaxStrokeDegree = value

    # Set lower stroke limit in pulse
    def SetStrokeLimitMinPulse(self, axisnum, value):
        """
        Sets the lower stroke limit in pulse units for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the lower stroke limit.
            value (int): The lower stroke limit in pulse units.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MinStrokePulse = value

    # Set lower stroke limit in nanometers
    def SetStrokeLimitMinNanometer(self, axisnum, value):
        """
        Sets the lower stroke limit in nanometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the lower stroke limit.
            value (float): The lower stroke limit in nanometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MinStrokeNanometer = value

    # Set lower stroke limit in micrometers
    def SetStrokeLimitMinMicrometer(self, axisnum, value):
        """
        Sets the lower stroke limit in micrometers for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the lower stroke limit.
            value (float): The lower stroke limit in micrometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MinStrokeMicrometer = value

    # Set lower stroke limit in millimeters
    def SetStrokeLimitMinMillimeter(self, axisnum, value):
        """
        Sets the lower stroke limit in millimeters for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the lower stroke limit.
            value (float): The lower stroke limit in millimeters.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MinStrokeMillimeter = value

    # Set lower stroke limit in degrees
    def SetStrokeLimitMinDegree(self, axisnum, value):
        """
        Sets the lower stroke limit in degrees for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the lower stroke limit.
            value (float): The lower stroke limit in degrees.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].MinStrokeDegree = value

    # get stage full step value in μｍ                        (linear stage)
    def GetFullStepInMicrometer(self,axisnum):
        """
        Gets the full step value in micrometers for the specified linear stage axis.

        Args:
            axisnum (int): The axis number for which to retrieve the full step value.

        Returns:
            float: The full step value in micrometers for the specified linear stage axis.
        """
        if 1<=axisnum<= self.__axis_count:
            return self.__axis[axisnum-1].FullstepMoveValueMicrometer
        else:
            return 2  # base full step for all linear SK Stage
    
    # set stage full step value in μｍ 
    def SetFullStepInMicrometer(self,axisnum,value):
        """
        Sets the full step value in micrometers for the specified linear stage axis.

        Args:
            axisnum (int): The axis number for which to set the full step value.
            value (float): The full step value in micrometers.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum-1].FullstepMoveValueMicrometer = value
        
    # get stage full step value in degree                     (rotation stage)
    def GetFullStepInDegree(self,axisnum):
        """
        Gets the full step value in degrees for the specified rotation stage axis.

        Args:
            axisnum (int): The axis number for which to retrieve the full step value.

        Returns:
            float: The full step value in degrees for the specified rotation stage axis.
        """
        if 1<=axisnum<= self.__axis_count:
            return self.__axis[axisnum-1].FullstepMoveValueDegree
        else:
            return 0.005  # base full step for all rotation SK Stage
        
    # set stage full step in degree 
    def SetFullStepInDegree(self,axisnum, value ):
        """
        Sets the full step value in degrees for the specified rotation stage axis.

        Args:
            axisnum (int): The axis number for which to set the full step value.
            value (float): The full step value in degrees.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum-1].FullstepMoveValueDegree = value

    # Get speed in pulse per second
    def GetSpeedPulse(self, axisnum):
        """
        Gets the speed in pulse per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the speed.

        Returns:
            int: The speed in pulse per second for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedFastPulse
        else:
            return 0

    # Get speed in nanometers per second
    def GetSpeedNanometer(self, axisnum):
        """
        Gets the speed in pulse per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the speed.

        Returns:
            int: The speed in pulse per second for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedFastNanometer
        else:
            return 0

    # Get speed in micrometers per second
    def GetSpeedMicrometer(self, axisnum):
        """
        Gets the speed in micrometers per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the speed.

        Returns:
            float: The speed in micrometers per second for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedFastMicrometer
        else:
            return 0.0
        
    # Get speed in millimeters per second
    def GetSpeedMillimeter(self, axisnum):
        """
        Gets the speed in millimeters per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the speed.

        Returns:
            float: The speed in millimeters per second for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedFastMillimeter
        else:
            return 0.0

    # Get speed in degrees per second
    def GetSpeedDegree(self, axisnum):
        """
        Gets the speed in degrees per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the speed.

        Returns:
            float: The speed in degrees per second for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedFastDegree
        else:
            return 0.0

    # Set speed in pulse per second
    def SetSpeedPulse(self, axisnum, value):
        """
        Sets the speed in pulse per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the speed.
            value (int): The speed in pulse per second.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedFastPulse = value

    # Set speed in nanometers per second
    def SetSpeedNanometer(self, axisnum, value):
        """
        Sets the speed in nanometers per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the speed.
            value (float): The speed in nanometers per second.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedFastNanometer = value

    # Set speed in micrometers per second
    def SetSpeedMicrometer(self, axisnum, value):
        """
        Sets the speed in micrometers per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the speed.
            value (float): The speed in micrometers per second.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedFastMicrometer = value

    # Set speed in millimeters per second
    def SetSpeedMillimeter(self, axisnum, value):
        """
        Sets the speed in millimeters per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the speed.
            value (float): The speed in millimeters per second.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedFastMillimeter = value

    # Set speed in degrees per second
    def SetSpeedDegree(self, axisnum, value):
        """
        Sets the speed in degrees per second for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the speed.
            value (float): The speed in degrees per second.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedFastDegree = value

    # Get acceleration time in milliseconds
    def GetAccelTime(self, axisnum):
        """
        Gets the acceleration time in milliseconds for the specified axis.

        Args:
            axisnum (int): The axis number for which to retrieve the acceleration time.

        Returns:
            int: The acceleration time in milliseconds for the specified axis.
        """
        if 1 <= axisnum <= self.__axis_count:
            return self.__axis[axisnum - 1].SpeedActMillisecond
        else:
            return 100

    # Set acceleration time in milliseconds
    def SetAccelTime(self, axisnum, value):
        """
        Sets the acceleration time in milliseconds for the specified axis.

        Args:
            axisnum (int): The axis number for which to set the acceleration time.
            value (int): The acceleration time in milliseconds.

        Returns:
            None
        """
        if 1 <= axisnum <= self.__axis_count:
            self.__axis[axisnum - 1].SpeedActMillisecond = value

    #endregion

#region stage methods
    # Region for stage control functions

    # Region for status processing

    # Get status for 1/2/4 axes
    def UpdateStatus(self):
        """
        Updates the status of the controller for 1, 2, or 4 axes.

        Returns:
            bool: True if the status update was successful, False otherwise.
        """
        ret = False

        if self.__axis_count == 1:
            ret = self.GetStatusAxis1()
        elif self.__axis_count == 2:
            ret = self.GetStatusAxis2()
        elif self.__axis_count == 4:
            ret = self.GetStatusAxis4()

        return ret

    # Status retrieval for 1 axis
    def GetStatusAxis1(self):
        """
        Retrieves the status for a 1-axis controller.

        Returns:
            bool: True if status retrieval was successful, False otherwise.
        """
        sendcom = ""
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            sendcom = "Q:"
            sendcom = bytes(sendcom, encoding="ascii") + b'\r\n'

            # Send status check command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive status
            reccom = self.comports.readline()

            # Coordinate value
            self.__axis[0].PositionPulse = int(reccom.decode('utf-8')[1:10].replace(' ',''))

            if reccom[0] == "-":
                self.__axis[0].PositionPulse *= -1

            # Hard limit detection
            if reccom[13] == "K":
                self.__axis[0].limit_state = clsStageAxisSHOT.AxisLimitState.LimitState_None
            elif reccom[13] == "L":
                self.__axis[0].limit_state = clsStageAxisSHOT.AxisLimitState.LimitState_Hard

            # Soft limit detection
            for i in range(self.__axis_count):
                if self.__axis[i].limit_state != clsStageAxisSHOT.AxisLimitState.LimitState_Hard:
                    if (self.__axis[i].PositionPulse ==
                            self.__axis[i].MaxStrokePulse - self.__axis[i].OffsetMoriginPulse) or (
                            self.__axis[i].PositionPulse == self.__axis[i].MinStrokePulse - self.__axis[i].OffsetMoriginPulse):
                        self.__axis[i].limit_state = clsStageAxisSHOT.AxisLimitState.LimitState_Soft

            # BUSY flag
            if reccom.decode('utf-8')[15] == "B":
                self.__busy_flag = True
            elif reccom.decode('utf-8')[15] == "R":
                self.__busy_flag = False

            return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

    # Status retrieval for 2 axes
    def GetStatusAxis2(self):
        """
        Retrieves the status for a 2-axis controller.

        Returns:
        bool: True if status retrieval was successful, False otherwise.
        """
        sendcom = ""
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            sendcom = "Q:"
            sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'

            # Send status check command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive status
            reccom = self.comports.readline()

            # Coordinate values
            for i in range(self.__axis_count):
                split = reccom.decode('utf-8').split(',')
                self.__axis[i].PositionPulse = int(split[i].replace(' ',''))

            # Hard limit detection
            if reccom.decode('utf-8')[24] == "K":
                self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
                self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            elif reccom.decode('utf-8')[24] == "L":
                self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
                self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            elif reccom.decode('utf-8')[24] == "M":
                self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
                self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            elif reccom.decode('utf-8')[24] == "W":
                self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
                self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard

            # Soft limit detection
            for i in range(self.__axis_count):
                if self.__axis[i].limit_state != clsStageAxisSHOT.AxisLimitState.LimitState_Hard:
                    if (self.__axis[i].PositionPulse ==
                            self.__axis[i].MaxStrokePulse - self.__axis[i].OffsetMoriginPulse) or (
                            self.__axis[i].PositionPulse == self.__axis[i].MinStrokePulse - self.__axis[i].OffsetMoriginPulse):
                        self.__axis[i].limit_state = clsStageAxisSHOT.AxisLimitState.LimitState_Soft

            # BUSY flag
            if  reccom.decode('utf-8')[26] == "B":
                self.__busy_flag = True
            elif  reccom.decode('utf-8')[26] == "R":
                self.__busy_flag = False

            return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

    # Status retrieval for 4 axes
    def GetStatusAxis4(self):
        """
        Retrieves the status for a 4-axis controller.

        Returns:
        bool: True if status retrieval was successful, False otherwise.
        """
        sendcom = ""
        reccom = ""
        cnt = 0

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            while True:
                # Construct command
                sendcom = "Q:"
                sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'

                # Send status check command
                self.comports.write(sendcom)

                # Sleep briefly to allow time for data to be received
                time.sleep(0.1)

                # Check if there is data available for reading
                if self.comports.in_waiting > 0:
                    reccom = self.comports.readline()

                    break
                else:
                    # Retry process
                    cnt += 1
                    if cnt >= 5:
                        self.__last_error_message = "Status retrieval error"
                        return False

                    if self.comports.isOpen():
                        self.comports.close()
                        self.OpenSerialPort(self.__portNo,self.__controller_model,self.BaudRate)
                    else:
                        self.OpenSerialPort(self.__portNo,self.__controller_model,self.BaudRate)
            
            if reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ str(reccom)
                return False
            
            # Coordinate values
            for i in range(self.__axis_count):
                split = reccom.decode('utf-8').split(',')
                self.__axis[i].PositionPulse = int(split[i].replace(' ',''))

            # Hard limit detection
            self.CheckLimitStateAxis4(reccom.decode('utf-8')[46])

            # Soft limit detection
            for k in range(self.__axis_count):
                if self.__axis[k].limit_state != clsStageAxisSHOT.AxisLimitState.LimitState_Hard:
                    if (self.__axis[k].PositionPulse ==
                            self.__axis[k].MaxStrokePulse - self.__axis[k].OffsetMoriginPulse) or (
                            self.__axis[k].PositionPulse == self.__axis[k].MinStrokePulse - self.__axis[k].OffsetMoriginPulse):
                        self.__axis[k].limit_state = clsStageAxisSHOT.AxisLimitState.LimitState_Soft

            # BUSY flag
            if reccom.decode('utf-8')[48] == "B":
                self.__busy_flag = True
            elif reccom.decode('utf-8')[48] == "R":
                self.__busy_flag = False

            return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

    # Check for hard limit detection
    def CheckLimitStateAxis4(self, reccom):
        """
        Checks for hard limit detection on a 4-axis controller.

        Args:
            reccom (str): The received command indicating hard limit status.

        Returns:
            one
        """
        # Handle different hard limit states
        if reccom == "K":
            for i in range(self.__axis_count):
                self.__axis[i].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "1":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "2":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "3":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "4":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "5":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "6":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "7":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
        elif reccom == "8":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "9":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "A":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "B":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "C":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "D":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "E":
            self.__axis[0].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_None
            self.__axis[1].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[2].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
            self.__axis[3].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard
        elif reccom == "W":
            for i in range(self.__axis_count):
                self.__axis[i].LimitState = clsStageAxisSHOT.AxisLimitState.LimitState_Hard

    # Positioning status check (Busy/Ready)
    def PositioningStatus(self):
        """
        Checks the positioning status (Busy/Ready) of the controller.

        Returns:
            bool: True if positioning status check was successful, False otherwise.
        """
        sendcom = "!:"
        sendcom = bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            # Set member variable
            if reccom == b"B\r\n":
                self.__busy_flag = True
            elif reccom == b"R\r\n":
                self.__busy_flag = False

            return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

    # Mechanical origin return (single axis)
    def ReturnMechanicalOriginSingle(self, axisnum):
        """
        Returns a single axis to its mechanical origin position.

        Args:
            axisnum (int): The axis number to return to the mechanical origin.

        Returns:
            bool: True if returning to mechanical origin position was successful, False otherwise.
        """
        sendcom = "H:" + str(axisnum)
        sendcom = bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)
            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            # Reset origin offset
            if reccom == self.RECCOM_OK:
                self.__axis[axisnum - 1].OffsetMoriginPulse = 0
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Mechanical origin return (all axes)
    def ReturnMechanicalOriginAll(self):
        """
        Returns all axes to their mechanical origin positions.

        Returns:
            bool: True if returning to mechanical origin positions was successful, False otherwise.
        """
        sendcom = "H:W"
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            # Reset origin offset
            if reccom == self.RECCOM_OK:
                for i in range(self.__axis_count):
                    self.__axis[i].OffsetMoriginPulse = 0
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Region for absolute positioning 

    # Logical origin return (single axis)
    def ReturnLogicalOriginSingle(self, axisnum):
        """
        Returns a single axis to its logical origin position.

        Args:
            axisnum (int): The axis number to return to the logical origin.

        Returns:
            bool: True if returning to logical origin position was successful, False otherwise.
        """
        return self.AbsoluteDriveSinglePulse(axisnum, 0)

    # Logical origin return (all axes)
    def ReturnLogicalOriginAll(self):
        """
        Returns all axes to their logical origin positions.

        Returns:
            bool: True if returning to logical origin positions was successful, False otherwise.
        """
        target = [0] * self.__axis_count
        return self.AbsoluteDriveAllPulse(target)

    # Logical origin set (single axis)
    def SetLogicalOriginSingle(self, axisnum):
        """
        Sets the logical origin for a single axis to the current position.

        Args:
            axisnum (int): The axis number for which to set the logical origin.

        Returns:
            bool: True if setting the logical origin was successful, False otherwise.
        """
        sendcom = "R:" + str(axisnum)
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Get current position
            currentposition = self.__axis[axisnum - 1].PositionPulse

            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            # Reset origin offset
            if reccom == self.RECCOM_OK:
                self.__axis[axisnum - 1].OffsetMoriginPulse += currentposition
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Logical origin set (all axes)
    def SetLogicalOriginAll(self):
        """
        Sets the logical origin for all axes to their current positions.

        Returns:
            bool: True if setting the logical origin was successful, False otherwise.
        """
        sendcom = "R:W"
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Get current positions
            currentposition = [self.__axis[i].PositionPulse for i in range(self.__axis_count)]

            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            # Reset origin offset
            if reccom == self.RECCOM_OK:
                for i in range(self.__axis_count):
                    self.__axis[i].OffsetMoriginPulse += currentposition[i]
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Stop drive (single axis)
    def StopDriveSingle(self, axisnum):
        """
        Stops the drive for a single axis.

        Args:
            axisnum (int): The axis number for which to stop the drive.

        Returns:
            bool: True if stopping the drive was successful, False otherwise.
        """
        sendcom = "L:" + str(axisnum)
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            if reccom == self.RECCOM_OK:
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Stop drive (all axes)
    def StopDriveAll(self):
        """
        Stops the drive for all axes.

        Returns:
            bool: True if stopping the drive for all axes was successful, False otherwise.
        """
        sendcom = "L:W"
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            if reccom == self.RECCOM_OK:
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Emergency stop
    def EmergencyStop(self):
        """
        Emergency Stop for all axes.

        Returns:
            bool: True if stopping the drive for all axes was successful, False otherwise.
        """
        sendcom = "L:E"
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Construct command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command (OK/NG)
            reccom = self.comports.readline()

            if reccom == self.RECCOM_OK:
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Trim stroke limit pulse
    def TrimStrokeLimitPulse(self, axisnum, target):
        """
        Trims the stroke limit pulse for a single axis based on the target position.

        Args:
            axisnum (int): The axis number for which to trim the stroke limit pulse.
            target (float): The target position in pulses.

        Returns:
            float: The trimmed safe position in pulses.
        """
        safe_position = 0

        if target < self.__axis[axisnum - 1].MinStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse:
            safe_position = self.__axis[axisnum - 1].MinStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse
        elif self.__axis[axisnum - 1].MaxStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse < target:
            safe_position = self.__axis[axisnum - 1].MaxStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse
        else:
            safe_position = target

        return safe_position

    # Absolute drive (single axis - pulse)
    def AbsoluteDriveSinglePulse(self, axisnum, target):
        """
        Drives a single axis to an absolute position in pulses.

        Args:
            axisnum (int): The axis number to drive.
            target (float): The target position in pulses.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        direction = "+" if target > 0 else "-"
        safe_target = self.TrimStrokeLimitPulse(axisnum, target)
        sendcom1 = f"A:{axisnum}{direction}P{abs(safe_target):.0f}"
        sendcom1= bytes(sendcom1, encoding="ascii") + b'\r\n'
        sendcom2 = "G:"
        sendcom2= bytes(sendcom2, encoding="ascii") + b'\r\n'
        reccom1, reccom2 = "", ""

        try:
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            self.comports.write(sendcom1)
            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            reccom1 = self.comports.readline()

            if reccom1 == self.RECCOM_OK:
                self.comports.write(sendcom2)

                # Sleep briefly to allow time for data to be received
                time.sleep(0.1)
                

                reccom2 = self.comports.readline()

                if reccom2 == self.RECCOM_OK:
                    return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Absolute drive single Nanometer 
    def AbsoluteDriveSingleNanometer(self, axisnum, target):
        """
        Drives a single axis to an absolute position in nanometers.

        Args:
            axisnum (int): The axis number to drive.
            target (float): The target position in nanometers.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.AbsoluteDriveSinglePulse(axisnum, target / self.__axis[axisnum - 1].PulseToNanometer)

    # Absolute drive single micrometer 
    def AbsoluteDriveSingleMicrometer(self, axisnum, target):
        """
        Drives a single axis to an absolute position in micrometers.

        Args:
            axisnum (int): The axis number to drive.
            target (float): The target position in micrometers.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.AbsoluteDriveSinglePulse(axisnum, target / self.__axis[axisnum - 1].PulseToMicrometer)

    # Absolute drive single mm 
    def AbsoluteDriveSingleMillimeter(self, axisnum, target):
        """
        Drives a single axis to an absolute position in millimeters.

        Args:
            axisnum (int): The axis number to drive.
            target (float): The target position in millimeters.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.AbsoluteDriveSinglePulse(axisnum, target / self.__axis[axisnum - 1].PulseToMillimeter)

    # Absolute drive single degree 
    def AbsoluteDriveSingleDegree(self, axisnum, target):
        """
    Drives a single axis to an absolute position in degrees.

    Args:
        axisnum (int): The axis number to drive.
        target (float): The target position in degrees.

    Returns:
        bool: True if the drive was successful, False otherwise.
    """
        return self.AbsoluteDriveSinglePulse(axisnum, target / self.__axis[axisnum - 1].PulseToDegree)

    # Absolute drive all axis pulses 
    def AbsoluteDriveAllPulse(self, target):
        """
        Drives all axes to absolute positions in pulses.

        Args:
            target (list): A list of target positions in pulses for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        safe_target = [0] * self.__axis_count
        direction = ["+"] * self.__axis_count
        reccom1, reccom2 = "", ""

        for i in range(1, self.__axis_count + 1):
            buff = target[i - 1]
            safe_target[i - 1] = self.TrimStrokeLimitPulse(i, buff)

        for j in range(self.__axis_count):
            if safe_target[j] <= 0:
                direction[j] = "-"

        try:
            self.comports.flushOutput()
            self.comports.reset_input_buffer()
            sendcom1 = "A:W" + "".join([direction[k] + "P" + str(abs(safe_target[k])) for k in range(self.__axis_count)])
            sendcom1= bytes(sendcom1, encoding="ascii") + b'\r\n'
            self.comports.write(sendcom1)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            reccom1 = self.comports.readline()

            if reccom1 == self.RECCOM_OK:
                sendcom2 = "G:"
                sendcom2= bytes(sendcom2, encoding="ascii") + b'\r\n'
                self.comports.write(sendcom2)

                # Sleep briefly to allow time for data to be received
                time.sleep(0.1)

                reccom2 = self.comports.readline()

                if reccom2 == self.RECCOM_OK:
                    return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Absolute Drive All Nanometer
    def AbsoluteDriveAllNanometer(self, target):
        """
        Drives all axes to absolute positions in nanometers.

        Args:
            target (list): A list of target positions in nanometers for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_target = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_target[i] = target[i] / self.__axis[i].PulseToNanometer
        return self.AbsoluteDriveAllPulse(self,conv_target)
    
    # Absolute Drive All Micrometer  
    def AbsoluteDriveAllMicrometer(self, target):
        """
        Drives all axes to absolute positions in micrometers.

        Args:
            target (list): A list of target positions in micrometers for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_target = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_target[i] = target[i] / self.__axis[i].PulseToMicrometer
        return self.AbsoluteDriveAllPulse(conv_target)

    # Absolute Drive All mm  
    def AbsoluteDriveAllMillimeter(self, target):
        """
        Drives all axes to absolute positions in millimeters.

        Args:
            target (list): A list of target positions in millimeters for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_target = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_target[i] = target[i] / self.__axis[i].PulseToMillimeter
        return self.AbsoluteDriveAllPulse(conv_target)

    # Absolute Drive All degree  
    def AbsoluteDriveAllDegree(self, target):
        """
        Drives all axes to absolute positions in degrees.

        Args:
            target (list): A list of target positions in degrees for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_target = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_target[i] = target[i] / self.__axis[i].PulseToDegree
        return self.AbsoluteDriveAllPulse(conv_target)

    # Region "Relative Drive Processing"

    #Relative drive (single axis: pulse)
    def RelativeDriveSinglePulse(self, axisnum, pitch):
        """
        Drives a single axis to a relative position in pulses.

        Args:
            axisnum (int): The axis number to drive.
            pitch (int): The relative position change in pulses.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.AbsoluteDriveSinglePulse(axisnum, self.__axis[axisnum - 1].PositionPulse + pitch)

    #Relative drive (single axis: nanometer)    
    def RelativeDriveSingleNanometer(self, axisnum, pitch):
        """
        Drives a single axis to a relative position in nanometers.

        Args:
            axisnum (int): The axis number to drive.
            pitch (int): The relative position change in nanometers.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.RelativeDriveSinglePulse(axisnum, pitch / self.__axis[axisnum - 1].PulseToNanometer)

    #Relative drive (single axis: micrometer)
    def RelativeDriveSingleMicrometer(self, axisnum, pitch):
        """
        Drives a single axis to a relative position in micrometers.

        Args:
            axisnum (int): The axis number to drive.
            pitch (int): The relative position change in micrometers.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.RelativeDriveSinglePulse(axisnum, pitch / self.__axis[axisnum - 1].PulseToMicrometer)

    #Relative drive (single axis: mm)
    def RelativeDriveSingleMillimeter(self, axisnum, pitch):
        """
        Drives a single axis to a relative position in millimeters.

        Args:
            axisnum (int): The axis number to drive.
            pitch (float): The relative position change in millimeters.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.RelativeDriveSinglePulse(axisnum, pitch / self.__axis[axisnum - 1].PulseToMillimeter)

    #Relative drive (single axis: degree)
    def RelativeDriveSingleDegree(self, axisnum, pitch):
        """
        Drives a single axis to a relative position in degrees.

        Args:
            axisnum (int): The axis number to drive.
            pitch (float): The relative position change in degrees.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        return self.RelativeDriveSinglePulse(axisnum, pitch / self.__axis[axisnum - 1].PulseToDegree)

    #Relative drive (all axis: pulse)
    def RelativeDriveAllPulse(self, pitch):
        """
        Drives all axes to relative positions in pulses.

        Args:
            pitch (list): A list of relative position changes in pulses for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_pitch = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_pitch[i] = self.__axis[i].PositionPulse + pitch[i]
        return self.AbsoluteDriveAllPulse(conv_pitch)

    #Relative drive (all axis: nanometer)
    def RelativeDriveAllNanometer(self, pitch):
        """
        Drives all axes to relative positions in nanometers.

        Args:
            pitch (list): A list of relative position changes in nanometers for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_pitch = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_pitch[i] = pitch[i] / self.__axis[i].PulseToNanometer
        return self.RelativeDriveAllPulse(conv_pitch)

    #Relative drive (all axis: micrometer)
    def RelativeDriveAllMicrometer(self, pitch):
        """
        Drives all axes to relative positions in micrometers.

        Args:
            pitch (list): A list of relative position changes in micrometers for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_pitch = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_pitch[i] = pitch[i] / self.__axis[i].PulseToMicrometer
        return self.RelativeDriveAllPulse(conv_pitch)

    #Relative drive (all axis: mm)
    def RelativeDriveAllMillimeter(self, pitch):
        """
        Drives all axes to relative positions in millimeters.

        Args:
            pitch (list): A list of relative position changes in millimeters for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_pitch = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_pitch[i] = pitch[i] / self.__axis[i].PulseToMillimeter
        return self.RelativeDriveAllPulse(conv_pitch)

    #Relative drive (all axis: degree)
    def RelativeDriveAllDegree(self, pitch):
        """
        Drives all axes to relative positions in degrees.

        Args:
            pitch (list): A list of relative position changes in degrees for all axes.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        conv_pitch = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_pitch[i] = pitch[i] / self.__axis[i].PulseToDegree
        return self.RelativeDriveAllPulse(conv_pitch)

    # JOG drive (single axis).
    def JOGDriveSingle(self, axisnum, plusflag):
        """
        Drives a single axis in a jogging manner.

        Args:
            axisnum (int): The axis number to jog.
            plusflag (bool): True to jog in the positive direction, False for the negative direction.

        Returns:
            bool: True if the jog was successful, False otherwise.
        """
        PositionTo = self.__axis[axisnum - 1].MaxStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse if plusflag else self.__axis[axisnum - 1].MinStrokePulse - self.__axis[axisnum - 1].OffsetMoriginPulse
        return self.AbsoluteDriveSinglePulse(axisnum, PositionTo)

    # JOG drive (all axes).
    def JOGDriveAll(self, plusflag):
        """
        Drives all axes in a jogging manner.

        Args:
            plusflag (list): A list of booleans indicating the jogging direction for each axis.

        Returns:
            bool: True if the jog was successful, False otherwise.
        """
        PositionTo = [0] * self.__axis_count
        for i in range(self.__axis_count):
            PositionTo[i] = self.__axis[i].MaxStrokePulse - self.__axis[i].OffsetMoriginPulse if plusflag[i] else self.__axis[i].MinStrokePulse - self.__axis[i].OffsetMoriginPulse
        return self.AbsoluteDriveAllPulse(PositionTo)

    #Check speed parameters (pulse).
    def CheckSpeedParameters(self, fast, slow, act):
        """
        Checks the validity of speed parameters for a drive.

        Args:
            fast (int): The fast speed setting in pulses per second.
            slow (int): The slow speed setting in pulses per second.
            act (int): The acceleration/deceleration time setting in milliseconds.

        Returns:
            bool: True if speed parameters are valid, False otherwise.
        """
        if slow < 1 or slow > 500000:
            self.__last_error_message = "Invalid slow speed setting."
            return False
        if fast < 1 or fast > 500000:
            self.__last_error_message = "Invalid fast speed setting."
            return False
        if slow > fast:
            self.__last_error_message = "Slow speed should be less than fast speed."
            return False
        if act < 0 or act > 1000:
            self.__last_error_message = "Invalid acceleration/deceleration time setting."
            return False
        return True

    # Set speed (single axis: pulse/sec).
    def SetSpeedSinglePulse(self, axisnum, value, act):
        """
        Sets the speed for a single axis in pulses per second.

        Args:
            axisnum (int): The axis number to set the speed for.
            value (int): The fast speed setting in pulses per second.
            act (int): The acceleration/deceleration time in milliseconds.

        Returns:
            bool: True if the speed setting was successful, False otherwise.
        """
        slow = value // 2  # Automatically set Slow speed based on Fast speed

        # Check speed parameters
        if not self.CheckSpeedParameters(value, slow, act):
            return False

        sendcom = f"D:{axisnum}S{slow:.0f}F{value:.0f}R{act:.0f}"
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Send command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command response (OK/NG)
            reccom = self.comports.readline()
            if reccom == self.RECCOM_OK:
                self.__axis[axisnum - 1].SpeedFastPulse = value
                self.__axis[axisnum - 1].SpeedSlowPulse = slow
                self.__axis[axisnum - 1].SpeedActMillisecond = act
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Set speed (single axis: nm/sec).
    def SetSpeedSingleNanometer(self, axisnum, value, act):
        """
        Sets the speed for a single axis in nanometers per second.

        Args:
            axisnum (int): The axis number to set the speed for.
            value (int): The fast speed setting in nanometers per second.
            act (int): The acceleration/deceleration time in milliseconds.

        Returns:
            bool: True if the speed setting was successful, False otherwise.
        """
        conv_fast = value // self.__axis[axisnum - 1].PulseToNanometer
        return self.SetSpeedSinglePulse(axisnum, conv_fast, act)

    # Set speed (single axis: um/sec).
    def SetSpeedSingleMicrometer(self, axisnum, value, act):
        """
        Sets the speed for a single axis in micrometers per second.

        Args:
            axisnum (int): The axis number to set the speed for.
            value (int): The fast speed setting in micrometers per second.
            act (int): The acceleration/deceleration time in milliseconds.

        Returns:
            bool: True if the speed setting was successful, False otherwise.
        """
        conv_fast = int(value // self.__axis[axisnum - 1].PulseToMicrometer)
        return self.SetSpeedSinglePulse(axisnum, conv_fast, act)

    # Set speed (single axis: mm/sec).
    def SetSpeedSingleMillimeter(self, axisnum, value, act):
        """
        Sets the speed for a single axis in millimeters per second.

        Args:
            axisnum (int): The axis number to set the speed for.
            value (float): The fast speed setting in millimeters per second.
            act (int): The acceleration/deceleration time in milliseconds.

        Returns:
            bool: True if the speed setting was successful, False otherwise.
        """
        conv_fast = int(value // self.__axis[axisnum - 1].PulseToMillimeter)
        return self.SetSpeedSinglePulse(axisnum, conv_fast, act)

    # Set speed (single axis: deg/sec).
    def SetSpeedSingleDegree(self, axisnum, value, act):
        """
        Sets the speed for a single axis in degrees per second.

        Args:
            axisnum (int): The axis number to set the speed for.
            value (float): The fast speed setting in degrees per second.
            act (int): The acceleration/deceleration time in milliseconds.

        Returns:
            bool: True if the speed setting was successful, False otherwise.
        """
        conv_fast = int(value // self.__axis[axisnum - 1].PulseToDegree)
        return self.SetSpeedSinglePulse(axisnum, conv_fast, act)

    # Set speed (all axes: pulse/sec).
    def SetSpeedAllPulse(self, value, act):
        """
        Sets the speed for all axes in pulses per second.

        Args:
            value (list): A list of fast speed settings for all axes in pulses per second.
            act (list): A list of acceleration/deceleration times for all axes in milliseconds.

        Returns:
            bool: True if the speed settings were successful, False otherwise.
        """
        slow = [0] * self.__axis_count
        for i in range(self.__axis_count):
            slow[i] = value[i] / 2  # Automatically set Slow speed based on Fast speed

        # Check speed parameters for all axes
        for j in range(self.__axis_count):
            if not self.CheckSpeedParameters(value[j], slow[j], act[j]):
                return False

        sendcom = "D:W"
        for k in range(self.__axis_count):
            sendcom += f"S{slow[k]:.0f}F{value[k]:.0f}R{act[k]:.0f}"
            
        sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
        reccom = ""

        try:
            # Initialize send/receive buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            # Send command
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            # Receive command response (OK/NG)
            reccom = self.comports.readline()

            # Confirm speed parameters
            if reccom == self.RECCOM_OK:
                for n in range(self.__axis_count):
                    self.__axis[n].SpeedFastPulse = value[n]
                    self.__axis[n].SpeedSlowPulse = slow[n]
                    self.__axis[n].SpeedActMillisecond = act[n]
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

        return False

    # Set speed (all axes: nm/sec).
    def SetSpeedAllNanometer(self, value, act):
        """
        Sets the speed for all axes in nanometers per second.

        Args:
            value (list): A list of fast speed settings for all axes in nanometers per second.
            act (list): A list of acceleration/deceleration times for all axes in milliseconds.

        Returns:
            bool: True if the speed settings were successful, False otherwise.
        """
        conv_fast = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_fast[i] = value[i] // self.__axis[i].PulseToNanometer
        return self.SetSpeedAllPulse(conv_fast, act)

    # Set speed (all axes: um/sec).
    def SetSpeedAllMicrometer(self, value, act):
        """
        Sets the speed for all axes in micrometers per second.

        Args:
            value (list): A list of fast speed settings for all axes in micrometers per second.
            act (list): A list of acceleration/deceleration times for all axes in milliseconds.

        Returns:
            bool: True if the speed settings were successful, False otherwise.
        """
        conv_fast = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_fast[i] = int(value[i] // self.__axis[i].PulseToMicrometer)
        return self.SetSpeedAllPulse(conv_fast, act)

    # Set speed (all axes: mm/sec).
    def SetSpeedAllMillimeter(self, value, act):
        """
        Sets the speed for all axes in millimeters per second.

        Args:
            value (list): A list of fast speed settings for all axes in millimeters per second.
            act (list): A list of acceleration/deceleration times for all axes in milliseconds.

        Returns:
            bool: True if the speed settings were successful, False otherwise.
        """
        conv_fast = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_fast[i] = int(value[i] / self.__axis[i].PulseToMillimeter)
        return self.SetSpeedAllPulse(conv_fast, act)

    # Set speed (all axes: deg/sec).
    def SetSpeedAllDegree(self, value, act):
        """
        Sets the speed for all axes in degrees per second.

        Args:
            value (list): A list of fast speed settings for all axes in degrees per second.
            act (list): A list of acceleration/deceleration times for all axes in milliseconds.

        Returns:
            bool: True if the speed settings were successful, False otherwise.
        """
        conv_fast = [0] * self.__axis_count
        for i in range(self.__axis_count):
            conv_fast[i] = int(value[i] // self.__axis[i].PulseToDegree)
        return self.SetSpeedAllPulse(conv_fast, act)

    # Interpolation (x,Y)
    def LinearInterpolationPulse(self, move_x, move_y):
        """
        Performs linear interpolation in pulses for two axes (x and Y).

        Args:
            move_x (int): The relative movement in pulses along the x-axis.
            move_y (int): The relative movement in pulses along the Y-axis.

        Returns:
            bool: True if the interpolation was successful, False otherwise.
        """
        safe_x = self.TrimStrokeLimitPulse(1, self.GetPositionPulse(1) + move_x)
        safe_y = self.TrimStrokeLimitPulse(2, self.GetPositionPulse(2) + move_y)
        direc_x = "+" if safe_x > 0 else "-"
        direc_y = "+" if safe_y > 0 else "-"

        try:
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            sendcom1 = f"K:W{direc_x}P{abs(safe_x):.0f}{direc_y}P{abs(safe_y):.0f}"
            sendcom1= bytes(sendcom1, encoding="ascii") + b'\r\n'
            self.comports.write(sendcom1)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            reccom1 = self.comports.readline()
            if reccom1 == self.RECCOM_OK:
                sendcom2 = "G:"
                sendcom2= bytes(sendcom2, encoding="ascii") + b'\r\n'
                self.comports.write(sendcom2)

                # Sleep briefly to allow time for data to be received
                time.sleep(0.1)

                reccom2 = self.comports.readline()
                if reccom2 == self.RECCOM_OK:
                    return True


        except Exception as ex:
            self.__last_error_message = str(ex)
            return False
        
        return False

    # interpolation nanometer
    def LinearInterpolationNanometer(self, move_x, move_y):
        """
        Performs linear interpolation in nanometers for two axes (x and Y).

        Args:
            move_x (float): The relative movement in nanometers along the x-axis.
            move_y (float): The relative movement in nanometers along the Y-axis.

        Returns:
            bool: True if the interpolation was successful, False otherwise.
        """
        return self.LinearInterpolationPulse(move_x / self.__axis(1).PulseToNanometer, move_y / self.__axis(2).PulseToNanometer)

    # interpolation micrometer
    def LinearInterpolationMicrometer(self, move_x, move_y):
        """
        Performs linear interpolation in micrometers for two axes (x and Y).

        Args:
            move_x (float): The relative movement in micrometers along the x-axis.
            move_y (float): The relative movement in micrometers along the Y-axis.

        Returns:
            bool: True if the interpolation was successful, False otherwise.
        """
        return self.LinearInterpolationPulse(move_x / self.__axis(1).PulseToMicrometer, move_y / self.__axis(2).PulseToMicrometer)

    # interpolation mm
    def LinearInterpolationMillimeter(self, move_x, move_y):
        """
        Performs linear interpolation in millimeters for two axes (x and y).

        Args:
            move_x (float): The relative movement in millimeters along the x-axis.
            move_y (float): The relative movement in millimeters along the y-axis.

        Returns:
            bool: True if the interpolation was successful, False otherwise.
        """
        return self.LinearInterpolationPulse(move_x / self.__axis[0].PulseToMillimeter, move_y / self.__axis[1].PulseToMillimeter)
    
    #　Set resolution
    def SetResolution(self, axisnum, value):
        """
        Sets the resolution (division number) for a specific axis.

        Args:
            axisnum (int): The axis number.
            value (float): The new resolution value.

        Returns:
            bool: True if the resolution was set successfully, False otherwise.
        """
        try:
            self.comports.flushOutput()
            self.comports.reset_input_buffer()

            sendcom = f"S:{axisnum}{value:.0f}"
            sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)

            reccom = self.comports.readline()
            if reccom == self.RECCOM_OK:
                #self.__axis[axisnum-1].SetDefaultparameterByDiv(value)
                self.__axis[axisnum-1].DivisionNumber = value
                return True
            elif reccom == self.RECCOM_NG:
                self.__last_error_message = "error in reading serial "+ reccom
            else:
                self.__last_error_message = "no reading data"

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False
        
        return False

    # Generic command for sending and receiving data
    def GenericCommand(self, sendcom):
        """
        Sends a generic command and receives a response.

        Args:
            sendcom (str): The command to send.

        Returns:
            bool: True if the command was sent and received successfully, False otherwise.
        """
        try:
            # Initialize communication buffers
            self.comports.flushOutput()
            self.comports.reset_input_buffer()
            
            # Send the command
            sendcom= bytes(sendcom, encoding="ascii") + b'\r\n'
            self.comports.write(sendcom)

            # Sleep briefly to allow time for data to be received
            time.sleep(0.1)
            
            # Read the response
            reccom = self.comports.readline()
            self.__send_command = sendcom
            self.__receive_command = reccom

            return True

        except Exception as ex:
            self.__last_error_message = str(ex)
            return False      
    
    # Open the COM port
    def OpenSerialPort(self, port, controller, bRate=BaudRateclass.BR_9600):
        """
        Opens the specified COM port with the given controller model and baud rate.

        Args:
            port (str): The COM port to open.
            controller (str): The model of the controller (e.g., "GIP-101", "SHOT-702 / SHOT-302GS").
            bRate (int): The baud rate for communication (default is BaudRateclass.BR_9600).

        Returns:
            bool: True if the COM port was successfully opened, False otherwise.
        """
        try:
            # Set the controller model for reference
            self.__controller_model = controller

            # Configure the serial port based on the controller model
            if self.__controller_model == "GIP-101":
                ser = serial.Serial(port, baudrate=bRate, timeout=0, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS)
            elif self.__controller_model in ["SHOT-702", "SHOT-302GS", "SHOT-304GS"]:
                ser = serial.Serial(port, baudrate=bRate, timeout=0, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS)
            else:
                ser = serial.Serial(port, baudrate=bRate, timeout=0, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS)

            # Set the 'comports' attribute to the opened serial port
            self.comports = ser

            return True  # Successful COM port opening

        except Exception as ex:
            # Capture and store any exceptions that occur
            self.__last_error_message = str(ex)
            return False  # Failed to open COM port

    # Close the COM port
    def CloseSerialPort(self):
        """
        Closes the opened COM port.

        Returns:
            bool: True if the COM port was successfully closed, False otherwise.
        """
        try:
            if (self.comports.is_open):
                self.comports.close()
                return True
            else:
                self.__last_error_message= "comport is already closed"
                return False           
        except Exception as ex:
            self.__last_error_message = str(ex)
            return False

    # Connect to the COM port and update status simultaneously
    def IsComConnected(self):
        """
        Checks if the COM port is connected and updates the status if possible.

        Returns:
            bool: True if the COM port is connected and status updated, False otherwise.
        """
        if not self.comports.is_open:
            return False

        # Check and connect while also requesting the status
        if self.UpdateStatus():
            return True
        else:
            self.CloseSerialPort()

        return False

    #endregion 
