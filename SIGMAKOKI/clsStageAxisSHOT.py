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

    @property
    def FullstepMoveValueMicrometer(self):
        return self.fullstep_um

    @FullstepMoveValueMicrometer.setter
    def FullstepMoveValueMicrometer(self, value):
        self.fullstep_um = value

    @property
    def FullstepMoveValueDegree(self):
        return self.fullstep_deg

    @FullstepMoveValueDegree.setter
    def FullstepMoveValueDegree(self, value):
        self.fullstep_deg = value

    @property
    def DivisionNumber(self):
        return self.division_number

    @DivisionNumber.setter
    def DivisionNumber(self, value):
        self.SetDefaultparameterByDiv(value)
        self.division_number = value

    @property
    def PositionPulse(self):
        """
        Gets or sets the position in pulses.
        """
        return self.position_pulse

    @PositionPulse.setter
    def PositionPulse(self, value):
        self.position_pulse = value

    @property
    def PositionNanometer(self):
        """
        Gets or sets the position in nanometers.
        """
        return self.position_pulse * self.pulse_to_nm

    @PositionNanometer.setter
    def PositionNanometer(self, value):
        self.position_pulse = value / self.pulse_to_nm

    @property
    def PositionMicrometer(self):
        """
        Gets or sets the position in micrometers.
        """
        return float(self.PositionNanometer / 1000)

    @PositionMicrometer.setter
    def PositionMicrometer(self, value):
        self.PositionNanometer = int(value * 1000)

    @property
    def PositionMillimeter(self):
        """
        Gets or sets the position in millimeters.
        """
        return float(self.PositionNanometer / 1000000)

    @PositionMillimeter.setter
    def PositionMillimeter(self, value):
        self.PositionNanometer = int(value * 1000000)

    @property
    def PositionDegree(self):
        """
        Gets or sets the position in degrees.
        """
        return float(self.position_pulse * self.pulse_to_deg)

    @PositionDegree.setter
    def PositionDegree(self, value):
        self.position_pulse = float(value / self.pulse_to_deg)

    @property
    def PulseToNanometer(self):
        """
        Gets or sets the conversion factor from pulses to nanometers.
        """
        return self.pulse_to_nm

    @PulseToNanometer.setter
    def PulseToNanometer(self, value):
        self.pulse_to_nm = value

    @property
    def PulseToMicrometer(self):
        """
        Gets or sets the conversion factor from pulses to micrometers.
        """
        return float(self.pulse_to_nm / 1000)

    @PulseToMicrometer.setter
    def PulseToMicrometer(self, value):
        self.pulse_to_nm = int(value * 1000)

    # Property for Pulse to millimeter conversion value
    @property
    def PulseToMillimeter(self):
        """ 
        Property for Pulse to millimeter conversion value
        """
        return float(self.pulse_to_nm / 1000000)

    @PulseToMillimeter.setter
    def PulseToMillimeter(self, value):
        self.pulse_to_mm = float(value * 1000000)

    
    @property
    def PulseToDegree(self):
        """
        Property for Pulse to degree conversion value
        """
        return self.pulse_to_degree

    @PulseToDegree.setter
    def PulseToDegree(self, value):
        self.pulse_to_degree = float(value)

    @property
    def LimitState(self) -> AxisLimitState:
        """
        Property for Limit state
        """
        return self.limit_state

    @LimitState.setter
    def LimitState(self, axisLimitState : AxisLimitState):
        self.limit_state = axisLimitState

    @property
    def SpeedFastPulse(self):
        """
        Property for Speed (F: pulse/sec)
        """
        return self.speed_fast

    @SpeedFastPulse.setter
    def SpeedFastPulse(self, value):
        self.speed_fast = value

    @property
    def SpeedFastNanometer(self):
        """
        Property for Speed (F: nm/sec)
        """
        return self.speed_fast* self.pulse_to_nm

    @SpeedFastNanometer.setter
    def SpeedFastNanometer(self, value):
        self.speed_fast = int(value / self.pulse_to_nm)

    @property
    def SpeedFastMicrometer(self):
        """
        Gets or sets the fast speed in micrometers per second (F: um/sec).
        """
        return float(self.SpeedFastNanometer / 1000)

    @SpeedFastMicrometer.setter
    def SpeedFastMicrometer(self, value):
        self.SpeedFastNanometer = int(value * 1000)

    @property
    def SpeedFastMillimeter(self):
        """
        Gets or sets the fast speed in millimeters per second (F: mm/sec).
        """
        return float(self.SpeedFastNanometer / 1000000)

    @SpeedFastMillimeter.setter
    def SpeedFastMillimeter(self, value):
        self.SpeedFastNanometer = int(value * 1000000)

    @property
    def SpeedFastDegree(self):
        """
        Gets or sets the fast speed in degrees per second (F: deg/sec).
        """
        return float(self.speed_fast * self.pulse_to_deg)

    @SpeedFastDegree.setter
    def SpeedFastDegree(self, value):
        self.speed_fast = int(value / self.pulse_to_deg)

    @property
    def SpeedSlowPulse(self):
        """
        Gets or sets the slow speed in pulses per second (S: pulse/sec).
        """
        return self.speed_slow

    @SpeedSlowPulse.setter
    def SpeedSlowPulse(self, value):
        self.speed_slow = value

    @property
    def SpeedActMillisecond(self):
        """
        Gets or sets the acceleration/deceleration time in milliseconds (R: msec).
        """
        return self.speed_act

    @SpeedActMillisecond.setter
    def SpeedActMillisecond(self, value):
        self.speed_act = value

    @property
    def MaxStrokePulse(self):
        """
        Gets or sets the maximum stroke in pulses (upper limit).
        """
        return self.stroke_limit_max

    @MaxStrokePulse.setter
    def MaxStrokePulse(self, value):
        self.stroke_limit_max = value

    @property
    def MaxStrokeNanometer(self):
        """
        Gets or sets the maximum stroke in nanometers (upper limit).
        """
        return self.stroke_limit_max * self.pulse_to_nm

    @MaxStrokeNanometer.setter
    def MaxStrokeNanometer(self, value):
        self.stroke_limit_max = value / self.pulse_to_nm

    @property
    def MaxStrokeMicrometer(self):
        """
        Gets or sets the maximum stroke in micrometers (upper limit).
        """
        return float(self.MaxStrokeNanometer / 1000)

    @MaxStrokeMicrometer.setter
    def MaxStrokeMicrometer(self, value):
        self.MaxStrokeNanometer = int(value * 1000)

    @property
    def MaxStrokeMillimeter(self):
        """
        Gets or sets the maximum stroke in millimeters (upper limit).
        """
        return float(self.MaxStrokeNanometer / 1000000)

    @MaxStrokeMillimeter.setter
    def MaxStrokeMillimeter(self, value):
        self.MaxStrokeNanometer = int(value * 1000000)

    @property
    def MaxStrokeDegree(self):
        """
        Gets or sets the maximum stroke in degrees (upper limit).
        """
        return float(self.stroke_limit_max)

    @MaxStrokeDegree.setter
    def MaxStrokeDegree(self, value):
        self.stroke_limit_max = int(value / self.pulse_to_deg)

    @property
    def MinStrokePulse(self):
        """
        Gets or sets the minimum stroke in pulses (lower limit).
        """
        return self.stroke_limit_min

    @MinStrokePulse.setter
    def MinStrokePulse(self, value):
        self.stroke_limit_min = value

    @property
    def MinStrokeNanometer(self):
        """
        Gets or sets the minimum stroke in nanometers (lower limit).
        """
        return self.stroke_limit_min * self.pulse_to_nm

    @MinStrokeNanometer.setter
    def MinStrokeNanometer(self, value):
        self.stroke_limit_min = value / self.pulse_to_nm

    @property
    def MinStrokeMicrometer(self):
        """
        Gets or sets the minimum stroke in micrometers (lower limit).
        """
        return float(self.MinStrokeNanometer / 1000)

    @MinStrokeMicrometer.setter
    def MinStrokeMicrometer(self, value):
        self.MinStrokeNanometer = int(value * 1000)

    @property
    def MinStrokeMillimeter(self):
        """
        Gets or sets the minimum stroke in millimeters (lower limit).
        """
        return float(self.MinStrokeNanometer / 1000000)

    @MinStrokeMillimeter.setter
    def MinStrokeMillimeter(self, value):
        self.MinStrokeNanometer = int(value * 1000000)

    @property
    def MinStrokeDegree(self):
        """
        Gets or sets the minimum stroke in degrees (lower limit).
        """
        return float(self.stroke_limit_min)

    @MinStrokeDegree.setter
    def MinStrokeDegree(self, value):
        self.stroke_limit_min = int(value / self.pulse_to_deg)

    @property
    def OffsetMoriginPulse(self):
        """
        Gets or sets the machine origin offset in pulses (distance between machine origin and electrical origin: pulse).
        """
        return self.offset_morigin

    @OffsetMoriginPulse.setter
    def OffsetMoriginPulse(self, value):
        self.offset_morigin = value

    @property
    def OffsetMoriginNanometer(self):
        """
        Gets or sets the machine origin offset in nanometers (distance between machine origin and electrical origin: nm).
        """
        return self.offset_morigin * self.pulse_to_nm

    @OffsetMoriginNanometer.setter
    def OffsetMoriginNanometer(self, value):
        self.offset_morigin = int(value / self.pulse_to_nm)

    @property
    def OffsetMoriginMicrometer(self):
        """
        Gets or sets the machine origin offset in micrometers (distance between machine origin and electrical origin: um).
        """
        return float(self.OffsetMoriginNanometer / 1000)

    @OffsetMoriginMicrometer.setter
    def OffsetMoriginMicrometer(self, value):
        self.OffsetMoriginNanometer = int(value * 1000)

    @property
    def OffsetMoriginMillimeter(self):
        """
        Gets or sets the machine origin offset in millimeters (distance between machine origin and electrical origin: mm).
        """
        return float(self.OffsetMoriginNanometer / 1000000)

    @OffsetMoriginMillimeter.setter
    def OffsetMoriginMillimeter(self, value):
        self.OffsetMoriginNanometer = int(value * 1000000)

    @property
    def OffsetMoriginDegree(self):
        """
        Gets or sets the machine origin offset in degrees (distance between machine origin and electrical origin: deg).
        """
        return float(self.offset_morigin * self.pulse_to_deg)

    @OffsetMoriginDegree.setter
    def OffsetMoriginDegree(self, value):
        self.offset_morigin = int(value / self.pulse_to_deg)

    #endregion

