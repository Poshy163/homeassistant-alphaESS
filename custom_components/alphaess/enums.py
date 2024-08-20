"""Parent class for AlphaESSNames enum."""
from enum import Enum, unique


@unique
class AlphaESSNames(str, Enum):
    """Device names used by AlphaESS."""

    SolarProduction = "Solar Production"
    SolarToBattery = "Solar to Battery"
    SolarToGrid = "Solar to Grid"
    SolarToLoad = "Solar to Load"
    TotalLoad = "Total Load"
    GridToLoad = "Grid to Load"
    GridToBattery = "Grid to Battery"
    StateOfCharge = "State of Charge"
    Charge = "Charge"
    Discharge = "Discharge"
    EVCharger = "EV Charger"
    Generation = "Instantaneous Generation"
    PPV1 = "Instantaneous PPV1"
    PPV2 = "Instantaneous PPV2"
    PPV3 = "Instantaneous PPV3"
    PPV4 = "Instantaneous PPV4"
    BatterySOC = "Instantaneous Battery SOC"
    BatteryIO = "Instantaneous Battery I/O"
    GridIOTotal = "Instantaneous Grid I/O Total"
    GridIOL1 = "Instantaneous Grid I/O L1"
    GridIOL2 = "Instantaneous Grid I/O L2"
    GridIOL3 = "Instantaneous Grid I/O L3"
    Load = "Instantaneous Load"
    Income = "Total Income"
    SelfSufficiency = "Self Sufficiency"
    SelfConsumption = "Self Consumption"
    EmsStatus = "EMS Status"
    usCapacity = "Maximum Battery Capacity"
    cobat = "Installed Capacity"
    surplusCobat = "Current Capacity"

