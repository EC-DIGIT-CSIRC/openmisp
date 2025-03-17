"""Taxonomy model for Industrial Control System (ICS)."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IcsTaxonomyPredicate(str, Enum):
    OT_SECURITY_ISSUES = "ot-security-issues"
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_AUTOMATIC_AUTOMOBILE_VEHICLE_AVIATION = (
        "ot-network-data-transmission-protocols-automatic-automobile-vehicle-aviation"
    )
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_AUTOMATIC_METER_READING = (
        "ot-network-data-transmission-protocols-automatic-meter-reading"
    )
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_INDUSTRIAL_CONTROL_SYSTEM = (
        "ot-network-data-transmission-protocols-industrial-control-system"
    )
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_BUILDING_AUTOMATION = (
        "ot-network-data-transmission-protocols-building-automation"
    )
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_POWER_SYSTEM_AUTOMATION = (
        "ot-network-data-transmission-protocols-power-system-automation"
    )
    OT_NETWORK_DATA_TRANSMISSION_PROTOCOLS_PROCESS_AUTOMATION = (
        "ot-network-data-transmission-protocols-process-automation"
    )
    OT_COMMUNICATION_INTERFACE = "ot-communication-interface"
    OT_OPERATING_SYSTEMS = "ot-operating-systems"
    OT_COMPONENTS_CATEGORY = "ot-components-category"


class IcsTaxonomyOtSecurityIssuesEntry(str, Enum):
    MESSAGE_AUTHENTICATION = "Message Authentication"
    MESSAGE_INTEGRITY_CHECKING = "Message Integrity Checking"
    MESSAGE_ENCRYPTION = "Message Encryption"
    COMMAND_INJECTION = "Command Injection"
    REPLAY_ATTACK = "Replay Attack"
    MAN_IN_THE_MIDDLE__MITM__ATTACK = "Man in the middle (MITM) Attack"
    UNDOCUMENTED_INSTRUCTIONS = "Undocumented instructions"
    VENDOR_PROPRIETARY_PROTOCOLS = "Vendor proprietary protocols"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticAutomobileVehicleAviationEntry(str, Enum):
    ARINC_429 = "ARINC 429"
    CAN_BUS__ARINC_825_SAE_J1939_NMEA_2000_FMS_ = "CAN bus (ARINC 825 SAE J1939 NMEA 2000 FMS)"
    FACTORY_INSTRUMENTATION_PROTOCOL = "Factory Instrumentation Protocol"
    FLEX_RAY = "FlexRay"
    IEBUS = "IEBus"
    J1587 = "J1587"
    J1708 = "J1708"
    KEYWORD_PROTOCOL_2000 = "Keyword Protocol 2000"
    UNIFIED_DIAGNOSTIC_SERVICES = "Unified Diagnostic Services"
    LIN = "LIN"
    MOST = "MOST"
    VAN = "VAN"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticMeterReadingEntry(str, Enum):
    ANSI_C12_18 = "ANSI C12.18"
    IEC_61107 = "IEC 61107"
    DLMS_IEC_62056 = "DLMS/IEC 62056"
    M_BUS = "M-Bus"
    MODBUS = "Modbus"
    ZIG_BEE = "ZigBee"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsIndustrialControlSystemEntry(str, Enum):
    MTCONNECT = "MTConnect"
    OPC = "OPC"
    DA = "DA"
    HDA = "HDA"
    UA = "UA"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsBuildingAutomationEntry(str, Enum):
    T_1_WIRE = "1-Wire"
    BACNET = "BACnet"
    C_BUS = "C-Bus"
    CEBUS = "CEBus"
    DALI = "DALI"
    DSI = "DSI"
    DY_NET = "DyNet"
    FACTORY_INSTRUMENTATION_PROTOCOL = "Factory Instrumentation Protocol"
    KNX = "KNX"
    LON_TALK = "LonTalk"
    MODBUS = "Modbus"
    O_BIX = "oBIX"
    VSCP = "VSCP"
    X10 = "X10"
    X_AP = "xAP"
    X_PL = "xPL"
    ZIG_BEE = "ZigBee"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsPowerSystemAutomationEntry(str, Enum):
    IEC_60870 = "IEC 60870"
    DNP3 = "DNP3"
    FACTORY_INSTRUMENTATION_PROTOCOL = "Factory Instrumentation Protocol"
    IEC_61850 = "IEC 61850"
    IEC_62351 = "IEC 62351"
    MODBUS = "Modbus"
    PROFIBUS = "Profibus"


class IcsTaxonomyOtNetworkDataTransmissionProtocolsProcessAutomationEntry(str, Enum):
    AS_I = "AS-i"
    BSAP = "BSAP"
    CC_LINK_INDUSTRIAL_NETWORKS = "CC-Link Industrial Networks"
    CIP = "CIP"
    CAN_BUS = "CAN bus"
    CONTROL_NET = "ControlNet"
    DF_1 = "DF-1"
    DIRECT_NET = "DirectNET"
    ETHER_CAT = "EtherCAT"
    ETHERNET_GLOBAL_DATA__EGD_ = "Ethernet Global Data (EGD)"
    ETHERNET_POWERLINK = "Ethernet Powerlink"
    ETHER_NET_IP = "EtherNet/IP"
    EXPERIMENTAL_PHYSICS_AND_INDUSTRIAL_CONTROL_SYSTEM__EPICS__STREAM_DEVICE_PROTOCOL__I_E_RF_FREQ_499_655_MHZ_ = (
        "Experimental Physics and Industrial Control System (EPICS) StreamDevice protocol (i.e RF:FREQ 499.655 MHZ)"
    )
    FACTORY_INSTRUMENTATION_PROTOCOL = "Factory Instrumentation Protocol"
    FINS = "FINS"
    FOUNDATION_FIELDBUS__H1_HSE_ = "FOUNDATION fieldbus (H1 HSE)"
    GE_SRTP = "GE SRTP"
    HART_PROTOCOL = "HART Protocol"
    HONEYWELL_SDS = "Honeywell SDS"
    HOST_LINK = "HostLink"
    INTERBUS = "INTERBUS"
    IO_LINK = "IO-Link"
    MECHATROLINK = "MECHATROLINK"
    MELSEC_NET = "MelsecNet"
    MODBUS = "Modbus"
    OPTOMU = "Optomu"
    PIE_P = "PieP"
    PROFIBUS = "Profibus"
    PROFINET_IO = "PROFINET IO"
    RAPIENET = "RAPIEnet"
    SERCOS_INTERFACE = "SERCOS interface"
    SERCOS_III = "SERCOS III"
    SINEC_H1 = "Sinec H1"
    SYNQ_NET = "SynqNet"
    TTETHERNET = "TTEthernet"
    TCP_IP = "TCP/IP"


class IcsTaxonomyOtCommunicationInterfaceEntry(str, Enum):
    RS_232 = "rs-232"
    RS_422__RS_423_OR_RS_485 = "rs-422, rs-423 or rs-485"
    IEEE_488_GPIB = "ieee-488-gpib"
    IEEE_1394_FIREWIRE = "ieee-1394-firewire"
    USB_UNIVERSAL_SERIAL_BUS = "usb-universal-serial-bus"
    ETHERNET = "ethernet"
    OTHERS = "others"


class IcsTaxonomyOtOperatingSystemsEntry(str, Enum):
    RTOS = "rtos"
    LINUX_EMBEDDED_BASE_OS = "linux-embedded-base-os"
    BSD = "bsd"
    MICROSOFT = "microsoft"


class IcsTaxonomyOtComponentsCategoryEntry(str, Enum):
    PROGRAMMABLE_LOGIC_CONTROLLER = "programmable-logic-controller"
    REMOTE_TERMINAL_UNIT = "remote-terminal-unit"
    HUMAN_MACHINE_INTERFACE = "human-machine-interface"
    SENSORS = "sensors"
    ACTUATORS = "actuators"
    COMMUNICATIONS = "communications"
    SUPERVISORY_LEVEL_DEVICES = "supervisory-level-devices"


class IcsTaxonomy(BaseModel):
    """Model for the Industrial Control System (ICS) taxonomy."""

    namespace: str = "ics"
    description: str = """FIRST.ORG CTI SIG - MISP Proposal for ICS/OT Threat Attribution (IOC) Project"""
    version: int = 1
    exclusive: bool = False
    predicates: List[IcsTaxonomyPredicate] = []
    ot_security_issues_entries: List[IcsTaxonomyOtSecurityIssuesEntry] = []
    ot_network_data_transmission_protocols_automatic_automobile_vehicle_aviation_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticAutomobileVehicleAviationEntry
    ] = []
    ot_network_data_transmission_protocols_automatic_meter_reading_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticMeterReadingEntry
    ] = []
    ot_network_data_transmission_protocols_industrial_control_system_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsIndustrialControlSystemEntry
    ] = []
    ot_network_data_transmission_protocols_building_automation_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsBuildingAutomationEntry
    ] = []
    ot_network_data_transmission_protocols_power_system_automation_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsPowerSystemAutomationEntry
    ] = []
    ot_network_data_transmission_protocols_process_automation_entries: List[
        IcsTaxonomyOtNetworkDataTransmissionProtocolsProcessAutomationEntry
    ] = []
    ot_communication_interface_entries: List[IcsTaxonomyOtCommunicationInterfaceEntry] = []
    ot_operating_systems_entries: List[IcsTaxonomyOtOperatingSystemsEntry] = []
    ot_components_category_entries: List[IcsTaxonomyOtComponentsCategoryEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
