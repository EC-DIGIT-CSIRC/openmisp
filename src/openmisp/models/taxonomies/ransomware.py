"""Taxonomy model for ransomware types and elements."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RansomwareTaxonomyPredicate(str, Enum):
    TYPE = "type"
    ELEMENT = "element"
    COMPLEXITY_LEVEL = "complexity-level"
    PURPOSE = "purpose"
    TARGET = "target"
    INFECTION = "infection"
    COMMUNICATION = "communication"
    MALICIOUS_ACTION = "malicious-action"


class RansomwareTaxonomyTypeEntry(str, Enum):
    SCAREWARE = "scareware"
    LOCKER_RANSOMWARE = "locker-ransomware"
    CRYPTO_RANSOMWARE = "crypto-ransomware"


class RansomwareTaxonomyElementEntry(str, Enum):
    RANSOMNOTE = "ransomnote"
    RANSOMWARE_APPENDED_EXTENSION = "ransomware-appended-extension"
    RANSOMWARE_ENCRYPTED_EXTENSIONS = "ransomware-encrypted-extensions"
    RANSOMWARE_EXCLUDED_EXTENSIONS = "ransomware-excluded-extensions"
    DROPPER = "dropper"
    DOWNLOADER = "downloader"


class RansomwareTaxonomyComplexityLevelEntry(str, Enum):
    NO_ACTUAL_ENCRYPTION_SCAREWARE = "no-actual-encryption-scareware"
    DISPLAY_RANSOMNOTE_BEFORE_ENCRYPTING = "display-ransomnote-before-encrypting"
    DECRYPTION_ESSENTIALS_EXTRACTED_FROM_BINARY = "decryption-essentials-extracted-from-binary"
    DERIVED_ENCRYPTION_KEY_PREDICTED__ = "derived-encryption-key-predicted  "
    SAME_KEY_USED_FOR_EACH_INFECTION = "same-key used-for-each-infection"
    ENCRYPTION_CIRCUMVENTED = "encryption-circumvented"
    FILE_RESTORATION_POSSIBLE_USING_SHADOW_VOLUME_COPIES = "file-restoration-possible-using-shadow-volume-copies"
    FILE_RESTORATION_POSSIBLE_USING_BACKUPS = "file-restoration-possible-using-backups"
    KEY_RECOVERED_FROM_FILE_SYSTEM_OR_MEMORY = "key-recovered-from-file-system-or-memory"
    DUE_DILIGENCE_PREVENTED_RANSOMWARE_FROM_ACQUIRING_KEY = "due-diligence-prevented-ransomware-from-acquiring-key"
    CLICK_AND_RUN_DECRYPTOR_EXISTS = "click-and-run-decryptor-exists"
    KILL_SWITCH_EXISTS_OUTSIDE_OF_ATTACKER_S_CONTROL = "kill-switch-exists-outside-of-attacker-s-control"
    DECRYPTION_KEY_RECOVERED_FROM_A_C_C_SERVER_OR_NETWORK_COMMUNICATIONS = (
        "decryption-key-recovered-from-a-C&C-server-or-network-communications"
    )
    CUSTOM_ENCRYPTION_ALGORITHM_USED = "custom-encryption-algorithm-used"
    DECRYPTION_KEY_RECOVERED_UNDER_SPECIALIZED_LAB_SETTING = "decryption-key-recovered-under-specialized-lab-setting"
    SMALL_SUBSET_OF_FILES_LEFT_UNENCRYPTED = "small-subset-of-files-left-unencrypted"
    ENCRYPTION_MODEL_IS_SEEMINGLY_FLAWLESS = "encryption-model-is-seemingly-flawless"


class RansomwareTaxonomyPurposeEntry(str, Enum):
    DEPLOYED_AS_RANSOMWARE_EXTORTION = "deployed-as-ransomware-extortion"
    DEPLOYED_TO_SHOWCASE_SKILLS_FOR_FUN_OR_FOR_TESTING_PURPOSES = (
        "deployed-to-showcase-skills-for-fun-or-for-testing-purposes"
    )
    DEPLOYED_AS_SMOKESCREEN = "deployed-as-smokescreen"
    DEPLOYED_TO_CAUSE_FRUSTRATION = "deployed-to-cause-frustration"
    DEPLOYED_OUT_OF_FRUSTRATION = "deployed-out-of-frustration"
    DEPLOYED_AS_A_COVER_UP = "deployed-as-a-cover-up"
    DEPLOYED_AS_A_PENETRATION_TEST_OR_USER_AWARENESS_TRAINING = (
        "deployed-as-a-penetration-test-or-user-awareness-training"
    )
    DEPLOYED_AS_A_MEANS_OF_DISRUPTION_DESTRUCTION = "deployed-as-a-means-of-disruption-destruction"


class RansomwareTaxonomyTargetEntry(str, Enum):
    PC_WORKSTATION = "pc-workstation"
    NAS = "nas"
    VM = "vm"
    MOBILE_DEVICE = "mobile-device"
    IOT_CPS_DEVICE = "iot-cps-device"
    END_USER = "end-user"
    ORGANISATION = "organisation"


class RansomwareTaxonomyInfectionEntry(str, Enum):
    PHISHING_E_MAILS = "phishing-e=mails"
    SMS_INSTANT_MESSAGE = "sms-instant-message"
    MALICIOUS_APPS = "malicious-apps"
    DRIVE_BY_DOWNLOAD = "drive-by-download"
    VULNERABILITIES = "vulnerabilities"


class RansomwareTaxonomyCommunicationEntry(str, Enum):
    HARD_CODED_IP = "hard-coded-ip"
    DGA_BASED = "dga-based"


class RansomwareTaxonomyMaliciousActionEntry(str, Enum):
    SYMMETRIC_KEY_ENCRYPTION = "symmetric-key-encryption"
    ASYMMETRIC_KEY_ENCRYPTION = "asymmetric-key-encryption"
    HYBRID_KEY_ENCRYPTION = "hybrid-key-encryption"
    SCREEN_LOCKING = "screen-locking"
    BROWSER_LOCKING = "browser-locking"
    MBR_LOCKING = "mbr-locking"
    DATA_EXFILTRATION = "data-exfiltration"


class RansomwareTaxonomy(BaseModel):
    """Model for the ransomware types and elements taxonomy."""

    namespace: str = "ransomware"
    description: str = """Ransomware is used to define ransomware types and the elements that compose them."""
    version: int = 6
    exclusive: bool = False
    predicates: List[RansomwareTaxonomyPredicate] = []
    type_entries: List[RansomwareTaxonomyTypeEntry] = []
    element_entries: List[RansomwareTaxonomyElementEntry] = []
    complexity_level_entries: List[RansomwareTaxonomyComplexityLevelEntry] = []
    purpose_entries: List[RansomwareTaxonomyPurposeEntry] = []
    target_entries: List[RansomwareTaxonomyTargetEntry] = []
    infection_entries: List[RansomwareTaxonomyInfectionEntry] = []
    communication_entries: List[RansomwareTaxonomyCommunicationEntry] = []
    malicious_action_entries: List[RansomwareTaxonomyMaliciousActionEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
