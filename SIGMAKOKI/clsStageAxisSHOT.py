from enum import Enum

class clsStageAxisSHOT:

    #region Constructor
    def __init__(self):
        # Axis information
        self.position_pulse = self.POSITION_PULSE_DEFAULT
        self.fullstep_um = self.FULLSTEP_MICROMETER_DEFAULT
        self.fullstep_deg = self.FULLSTEP_DEGREE_DEFAULT
        self.division_number = self.DIVISION_NUMBER_DEFAULT
        self.pulse_to_nm = self.PULSE_TO_NANOMETER_DEFAULT
        self.pulse_to_deg = self.PULSE_TO_DEGREE_DEFAULT
        self.limit_state = self.LIMIT_STATE_DEFAULT

        # Speed
        self.speed_fast = self.SPEED_FAST_DEFAULT
        self.speed_slow = self.SPEED_SLOW_DEFAULT
        self.speed_act = self.SPEED_ACT_DEFAULT

        # Stroke limits
        self.stroke_limit_max = self.STROKE_LIMIT_MAX_DEFAULT
        self.stroke_limit_min = self.STROKE_LIMIT_MIN_DEFAULT

        # Machine origin offset
        self.offset_morigin = self.OFFSET_MORIGIN_DEFAULT
    #endregion Data

    #region data & Enumerations
    class DivisionNum(Enum):
        Div1 = 1
        Div2 = 2
        Div4 = 4
        Div5 = 5
        Div8 = 8
        Div10 = 10
        Div20 = 20
        Div25 = 25
        Div40 = 40
        Div50 = 50
        Div80 = 80
        Div100 = 100
        Div125 = 125
        Div200 = 200
        Div250 = 250

    class AxisLimitState:
        LimitState_None =0
        LimitState_Soft =1
        LimitState_Hard =2

    # Initial values
    POSITION_PULSE_DEFAULT = 0
    FULLSTEP_MICROMETER_DEFAULT = 2.0
    FULLSTEP_DEGREE_DEFAULT = 0.005
    DIVISION_NUMBER_DEFAULT = DivisionNum.Div2
    PULSE_TO_NANOMETER_DEFAULT = 100
    PULSE_TO_DEGREE_DEFAULT = 0.0025
    LIMIT_STATE_DEFAULT = AxisLimitState.LimitState_None
    SPEED_FAST_DEFAULT = 30000
    SPEED_SLOW_DEFAULT = 15000
    SPEED_ACT_DEFAULT = 100
    STROKE_LIMIT_MAX_DEFAULT = 99999999
    STROKE_LIMIT_MIN_DEFAULT = -99999999
    OFFSET_MORIGIN_DEFAULT = 0
    MICROMETER_TO_NANOMETER =1000
    #endregion

    #region default data by resolution

    def SetDefaultparameterByDiv(self, div):
        if any(div == item.value for item in clsStageAxisSHOT.DivisionNum):
            self.pulse_to_nm= self.fullstep_um * self.MICROMETER_TO_NANOMETER/div
            self.pulse_to_deg= self.fullstep_deg/div
            return True
        else:
            return False

    #endregion

    #region Properties

    # Fullstep Move Value in Micrometers
    @property
    def FullstepMoveValueMicrometer(self):
        """
        Gets the full step move value in micrometers.

        Returns:
        float: The full step move value in micrometers.
        """
        return self.fullstep_um

    @FullstepMoveValueMicrometer.setter
    def FullstepMoveValueMicrometer(self, value):
        """
        Sets the full step move value in micrometers.

        Args:
        value (float): The full step move value to set in micrometers.

        Returns:
        None
        """
        self.fullstep_um = value

    # Fullstep Move Value in Degrees
    @property
    def FullstepMoveValueDegree(self):
        """
        Gets the full step move value in degrees.

        Returns:
        float: The full step move value in degrees.
        """
        return self.fullstep_deg

    @FullstepMoveValueDegree.setter
    def FullstepMoveValueDegree(self, value):
        """
        Sets the full step move value in degrees.

        Args:
        value (float): The full step move value to set in degrees.

        Returns:
        None
        """
        self.fullstep_deg = value

    # Division Number
    @property
    def DivisionNumber(self):
        """
        Gets the division number.

        Returns:
        int: The division number.
        """
        return self.division_number

    @DivisionNumber.setter
    def DivisionNumber(self, value):
        """
        Sets the division number and updates other parameters accordingly.

        Args:
        value (int): The division number to set.

        Returns:
        None
        """
        self.SetDefaultparameterByDiv(value)
        self.division_number = value

    # Position in Pulses
    @property
    def PositionPulse(self):
        """
        Gets or sets the position in pulses.

        Returns:
        int: The position in pulses.
        """
        return self.position_pulse

    @PositionPulse.setter
    def PositionPulse(self, value):
        """
        Sets the position in pulses.

        Args:
        value (int): The position in pulses to set.

        Returns:
        None
        """
        self.position_pulse = value

    # Position in Nanometers
    @property
    def PositionNanometer(self):
        """
        Gets or sets the position in nanometers.

        Returns:
        float: The position in nanometers.
        """
        return self.position_pulse * self.pulse_to_nm

    @PositionNanometer.setter
    def PositionNanometer(self, value):
        """
        Sets the position in nanometers.

        Args:
        value (float): The position in nanometers to set.

        Returns:
        None
        """
        self.position_pulse = value / self.pulse_to_nm

    # Position in Micrometers
    @property
    def PositionMicrometer(self):
        """
        Gets or sets the position in micrometers.

        Returns:
        float: The position in micrometers.
        """
        return float(self.PositionNanometer / 1000)

    @PositionMicrometer.setter
    def PositionMicrometer(self, value):
        """
        Sets the position in micrometers.

        Args:
        value (float): The position in micrometers to set.

        Returns:
        None
        """
        self.PositionNanometer = int(value * 1000)

    # Position in Millimeters
    @property
    def PositionMillimeter(self):
        """
        Gets or sets the position in millimeters.

        Returns:
        float: The position in millimeters.
        """
        return float(self.PositionNanometer / 1000000)

    @PositionMillimeter.setter
    def PositionMillimeter(self, value):
        """
        Sets the position in millimeters.

        Args:
        value (float): The position in millimeters to set.

        Returns:
        None
        """
        self.PositionNanometer = int(value * 1000000)

    # Position in Degrees
    @property
    def PositionDegree(self):
        """
        Gets or sets the position in degrees.

        Returns:
        float: The position in degrees.
        """
        return float(self.position_pulse * self.pulse_to_deg)

    @PositionDegree.setter
    def PositionDegree(self, value):
        """
        Sets the position in degrees.

        Args:
        value (float): The position in degrees to set.

        Returns:
        None
        """
        self.position_pulse = float(value / self.pulse_to_deg)

    # Pulse to Nanometer Conversion Factor
    @property
    def PulseToNanometer(self):
        """
        Gets or sets the conversion factor from pulses to nanometers.

        Returns:
        float: The pulse to nanometer conversion factor.
        """
        return self.pulse_to_nm

    @PulseToNanometer.setter
    def PulseToNanometer(self, value):
        """
        Sets the pulse to nanometer conversion factor.

        Args:
        value (float): The pulse to nanometer conversion factor to set.

        Returns:
        None
        """
        self.pulse_to_nm = value

    # Pulse to Micrometer Conversion Factor
    @property
    def PulseToMicrometer(self):
        """
        Gets or sets the conversion factor from pulses to micrometers.

        Returns:
        float: The pulse to micrometer conversion factor.
        """
        return float(self.pulse_to_nm / 1000)

    @PulseToMicrometer.setter
    def PulseToMicrometer(self, value):
        """
        Sets the pulse to micrometer conversion factor.

        Args:
        value (float): The pulse to micrometer conversion factor to set.

        Returns:
        None
        """
        self.pulse_to_nm = int(value * 1000)

    # Property for Pulse to millimeter conversion value
    @property
    def PulseToMillimeter(self):
        """
        Sets the pulse to millimeter conversion factor.

        Args:
        value (float): The pulse to millimeter conversion factor to set.

        Returns:
        None
        """
        return float(self.pulse_to_nm / 1000000)

    @PulseToMillimeter.setter
    def PulseToMillimeter(self, value):
        """
        Gets or sets the conversion factor from pulses to degrees.

        Returns:
        float: The pulse to degree conversion factor.
        """
        self.pulse_to_mm = float(value * 1000000)

    # Pulse to Degree Conversion Value
    @property
    def PulseToDegree(self):
        """
        Gets or sets the conversion factor from pulses to degrees.

        Returns:
        float: The pulse to degree conversion factor.
        """
        return self.pulse_to_degree

    @PulseToDegree.setter
    def PulseToDegree(self, value):
        """
        Sets the pulse to degree conversion factor.

        Args:
        value (float): The pulse to degree conversion factor to set.

        Returns:
        None
        """
        self.pulse_to_degree = float(value)

    # Limit State
    @property
    def LimitState(self) -> AxisLimitState:
        """
        Gets or sets the limit state.

        Returns:
        AxisLimitState: The limit state.
        """
        return self.limit_state

    @LimitState.setter
    def LimitState(self, axisLimitState : AxisLimitState):
        """
        Sets the limit state.

        Args:
        axisLimitState (AxisLimitState): The limit state to set.

        Returns:
        None
        """
        self.limit_state = axisLimitState

    # Speed in Pulse per Second
    @property
    def SpeedFastPulse(self):
        """
        Gets or sets the fast speed in pulses per second (F: pulse/sec).

        Returns:
        float: The fast speed in pulses per second.
        """
        return self.speed_fast

    @SpeedFastPulse.setter
    def SpeedFastPulse(self, value):
        """
        Sets the fast speed in pulses per second.

        Args:
        value (float): The fast speed in pulses per second to set.

        Returns:
        None
        """
        self.speed_fast = value

    # Speed in Nanometers per Second
    @property
    def SpeedFastNanometer(self):
        """
        Gets or sets the fast speed in nanometers per second (F: nm/sec).

        Returns:
        float: The fast speed in nanometers per second.
        """
        return self.speed_fast* self.pulse_to_nm

    @SpeedFastNanometer.setter
    def SpeedFastNanometer(self, value):
        """
        Sets the fast speed in nanometers per second.

        Args:
        value (float): The fast speed in nanometers per second to set.

        Returns:
        None
        """
        self.speed_fast = int(value / self.pulse_to_nm)

    # Speed in Micrometers per Second
    @property
    def SpeedFastMicrometer(self):
        """
        Gets or sets the fast speed in micrometers per second (F: um/sec).

        Returns:
        float: The fast speed in micrometers per second.
        """
        return float(self.SpeedFastNanometer / 1000)

    @SpeedFastMicrometer.setter
    def SpeedFastMicrometer(self, value):
        """
        Sets the fast speed in micrometers per second.

        Args:
        value (float): The fast speed in micrometers per second to set.

        Returns:
        None
        """
        self.SpeedFastNanometer = int(value * 1000)

    # Speed in Millimeters per Second
    @property
    def SpeedFastMillimeter(self):
        """
        Gets or sets the fast speed in millimeters per second (F: mm/sec).

        Returns:
        float: The fast speed in millimeters per second.
        """
        return float(self.SpeedFastNanometer / 1000000)

    @SpeedFastMillimeter.setter
    def SpeedFastMillimeter(self, value):
        """
        Sets the fast speed in millimeters per second.

        Args:
        value (float): The fast speed in millimeters per second to set.

        Returns:
        None
        """
        self.SpeedFastNanometer = int(value * 1000000)

    # Speed in Degrees per Second
    @property
    def SpeedFastDegree(self):
        """
        Gets or sets the fast speed in degrees per second (F: deg/sec).
        """
        return float(self.speed_fast * self.pulse_to_deg)

    @SpeedFastDegree.setter
    def SpeedFastDegree(self, value):
        """
        Sets the fast speed in degrees per second.

        Args:
        value (float): The fast speed in degrees per second to set.
        """
        self.speed_fast = int(value / self.pulse_to_deg)

    # Speed Slow in Pulse per Second (S: pulse/sec)
    @property
    def SpeedSlowPulse(self):
        """
        Gets or sets the slow speed in pulses per second (S: pulse/sec).
        """
        return self.speed_slow

    @SpeedSlowPulse.setter
    def SpeedSlowPulse(self, value):
        """
        Sets the slow speed in pulses per second.

        Args:
        value (float): The slow speed in pulses per second to set.
        """
        self.speed_slow = value

    # Acceleration/Deceleration Time in Milliseconds (R: msec)
    @property
    def SpeedActMillisecond(self):
        """
        Gets or sets the acceleration/deceleration time in milliseconds (R: msec).
        """
        return self.speed_act

    @SpeedActMillisecond.setter
    def SpeedActMillisecond(self, value):
        """
        Sets the acceleration/deceleration time in milliseconds.

        Args:
        value (int): The acceleration/deceleration time in milliseconds to set.
        """
        self.speed_act = value

    # Maximum Stroke (Upper Limit) in Pulses
    @property
    def MaxStrokePulse(self):
        """
        Gets or sets the maximum stroke in pulses (upper limit).
        """
        return self.stroke_limit_max

    @MaxStrokePulse.setter
    def MaxStrokePulse(self, value):
        """
        Sets the maximum stroke in pulses (upper limit).

        Args:
        value (int): The maximum stroke in pulses to set.
        """
        self.stroke_limit_max = value

    # Maximum Stroke (Upper Limit) in Nanometers
    @property
    def MaxStrokeNanometer(self):
        """
        Gets or sets the maximum stroke in nanometers (upper limit).
        """
        return self.stroke_limit_max * self.pulse_to_nm

    @MaxStrokeNanometer.setter
    def MaxStrokeNanometer(self, value):
        """
        Sets the maximum stroke in nanometers (upper limit).

        Args:
        value (int): The maximum stroke in nanometers to set.
        """
        self.stroke_limit_max = value / self.pulse_to_nm

    # Maximum Stroke (Upper Limit) in Micrometers
    @property
    def MaxStrokeMicrometer(self):
        """
        Gets or sets the maximum stroke in micrometers (upper limit).
        """
        return float(self.MaxStrokeNanometer / 1000)

    @MaxStrokeMicrometer.setter
    def MaxStrokeMicrometer(self, value):
        """
        Sets the maximum stroke in micrometers (upper limit).

        Args:
        value (float): The maximum stroke in micrometers to set.
        """
        self.MaxStrokeNanometer = int(value * 1000)

    # Maximum Stroke (Upper Limit) in Millimeters
    @property
    def MaxStrokeMillimeter(self):
        """
        Gets or sets the maximum stroke in millimeters (upper limit).
        """
        return float(self.MaxStrokeNanometer / 1000000)

    @MaxStrokeMillimeter.setter
    def MaxStrokeMillimeter(self, value):
        """
        Sets the maximum stroke in millimeters (upper limit).

        Args:
        value (float): The maximum stroke in millimeters to set.
        """
        self.MaxStrokeNanometer = int(value * 1000000)

    # Maximum Stroke (Upper Limit) in Degrees
    @property
    def MaxStrokeDegree(self):
        """
        Gets or sets the maximum stroke in degrees (upper limit).
        """
        return float(self.stroke_limit_max)

    @MaxStrokeDegree.setter
    def MaxStrokeDegree(self, value):
        """
        Sets the maximum stroke in degrees (upper limit).

        Args:
        value (float): The maximum stroke in degrees to set.
        """
        self.stroke_limit_max = int(value / self.pulse_to_deg)

    # Minimum Stroke (Lower Limit) in Pulses
    @property
    def MinStrokePulse(self):
        """
        Gets or sets the minimum stroke in pulses (lower limit).
        """
        return self.stroke_limit_min

    @MinStrokePulse.setter
    def MinStrokePulse(self, value):
        """
        Sets the minimum stroke in pulses (lower limit).

        Args:
        value (int): The minimum stroke in pulses to set.
        """
        self.stroke_limit_min = value

    # Minimum Stroke (Lower Limit) in Nanometers
    @property
    def MinStrokeNanometer(self):
        """
        Gets or sets the minimum stroke in nanometers (lower limit).
        """
        return self.stroke_limit_min * self.pulse_to_nm

    @MinStrokeNanometer.setter
    def MinStrokeNanometer(self, value):
        """
        Sets the minimum stroke in nanometers (lower limit).

        Args:
        value (int): The minimum stroke in nanometers to set.
        """
        self.stroke_limit_min = value / self.pulse_to_nm

    # Minimum Stroke (Lower Limit) in Micrometers
    @property
    def MinStrokeMicrometer(self):
        """
        Gets or sets the minimum stroke in micrometers (lower limit).
        """
        return float(self.MinStrokeNanometer / 1000)

    @MinStrokeMicrometer.setter
    def MinStrokeMicrometer(self, value):
        """
        Sets the minimum stroke in micrometers (lower limit).

        Args:
        value (float): The minimum stroke in micrometers to set.
        """
        self.MinStrokeNanometer = int(value * 1000)

    # Minimum Stroke (Lower Limit) in Millimeters
    @property
    def MinStrokeMillimeter(self):
        """
        Gets or sets the minimum stroke in millimeters (lower limit).
        """
        return float(self.MinStrokeNanometer / 1000000)

    @MinStrokeMillimeter.setter
    def MinStrokeMillimeter(self, value):
        """
        Sets the minimum stroke in millimeters (lower limit).

        Args:
        value (float): The minimum stroke in millimeters to set.
        """
        self.MinStrokeNanometer = int(value * 1000000)

    # Minimum Stroke (Lower Limit) in Degrees
    @property
    def MinStrokeDegree(self):
        """
        Gets or sets the minimum stroke in degrees (lower limit).
        """
        return float(self.stroke_limit_min)

    @MinStrokeDegree.setter
    def MinStrokeDegree(self, value):
        """
        Sets the minimum stroke in degrees (lower limit).

        Args:
        value (float): The minimum stroke in degrees to set.
        """
        self.stroke_limit_min = int(value / self.pulse_to_deg)

    # Offset from Machine Origin in Pulses
    @property
    def OffsetMoriginPulse(self):
        """
        Gets or sets the machine origin offset in pulses (distance between machine origin and electrical origin: pulse).
        """
        return self.offset_morigin

    @OffsetMoriginPulse.setter
    def OffsetMoriginPulse(self, value):
        """
        Sets the machine origin offset in pulses.

        Args:
        value (int): The machine origin offset in pulses to set.
        """
        self.offset_morigin = value

    # Offset from Machine Origin in Nanometers
    @property
    def OffsetMoriginNanometer(self):
        """
        Gets or sets the machine origin offset in nanometers (distance between machine origin and electrical origin: nm).
        """
        return self.offset_morigin * self.pulse_to_nm

    @OffsetMoriginNanometer.setter
    def OffsetMoriginNanometer(self, value):
        """
        Sets the machine origin offset in nanometers.

        Args:
        value (int): The machine origin offset in nanometers to set.
        """
        self.offset_morigin = int(value / self.pulse_to_nm)

    # Offset from Machine Origin in Micrometers
    @property
    def OffsetMoriginMicrometer(self):
        """
        Gets or sets the machine origin offset in micrometers (distance between machine origin and electrical origin: um).
        """
        return float(self.OffsetMoriginNanometer / 1000)

    @OffsetMoriginMicrometer.setter
    def OffsetMoriginMicrometer(self, value):
        """
        Sets the machine origin offset in micrometers.

        Args:
        value (float): The machine origin offset in micrometers to set.
        """
        self.OffsetMoriginNanometer = int(value * 1000)

    # Offset from Machine Origin in Millimeters
    @property
    def OffsetMoriginMillimeter(self):
        """
        Gets or sets the machine origin offset in millimeters (distance between machine origin and electrical origin: mm).
        """
        return float(self.OffsetMoriginNanometer / 1000000)

    @OffsetMoriginMillimeter.setter
    def OffsetMoriginMillimeter(self, value):
        """
        Sets the machine origin offset in millimeters.

        Args:
        value (float): The machine origin offset in millimeters to set.
        """
        self.OffsetMoriginNanometer = int(value * 1000000)

    # Offset from Machine Origin in Degrees
    @property
    def OffsetMoriginDegree(self):
        """
        Gets or sets the machine origin offset in degrees (distance between machine origin and electrical origin: deg).
        """
        return float(self.offset_morigin * self.pulse_to_deg)

    @OffsetMoriginDegree.setter
    def OffsetMoriginDegree(self, value):
        """
        Sets the machine origin offset in degrees.

        Args:
        value (float): The machine origin offset in degrees to set.
        """
        self.offset_morigin = int(value / self.pulse_to_deg)

    #endregion

