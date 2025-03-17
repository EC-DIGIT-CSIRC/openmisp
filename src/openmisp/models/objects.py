# This mapping is automatically generated from MISP data

from enum import Enum
from typing import Dict

from .attributes import AttributeType


class ObjectType(Enum):
    ABUSEIPDB = "abuseipdb"
    ADS = "ADS"
    AIL_LEAK = "ail-leak"
    AIS = "ais"
    AIS_INFO = "ais-info"
    AI_CHAT_PROMPT = "ai-chat-prompt"
    ANDROID_APP = "android-app"
    ANDROID_PERMISSION = "android-permission"
    ANNOTATION = "annotation"
    ANONYMISATION = "anonymisation"
    APIVOID_EMAIL_VERIFICATION = "apivoid-email-verification"
    ARTIFACT = "artifact"
    ASN = "asn"
    ATTACKER_INFRA = "attacker-infra"
    ATTACK_PATTERN = "attack-pattern"
    ATTACK_STEP = "attack-step"
    AUTHENTICATION_FAILURE_REPORT = "authentication-failure-report"
    AUTHENTICODE_SIGNERINFO = "authenticode-signerinfo"
    AVAILABILITY_IMPACT = "availability-impact"
    AV_SIGNATURE = "av-signature"
    BANK_ACCOUNT = "bank-account"
    BGP_HIJACK = "bgp-hijack"
    BGP_RANKING = "bgp-ranking"
    BLOG = "blog"
    BOLETO = "boleto"
    BTC_TRANSACTION = "btc-transaction"
    BTC_WALLET = "btc-wallet"
    C2_LIST = "c2-list"
    CAP_ALERT = "cap-alert"
    CAP_INFO = "cap-info"
    CAP_RESOURCE = "cap-resource"
    CERT_PL_PHISHING = "cert-pl-phishing"
    CLOTH = "cloth"
    COIN_ADDRESS = "coin-address"
    COMMAND = "command"
    COMMAND_LINE = "command-line"
    CONCORDIA_MTMF_INTRUSION_SET = "concordia-mtmf-intrusion-set"
    CONFIDENTIALITY_IMPACT = "confidentiality-impact"
    COOKIE = "cookie"
    CORTEX = "cortex"
    CORTEX_TAXONOMY = "cortex-taxonomy"
    COURSE_OF_ACTION = "course-of-action"
    COVID19_CSSE_DAILY_REPORT = "covid19-csse-daily-report"
    COVID19_DXY_LIVE_CITY = "covid19-dxy-live-city"
    COVID19_DXY_LIVE_PROVINCE = "covid19-dxy-live-province"
    COWRIE = "cowrie"
    CPE_ASSET = "cpe-asset"
    CREDENTIAL = "credential"
    CREDIT_CARD = "credit-card"
    CROWDSEC_IP_CONTEXT = "crowdsec-ip-context"
    CROWDSTRIKE_REPORT = "crowdstrike-report"
    CRYPTOCURRENCY_TRANSACTION = "cryptocurrency-transaction"
    CRYPTO_MATERIAL = "crypto-material"
    CS_BEACON_CONFIG = "cs-beacon-config"
    CTF_CHALLENGE = "ctf-challenge"
    CYTOMIC_ORION_FILE = "cytomic-orion-file"
    CYTOMIC_ORION_MACHINE = "cytomic-orion-machine"
    DARK_PATTERN_ITEM = "dark-pattern-item"
    DDOS = "ddos"
    DDOS_CLAIM = "ddos-claim"
    DDOS_CONFIG = "ddos-config"
    DEVICE = "device"
    DIAMETER_ATTACK = "diameter-attack"
    DIAMOND = "diamond"
    DIRECTORY = "directory"
    DKIM = "dkim"
    DNS_RECORD = "dns-record"
    DOMAIN_CRAWLED = "domain-crawled"
    DOMAIN_IP = "domain-ip"
    DOM_HASH = "dom-hash"
    EDR_REPORT = "edr-report"
    ELF = "elf"
    ELF_SECTION = "elf-section"
    EMAIL = "email"
    EMPLOYEE = "employee"
    ERROR_MESSAGE = "error-message"
    EVENT = "event"
    EXPLOIT = "exploit"
    EXPLOIT_POC = "exploit-poc"
    EXTERNAL_IMPACT = "external-impact"
    FACEBOOK_ACCOUNT = "facebook-account"
    FACEBOOK_GROUP = "facebook-group"
    FACEBOOK_PAGE = "facebook-page"
    FACEBOOK_POST = "facebook-post"
    FACEBOOK_REACTION = "facebook-reaction"
    FACIAL_COMPOSITE = "facial-composite"
    FAIL2BAN = "fail2ban"
    FAVICON = "favicon"
    FILE = "file"
    FLOWINTEL_CM_CASE = "flowintel-cm-case"
    FLOWINTEL_CM_TASK = "flowintel-cm-task"
    FLOWINTEL_CM_TASK_NOTE = "flowintel-cm-task-note"
    FORENSIC_CASE = "forensic-case"
    FORENSIC_EVIDENCE = "forensic-evidence"
    FORGED_DOCUMENT = "forged-document"
    FTM_AIRPLANE = "ftm-Airplane"
    FTM_ASSESSMENT = "ftm-Assessment"
    FTM_ASSET = "ftm-Asset"
    FTM_ASSOCIATE = "ftm-Associate"
    FTM_AUDIO = "ftm-Audio"
    FTM_BANKACCOUNT = "ftm-BankAccount"
    FTM_CALL = "ftm-Call"
    FTM_COMPANY = "ftm-Company"
    FTM_CONTRACT = "ftm-Contract"
    FTM_CONTRACTAWARD = "ftm-ContractAward"
    FTM_COURTCASE = "ftm-CourtCase"
    FTM_COURTCASEPARTY = "ftm-CourtCaseParty"
    FTM_DEBT = "ftm-Debt"
    FTM_DIRECTORSHIP = "ftm-Directorship"
    FTM_DOCUMENT = "ftm-Document"
    FTM_DOCUMENTATION = "ftm-Documentation"
    FTM_ECONOMICACTIVITY = "ftm-EconomicActivity"
    FTM_EMAIL = "ftm-Email"
    FTM_EVENT = "ftm-Event"
    FTM_FAMILY = "ftm-Family"
    FTM_FOLDER = "ftm-Folder"
    FTM_HYPERTEXT = "ftm-HyperText"
    FTM_IMAGE = "ftm-Image"
    FTM_LAND = "ftm-Land"
    FTM_LEGALENTITY = "ftm-LegalEntity"
    FTM_LICENSE = "ftm-License"
    FTM_MEMBERSHIP = "ftm-Membership"
    FTM_MESSAGE = "ftm-Message"
    FTM_ORGANIZATION = "ftm-Organization"
    FTM_OWNERSHIP = "ftm-Ownership"
    FTM_PACKAGE = "ftm-Package"
    FTM_PAGE = "ftm-Page"
    FTM_PAGES = "ftm-Pages"
    FTM_PASSPORT = "ftm-Passport"
    FTM_PAYMENT = "ftm-Payment"
    FTM_PERSON = "ftm-Person"
    FTM_PLAINTEXT = "ftm-PlainText"
    FTM_PUBLICBODY = "ftm-PublicBody"
    FTM_REALESTATE = "ftm-RealEstate"
    FTM_REPRESENTATION = "ftm-Representation"
    FTM_ROW = "ftm-Row"
    FTM_SANCTION = "ftm-Sanction"
    FTM_SUCCESSION = "ftm-Succession"
    FTM_TABLE = "ftm-Table"
    FTM_TAXROLL = "ftm-TaxRoll"
    FTM_UNKNOWNLINK = "ftm-UnknownLink"
    FTM_USERACCOUNT = "ftm-UserAccount"
    FTM_VEHICLE = "ftm-Vehicle"
    FTM_VESSEL = "ftm-Vessel"
    FTM_VIDEO = "ftm-Video"
    FTM_WORKBOOK = "ftm-Workbook"
    GAME_CHEAT = "game-cheat"
    GENERALIZING_PERSUASION_FRAMEWORK = "generalizing-persuasion-framework"
    GEOLOCATION = "geolocation"
    GITHUB_USER = "github-user"
    GITLAB_USER = "gitlab-user"
    GIT_VULN_FINDER = "git-vuln-finder"
    GOOGLE_SAFE_BROWSING = "google-safe-browsing"
    GOOGLE_THREAT_INTELLIGENCE_REPORT = "google-threat-intelligence-report"
    GREYNOISE_IP = "greynoise-ip"
    GTP_ATTACK = "gtp-attack"
    HASHLOOKUP = "hashlookup"
    HHHASH = "hhhash"
    HTTP_REQUEST = "http-request"
    IDENTITY = "identity"
    ILR_IMPACT = "ilr-impact"
    ILR_NOTIFICATION_INCIDENT = "ilr-notification-incident"
    IMAGE = "image"
    IMPERSONATION = "impersonation"
    IMSI_CATCHER = "imsi-catcher"
    INCIDENT = "incident"
    INFRASTRUCTURE = "infrastructure"
    INSTANT_MESSAGE = "instant-message"
    INSTANT_MESSAGE_GROUP = "instant-message-group"
    INTEGRITY_IMPACT = "integrity-impact"
    INTEL471_VULNERABILITY_INTELLIGENCE = "intel471-vulnerability-intelligence"
    INTELMQ_EVENT = "intelmq_event"
    INTELMQ_REPORT = "intelmq_report"
    INTERNAL_REFERENCE = "internal-reference"
    INTERPOL_NOTICE = "interpol-notice"
    INTRUSION_SET = "intrusion-set"
    IOT_DEVICE = "iot-device"
    IOT_FIRMWARE = "iot-firmware"
    IP_API_ADDRESS = "ip-api-address"
    IP_PORT = "ip-port"
    IRC = "irc"
    JA3 = "ja3"
    JA3S = "ja3s"
    JA4_PLUS = "ja4-plus"
    JARM = "jarm"
    KEYBASE_ACCOUNT = "keybase-account"
    LANGUAGE_CONTENT = "language-content"
    LEAKED_DOCUMENT = "leaked-document"
    LEGAL_ENTITY = "legal-entity"
    LNK = "lnk"
    MACHO = "macho"
    MACHO_SECTION = "macho-section"
    MACTIME_TIMELINE_ANALYSIS = "mactime-timeline-analysis"
    MALWARE = "malware"
    MALWARE_ANALYSIS = "malware-analysis"
    MALWARE_CONFIG = "malware-config"
    MEME_IMAGE = "meme-image"
    MICROBLOG = "microblog"
    MONETARY_IMPACT = "monetary-impact"
    MUTEX = "mutex"
    NARRATIVE = "narrative"
    NETFLOW = "netflow"
    NETWORK_CONNECTION = "network-connection"
    NETWORK_PROFILE = "network-profile"
    NETWORK_SOCKET = "network-socket"
    NETWORK_TRAFFIC = "network-traffic"
    NEWS_AGENCY = "news-agency"
    NEWS_MEDIA = "news-media"
    OPENTIDE = "opentide"
    OPEN_DATA_SECURITY = "open-data-security"
    ORGANIZATION = "organization"
    ORIGINAL_IMPORTED_FILE = "original-imported-file"
    PALOALTO_THREAT_EVENT = "paloalto-threat-event"
    PARLER_ACCOUNT = "parler-account"
    PARLER_COMMENT = "parler-comment"
    PARLER_POST = "parler-post"
    PASSIVE_DNS = "passive-dns"
    PASSIVE_DNS_DNSDBFLEX = "passive-dns-dnsdbflex"
    PASSIVE_SSH = "passive-ssh"
    PASTE = "paste"
    PCAP_METADATA = "pcap-metadata"
    PE = "pe"
    PERSNONA = "persnona"
    PERSON = "person"
    PERSONIFICATION = "personification"
    PE_OPTIONAL_HEADER = "pe-optional-header"
    PE_SECTION = "pe-section"
    PGP_META = "pgp-meta"
    PHISHING = "phishing"
    PHISHING_KIT = "phishing-kit"
    PHONE = "phone"
    PHONE_NUMBER = "phone-number"
    PHYSICAL_IMPACT = "physical-impact"
    POSTAL_ADDRESS = "postal-address"
    PROBABILISTIC_DATA_STRUCTURE = "probabilistic-data-structure"
    PROCESS = "process"
    PUBLICATION = "publication"
    PYTHON_ETVX_EVENT_LOG = "python-etvx-event-log"
    QUERY = "query"
    R2GRAPHITY = "r2graphity"
    RANSOMWARE_GROUP_POST = "ransomware-group-post"
    RANSOM_NEGOTIATION = "ransom-negotiation"
    REDDIT_ACCOUNT = "reddit-account"
    REDDIT_COMMENT = "reddit-comment"
    REDDIT_POST = "reddit-post"
    REDDIT_SUBREDDIT = "reddit-subreddit"
    REGEXP = "regexp"
    REGISTRY_KEY = "registry-key"
    REGISTRY_KEY_VALUE = "registry-key-value"
    REGRIPPER_NTUSER = "regripper-NTUser"
    REGRIPPER_SAM_HIVE_SINGLE_USER = "regripper-sam-hive-single-user"
    REGRIPPER_SAM_HIVE_USER_GROUP = "regripper-sam-hive-user-group"
    REGRIPPER_SOFTWARE_HIVE_APPINIT_DLLS = "regripper-software-hive-appInit-DLLS"
    REGRIPPER_SOFTWARE_HIVE_APPLICATIONS_INSTALLED = "regripper-software-hive-applications-installed"
    REGRIPPER_SOFTWARE_HIVE_APPLICATION_PATHS = "regripper-software-hive-application-paths"
    REGRIPPER_SOFTWARE_HIVE_BHO = "regripper-software-hive-BHO"
    REGRIPPER_SOFTWARE_HIVE_COMMAND_SHELL = "regripper-software-hive-command-shell"
    REGRIPPER_SOFTWARE_HIVE_SOFTWARE_RUN = "regripper-software-hive-software-run"
    REGRIPPER_SOFTWARE_HIVE_USERPROFILE_WINLOGON = "regripper-software-hive-userprofile-winlogon"
    REGRIPPER_SOFTWARE_HIVE_WINDOWS_GENERAL_INFO = "regripper-software-hive-windows-general-info"
    REGRIPPER_SYSTEM_HIVE_FIREWALL_CONFIGURATION = "regripper-system-hive-firewall-configuration"
    REGRIPPER_SYSTEM_HIVE_GENERAL_CONFIGURATION = "regripper-system-hive-general-configuration"
    REGRIPPER_SYSTEM_HIVE_NETWORK_INFORMATION = "regripper-system-hive-network-information"
    REGRIPPER_SYSTEM_HIVE_SERVICES_DRIVERS = "regripper-system-hive-services-drivers"
    REPORT = "report"
    RESEARCH_SCANNER = "research-scanner"
    RISK_ASSESSMENT_REPORT = "risk-assessment-report"
    ROGUE_DNS = "rogue-dns"
    RTIR = "rtir"
    SANDBOX_REPORT = "sandbox-report"
    SB_SIGNATURE = "sb-signature"
    SCAN_RESULT = "scan-result"
    SCHEDULED_EVENT = "scheduled-event"
    SCHEDULED_TASK = "scheduled-task"
    SCRIPPSCO2_C13_DAILY = "scrippsco2-c13-daily"
    SCRIPPSCO2_C13_MONTHLY = "scrippsco2-c13-monthly"
    SCRIPPSCO2_CO2_DAILY = "scrippsco2-co2-daily"
    SCRIPPSCO2_CO2_MONTHLY = "scrippsco2-co2-monthly"
    SCRIPPSCO2_O18_DAILY = "scrippsco2-o18-daily"
    SCRIPPSCO2_O18_MONTHLY = "scrippsco2-o18-monthly"
    SCRIPT = "script"
    SECURITY_PLAYBOOK = "security-playbook"
    SHADOWSERVER_MALWARE_URL_REPORT = "shadowserver-malware-url-report"
    SHADOWSERVER_SCAN_HTTP_PROXY = "shadowserver-scan-http-proxy"
    SHELL_COMMANDS = "shell-commands"
    SHODAN_REPORT = "shodan-report"
    SHORTENED_LINK = "shortened-link"
    SHORT_MESSAGE_SERVICE = "short-message-service"
    SIGMA = "sigma"
    SIGMF_ARCHIVE = "sigmf-archive"
    SIGMF_EXPANDED_RECORDING = "sigmf-expanded-recording"
    SIGMF_RECORDING = "sigmf-recording"
    SOCIAL_MEDIA_GROUP = "social-media-group"
    SOFTWARE = "software"
    SPAMBEE_REPORT = "spambee-report"
    SPEARPHISHING_ATTACHMENT = "spearphishing-attachment"
    SPEARPHISHING_LINK = "spearphishing-link"
    SPLUNK = "splunk"
    SS7_ATTACK = "ss7-attack"
    SSH_AUTHORIZED_KEYS = "ssh-authorized-keys"
    STAIRWELL = "stairwell"
    STIX2_PATTERN = "stix2-pattern"
    STOCK = "stock"
    SUBMARINE = "submarine"
    SURICATA = "suricata"
    TARGET_SYSTEM = "target-system"
    TASK = "task"
    TATTOO = "tattoo"
    TELEGRAM_ACCOUNT = "telegram-account"
    TELEGRAM_BOT = "telegram-bot"
    TEMPORAL_EVENT = "temporal-event"
    THAICERT_GROUP_CARDS = "thaicert-group-cards"
    THREATGRID_REPORT = "threatgrid-report"
    TIMECODE = "timecode"
    TIMESKETCH_MESSAGE = "timesketch_message"
    TIMESKETCH_TIMELINE = "timesketch-timeline"
    TIMESTAMP = "timestamp"
    TOR_HIDDENSERVICE = "tor-hiddenservice"
    TOR_NODE = "tor-node"
    TRACEABILITY_IMPACT = "traceability-impact"
    TRACKING_ID = "tracking-id"
    TRANSACTION = "transaction"
    TRANSLATION = "translation"
    TRANSPORT_TICKET = "transport-ticket"
    TRUSTAR_REPORT = "trustar_report"
    TSK_CHATS = "tsk-chats"
    TSK_WEB_BOOKMARK = "tsk-web-bookmark"
    TSK_WEB_COOKIE = "tsk-web-cookie"
    TSK_WEB_DOWNLOADS = "tsk-web-downloads"
    TSK_WEB_HISTORY = "tsk-web-history"
    TSK_WEB_SEARCH_QUERY = "tsk-web-search-query"
    TWITTER_ACCOUNT = "twitter-account"
    TWITTER_LIST = "twitter-list"
    TWITTER_POST = "twitter-post"
    TYPOSQUATTING_FINDER = "typosquatting-finder"
    TYPOSQUATTING_FINDER_RESULT = "typosquatting-finder-result"
    URL = "url"
    USER_ACCOUNT = "user-account"
    USER_ACTION = "user-action"
    VEHICLE = "vehicle"
    VICTIM = "victim"
    VIRUSTOTAL_GRAPH = "virustotal-graph"
    VIRUSTOTAL_REPORT = "virustotal-report"
    VIRUSTOTAL_SUBMISSION = "virustotal-submission"
    VULNERABILITY = "vulnerability"
    WEAKNESS = "weakness"
    WHOIS = "whois"
    WINDOWS_SERVICE = "windows-service"
    X509 = "x509"
    X_HEADER = "x-header"
    YABIN = "yabin"
    YARA = "yara"
    YOUTUBE_CHANNEL = "youtube-channel"
    YOUTUBE_COMMENT = "youtube-comment"
    YOUTUBE_PLAYLIST = "youtube-playlist"
    YOUTUBE_VIDEO = "youtube-video"


class ObjectRelation(Enum):
    AAAA_RECORD = "aaaa-record"
    ABA_RTN = "aba-rtn"
    ABOUT = "about"
    ABUSE_CONFIDENCE_SCORE = "abuse-confidence-score"
    ACADEMIC_INSTITUTION = "academic-institution"
    ACCESS = "access"
    ACCESSIBILITY = "accessibility"
    ACCESS_TIME = "access-time"
    ACCOUNT = "account"
    ACCOUNTNUMBER = "accountNumber"
    ACCOUNTTYPE = "accountType"
    ACCOUNT_AVATAR = "account-avatar"
    ACCOUNT_AVATAR_URL = "account-avatar-url"
    ACCOUNT_ID = "account-id"
    ACCOUNT_NAME = "account-name"
    ACCOUNT_TYPE = "account-type"
    ACCOUNT_URL = "account-url"
    ACCURACY_RADIUS = "accuracy-radius"
    ACD_ELEMENT = "acd-element"
    ACQUISITION_METHOD = "acquisition-method"
    ACQUISITION_TOOLS = "acquisition-tools"
    ACTION = "action"
    ACTIONS = "actions"
    ACTIONS_CORRECTIVE = "actions-corrective"
    ACTIONS_POSTERIEUR = "actions-posterieur"
    ACTIVE = "active"
    ACTIVE_USER_COUNT = "active-user-count"
    ACTIVITYTYPE = "activityType"
    ACTIVITY_LOCATION_OPEN_SOURCE = "activity-location-open-source"
    ACTIVITY_LOCATION_PRIVATE = "activity-location-private"
    ACTIVITY_LOCATION_UNDERGROUND = "activity-location-underground"
    ACTOR = "actor"
    ACTORS_RECEIVER = "actors_receiver"
    ACTORS_SPEAKER_MOTIVATION = "actors_speaker_motivation"
    ACTORS_SPEAKER_TYPE = "actors_speaker_type"
    ACTOR_GEO_STATS_30D = "actor-geo-stats-30d"
    ACTOR_TOTAL_STATS_30D = "actor-total-stats-30d"
    ACT_AS = "act-as"
    ADDITIONAL_COMMENTS = "additional-comments"
    ADDITIONAL_FILE = "additional-file"
    ADDITIONAL_RESOURCES = "additional_resources"
    ADDRESS = "address"
    ADDRESSES = "addresses"
    ADDRESS_CRYPTO = "address-crypto"
    ADDRESS_FAMILY = "address-family"
    ADDRESS_OF_ENTRYPOINT = "address-of-entrypoint"
    ADDRESS_XMR = "address-xmr"
    ADMINISTRATIVE_AREA = "administrative-area"
    ADMINISTRATOR = "administrator"
    ADVESARY = "Advesary"
    AFFECTED_GAME = "affected-game"
    AGE_RANGE = "age-range"
    ALEPHURL = "alephUrl"
    ALIAS = "alias"
    ALIASES = "aliases"
    ALTERATION = "alteration"
    ALTITUDE = "altitude"
    AMENDED = "amended"
    AMOUNT = "amount"
    AMOUNTEUR = "amountEur"
    AMOUNTUSD = "amountUsd"
    ANALYSIS_DATE = "analysis-date"
    ANALYSIS_DEFINITION_VERSION = "analysis_definition_version"
    ANALYSIS_ENGINE_VERSION = "analysis_engine_version"
    ANALYSIS_START_DATE = "analysis-start-date"
    ANALYSIS_SUBMITTED_AT = "analysis_submitted_at"
    ANNUAL_REVENUE_EUR = "annual_revenue_EUR"
    APARTMENT = "apartment"
    APP = "app"
    APPID = "appid"
    APPLICATION = "application"
    APPLICATIONID = "ApplicationId"
    APPLICATIONS_INSTALLED = "applications-installed"
    APPLICATIONS_RUN = "applications-run"
    APPLICATION_NAME = "application-name"
    APPLICATION_PATH = "application-path"
    APP_LAST_WRITE_TIME = "app-last-write-time"
    APP_NAME = "app-name"
    APP_USED = "app-used"
    ARCH = "arch"
    ARCHITECTURE = "architecture"
    ARCHITECTURE_EXECUTION_ENV = "architecture_execution_env"
    ARCHIVE = "archive"
    AREA = "area"
    ARGS = "args"
    ARMAMENT = "armament"
    ARTICLE = "article"
    ARTIFACT_DROPPED_MD5 = "artifact-dropped-md5"
    ARTIFACT_DROPPED_NAME = "artifact-dropped-name"
    ARTIFACT_DROPPED_SHA1 = "artifact-dropped-sha1"
    ARTIFACT_DROPPED_SHA256 = "artifact-dropped-sha256"
    AS = "AS"
    ASN = "asn"
    ASSESSMENTID = "assessmentId"
    ASSET_TYPE = "asset_type"
    AS_NAME = "as-name"
    AS_NUM = "as-num"
    ATTACHMENT = "attachment"
    ATTACHMENTS = "attachments"
    ATTACHMENT_MD5 = "attachment-md5"
    ATTACHMENT_NAME = "attachment-name"
    ATTACHMENT_SHA1 = "attachment-sha1"
    ATTACHMENT_SHA256 = "attachment-sha256"
    ATTACKNAME = "AttackName"
    ATTACK_DETAILS = "attack-details"
    ATTACK_TYPE = "attack-type"
    AUDIENCE = "audience"
    AUTHENTIHASH = "authentihash"
    AUTHOR = "author"
    AUTHOREDAT = "authoredAt"
    AUTHORED_DATE = "authored_date"
    AUTHORITY = "authority"
    AUTHORIZED = "authorized"
    AUTHOR_EMAIL = "author-email"
    AUTOADMINLOGON = "AutoAdminLogon"
    AUTORESTARTSHELL = "AutoRestartShell"
    AUTRES_INFORMATIONS = "autres-informations"
    AVAILABILITY_IMPACT = "availability_impact"
    AVATAR_URL = "avatar_url"
    A_B_TEST = "a/b-test"
    A_RECORD = "a-record"
    B = "b"
    BACKGROUND = "background"
    BACKGROUND_NOISE = "background-noise"
    BACKSCATTER_THRESHOLD = "backscatter-threshold"
    BADGE = "badge"
    BAILIWICK = "bailiwick"
    BALANCE = "balance"
    BALANCE_BTC = "balance_BTC"
    BANKADDRESS = "bankAddress"
    BANKNAME = "bankName"
    BANK_NAME = "bank_name"
    BANNED_IP = "banned-ip"
    BANNER = "banner"
    BANNER_BACKGROUND_IMAGE = "banner-background-image"
    BANNER_BACKGROUND_URL = "banner-background-url"
    BASE64 = "base64"
    BASE_OF_CODE = "base-of-code"
    BASE_OF_DATA = "base-of-data"
    BASICAUTH_PASSWORD = "basicauth-password"
    BASICAUTH_USER = "basicauth-user"
    BCC = "bcc"
    BCC_DISPLAY_NAME = "bcc-display-name"
    BEACON_HOST = "beacon-host"
    BEACON_HOST_1 = "beacon_host"
    BEACON_HTTP_GET = "beacon_http_get"
    BEACON_HTTP_POST = "beacon_http_post"
    BEACON_TYPE = "beacon-type"
    BEACON_TYPE_1 = "beacon_type"
    BEAM = "beam"
    BEARD = "beard"
    BEHAVIORS = "behaviors"
    BENEFICIARY = "beneficiary"
    BENEFICIARY_BANK_ACCOUNT = "beneficiary-bank-account"
    BENEFICIARY_BANK_AGENCY = "beneficiary-bank-agency"
    BENEFICIARY_COMMENT = "beneficiary-comment"
    BHO_KEY_LAST_WRITE_TIME = "BHO-key-last-write-time"
    BHO_NAME = "BHO-name"
    BIC = "bic"
    BIKCODE = "bikCode"
    BINARY_MD5 = "binary-md5"
    BINARY_MD5_1 = "binary_md5"
    BINARY_SHA1 = "binary-sha1"
    BINARY_SHA1_1 = "binary_sha1"
    BINARY_SHA256 = "binary-sha256"
    BINARY_SHA256_1 = "binary_sha256"
    BINWALK_ENTROPY_GRAPH = "binwalk-entropy-graph"
    BINWALK_OUTPUT = "binwalk-output"
    BIO = "bio"
    BIRTHDATE = "birthDate"
    BIRTHMARK = "birthmark"
    BIRTHPLACE = "birthPlace"
    BIRTH_CERTIFICATE_NUMBER = "birth-certificate-number"
    BIRTH_DROID_FILE_IDENTIFIER = "birth-droid-file-identifier"
    BIRTH_DROID_VOLUME_IDENTIFIER = "birth-droid-volume-identifier"
    BITCOIN_ADDRESS = "BITCOIN_ADDRESS"
    BLIND_SPOTS_AND_ASSUMPTIONS = "blind_spots_and_assumptions"
    BLOG = "blog"
    BLOOMBERG_EXCHANGE_CODE = "bloomberg-exchange-code"
    BODY = "body"
    BODYHTML = "bodyHtml"
    BODYTEXT = "bodyText"
    BODY_TYPE = "body-type"
    BOLETO_NUMBER = "boleto-number"
    BOOT_LOG = "boot-log"
    BOTTOM_ACCESSORIES = "bottom-accessories"
    BRANCH = "branch"
    BRANCHES = "branches"
    BRAND = "brand"
    BROWSER = "browser"
    BTC_ADDRESS = "btc-address"
    BTC_RECEIVED = "BTC_received"
    BTC_SENT = "BTC_sent"
    BUILDDATE = "buildDate"
    BUILDERS = "builders"
    BUILDGUID = "BuildGUID"
    BUILDLAB = "BuildLab"
    BUILDLABEX = "BuildLabEx"
    BUSINESS = "business"
    BUSINESS_UNIT = "business-unit"
    BVDID = "bvdId"
    BYTE_COUNT = "byte-count"
    C13_VALUE = "c13-value"
    C2 = "c2"
    C2_DOMAIN = "c2-domain"
    C2_IP = "c2-ip"
    C2_IPPORT = "c2-ipport"
    C2_URL = "c2-url"
    CACHEDLOGONCOUNT = "CachedLogonCount"
    CADASTRALCODE = "cadastralCode"
    CAEMCODE = "caemCode"
    CALLBACKS = "callbacks"
    CALLBACK_AVERAGE = "callback-average"
    CALLBACK_LARGEST = "callback-largest"
    CALLERNUMBER = "callerNumber"
    CALLSIGN = "callSign"
    CALL_SIGN = "call-sign"
    CANCELLED = "cancelled"
    CAN_ESCALATE_PRIVS = "can_escalate_privs"
    CAPABILITY = "Capability"
    CAPABILITY_1 = "capability"
    CAPITAL = "capital"
    CAPTURE_INTERFACE = "capture-interface"
    CAPTURE_LENGTH = "capture-length"
    CAPTURE_ORIGIN = "capture-origin"
    CARD_SECURITY_CODE = "card-security-code"
    CASENUMBER = "caseNumber"
    CASE_NAME = "case-name"
    CASE_NUMBER = "case-number"
    CASE_OWNER_ORG_NAME = "case-owner-org-name"
    CASE_OWNER_ORG_UUID = "case-owner-org-uuid"
    CASE_UUID = "case-uuid"
    CATEGORIZATION = "categorization"
    CATEGORIZATION_OTHERS = "categorization_others"
    CATEGORY = "Category"
    CATEGORY_1 = "category"
    CAUSE_INITIALE_INCIDENT = "cause-initiale-incident"
    CC = "cc"
    CCDNUMBER = "ccdNumber"
    CCDVALUE = "ccdValue"
    CC_DISPLAY_NAME = "cc-display-name"
    CC_NUMBER = "cc-number"
    CELLID = "cellid"
    CELLS = "cells"
    CENSUSBLOCK = "censusBlock"
    CERTAINTY = "certainty"
    CERTIFICATE = "certificate"
    CERTIFICATE_COMMON_NAME = "certificate-common-name"
    CERTIFICATE_COUNTRY = "certificate-country"
    CERTIFICATE_CREATION_DATE = "certificate-creation-date"
    CERTIFICATE_EXPIRY_DATE = "certificate-expiry-date"
    CERTIFICATE_ISSUER = "certificate-issuer"
    CERTIFICATE_ORGANIZATION = "certificate-organization"
    CERTIFICATE_ORGANIZATION_LOCALITY = "certificate-organization-locality"
    CERTIFICATE_ORGANIZATION_STATE = "certificate-organization-state"
    CERTIFICATE_ORGANIZATION_UNIT = "certificate-organization-unit"
    CERTIFICATE_SHA256 = "certificate-sha256"
    CHANNEL = "channel"
    CHANNEL_AVATAR = "channel-avatar"
    CHANNEL_BANNER = "channel-banner"
    CHANNEL_ID = "channel-id"
    CHANNEL_NAME = "channel-name"
    CHARACTERISTIC = "characteristic"
    CHARACTERISTICS = "characteristics"
    CHARACTERISTICS_HEX = "characteristics-hex"
    CHARGES = "charges"
    CHATSITE = "chatsite"
    CHATSITE_ID_PRIVATE = "chatsite_id_private"
    CHATSITE_ID_PUBLIC = "chatsite_id_public"
    CHAT_ID = "chat-id"
    CHEAT_NAME = "cheat-name"
    CHEAT_SCREENSHOT = "cheat-screenshot"
    CHEAT_TYPE = "cheat-type"
    CHEAT_VERSION = "cheat-version"
    CHECKSUM = "checksum"
    CHILD_PID = "child-pid"
    CHINA_FREE_EMAIL = "china_free_email"
    CIDR_BLOCK = "CIDR_BLOCK"
    CIKCODE = "cikCode"
    CITY = "city"
    CLAIM_VALIDITY = "claim-validity"
    CLASS = "class"
    CLASSIFICATION = "classification"
    CLASSIFICATIONNAME = "classificationName"
    CLASSIFICATIONS = "classifications"
    CLASSIFICATION_IDENTIFIER = "classification.identifier"
    CLASSIFICATION_TAXONOMY = "classification.taxonomy"
    CLASSIFICATION_TYPE = "classification.type"
    CLIENTCREATIONDATEUTC = "clientCreationDateUTC"
    CLIENTID = "clientId"
    CLIENTNAME = "clientName"
    CLIENT_NUMBER = "client-number"
    CLOSED = "closed"
    CLOSEDATE = "closeDate"
    CLOTH_COLOR = "cloth-color"
    CLOTH_PICTURE = "cloth-picture"
    CMDCODE = "CmdCode"
    CMTMF_ATCKID = "CMTMF_ATCKID"
    CNAME_RECORD = "cname-record"
    CO2_VALUE = "co2-value"
    COATOCODE = "coatoCode"
    CODE = "code"
    COLLECTION = "collection"
    COLOR_OF_EYES = "color-of-eyes"
    COLOUR_OF_EYES = "colour-of-eyes"
    COLOUR_OF_HAIR = "colour-of-hair"
    COLUMNS = "columns"
    COMMAND = "command"
    COMMAND_LINE = "command-line"
    COMMAND_LINE_1 = "command_line"
    COMMENT = "comment"
    COMMENTS = "COMMENTS"
    COMMENTS_1 = "Comments"
    COMMENTS_2 = "comments"
    COMMENT_DEPTH = "comment-depth"
    COMMERCIAL_NAME = "commercial-name"
    COMMITTED_DATE = "committed_date"
    COMMIT_ID = "commit-id"
    COMMODITIES = "commodities"
    COMMUNITY_ID = "community-id"
    COMMUNITY_SCORE = "community-score"
    COMPANIESMENTIONED = "companiesMentioned"
    COMPANY = "company"
    COMPANY_NAME = "company-name"
    COMPCS = "compCS"
    COMPILATION_DATE = "compilation-date"
    COMPILATION_TIMESTAMP = "compilation-timestamp"
    COMPLEMENT = "complement"
    COMPLETED = "completed"
    COMPUTER = "Computer"
    COMPUTER_NAME = "computer-name"
    CONFIG = "config"
    CONFIGURATION_VERSION = "configuration_version"
    CONFIG_MD5 = "config-md5"
    CONFIG_MD5_1 = "config_md5"
    CONFIG_SHA1 = "config-sha1"
    CONFIG_SHA1_1 = "config_sha1"
    CONFIG_SHA256 = "config-sha256"
    CONFIG_SHA256_1 = "config_sha256"
    CONFIRMED = "confirmed"
    CONNECTION = "connection"
    CONSTITUENCY = "constituency"
    CONTACT = "contact"
    CONTACT_DETAIL = "contact-detail"
    CONTACT_EMAIL = "contact_email"
    CONTACT_INFORMATION = "contact_information"
    CONTACT_PHONE = "contact_phone"
    CONTENT = "content"
    CONTENTHASH = "contentHash"
    CONTENT_LENGTH = "content-length"
    CONTENT_LENGTH_1 = "content_length"
    CONTENT_TYPE = "content-type"
    CONTENT_TYPE_1 = "content_type"
    CONTEXT = "context"
    CONTRACTDATE = "contractDate"
    CONTRIBUTOR = "contributor"
    CONTROVERSY = "controversy"
    CONVERSATIONS = "conversations"
    CONVERSION_RATE = "conversion_rate"
    CONVERSION_TIME = "conversion_time"
    COOKIE = "cookie"
    COOKIE_NAME = "cookie-name"
    COOKIE_VALUE = "cookie-value"
    COPY = "copy"
    CORRELATION_ID = "Correlation-ID"
    CORTEX_URL = "cortex_url"
    COST = "cost"
    COUNT = "count"
    COUNTERMEASURES = "countermeasures"
    COUNTRY = "country"
    COUNTRYCODE = "countrycode"
    COUNTRY_CODE = "country-code"
    COUNTRY_CODE_NUMERIC = "country-code-numeric"
    COUNTRY_REGION = "country-region"
    COUNTY = "county"
    COURSE_OVER_GROUND = "course-over-ground"
    COURT = "court"
    COVER_PHOTO = "cover-photo"
    CPE = "cpe"
    CPVCODE = "cpvCode"
    CRAWLER = "crawler"
    CREATED = "created"
    CREATEDATE = "createDate"
    CREATED_AT = "created-at"
    CREATE_THREAD = "create-thread"
    CREATIONDATE = "creationDate"
    CREATION_DATE = "creation-date"
    CREATION_TIME = "creation-time"
    CREATOR = "creator"
    CREATOR_ID = "creator-id"
    CREDENTIAL = "credential"
    CREDIT = "credit"
    CRITERIA = "criteria"
    CRITICALITY = "criticality"
    CRITICAL_TASKS = "critical_tasks"
    CROSSPOST = "crosspost"
    CROSSPOST_UNSAFE = "crosspost-unsafe"
    CRSNUMBER = "crsNumber"
    CRYPTOCURRENCY_ADDRESSES = "cryptocurrency_addresses"
    CSDVERSION = "CSDVersion"
    CSVHASH = "csvHash"
    CURRENCY = "currency"
    CURRENCY_ACTUAL = "currency_actual"
    CURRENCY_CODE = "currency-code"
    CURRENTBUILD = "CurrentBuild"
    CURRENTBUILDTYPE = "CurrentBuildType"
    CURRENTVERSION = "CurrentVersion"
    CURRENT_BALANCE = "current-balance"
    CURRENT_CONFIRMED = "current-confirmed"
    CURRENT_DIRECTORY = "current-directory"
    CURVE_LENGTH = "curve-length"
    CUSTOMSAMOUNT = "customsAmount"
    CUSTOMSPROCEDURE = "customsProcedure"
    CVE = "CVE"
    CVES = "cves"
    CVE_1 = "cve"
    CVE_ID = "cve-id"
    CVSS_SCORE = "cvss-score"
    CVSS_SCORE_V2 = "cvss-score-v2"
    CVSS_SCORE_V3 = "cvss-score-v3"
    CVSS_STRING = "cvss-string"
    D = "d"
    DANGLING_STRINGS = "dangling-strings"
    DATA = "data"
    DATASET = "dataset"
    DATATYPE = "datatype"
    DATA_DOI = "data_doi"
    DATA_LEAKED = "data_leaked"
    DATA_STOLEN = "data_stolen"
    DATA_TYPE = "data-type"
    DATE = "date"
    DATETIME = "datetime"
    DATETIME_ACCESSED = "datetime-accessed"
    DATETIME_BOOKMARKED = "datetime-bookmarked"
    DATETIME_CREATED = "datetime-created"
    DATETIME_RECEIVED = "datetime-received"
    DATETIME_SEARCHED = "datetime-searched"
    DATETIME_SENT = "datetime-sent"
    DATE_BALANCE = "date-balance"
    DATE_FIRST_REGISTRATION = "date-first-registration"
    DATE_FOUND = "date-found"
    DATE_INCIDENT = "date-incident"
    DATE_OF_ARRIVAL = "date-of-arrival"
    DATE_OF_BIRTH = "date-of-birth"
    DATE_OF_DEPARTURE = "date-of-departure"
    DATE_OF_DISAPPEARANCE = "date-of-disappearance"
    DATE_OF_INCEPTION = "date-of-inception"
    DATE_OF_PURCHASE = "date-of-purchase"
    DATE_POSTING = "date-posting"
    DATE_PRE_NOTIFICATION = "date-pre-notification"
    DATE_PUBLISHED = "date-published"
    DDOS_TOOL = "ddos-tool"
    DEADLINE = "deadline"
    DEATH = "death"
    DEATHDATE = "deathDate"
    DECISIONREASON = "decisionReason"
    DECRYPTION_KEY = "decryption_key"
    DEFAULTUSERNAME = "DefaultUserName"
    DELIMITATION_GEOGRAPHIQUE = "delimitation-geographique"
    DEPARTURECOUNTRY = "departureCountry"
    DEPTH = "depth"
    DEREFURI = "derefUri"
    DESCRIPTION = "Description"
    DESCRIPTION_1 = "description"
    DESCRIPTION_INCIDENT = "description-incident"
    DESCRIPTION_PROBLEME_SERVICES_URGENCE = "description-probleme-services-urgence"
    DESTINATION = "destination"
    DESTINATIONCOUNTRY = "destinationCountry"
    DESTINATION_ABUSE_CONTACT = "destination.abuse_contact"
    DESTINATION_ACCOUNT = "destination.account"
    DESTINATION_ALLOCATED = "destination.allocated"
    DESTINATION_ASN = "destination.asn"
    DESTINATION_AS_NAME = "destination.as_name"
    DESTINATION_DOMAIN_SUFFIX = "destination.domain_suffix"
    DESTINATION_FQDN = "destination.fqdn"
    DESTINATION_GEOLOCATION_CC = "destination.geolocation.cc"
    DESTINATION_GEOLOCATION_CITY = "destination.geolocation.city"
    DESTINATION_GEOLOCATION_COUNTRY = "destination.geolocation.country"
    DESTINATION_GEOLOCATION_LATITUDE = "destination.geolocation.latitude"
    DESTINATION_GEOLOCATION_LONGITUDE = "destination.geolocation.longitude"
    DESTINATION_GEOLOCATION_REGION = "destination.geolocation.region"
    DESTINATION_GEOLOCATION_STATE = "destination.geolocation.state"
    DESTINATION_HOST = "Destination-Host"
    DESTINATION_IP = "destination.ip"
    DESTINATION_LOCAL_HOSTNAME = "destination.local_hostname"
    DESTINATION_LOCAL_IP = "destination.local_ip"
    DESTINATION_NETWORK = "destination.network"
    DESTINATION_PORT = "destination.port"
    DESTINATION_REALM = "Destination-Realm"
    DESTINATION_REGISTRY = "destination.registry"
    DESTINATION_REVERSE_DNS = "destination.reverse_dns"
    DESTINATION_TOR_NODE = "destination.tor_node"
    DESTINATION_URL = "destination.url"
    DESTINATION_URLPATH = "destination.urlpath"
    DETAILS_SERVICE = "details-service"
    DETECTEDCOUNTRY = "detectedCountry"
    DETECTEDLANGUAGE = "detectedLanguage"
    DETECTED_ASN = "detected-asn"
    DETECTION = "detection"
    DETECTIONS = "detections"
    DETECTION_METHOD = "detection_method"
    DETECTION_RATIO = "detection-ratio"
    DETERMINATION = "determination"
    DEVICE_TYPE = "device-type"
    DHCP_DOMAIN = "DHCP-domain"
    DHCP_IP_ADDRESS = "DHCP-IP-address"
    DHCP_NAME_SERVER = "DHCP-name-server"
    DHCP_SERVER = "DHCP-server"
    DHCP_SUBNET_MASK = "DHCP-subnet-mask"
    DIGEST = "digest"
    DIGEST_ALGORITHM = "digest_algorithm"
    DIGEST_BASE64 = "digest-base64"
    DIMENSION_A = "dimension-a"
    DIMENSION_B = "dimension-b"
    DIMENSION_C = "dimension-c"
    DIMENSION_D = "dimension-d"
    DIRECTION = "Direction"
    DIRECTIONOFTRANSPORTATION = "directionOfTransportation"
    DIRECTION_1 = "direction"
    DIRTY_WORDS_DOMAIN = "dirty_words_domain"
    DIRTY_WORDS_USERNAME = "dirty_words_username"
    DISABLECAD = "DisableCAD"
    DISABLED = "disabled"
    DISABLE_NOTIFICATION = "disable-notification"
    DISCOUNT = "discount"
    DISPLACEMENT = "displacement"
    DISPLAY = "display"
    DISPLAYED_NAME = "displayed-name"
    DISPLAY_NAME = "display-name"
    DISPOSABLE = "disposable"
    DISSOLUTIONDATE = "dissolutionDate"
    DISTINGUISHING_MARKS_AND_CHARACTERISTICS = "distinguishing-marks-and-characteristics"
    DKIM = "dkim"
    DLL_CHARACTERISTICS = "dll-characteristics"
    DLL_CHARACTERISTICS_HEX = "dll-characteristics-hex"
    DLL_LAST_WRITE_TIME = "DLL-last-write-time"
    DLL_NAME = "DLL-name"
    DLL_PATH = "DLL-path"
    DMARC_CONFIGURED = "dmarc_configured"
    DMARC_ENFORCED = "dmarc_enforced"
    DNI = "dni"
    DNS_NAME = "dns-name"
    DNS_NAMES = "dns_names"
    DNS_SERVER = "dns-server"
    DOCUMENT = "document"
    DOCUMENTNUMBER = "documentNumber"
    DOCUMENTTYPE = "documentType"
    DOCUMENT_NAME = "document-name"
    DOCUMENT_TEXT = "document-text"
    DOCUMENT_TYPE = "document-type"
    DOI = "DOI"
    DOLLAREXCHRATE = "dollarExchRate"
    DOMAIN = "domain"
    DOMAIN_DST = "domain-dst"
    DOMAIN_FAMILY = "domain-family"
    DOMAIN_IP = "domain-ip"
    DOMAIN_NAME = "domain-name"
    DOMAIN_POPULAR = "domain_popular"
    DOMAIN_WITHOUT_TLD = "domain_without_tld"
    DOM_HASH = "dom-hash"
    DOWNVOTES = "downvotes"
    DPORT = "dport"
    DRAUGHT = "draught"
    DRILL_DOWN = "drill-down"
    DRIVERS = "drivers"
    DROID_FILE_IDENTIFIER = "droid-file-identifier"
    DROID_VOLUME_IDENTIFIER = "droid-volume-identifier"
    DST = "dst"
    DSTLOC = "dstloc"
    DST_AS = "dst-as"
    DST_BYTES_COUNT = "dst-bytes-count"
    DST_BYTES_COUNT_1 = "dst_bytes_count"
    DST_DOMAIN = "dst-domain"
    DST_HOSTNAME = "dst_hostname"
    DST_IP = "dst-ip"
    DST_IP_1 = "dst_ip"
    DST_MAC = "dst_mac"
    DST_MISC = "dst-misc"
    DST_PACKETS = "dst_packets"
    DST_PACKETS_COUNT = "dst-packets-count"
    DST_PORT = "dst-port"
    DST_PORT_1 = "dst_port"
    DUNSCODE = "dunsCode"
    DUPLICATE = "duplicate"
    DUPLICATE_NUMBER = "duplicate_number"
    DURATION = "duration"
    DUREE = "duree"
    DYNO_POWER = "dyno-power"
    E = "e"
    EARLIEST = "earliest"
    ECDSA_TYPE = "ecdsa-type"
    EDITED = "edited"
    EDITION = "edition"
    EDITIONID = "EditionID"
    EDUCATIONAL_DOMAIN = "educational_domain"
    EFFECTIVE = "effective"
    EFFICACY = "efficacy"
    EMAIL = "email"
    EMAILMENTIONED = "emailMentioned"
    EMAILS = "emails"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    EMAIL_ADDRESS_1 = "email-address"
    EMAIL_ADDRESS_2 = "email_address"
    EMAIL_BODY = "email-body"
    EMAIL_BODY_ATTACHMENT = "email-body-attachment"
    EMAIL_CONTACT_INCIDENT = "email-contact-incident"
    EMAIL_SENDER = "email-sender"
    EMAIL_TYPE = "email-type"
    EMBEDDED_LINK = "embedded-link"
    EMBEDDED_SAFE_LINK = "embedded-safe-link"
    EML = "eml"
    EMPLOYEE_TYPE = "employee-type"
    ENBLED_FIREWALL = "enbled-firewall"
    ENCCS = "encCS"
    ENCODED_DATA = "encoded-data"
    ENCODED_DATA_1 = "encoded_data"
    ENCODED_LENGTH = "encoded-length"
    ENCODED_LENGTH_1 = "encoded_length"
    ENCODING = "encoding"
    ENCRYPTED = "encrypted"
    ENCRYPTION_ALGORITHM = "encryption_algorithm"
    ENCRYPTION_FUNCTION = "encryption-function"
    ENCUMBRANCE = "encumbrance"
    END = "end"
    ENDDATE = "endDate"
    ENDPOINT_ID = "endpoint-id"
    ENDURANCE = "endurance"
    END_MARKER_TIMECODE = "end-marker-timecode"
    END_TIME = "end_time"
    END_TIMECODE = "end-timecode"
    END_TIME_FIDELITY = "end_time_fidelity"
    ENTITY_NAME = "entity-name"
    ENTROPY = "entropy"
    ENTRYPOINT_ADDRESS = "entrypoint-address"
    ENTRYPOINT_SECTION_AT_POSITION = "entrypoint-section-at-position"
    ENVIRONMENT = "environment"
    ENVIRONMENT_VARIABLES = "environment-variables"
    EPSG = "epsg"
    ERROR = "error"
    ETA = "ETA"
    EVENT = "event"
    EVENTCODE = "eventCode"
    EVENTID = "EventID"
    EVENTID_1 = "eventid"
    EVENT_ALIAS = "event-alias"
    EVENT_CHANNEL = "event-channel"
    EVENT_DATA = "Event-data"
    EVENT_DATE_TIME = "event-date-time"
    EVENT_DESCRIPTION_TARGET = "event_description.target"
    EVENT_DESCRIPTION_TEXT = "event_description.text"
    EVENT_DESCRIPTION_URL = "event_description.url"
    EVENT_HASH = "event_hash"
    EVENT_ID = "event-id"
    EVENT_LISTING = "event-listing"
    EVENT_NAME = "event-name"
    EVENT_TYPE = "event-type"
    EVENT_TYPE_1 = "event_type"
    EVIDENCES = "evidences"
    EVIDENCE_NUMBER = "evidence-number"
    EXCHANGE = "exchange"
    EXECUTABLE = "executable"
    EXECUTABLE_FILE_NAME = "executable-file-name"
    EXPECTED_ASN = "expected-asn"
    EXPECTED_RESPONSE = "expected-response"
    EXPIRATION = "expiration"
    EXPIRATION_DATE = "expiration-date"
    EXPIRES = "expires"
    EXPLOIT = "exploit"
    EXPLOITDB_ID = "exploitdb-id"
    EXPLOIT_AS_ATTACHMENT = "exploit-as-attachment"
    EXPLOIT_STATUS_AVAILABLE = "exploit-status-available"
    EXPLOIT_STATUS_NOT_OBSERVED = "exploit-status-not-observed"
    EXPLOIT_STATUS_PRODUCTIZED = "exploit-status-productized"
    EXPLOIT_STATUS_WEAPONIZED = "exploit-status-weaponized"
    EXPORT = "export"
    EXTENSION = "extension"
    EXTERIOR_COLOR = "exterior-color"
    EXTERNAL = "external"
    EXTERNAL_DEVICES = "external-devices"
    EXTERNAL_REFERENCES = "external-references"
    EXTRA = "extra"
    E_MAIL = "e-mail"
    FACIAL_COMPOSITE = "facial-composite"
    FAILURES = "failures"
    FAKE_PROCESS_NAME = "fake-process-name"
    FALSE_POSITIVES = "false-positives"
    FALSE_POSITIVES_1 = "false_positives"
    FATHERNAME = "fatherName"
    FATHER_S_FAMILY_NAME___FORENAME = "father-s-family-name-&-forename"
    FAVICON = "favicon"
    FAVICON_MMH3 = "favicon-mmh3"
    FAVORITE_COUNT = "favorite-count"
    FAX_NUMBER = "fax-number"
    FCC_ID = "fcc-id"
    FDENYTSCONNECTIONS_ = "fDenyTSConnections:"
    FEATURED_CHANNEL = "featured-channel"
    FEBRABAN_CODE = "febraban-code"
    FEEDBACKLOOP = "FeedbackLoop"
    FEEDBACK_REQUESTED = "feedback-requested"
    FEEDBACK_SENT = "feedback-sent"
    FEEDBACK_TIME = "feedback-time"
    FEED_ACCURACY = "feed.accuracy"
    FEED_CODE = "feed.code"
    FEED_DOCUMENTATION = "feed.documentation"
    FEED_NAME = "feed.name"
    FEED_PROVIDER = "feed.provider"
    FEED_URL = "feed.url"
    FFT_PLOT = "fft-plot"
    FILE = "file"
    FILEDATE = "fileDate"
    FILENAME = "FileName"
    FILENAME_1 = "fileName"
    FILENAME_2 = "filename"
    FILEPERMISSIONS = "filePermissions"
    FILESIZE = "FileSize"
    FILESIZE_1 = "fileSize"
    FILE_ALIGNMENT = "file-alignment"
    FILE_CONFIG = "file-config"
    FILE_DESCRIPTION = "file-description"
    FILE_ENCODING = "file-encoding"
    FILE_HASH = "file-hash"
    FILE_PATH = "file-path"
    FILE_SIZE = "file_size"
    FILE_VERSION = "file-version"
    FINAL_RANSOM = "final_ransom"
    FINGERPRINT = "fingerprint"
    FINISH_DATE = "finish-date"
    FIPS = "fips"
    FIRMWARE = "firmware"
    FIRSTNAME = "firstName"
    FIRST_LOGIN = "first_login"
    FIRST_NAME = "first-name"
    FIRST_NAME_1 = "first_name"
    FIRST_PACKET_SEEN = "first-packet-seen"
    FIRST_SEEN = "first-seen"
    FIRST_SEEN_1 = "first_seen"
    FIRST_SUBMISSION = "first-submission"
    FLAG = "flag"
    FLAGS = "flags"
    FLOW_COUNT = "flow-count"
    FNSCODE = "fnsCode"
    FOLLOWER = "follower"
    FOLLOWERS = "followers"
    FOLLOWING = "following"
    FORENAME = "forename"
    FORMAT = "format"
    FRAGMENT = "fragment"
    FREE_EMAIL = "free_email"
    FREQUENCY = "frequency"
    FROM = "from"
    FROM_COUNTRY = "from-country"
    FROM_DISPLAY_NAME = "from-display-name"
    FROM_DOMAIN = "from-domain"
    FROM_FUNDS_CODE = "from-funds-code"
    FROM_NAME = "from-name"
    FROM_NUMBER = "from-number"
    FROM_USER = "from-user"
    FSSCODE = "fssCode"
    FULL = "full"
    FULLPATH = "fullpath"
    FULL_LINE = "full-line"
    FULL_NAME = "full-name"
    FULL_NAME_1 = "full_name"
    FULL_USER_NAME = "full-user-name"
    FUNCTION = "function"
    G = "g"
    GAIN = "gain"
    GEARBOX = "gearbox"
    GENDER = "gender"
    GENERATOR = "generator"
    GENERATOR_FINANCIAL_INSTITUTION = "generator-financial-institution"
    GENERIC_SYMMETRIC_KEY = "generic-symmetric-key"
    GEO = "geo"
    GEOLOCATION_ALT = "geolocation_alt"
    GEOLOCATION_LAT = "geolocation_lat"
    GEOLOCATION_LONG = "geolocation_long"
    GET_PROC_ADDRESS = "get-proc-address"
    GIVENNAME = "givenName"
    GML = "gml"
    GOAL = "goal"
    GOALS = "goals"
    GOODSDESCRIPTION = "goodsDescription"
    GOOGLE_ANALYTICS_ID = "google-analytics-id"
    GOVERNMENT_DOMAIN = "government_domain"
    GROSSREGISTEREDTONNAGE = "grossRegisteredTonnage"
    GROUP = "group"
    GROUP_ALIAS = "group-alias"
    GROUP_COMMENT = "group-comment"
    GROUP_ID = "group-id"
    GROUP_NAME = "group-name"
    GROUP_TYPE = "group-type"
    GROUP_USERS = "group-users"
    GTASSIGNEE = "GtAssignee"
    GTLESSEE = "GtLessee"
    GTLESSOR = "GtLessor"
    GTPIMEI = "GtpImei"
    GTPIMSI = "GtpImsi"
    GTPINTERFACE = "GtpInterface"
    GTPMESSAGETYPE = "GtpMessageType"
    GTPMSISDN = "GtpMsisdn"
    GTPSERVINGNETWORK = "GtpServingNetwork"
    GTPVERSION = "GtpVersion"
    GTSUBLESSEE = "GtSubLessee"
    GUID = "guid"
    GUMMEI = "gummei"
    GUTI = "guti"
    GX = "Gx"
    GY = "Gy"
    H = "h"
    HAIRCUT = "haircut"
    HAIR_CHARACTERISTICS = "hair-characteristics"
    HAIR_COLOR = "hair-color"
    HANDLE = "handle"
    HASHTAG = "hashtag"
    HASSH = "hassh"
    HAS_A_RECORDS = "has_a_records"
    HAS_MX_RECORDS = "has_mx_records"
    HAS_SPF_RECORDS = "has_spf_records"
    HEADER = "header"
    HEADERS = "headers"
    HEADER_TITLE = "header-title"
    HEADLINE = "headline"
    HEAD_ACCESSORIES = "head-accessories"
    HEIGHT = "height"
    HEURISTIC_RAW_SCORE = "heuristic_raw_score"
    HEURISTIC_SCORE = "heuristic_score"
    HHHASH = "hhhash"
    HHHASH_HEADERS = "hhhash-headers"
    HHHASH_QUERY_HEADERS = "hhhash-query-headers"
    HHHASH_TOOL = "hhhash-tool"
    HIDDEN = "hidden"
    HIGHEST_PRIVILEGES = "highest-privileges"
    HIGH_PRICE = "high-price"
    HIJACKED_DOMAIN = "hijacked-domain"
    HINTS = "hints"
    HITS = "hits"
    HIVE = "hive"
    HOME_DIR = "home_dir"
    HOST = "host"
    HOSTING_PROVIDER = "hosting-provider"
    HOSTNAME = "hostname"
    HOSTNAME_DST = "hostname-dst"
    HOSTNAME_SOURCE = "hostname_source"
    HOSTNAME_SRC = "hostname-src"
    HTML_STRUCTURE = "html-structure"
    HTTP = "http"
    HTTP_CODE = "http-code"
    HTTP_CODE_1 = "http_code"
    HTTP_DATE = "http_date"
    HTTP_ONLY = "http-only"
    HTTP_REASON = "http_reason"
    HTTP_URL = "http-url"
    HTTP_URL_1 = "http_url"
    HUMAN = "human"
    HUMAN_VALIDATED = "human-validated"
    HW = "hw"
    IBAN = "iban"
    IBANMENTIONED = "ibanMentioned"
    IBCRUC = "ibcRuc"
    ICAOCODE = "icaoCode"
    ICIJID = "icijId"
    ICMP_TYPE = "icmp-type"
    ICON_IMG = "icon-img"
    ICON_IMG_URL = "icon-img-url"
    ID = "id"
    IDENTIFIER = "identifier"
    IDENTITY_CARD_NUMBER = "identity-card-number"
    IDENTITY_CLASS = "identity_class"
    IDNUMBER = "idNumber"
    IDRFLAGS = "IdrFlags"
    IG_CHEAT_BEHAVIOUR = "ig-cheat-behaviour"
    IIN = "iin"
    IMAGE = "image"
    IMAGE_BASE = "image-base"
    IMAGE_PATH = "image-path"
    IMAGE_TEXT = "image-text"
    IMAGE_URL = "image-url"
    IMEI = "imei"
    IMONUMBER = "imoNumber"
    IMO_NUMBER = "IMO-number"
    IMPACT = "impact"
    IMPACT_SERVICESW_URGENCE = "impact-servicesw-urgence"
    IMPACT_TYPE = "impact_type"
    IMPERSONATED_ACCOUNT_NAME = "impersonated-account-name"
    IMPERSONATED_ACCOUNT_URL = "impersonated-account-url"
    IMPFUZZY = "impfuzzy"
    IMPHASH = "imphash"
    IMPLEMENTATION = "implementation"
    IMPLEMENTATION_DETAILS = "implementation-details"
    IMPLEMENTATION_LANGUAGE = "implementation_language"
    IMPLEMENTER = "implementer"
    IMPORT = "import"
    IMPORTANT = "important"
    IMPORTED_SAMPLE = "imported-sample"
    IMPRESSIONS = "impressions"
    IMSI = "imsi"
    INCIDENT = "incident"
    INCIDENT_TYPE = "incident_type"
    INCOME = "income"
    INCORPORATIONDATE = "incorporationDate"
    INDEX = "index"
    INDEXTEXT = "indexText"
    INDEXUPDATEDAT = "indexUpdatedAt"
    INDICATIVE_VALUE = "indicative-value"
    INDICATOR_SUMMARY = "INDICATOR_SUMMARY"
    INDUSTRY = "industry"
    INFECTION_TYPE = "infection_type"
    INFORMATION_TYPE = "information_type"
    INFRASTRUCTURE = "Infrastructure"
    INFRASTRUCTURE_TYPE = "infrastructure_type"
    INITIAL_RANSOM = "initial_ransom"
    INNCODE = "innCode"
    INPUT = "input"
    INREPLYTO = "inReplyTo"
    INSTALLATIONTYPE = "InstallationType"
    INSTALLDATE = "InstallDate"
    INSTANT_MESSAGING_USED = "instant-messaging-used"
    INSTITUTION_CODE = "institution-code"
    INSTITUTION_NAME = "institution-name"
    INSTRUCTION = "instruction"
    INTEGRITY_LEVEL = "integrity-level"
    INTERACTIONS = "interactions"
    INTERCONNECTIONS_AFFECTEES = "interconnections-affectees"
    INTEREST_LEVEL_DISCLOSED_PUBLICLY = "interest-level-disclosed-publicly"
    INTEREST_LEVEL_EXPLOIT_SOUGHT = "interest-level-exploit-sought"
    INTEREST_LEVEL_RESEARCHED_PUBLICLY = "interest-level-researched-publicly"
    INTERFACE = "interface"
    INTERFACE_GUID = "interface-GUID"
    INTERFACE_IPCHECKINGENABLED = "interface-IPcheckingEnabled"
    INTERFACE_LAST_WRITE_TIME = "interface-last-write-time"
    INTERFACE_MEDIASUBTYPE = "interface-MediaSubType"
    INTERFACE_NAME = "interface-name"
    INTERFACE_PNPINSTANCEID = "interface-PnpInstanceID"
    INTERIOR_COLOR = "interior-color"
    INTERNAL_FILENAME = "internal-filename"
    INTERNAL_REFERENCE = "internal-reference"
    INVESTIGATION_STATUS = "investigation_status"
    INVOICEAMOUNT = "invoiceAmount"
    IN_REPLY_TO_DISPLAY_NAME = "in-reply-to-display-name"
    IN_REPLY_TO_PARLEY_ID = "in-reply-to-parley-id"
    IN_REPLY_TO_STATUS_ID = "in-reply-to-status-id"
    IN_REPLY_TO_USER_ID = "in-reply-to-user-id"
    IN_SERVICE_FROM = "in_service_from"
    IN_SERVICE_UNTIL = "in_service_until"
    IOC = "ioc"
    IOCS = "iocs"
    IP = "IP"
    IPDEST = "ipDest"
    IPMENTIONED = "ipMentioned"
    IPOCODE = "ipoCode"
    IPSRC = "ipSrc"
    IP_1 = "ip"
    IP_ADDRESS = "ip-address"
    IP_DST = "ip-dst"
    IP_PROTOCOL_NUMBER = "ip-protocol-number"
    IP_RANGE = "ip-range"
    IP_RANGE_SCORE = "ip-range-score"
    IP_SRC = "ip-src"
    IP_VERSION = "ip_version"
    IQ_SAMPLE = "iq-sample"
    IRSCODE = "irsCode"
    ISBN = "ISBN"
    ISERROR = "isError"
    ISO_MIC = "iso-mic"
    ISP = "ISP"
    ISSUED = "issued"
    ISSUER = "issuer"
    IS_ACTIVE = "is_active"
    IS_CA = "is_ca"
    IS_FAMILY = "is_family"
    IS_MALICIOUS = "is-malicious"
    IS_PUBLIC = "is-public"
    IS_SERVICE_ACCOUNT = "is_service_account"
    IS_SPOOFABLE = "is_spoofable"
    IS_TOR = "is-tor"
    IS_WHITELISTED = "is-whitelisted"
    IV = "iv"
    JA3S_FINGERPRINT_MD5 = "ja3s-fingerprint-md5"
    JA3_FINGERPRINT_MD5 = "ja3-fingerprint-md5"
    JA4_FINGERPRINT = "ja4-fingerprint"
    JA4_TYPE = "ja4-type"
    JARM = "jarm"
    JAR_MD5 = "jar-md5"
    JIBCODE = "jibCode"
    JOINED_DATE = "joined-date"
    JTAG_INTERFACE = "jtag-interface"
    JURISDICTION = "jurisdiction"
    K = "k"
    KERNEL_TIME = "kernel-time"
    KEY = "key"
    KEYALGS = "keyAlgs"
    KEYED_HASH_FUNCTION = "keyed-hash-function"
    KEYWORDS = "Keywords"
    KEYWORDS_1 = "keywords"
    KEY_ID = "key-id"
    KEY_LAST_WRITE_TIME = "key-last-write-time"
    KEY_PATH = "key-path"
    KEY_STEP = "key-step"
    KILL_CHAIN_PHASES = "kill_chain_phases"
    KIT_MAILER = "kit-mailer"
    KIT_NAME = "kit-name"
    KIT_URL = "kit-url"
    KNOWNMALICIOUS = "KnownMalicious"
    KPPCODE = "kppCode"
    LABELS = "labels"
    LAC = "lac"
    LANDTYPE = "landType"
    LANGUAGE = "language"
    LANGUAGE_SPOKEN = "language-spoken"
    LANG_ID = "lang-id"
    LASTNAME = "lastName"
    LASTSEENUTC = "lastSeenUtc"
    LAST_LOGIN = "last_login"
    LAST_LOGIN_TIME = "last-login-time"
    LAST_MODIFIED = "last-modified"
    LAST_NAME = "last-name"
    LAST_NAME_1 = "last_name"
    LAST_PACKET_SEEN = "last-packet-seen"
    LAST_SEEN = "last-seen"
    LAST_SEEN_1 = "last_seen"
    LAST_SUBMISSION = "last-submission"
    LAST_UPDATED = "last-updated"
    LAST_WRITE_DATE_TIME = "last-write-date-time"
    LAST_WRITE_TIME = "last-write-time"
    LATEST = "latest"
    LATITUDE = "latitude"
    LAYER3_PROTOCOL = "layer3-protocol"
    LAYER4_PROTOCOL = "layer4-protocol"
    LAYER7_PROTOCOL = "layer7-protocol"
    LEAK_SITE_URL = "leak-site-url"
    LEGALBASIS = "legalBasis"
    LEGALFORM = "legalForm"
    LEGAL_COPYRIGHT = "legal-copyright"
    LEGAL_FORM = "legal-form"
    LEGAL_NOTICE_CAPTION = "Legal-notice-caption"
    LEGAL_NOTICE_TEXT = "Legal-notice-text"
    LENGTH = "length"
    LEVEL = "level"
    LEVEL_OF_KNOWLEDGE = "level-of-knowledge"
    LICENSE = "license"
    LICENSE_ID = "license-id"
    LICENSE_ID_1 = "license_id"
    LICENSE_PLATE_NUMBER = "license-plate-number"
    LIKES = "likes"
    LINK = "link"
    LISTED = "listed"
    LNK_ACCESS_TIME = "lnk-access-time"
    LNK_COMMAND_LINE_ARGUMENTS = "lnk-command-line-arguments"
    LNK_CREATION_TIME = "lnk-creation-time"
    LNK_DESCRIPTION = "lnk-description"
    LNK_DRIVE_SERIAL_NUMBER = "lnk-drive-serial-number"
    LNK_DRIVE_TYPE = "lnk-drive-type"
    LNK_FILE_ATTRIBUTE_FLAGS = "lnk-file-attribute-flags"
    LNK_FILE_SIZE = "lnk-file-size"
    LNK_HOT_KEY_VALUE = "lnk-hot-key-value"
    LNK_ICON_INDEX = "lnk-icon-index"
    LNK_LOCAL_PATH = "lnk-local-path"
    LNK_MODIFICATION_TIME = "lnk-modification-time"
    LNK_RELATIVE_PATH = "lnk-relative-path"
    LNK_SHOW_WINDOW_VALUE = "lnk-show-window-value"
    LNK_VOLUME_LABEL = "lnk-volume-label"
    LNK_WORKING_DIRECTORY = "lnk-working-directory"
    LOADER_FLAGS = "loader-flags"
    LOCAL_REFERENCES = "local-references"
    LOCATION = "location"
    LOCATIONMENTIONED = "locationMentioned"
    LOG = "log"
    LOGFILE = "logfile"
    LOGIN_COUNT = "login-count"
    LOGLINE = "logline"
    LOGO = "logo"
    LOGON_USER_NAME = "logon-user-name"
    LONGITUDE = "longitude"
    LOSS_TYPE = "loss_type"
    LOTNUMBER = "lotNumber"
    LOW_PRICE = "low-price"
    MACCS = "macCS"
    MACHINEMUID = "machineMuid"
    MACHINENAME = "machineName"
    MACHINEPATH = "machinePath"
    MACHINE_IDENTIFIER = "machine-identifier"
    MACHINE_TYPE = "machine-type"
    MACHINE_TYPE_HEX = "machine-type-hex"
    MACHINE_VALIDATED = "machine-validated"
    MAC_ADDRESS = "MAC-address"
    MAC_DST = "mac-dst"
    MAC_SRC = "mac-src"
    MAGIC = "magic"
    MAGIC_HEX = "magic-hex"
    MAINCOUNTRY = "mainCountry"
    MAJOR_IMAGE_VERSION = "major-image-version"
    MAJOR_LINKER_VERSION = "major-linker-version"
    MAJOR_OS_VERSION = "major-os-version"
    MAJOR_SUBSYSTEM_VERSION = "major-subsystem-version"
    MAKE = "make"
    MALEVAL_PROBABILITY = "malEval-probability"
    MALEVAL_SEVERITY = "malEval-severity"
    MALICIOUS = "malicious"
    MALICIOUS_URL = "malicious-url"
    MALWARE = "MALWARE"
    MALWARE_HASH_MD5 = "malware.hash.md5"
    MALWARE_HASH_SHA1 = "malware.hash.sha1"
    MALWARE_HASH_SHA256 = "malware.hash.sha256"
    MALWARE_NAME = "malware.name"
    MALWARE_SAMPLE = "malware-sample"
    MALWARE_TYPE = "malware_type"
    MALWARE_VERSION = "malware.version"
    MANUFACTURER = "manufacturer"
    MAPAPPLICATIONCONTEXT = "MapApplicationContext"
    MAPGMLC = "MapGmlc"
    MAPGSMSCFGT = "MapGsmscfGT"
    MAPIMSI = "MapImsi"
    MAPMSCGT = "MapMscGT"
    MAPMSISDN = "MapMsisdn"
    MAPOPCODE = "MapOpCode"
    MAPSMSCGT = "MapSmscGT"
    MAPSMSTEXT = "MapSmsText"
    MAPSMSTP_DCS = "MapSmsTP-DCS"
    MAPSMSTP_OA = "MapSmsTP-OA"
    MAPSMSTP_PID = "MapSmsTP-PID"
    MAPSMSTYPENUMBER = "MapSmsTypeNumber"
    MAPUSSDCODING = "MapUssdCoding"
    MAPUSSDCONTENT = "MapUssdContent"
    MAPVERSION = "MapVersion"
    MAPVLRGT = "MapVlrGT"
    MAX_AMOUNT = "max_amount"
    MAX_ATTEMPTS = "max_attempts"
    MBSCODE = "mbsCode"
    MCC = "mcc"
    MD5 = "MD5"
    MD5_1 = "md5"
    MEDIA = "media"
    MEMBER_COUNT = "member-count"
    MEME_REFERENCE = "meme-reference"
    MEMORY_ALLOCATIONS = "memory-allocations"
    MESSAGE = "message"
    MESSAGEID = "messageId"
    MESSAGE_ID = "message-id"
    MESSAGE_TYPE = "message-type"
    METADATA = "metadata"
    METADATA_ONLY = "metadata_only"
    META_DOI = "meta_doi"
    METHOD = "method"
    METHODOLOGY = "Methodology"
    MIDDLENAME = "middleName"
    MIDDLE_NAME = "middle-name"
    MIMETYPE = "mimeType"
    MIMETYPE_1 = "mimetype"
    MIME_BOUNDARY = "mime-boundary"
    MIME_TYPE = "mime-type"
    MIME_TYPE_1 = "mime_type"
    MINOR_IMAGE_VERSION = "minor-image-version"
    MINOR_LINKER_VERSION = "minor-linker-version"
    MINOR_OS_VERSION = "minor-os-version"
    MINOR_SUBSYSTEM_VERSION = "minor-subsystem-version"
    MIN_AMOUNT = "min_amount"
    MISP_ATTRIBUTE_UUID = "misp.attribute_uuid"
    MISP_EVENT_UUID = "misp.event_uuid"
    MISP_UUID = "misp-uuid"
    MISS_API = "miss-api"
    MITRE_TECHNIQUES = "mitre-techniques"
    MMSI = "MMSI"
    MMSI_1 = "mmsi"
    MNC = "mnc"
    MODEL = "model"
    MODERATOR = "moderator"
    MODERATOR_OF = "moderator-of"
    MODIFICATION_DATE = "modification-date"
    MODIFICATION_TIME = "modification-time"
    MODIFIED = "modified"
    MODIFIEDAT = "modifiedAt"
    MODULE = "module"
    MODULES = "modules"
    MODULUS = "modulus"
    MONTHLY_C13 = "monthly-c13"
    MONTHLY_C13_SEASONAL_ADJUSTMENT = "monthly-c13-seasonal-adjustment"
    MONTHLY_C13_SMOOTHED = "monthly-c13-smoothed"
    MONTHLY_C13_SMOOTHED_SEASONAL_ADJUSTMENT = "monthly-c13-smoothed-seasonal-adjustment"
    MONTHLY_CO2 = "monthly-co2"
    MONTHLY_CO2_SEASONAL_ADJUSTMENT = "monthly-co2-seasonal-adjustment"
    MONTHLY_CO2_SMOOTHED = "monthly-co2-smoothed"
    MONTHLY_CO2_SMOOTHED_SEASONAL_ADJUSTMENT = "monthly-co2-smoothed-seasonal-adjustment"
    MONTHLY_O18 = "monthly-o18"
    MONTHLY_O18_SEASONAL_ADJUSTMENT = "monthly-o18-seasonal-adjustment"
    MONTHLY_O18_SMOOTHED = "monthly-o18-smoothed"
    MONTHLY_O18_SMOOTHED_SEASONAL_ADJUSTMENT = "monthly-o18-smoothed-seasonal-adjustment"
    MORE_INFORMATIONS = "more informations"
    MOTHERNAME = "motherName"
    MOTHERS_NAME = "mothers-name"
    MOTHER_S_FAMILY_NAME___FORENAME = "mother-s-family-name-&-forename"
    MOTIVATION = "motivation"
    MOUNT_POINTS = "mount-points"
    MP_EXPORT = "mp-export"
    MP_IMPORT = "mp-import"
    MSG = "msg"
    MSGTYPE = "msgType"
    MSISDN = "msisdn"
    MX_RECORD = "mx-record"
    N = "n"
    NAICS = "naics"
    NAME = "name"
    NAMECHANGEDATE = "nameChangeDate"
    NAMESERVER = "nameserver"
    NAMESMENTIONED = "namesMentioned"
    NAMESPACE = "namespace"
    NAME_OF_THE_ANALYST = "name-of-the-analyst"
    NARRATIVE_DISPROOF = "narrative-disproof"
    NARRATIVE_SUMMARY = "narrative-summary"
    NATIONALITY = "nationality"
    NATIONAL_DESTINATION_CODE = "national-destination-code"
    NAVIGATIONAL_STATUS = "navigational-status"
    NAVIGATIONAREA = "navigationArea"
    NEGOTIATIONS_SCREENSHOT = "negotiations_screenshot"
    NEGOTIATIONS_TRANSCRIPT = "negotiations_transcript"
    NEIGHBORHOOD = "neighborhood"
    NETWORK_CONNECTED_TO = "network-connected-to"
    NETWORK_KEY = "network-key"
    NETWORK_KEY_LAST_WRITE_TIME = "network-key-last-write-time"
    NETWORK_KEY_PATH = "network-key-path"
    NICKNAME = "nickname"
    NIC_HDL = "nic-hdl"
    NIE = "nie"
    NIF = "nif"
    NODE = "node"
    NODE_ID = "node_id"
    NOISE = "noise"
    NOMBRE_UTILISATEURS_TOUCHES = "nombre-utilisateurs-touches"
    NOM_CONTACT_INCIDENT = "nom-contact-incident"
    NOM_ENTREPRISE = "nom-entreprise"
    NON_BANKING_INSTITUTION = "non-banking-institution"
    NOTE = "note"
    NOTES = "notes"
    NOTE_UUID = "note-uuid"
    NOTICEID = "noticeId"
    NOTICE_COLOR = "notice-color"
    NOTIFICATION = "notification"
    NOT_REFERENCED_STRINGS = "not-referenced-strings"
    NS_RECORD = "ns-record"
    NUKEONDELETE = "nukeOnDelete"
    NUMBER = "number"
    NUMBERAWARDS = "numberAwards"
    NUMBER_FLASK = "number-flask"
    NUMBER_OF_RVA_AND_SIZE = "number-of-rva-and-size"
    NUMBER_OF_SYMBOLS = "number-of-symbols"
    NUMBER_SECTIONS = "number-sections"
    NUM_CHANNELS = "num_channels"
    NUTSCODE = "nutsCode"
    O18_VALUE = "o18-value"
    OBJECTIVE = "objective"
    OBSERVED = "observed"
    OCCUPATION = "occupation"
    OFAC_IDENTIFICATION_NUMBER = "ofac-identification-number"
    OFFSET = "offset"
    OGRNCODE = "ogrnCode"
    OKOPFCODE = "okopfCode"
    OKPOCODE = "okpoCode"
    OKSMCODE = "oksmCode"
    OKVEDCODE = "okvedCode"
    ONLINE = "online"
    ONSET = "onset"
    ON_PREMISE_SANDBOX = "on-premise-sandbox"
    OPENCORPORATESURL = "opencorporatesUrl"
    OPENED = "opened"
    OPENTIDE_OBJECT = "opentide-object"
    OPENTIDE_RELATION = "opentide-relation"
    OPENTIDE_TYPE = "opentide-type"
    OPERATING_SYSTEM = "operating-system"
    OPERATIONAL_CODE = "Operational-code"
    OPERATOR = "operator"
    OPPPORTUNITIES = "oppportunities"
    OPTION = "option"
    ORG = "org"
    ORGANISATION = "organisation"
    ORGANIZATION = "organization"
    ORGANIZATION_TYPE = "organization-type"
    ORIGIN = "origin"
    ORIGINAL_DATE = "original-date"
    ORIGINAL_FILENAME = "original-filename"
    ORIGINAL_FILENAME_1 = "original_filename"
    ORIGINAL_LANGUAGE = "original-language"
    ORIGINAL_TEXT = "original-text"
    ORIGINCOUNTRY = "originCountry"
    ORIGIN_GITHUB_API = "origin-github-api"
    ORIGIN_HOST = "Origin-Host"
    ORIGIN_HOST_COUNTRYISO2 = "Origin-Host-CountryISO2"
    ORIGIN_HOST_OPERATORNAME = "Origin-Host-OperatorName"
    ORIGIN_HOST_TADIG = "Origin-Host-TADIG"
    ORIGIN_REALM = "Origin-Realm"
    ORIGIN_REALM_COUNTRYISO2 = "Origin-Realm-CountryISO2"
    ORIGIN_REALM_OPERATORNAME = "Origin-Realm-OperatorName"
    ORIGIN_REALM_TADIG = "Origin-Realm-TADIG"
    ORIGIN_URL = "origin-url"
    OS = "OS"
    OS_ABI = "os_abi"
    OTHER = "other"
    OTHER_FACIAL_FEATURES = "other-facial-features"
    OUTCOME = "outcome"
    OUTCOMES_ATTITUDE = "outcomes_attitude"
    OUTCOMES_BEHAVIOR = "outcomes_behavior"
    OUTCOMES_EMOTION = "outcomes_emotion"
    OUTCOMES_IDENTITY = "outcomes_identity"
    OUTPUT = "output"
    OWNERSHIPTYPE = "ownershipType"
    P = "p"
    PACKAGEARCH = "PackageArch"
    PACKAGEDESCRIPTION = "PackageDescription"
    PACKAGEMAINTAINER = "PackageMaintainer"
    PACKAGENAME = "PackageName"
    PACKAGERELEASE = "PackageRelease"
    PACKAGEVERSION = "PackageVersion"
    PACKET_COUNT = "packet-count"
    PAGE_ALIAS = "page-alias"
    PAGE_ID = "page-id"
    PAGE_NAME = "page-name"
    PAGE_TYPE = "page-type"
    PARAMETER = "parameter"
    PARENT_COMMAND = "parent-command"
    PARENT_COMMAND_LINE = "parent-command-line"
    PARENT_GUID = "parent-guid"
    PARENT_IMAGE = "parent-image"
    PARENT_PID = "parent-pid"
    PARENT_PROCESS_NAME = "parent-process-name"
    PARENT_PROCESS_PATH = "parent-process-path"
    PART = "part"
    PASSPORTNUMBER = "passportNumber"
    PASSPORT_COUNTRY = "passport-country"
    PASSPORT_CREATION = "passport-creation"
    PASSPORT_EXPIRATION = "passport-expiration"
    PASSPORT_NUMBER = "passport-number"
    PASSWORD = "password"
    PASSWORDEXPIRYWARINING = "PasswordExpiryWarining"
    PASSWORD_LAST_CHANGED = "password_last_changed"
    PASSWORD_STORED = "password-stored"
    PASTE = "paste"
    PASTE_FILE = "paste-file"
    PASTFLAGS = "pastFlags"
    PASTNAMES = "pastNames"
    PASTTYPES = "pastTypes"
    PATCH_STATUS = "patch-status"
    PATH = "path"
    PATHID = "pathID"
    PATHNAME = "PathName"
    PATH_DOWNLOADEDTO = "path-downloadedTo"
    PATH_ENCODING = "path-encoding"
    PATTERN_IN_FILE = "pattern-in-file"
    PATTERN_MATCHES = "pattern-matches"
    PATTERN_SELECTED = "pattern-selected"
    PAYLOAD_BIN = "payload_bin"
    PAYMENT_DUE_DATE = "payment-due-date"
    PAYMENT_STATUS = "payment-status"
    PAYMENT_VALUE = "payment-value"
    PAY_FOR_DELETION = "pay_for_deletion"
    PAY_FOR_ENCRYPTOR = "pay_for_encryptor"
    PDFHASH = "pdfHash"
    PEHASH = "pehash"
    PEM = "pem"
    PEOPLEMENTIONED = "peopleMentioned"
    PERCENTAGE = "percentage"
    PERCENTAGE_OF_REVENUE = "percentage_of_revenue"
    PERMALINK = "permalink"
    PERMISSION = "permission"
    PERSONALNUMBER = "personalNumber"
    PERSONAL_ACCOUNT_TYPE = "personal-account-type"
    PERSON_NAME = "person-name"
    PFRNUMBER = "pfrNumber"
    PGID = "pgid"
    PHASE = "Phase"
    PHASH_DCT_BASE64 = "phash-dct-base64"
    PHISHING_DOMAIN = "phishing-domain"
    PHISHING_IP = "phishing-ip"
    PHISHTANK_DETAIL_URL = "phishtank-detail-url"
    PHISHTANK_ID = "phishtank-id"
    PHNAME = "PhName"
    PHONE = "phone"
    PHONEMENTIONED = "phoneMentioned"
    PHONE_COMPANY = "phone-company"
    PHONE_NUMBER = "phone-number"
    PHOTO = "photo"
    PHSEQUENCE = "PhSequence"
    PICTURE_DEVICE = "picture-device"
    PICTURE_PCB = "picture-pcb"
    PID = "pid"
    PLACE_OF_BIRTH = "place-of-birth"
    PLACE_OF_DISAPPEARANCE = "place-of-disappearance"
    PLANNED = "planned"
    PLATFORM = "platform"
    PLATFORMS = "platforms"
    PLAYBOOK_ABSTRACTION = "playbook-abstraction"
    PLAYBOOK_BASE64 = "playbook-base64"
    PLAYBOOK_CREATION_TIME = "playbook-creation-time"
    PLAYBOOK_CREATOR = "playbook-creator"
    PLAYBOOK_FILE = "playbook-file"
    PLAYBOOK_ID = "playbook-id"
    PLAYBOOK_IMPACT = "playbook-impact"
    PLAYBOOK_MODIFICATION_TIME = "playbook-modification-time"
    PLAYBOOK_PRIORITY = "playbook-priority"
    PLAYBOOK_SEVERITY = "playbook-severity"
    PLAYBOOK_STANDARD = "playbook-standard"
    PLAYBOOK_TYPE = "playbook-type"
    PLAYBOOK_VALID_FROM = "playbook-valid-from"
    PLAYBOOK_VALID_UNTIL = "playbook-valid-until"
    PLAYLIST_ID = "playlist-id"
    PLAYLIST_NAME = "playlist-name"
    POC = "poc"
    POINTER_TO_SYMBOL_TABLE = "pointer-to-symbol-table"
    POINTS = "points"
    POLICE_DOMAIN = "police_domain"
    PORT = "port"
    PORTDEST = "PortDest"
    PORTRAIT = "portrait"
    PORTSRC = "PortSrc"
    POSITION = "position"
    POSSIBLY_SENSITIVE = "possibly-sensitive"
    POSSIBLY_SENSITIVE_APPEALABLE = "possibly-sensitive-appealable"
    POST = "post"
    POSTAL_CODE = "postal-code"
    POSTS = "posts"
    POST_CONTENT = "post-content"
    POST_ID = "post-id"
    POST_LOCATION = "post-location"
    POST_TITLE = "post-title"
    POURCENTAGE_UTILISATEURS_TOUCHES = "pourcentage-utilisateurs-touches"
    POWERDOWNAFTERSHUTDOWN = "PowerdownAfterShutDown"
    PRECISION = "precision"
    PRECREATEKNOWNFOLDERS = "PreCreateKnownFolders"
    PREDECESSOR = "predecessor"
    PREDICATE = "predicate"
    PREREQUISITES = "prerequisites"
    PRESENT_FAMILY_NAME = "present-family-name"
    PREVIOUSNAME = "previousName"
    PRICING = "pricing"
    PRIMARY_ASSET = "primary-asset"
    PRIMARY_MOTIVATION = "primary-motivation"
    PRIORITY = "priority"
    PRIVACY = "privacy"
    PRIVATE = "private"
    PRIVATE_KEYS = "private_keys"
    PRIVILEGED = "privileged"
    PROBABILITY = "probability"
    PROCEDURE = "procedure"
    PROCEDURENUMBER = "procedureNumber"
    PROCESSES = "processes"
    PROCESSINGERROR = "processingError"
    PROCESSINGSTATUS = "processingStatus"
    PROCESSING_TIMESTAMP = "processing-timestamp"
    PROCESSOR_ID = "Processor-ID"
    PROCESS_NAME = "process-name"
    PROCESS_STATE = "process-state"
    PRODUCER = "producer"
    PRODUCT = "product"
    PRODUCTID = "ProductID"
    PRODUCTNAME = "ProductName"
    PRODUCT_NAME = "product-name"
    PRODUCT_VERSION = "product-version"
    PROFILE = "profile"
    PROFILE_BANNER = "profile-banner"
    PROFILE_BANNER_URL = "profile-banner-url"
    PROFILE_IMAGE = "profile-image"
    PROFILE_IMAGE_URL = "profile-image-url"
    PROFILE_PHOTO = "profile-photo"
    PROGRAM = "program"
    PROGRAMME = "programme"
    PROGRAM_NAME = "program-name"
    PROJECT = "project"
    PROJECT_URL = "project_url"
    PROMPT = "prompt"
    PROOF = "proof"
    PROOF_OF_CONCEPT = "proof-of-concept"
    PROOF_SCREENSHOT = "proof-screenshot"
    PROPERTYTYPE = "propertyType"
    PROPULSION = "propulsion"
    PROTO = "proto"
    PROTOCOL = "protocol"
    PROTOCOL_APPLICATION = "protocol.application"
    PROTOCOL_TRANSPORT = "protocol.transport"
    PROVIDER = "provider"
    PROVINCE = "province"
    PROVINCE_STATE = "province-state"
    PROXY_AUTHENTICATE = "proxy_authenticate"
    PROXY_PASSWORD = "proxy-password"
    PROXY_USER = "proxy-user"
    PTR_RECORD = "ptr-record"
    PUBKEY_INFO_ALGORITHM = "pubkey-info-algorithm"
    PUBKEY_INFO_EXPONENT = "pubkey-info-exponent"
    PUBKEY_INFO_MODULUS = "pubkey-info-modulus"
    PUBKEY_INFO_SIZE = "pubkey-info-size"
    PUBLIC = "public"
    PUBLIC_GISTS = "public_gists"
    PUBLIC_KEY = "public-key"
    PUBLIC_KEYS = "public_keys"
    PUBLIC_REPOS = "public_repos"
    PUBLISHDATE = "publishDate"
    PUBLISHED = "published"
    PUBLISHEDAT = "publishedAt"
    PUBLISHER = "publisher"
    PUBLISHERURL = "publisherUrl"
    PURPOSE = "purpose"
    PURPOSE_OF_DOCUMENT = "purpose-of-document"
    PWD_FAIL_DATE = "pwd-fail-date"
    PWD_RESET_TIME = "pwd-reset-time"
    Q = "q"
    QUERIED_DOMAIN = "queried-domain"
    QUERY = "query"
    QUERY_RULE_NAME = "query-rule-name"
    QUERY_STRING = "query_string"
    QUESTIONS = "questions"
    QUEUE = "queue"
    R2_COMMIT_VERSION = "r2-commit-version"
    RANKING = "ranking"
    RANSOMWARE_GROUP = "ransomware-group"
    RATE_OF_TURN = "rate-of-turn"
    RATIO_API = "ratio-api"
    RATIO_FUNCTIONS = "ratio-functions"
    RATIO_SIMILARITY = "ratio-similarity"
    RATIO_STRING = "ratio-string"
    RAW = "raw"
    RAW_BASE64 = "raw-base64"
    RAW_DATA = "raw-data"
    RAW_RDATA = "raw_rdata"
    RAW_REPORT = "raw-report"
    RDATA = "rdata"
    REAL_NAME = "real-name"
    REASON = "reason"
    RECEIVED_DATE = "received-date"
    RECEIVED_HEADER_HOSTNAME = "received-header-hostname"
    RECEIVED_HEADER_IP = "received-header-ip"
    RECEIVERNUMBER = "receiverNumber"
    RECENT_FILES_ACCESSED = "recent-files-accessed"
    RECENT_FOLDERS_ACCESSED = "recent-folders-accessed"
    RECORDER = "recorder"
    RECORDID = "recordId"
    RECORDING_DATE = "recording-date"
    RECORD_COUNT = "record_count"
    RECORD_SIZE = "record_size"
    RECOVERABILITY = "recoverability"
    RECOVERED = "recovered"
    RECURRING_TYPE = "recurring-type"
    REDIRECT_URL = "redirect-url"
    REDRESS_NUMBER = "redress-number"
    REF = "ref"
    REFERENCE = "reference"
    REFERENCED_STRINGS = "referenced-strings"
    REFERENCES = "references"
    REFERENCE_LINK = "reference-link"
    REFERER = "referer"
    REFERRER = "referrer"
    REFSGLOBALVAR = "refsglobalvar"
    REGEXP = "regexp"
    REGEXP_TYPE = "regexp-type"
    REGION = "region"
    REGIONS = "regions"
    REGION_CODE = "region-code"
    REGISTEREDORGANIZATION = "RegisteredOrganization"
    REGISTEREDOWNER = "RegisteredOwner"
    REGISTRANT_EMAIL = "registrant-email"
    REGISTRANT_NAME = "registrant-name"
    REGISTRANT_ORG = "registrant-org"
    REGISTRANT_PHONE = "registrant-phone"
    REGISTRAR = "registrar"
    REGISTRATIONDATE = "registrationDate"
    REGISTRATIONNUMBER = "registrationNumber"
    REGISTRATIONPORT = "registrationPort"
    REGISTRATION_DATE = "registration-date"
    REGISTRATION_NUMBER = "registration-number"
    REGISTRY_KEY = "REGISTRY_KEY"
    RELATED_PAGE_ID = "related-page-id"
    RELATED_PAGE_NAME = "related-page-name"
    RELATED_WEAKNESS = "related-weakness"
    RELATIONSHIP = "relationship"
    RELATIVE_CORRELATION_ID = "Relative-Correlation-ID"
    REMARKS = "Remarks"
    REMARQUES = "remarques"
    REMOVAL_DATE = "removal-date"
    REPEAT = "repeat"
    REPLY_TO = "reply-to"
    REPLY_TO_DISPLAY_NAME = "reply-to-display-name"
    REPORTBOOTOK = "ReportBootOk"
    REPORT_CODE = "report-code"
    REPORT_FILE = "report-file"
    REPORT_LINK = "REPORT_LINK"
    REPORT_STATUS = "report-status"
    REPORT_UID = "report-uid"
    REPORT_URL = "report-url"
    REPOSITORY = "repository"
    REPUTATION = "reputation"
    REQUESTER = "requester"
    REQUEST_ID = "request-id"
    RESEARCH_DOMAIN = "research-domain"
    RESEARCH_LINKS = "research-links"
    RESOURCEDESC = "resourceDesc"
    RESOURCES = "Resources"
    RESOURCE_LEVEL = "resource_level"
    RESOURCE_PATH = "resource_path"
    RESPONSES = "responses"
    RESPONSETYPE = "responseType"
    RESPONSE_ACTION = "response-action"
    RESPONSI = "responsi"
    RESTRICTION = "restriction"
    RESULT = "Result"
    RESULTS = "results"
    RESULT_1 = "result"
    RESULT_NAME = "result_name"
    RETIRED = "retired"
    RETRIEVEDAT = "retrievedAt"
    RETURN_PATH = "return-path"
    RETWEET_COUNT = "retweet-count"
    REVERSE_DNS = "reverse-dns"
    REVIEWDATE = "reviewDate"
    REVOKED = "revoked"
    RICHPE = "richpe"
    RID = "rid"
    RIOT = "riot"
    RISKY_TLD = "risky_tld"
    RISK_LEVEL = "risk-level"
    ROGUE_DNS = "rogue-dns"
    ROLE = "role"
    ROLES = "roles"
    ROLE_ADDRESS = "role_address"
    ROOT_KEYS = "root-keys"
    ROWCOUNT = "rowCount"
    RRNAME = "rrname"
    RRTYPE = "rrtype"
    RSA_MODULUS_SIZE = "rsa-modulus-size"
    RTIR_ID = "rtir_id"
    RULES = "rules"
    RUNNING_ACCOUNT = "running-account"
    RUN_WHEN_USER_LOGGED_ON_ONLY = "run-when-user-logged-on-only"
    RUSSIAN_FREE_EMAIL = "russian_free_email"
    S = "s"
    SAAS_SANDBOX = "saas-sandbox"
    SAMPLE_DATETIME = "sample-datetime"
    SAMPLE_DATE_EXCEL = "sample-date-excel"
    SAMPLE_DATE_FRACTIONAL = "sample-date-fractional"
    SAMPLE_RATE = "sample_rate"
    SAMPLINGRATE = "samplingRate"
    SANDBOX_FILE = "sandbox-file"
    SANDBOX_TYPE = "sandbox-type"
    SCANNING_HOST = "scanning_host"
    SCANNING_IP = "scanning_ip"
    SCAN_END = "scan-end"
    SCAN_RESULT = "scan-result"
    SCAN_RESULT_FORMAT = "scan-result-format"
    SCAN_RESULT_QUERY = "scan-result-query"
    SCAN_RESULT_TOOL = "scan-result-tool"
    SCAN_START = "scan-start"
    SCAN_TYPE = "scan-type"
    SCCPCDGT = "SccpCdGT"
    SCCPCDGT_COUNTRY = "SccpCdGT-Country"
    SCCPCDGT_COUNTRYISO2 = "SccpCdGT-CountryISO2"
    SCCPCDGT_OPERATORNAME = "SccpCdGT-OperatorName"
    SCCPCDGT_TADIG = "SccpCdGT-TADIG"
    SCCPCDPC = "SccpCdPC"
    SCCPCDSSN = "SccpCdSSN"
    SCCPCGGT = "SccpCgGT"
    SCCPCGGT_COUNTRY = "SccpCgGT-Country"
    SCCPCGGT_COUNTRYISO2 = "SccpCgGT-CountryISO2"
    SCCPCGGT_OPERATORNAME = "SccpCgGT-OperatorName"
    SCCPCGGT_TADIG = "SccpCgGT-TADIG"
    SCCPCGPC = "SccpCgPC"
    SCCPCGSSN = "SccpCgSSN"
    SCHEDULE = "schedule"
    SCHEDULED_DATE = "scheduled-date"
    SCHEDULED_END = "scheduled_end"
    SCHEDULED_START = "scheduled_start"
    SCHEME = "scheme"
    SCOPE = "scope"
    SCORE = "score"
    SCORES = "scores"
    SCREENSHOT = "screenshot"
    SCREENSHOT_URL = "screenshot_url"
    SCRIPT = "script"
    SCRIPT_AS_ATTACHMENT = "script-as-attachment"
    SEARCH = "search"
    SECONDARY_MOTIVATION = "secondary-motivation"
    SECONDNAME = "secondName"
    SECRETARY = "secretary"
    SECTION_ALIGNMENT = "section-alignment"
    SECTOR = "sector"
    SECTORS = "sectors"
    SECURE = "secure"
    SELF_SIGNED = "self_signed"
    SENDER = "sender"
    SENDERNAME = "senderName"
    SENDER_IP = "sender-ip"
    SEND_DATE = "send-date"
    SENSOR = "sensor"
    SENSOR_ID = "sensor_id"
    SENT = "sent"
    SENT_DATE = "sent-date"
    SEQ = "seq"
    SEQUENCENUMBER = "sequenceNumber"
    SERIALNUMBER = "serialNumber"
    SERIAL_INTERFACE = "serial-interface"
    SERIAL_NUMBER = "serial-number"
    SERIES = "series"
    SERVER = "server"
    SERVER_NAME = "server-name"
    SERVICE = "service"
    SERVICE_ABUSE = "service-abuse"
    SESSION = "session"
    SESSIONID = "SessionId"
    SESSION_ID = "Session-ID"
    SETTINGS_COMPETITION_OBSERVERS = "settings_competition_observers"
    SETTINGS_COMPETITION_RECEIVERS = "settings_competition_receivers"
    SETTINGS_COMPETITION_SPEAKERS = "settings_competition_speakers"
    SETTINGS_CULTURE = "settings_culture"
    SETTINGS_PROCESS = "settings_process"
    SETTINGS_SPACE = "settings_space"
    SETTINGS_TIME = "settings_time"
    SEVERITY = "severity"
    SEX = "sex"
    SHA1 = "SHA1"
    SHA1_1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "SHA256"
    SHA256_1 = "sha256"
    SHA384 = "sha384"
    SHA3_224 = "sha3-224"
    SHA3_256 = "sha3-256"
    SHA3_384 = "sha3-384"
    SHA3_512 = "sha3-512"
    SHA512 = "sha512"
    SHA512_224 = "sha512/224"
    SHA512_256 = "sha512/256"
    SHAPE_OF_EYES = "shape-of-eyes"
    SHARESCOUNT = "sharesCount"
    SHARESCURRENCY = "sharesCurrency"
    SHARESTYPE = "sharesType"
    SHARESVALUE = "sharesValue"
    SHARE_LINK = "share-link"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHELL = "Shell"
    SHELL_1 = "shell"
    SHELL_COMMAND = "shell-command"
    SHELL_PATH = "shell-path"
    SHOE_SIZE = "shoe-size"
    SHORTENED_URL = "shortened-url"
    SHORTEST_PATH_TO_CREATE_THREAD = "shortest-path-to-create-thread"
    SHOULD_BLOCK = "should_block"
    SHUTDOWNFLAGS = "ShutdownFlags"
    SHUTDOWNWITHOUTLOGON = "ShutdownWithoutLogon"
    SHUTDOWN_TIME = "shutdown-time"
    SID = "SID"
    SIGMA = "sigma"
    SIGMA_RULE = "sigma_rule"
    SIGMA_RULE_NAME = "sigma-rule-name"
    SIGMF_ARCHIVE = "SigMF-archive"
    SIGMF_DATA = "SigMF-data"
    SIGMF_META = "SigMF-meta"
    SIGNATURE = "signature"
    SIGNATURE_ALGORITHM = "signature_algorithm"
    SIZE = "size"
    SIZE_IN_BYTES = "size-in-bytes"
    SIZE_OF_CODE = "size-of-code"
    SIZE_OF_HEADERS = "size-of-headers"
    SIZE_OF_HEAP_COMMIT = "size-of-heap-commit"
    SIZE_OF_HEAP_RESERVE = "size-of-heap-reserve"
    SIZE_OF_IMAGE = "size-of-image"
    SIZE_OF_INITIALISED_DATA = "size-of-initialised-data"
    SIZE_OF_OPTIONAL_HEADER = "size-of-optional-header"
    SIZE_OF_STACK_COMMIT = "size-of-stack-commit"
    SIZE_OF_STACK_RESERVE = "size-of-stack-reserve"
    SIZE_OF_UNINITIALISED_DATA = "size-of-uninitialised-data"
    SKIN_CHARATERISTICS = "skin-charateristics"
    SKIN_COMPLEXION = "skin-complexion"
    SMSC = "smsc"
    SOA_RECORD = "soa-record"
    SOCIAL_SECURITY_NUMBER = "social-security-number"
    SOCKET_TYPE = "socket-type"
    SOFTWARE = "SOFTWARE"
    SOFTWARETYPE = "SoftwareType"
    SOFTWARE_1 = "software"
    SOLUTIONS = "solutions"
    SOLVES = "solves"
    SOURCE = "Source"
    SOURCEURL = "sourceUrl"
    SOURCE_1 = "source"
    SOURCE_ABUSE_CONTACT = "source.abuse_contact"
    SOURCE_ACCOUNT = "source.account"
    SOURCE_ALLOCATED = "source.allocated"
    SOURCE_ASN = "source.asn"
    SOURCE_AS_NAME = "source.as_name"
    SOURCE_DOMAIN = "source-domain"
    SOURCE_DOMAIN_SUFFIX = "source.domain_suffix"
    SOURCE_FQDN = "source.fqdn"
    SOURCE_GEOLOCATION_CC = "source.geolocation.cc"
    SOURCE_GEOLOCATION_CITY = "source.geolocation.city"
    SOURCE_GEOLOCATION_COUNTRY = "source.geolocation.country"
    SOURCE_GEOLOCATION_CYMRU_CC = "source.geolocation.cymru_cc"
    SOURCE_GEOLOCATION_GEOIP_CC = "source.geolocation.geoip_cc"
    SOURCE_GEOLOCATION_LATITUDE = "source.geolocation.latitude"
    SOURCE_GEOLOCATION_LONGITUDE = "source.geolocation.longitude"
    SOURCE_GEOLOCATION_REGION = "source.geolocation.region"
    SOURCE_GEOLOCATION_STATE = "source.geolocation.state"
    SOURCE_IP = "source-ip"
    SOURCE_IP_1 = "source.ip"
    SOURCE_LOCAL_HOSTNAME = "source.local_hostname"
    SOURCE_LOCAL_IP = "source.local_ip"
    SOURCE_MISC = "source-misc"
    SOURCE_NETWORK = "source.network"
    SOURCE_PORT = "source.port"
    SOURCE_REGISTRY = "source.registry"
    SOURCE_REVERSE_DNS = "source.reverse_dns"
    SOURCE_TOR_NODE = "source.tor_node"
    SOURCE_URL = "source.url"
    SOURCE_URLPATH = "source.urlpath"
    SPACIAL_REFERENCE = "spacial-reference"
    SPEED_OVER_GROUND = "speed-over-ground"
    SPEED_SUBMERGED = "speed_submerged"
    SPEED_SURFACED = "speed_surfaced"
    SPF_RECORD = "spf-record"
    SPI_INTERFACE = "spi-interface"
    SPONSOR = "sponsor"
    SPORT = "sport"
    SRC = "src"
    SRCLOC = "srcloc"
    SRC_AS = "src-as"
    SRC_BYTES_COUNT = "src-bytes-count"
    SRC_BYTES_COUNT_1 = "src_bytes_count"
    SRC_HOSTNAME = "src_hostname"
    SRC_IP = "src_ip"
    SRC_MAC = "src_mac"
    SRC_PACKETS = "src_packets"
    SRC_PACKETS_COUNT = "src-packets-count"
    SRC_PORT = "src-port"
    SRC_PORT_1 = "src_port"
    SRV_RECORD = "srv-record"
    SSDEEP = "SSDEEP"
    SSDEEP_1 = "ssdeep"
    SSH_PUBLIC_KEY = "ssh-public-key"
    STAGE = "stage"
    STAIRWELL_FIRST_SEEN = "stairwell-first-seen"
    START = "start"
    STARTDATE = "startDate"
    START_DATE = "start-date"
    START_MARKER_TIMECODE = "start-marker-timecode"
    START_TIME = "Start-time"
    START_TIMECODE = "start-timecode"
    START_TIME_1 = "start-time"
    START_TIME_2 = "start_time"
    START_TIME_FIDELITY = "start_time_fidelity"
    STATE = "state"
    STATS_DELETIONS = "stats.deletions"
    STATS_FILES = "stats.files"
    STATS_INSERTIONS = "stats.insertions"
    STATS_LINES = "stats.lines"
    STATUS = "status"
    STATUS_CODE = "status-code"
    STIX2_PATTERN = "stix2-pattern"
    STRATEGY_ABSTRACT = "strategy_abstract"
    STREET = "street"
    SUBDOMAIN = "subdomain"
    SUBJECT = "subject"
    SUBMISSION_TIME = "submission-time"
    SUBMITTED_TIME = "submitted_time"
    SUBMITTER_ID = "submitter-id"
    SUBMIT_TEXT = "submit-text"
    SUBNET_ANNOUNCED = "subnet-announced"
    SUBREDDIT_ALIAS = "subreddit-alias"
    SUBREDDIT_NAME = "subreddit-name"
    SUBREDDIT_TYPE = "subreddit-type"
    SUBSCRIBER_COUNT = "subscriber-count"
    SUBSCRIBER_NUMBER = "subscriber-number"
    SUBSYSTEM = "subsystem"
    SUBSYSTEM_HEX = "subsystem-hex"
    SUBTITLE = "subtitle"
    SUBTYPE = "subtype"
    SUB_TYPE = "sub-type"
    SUCCESFUL = "succesful"
    SUCCESS = "success"
    SUCCESSOR = "successor"
    SUMMARY = "summary"
    SUPPORTING_EVIDENCE = "supporting-evidence"
    SURICATA = "suricata"
    SURNAME = "surname"
    SUSPICIOUS_DOMAIN = "suspicious_domain"
    SUSPICIOUS_EMAIL = "suspicious_email"
    SUSPICIOUS_USERNAME = "suspicious_username"
    SWID = "swid"
    SWIFT = "swift"
    SWIFTBIC = "swiftBic"
    SW_EDITION = "sw_edition"
    SYMBOL = "symbol"
    SYSTEM = "system"
    SYSTEMROOT = "SystemRoot"
    T = "t"
    TAG = "tag"
    TAGS = "tags"
    TAKEDOWN_REQUEST = "takedown-request"
    TAKEDOWN_REQUEST_TO = "takedown-request-to"
    TAKEDOWN_TIME = "takedown-time"
    TARGET = "target"
    TARGETED_IP_OF_SYSTEM = "targeted_ip_of_system"
    TARGETED_MACHINE = "targeted_machine"
    TARGET_COUNTRIES = "target-countries"
    TARGET_HW = "target_hw"
    TARGET_ID = "target-id"
    TARGET_SW = "target_sw"
    TASK_CATEGORY = "task-category"
    TASK_TYPE = "task_type"
    TASK_UUID = "task-uuid"
    TATTOO_BODY_PART = "tattoo-body-part"
    TATTOO_COLOR = "tattoo-color"
    TATTOO_DESCRIPTION = "tattoo-description"
    TATTOO_PICTURE = "tattoo-picture"
    TATTOO_SIZE = "tattoo-size"
    TATTOO_STYLE = "tattoo-style"
    TAXNUMBER = "taxNumber"
    TAXPAID = "taxPaid"
    TAXSTATUS = "taxStatus"
    TCPIP_KEY = "TCPIP-key"
    TCPIP_KEY_LAST_WRITE_TIME = "TCPIP-key-last-write-time"
    TCP_FLAGS = "tcp-flags"
    TEAM_MEMBER = "team-member"
    TECHNICAL_CONTEXT = "technical_context"
    TECHNIQUE = "technique"
    TELEPHONE_CONTACT_INCIDENT = "telephone-contact-incident"
    TELFHASH = "telfhash"
    TELLER = "teller"
    TENURE = "tenure"
    TEXT = "text"
    TEXTFIELD = "textfield"
    THREADTOPIC = "threadTopic"
    THREAD_ID = "Thread-ID"
    THREAD_INDEX = "thread-index"
    THREAT = "threat"
    THREATID = "threatid"
    THREATS = "threats"
    THREAT_ACTOR = "THREAT_ACTOR"
    THREAT_ACTOR_1 = "threat-actor"
    THREAT_ACTOR_EMAIL = "threat-actor-email"
    THREAT_ACTOR_INFRASTRUCTURE_PATTERN = "threat-actor-infrastructure-pattern"
    THREAT_ACTOR_INFRASTRUCTURE_VALUE = "threat-actor-infrastructure-value"
    THREAT_SCORE = "threat-score"
    THREAT_SCORE_1 = "threat_score"
    THR_CATEGORY = "thr_category"
    THUMBNAIL = "thumbnail"
    THUMBNAIL_URL = "thumbnail-url"
    TICKET_NUMBER = "ticket-number"
    TIME = "time"
    TIMESTAMP = "Timestamp"
    TIMESTAMP_1 = "timestamp"
    TIMESTAMP_DESC = "timestamp_desc"
    TIMESTAMP_SEEN = "timestamp_seen"
    TIMEZONE_BIAS = "timezone-bias"
    TIMEZONE_DAYLIGHT_BIAS = "timezone-daylight-bias"
    TIMEZONE_DAYLIGHT_DATE = "timezone-daylight-date"
    TIMEZONE_DAYLIGHT_NAME = "timezone-daylight-name"
    TIMEZONE_LAST_WRITE_TIME = "timezone-last-write-time"
    TIMEZONE_STANDARD_BIAS = "timezone-standard-bias"
    TIMEZONE_STANDARD_DATE = "timezone-standard-date"
    TIMEZONE_STANDARD_NAME = "timezone-standard-name"
    TIME_FIRST = "time_first"
    TIME_FIRST_MS = "time_first_ms"
    TIME_GENERATED = "time_generated"
    TIME_LAST = "time_last"
    TIME_LAST_MS = "time_last_ms"
    TIME_OBSERVATION = "time.observation"
    TIME_PRECISION = "time-precision"
    TIME_SOURCE = "time.source"
    TITLE = "title"
    TITLENUMBER = "titleNumber"
    TLD = "tld"
    TLP = "tlp"
    TLSH = "TLSH"
    TLSH_1 = "tlsh"
    TLS_IMPLEMENTATION = "tls-implementation"
    TMSI = "tmsi"
    TMSI_1 = "tmsi-1"
    TMSI_2 = "tmsi-2"
    TO = "to"
    TOKEN = "token"
    TONNAGE = "tonnage"
    TOOL = "tool"
    TOOLS_USED = "tools used"
    TOPICS = "topics"
    TOP_ACCESSORIES = "top-accessories"
    TOTAL = "total"
    TOTAL_API = "total-api"
    TOTAL_BITS = "total-bits"
    TOTAL_BPS = "total-bps"
    TOTAL_BYTES_SENT = "total-bytes-sent"
    TOTAL_CAPACITY = "total-capacity"
    TOTAL_CONFIRMED = "total-confirmed"
    TOTAL_CURED = "total-cured"
    TOTAL_DEATH = "total-death"
    TOTAL_FUNCTIONS = "total-functions"
    TOTAL_PACKETS_SENT = "total-packets-sent"
    TOTAL_PPS = "total-pps"
    TOTAL_RECEIVED = "total-received"
    TOTAL_SENT = "total-sent"
    TOTAL_TRANSACTIONS = "total-transactions"
    TO_COUNTRY = "to-country"
    TO_DISPLAY_NAME = "to-display-name"
    TO_FUNDS_CODE = "to-funds-code"
    TO_NAME = "to-name"
    TO_NUMBER = "to-number"
    TO_USER = "to-user"
    TRACEABILITY_IMPACT = "traceability_impact"
    TRACKER = "tracker"
    TRADINGCOUNTRY = "tradingCountry"
    TRAILING_BYTES = "trailing_bytes"
    TRAITEMENT_INCIDENT = "traitement-incident"
    TRANSACTIONNUMBER = "transactionNumber"
    TRANSACTION_NUMBER = "transaction-number"
    TRANSCRIPTION = "transcription"
    TRANSFER_ENCODING = "transfer_encoding"
    TRANSLATED_TEXT = "translated-text"
    TRANSLATION_LANGUAGE = "translation-language"
    TRANSLATION_SERVICE = "translation-service"
    TRANSLATION_TYPE = "translation-type"
    TRANSMODE_CODE = "transmode-code"
    TRANSMODE_COMMENT = "transmode-comment"
    TREATMENTS_MEDIUM = "treatments_medium"
    TREATMENTS_MESSAGE_CONTENT = "treatments_message_content"
    TREATMENTS_TOPIC = "treatments_topic"
    TRIGGER = "trigger"
    TROPHIES = "trophies"
    TRUE_HEADING = "true-heading"
    TRUE_HEADING_AT_OWN_POSITION = "true-heading-at-own-position"
    TRUNCATED_HASH_HTML_STRUCTURE = "truncated-hash-html-structure"
    TRUST = "trust"
    TRUST_LEVEL = "trust-level"
    TWEETS = "tweets"
    TWITTER_FOLLOWERS = "twitter-followers"
    TWITTER_FOLLOWING = "twitter-following"
    TWITTER_ID = "twitter-id"
    TWITTER_USERNAME = "twitter_username"
    TXT_RECORD = "txt-record"
    TYPE = "type"
    TYPED_URLS = "typed-urls"
    TYPE_OF_ACCOUNT = "type-of-account"
    TYPE_OF_ORGANIZATION = "type-of-organization"
    TYPE_OF_SHIP = "type-of-ship"
    TYPE_OF_TICKET = "type-of-ticket"
    TYPE_OF_TRANSPORT = "type-of-transport"
    UNDERGROUND_ACTIVITY_STATUS = "underground-activity-status"
    UNDERGROUND_ACTIVITY_SUMMARY = "underground-activity-summary"
    UNKNOWN_REFERENCES = "unknown-references"
    UPDATABLE = "updatable"
    UPDATE = "update"
    UPVOTES = "upvotes"
    URGENCY = "urgency"
    URI = "uri"
    URL = "URL"
    URL_1 = "url"
    URL_LEAKSITE = "url_leaksite"
    URL_REDIRECT = "url-redirect"
    URL_RFC5724 = "url-rfc5724"
    USED_CAPACITY = "used-capacity"
    USER = "User"
    USERID = "userid"
    USERINIT = "UserInit"
    USERNAME = "Username"
    USERNAME_1 = "username"
    USERNAME_QUOTED = "username-quoted"
    USER_1 = "user"
    USER_ACCOUNT = "user-account"
    USER_AGENT = "user-agent"
    USER_AVATAR = "user-avatar"
    USER_CREATOR = "user-creator"
    USER_FULLNAME = "user-fullname"
    USER_ID = "user-id"
    USER_ID_EMAIL = "user-id-email"
    USER_ID_NAME = "user-id-name"
    USER_INIT = "user-init"
    USER_NAME = "user-name"
    USER_PROCESS = "user-process"
    USER_PROFILE_KEY_LAST_WRITE_TIME = "user-profile-key-last-write-time"
    USER_PROFILE_KEY_PATH = "user-profile-key-path"
    USER_PROFILE_LAST_WRITE_TIME = "user-profile-last-write-time"
    USER_PROFILE_PATH = "user-profile-path"
    USER_TIME = "user-time"
    USE_SSL = "use-ssl"
    UUID = "uuid"
    VALIDATION = "validation"
    VALIDITY_NOT_AFTER = "validity-not-after"
    VALIDITY_NOT_BEFORE = "validity-not-before"
    VALID_FORMAT = "valid_format"
    VALID_TLD = "valid_tld"
    VALUE = "value"
    VALUE_BTC = "value_BTC"
    VALUE_EUR = "value_EUR"
    VALUE_USD = "value_USD"
    VARIATIONS_FOUND_NUMBER = "variations-found-number"
    VARIATIONS_NUMBER = "variations-number"
    VARIETY = "variety"
    VAT = "VAT"
    VATCODE = "vatCode"
    VEDCODE = "vedCode"
    VEDCODEDESCRIPTION = "vedCodeDescription"
    VENDOR = "vendor"
    VENDOR_IMPLEMENTATION_REF = "vendor-implementation-ref"
    VENDOR_NAME = "vendor-name"
    VERDICT = "verdict"
    VERIFICATION_TIME = "verification-time"
    VERIFIED = "verified"
    VERIFIED_USERNAME = "verified-username"
    VERSION = "version"
    VERSION_LINE = "version_line"
    VHASH = "vhash"
    VIA = "via"
    VICTIM = "Victim"
    VICTIM_1 = "victim"
    VIDEO_LINK = "video-link"
    VIDEO_TITLE = "video-title"
    VIDEO_TRANSCRIPT = "video-transcript"
    VIN = "vin"
    VIRTUAL_ADDRESS = "virtual_address"
    VIRTUAL_SIZE = "virtual_size"
    VOENCODE = "voenCode"
    VOLUME = "volume"
    VT_SHA256 = "vt-sha256"
    VULNERABILITY_STATUS = "vulnerability-status"
    VULNERABILITY_TYPE = "vulnerability-type"
    VULNERABLE_CONFIGURATION = "vulnerable-configuration"
    VULNERABLE_CONFIGURATION_1 = "vulnerable_configuration"
    WALLET_ADDRESS = "wallet-address"
    WATERFALL_PLOT = "waterfall-plot"
    WATERMARK = "watermark"
    WEAKALIAS = "weakAlias"
    WEAKNESS_ABS = "weakness-abs"
    WEALTH = "wealth"
    WEB = "web"
    WEBPAGE = "webpage"
    WEBSITE = "website"
    WEBSITE_RESSOURCE_DIFF = "website-ressource-diff"
    WEBSITE_SIMILARITY = "website-similarity"
    WEBSITE_TITLE = "website-title"
    WEB_SANDBOX = "web-sandbox"
    WEB_URL = "web_url"
    WEIGHT = "weight"
    WHITELIST = "whitelist"
    WHOIS_CREATION_DATE = "whois-creation-date"
    WHOIS_EXPIRATION_DATE = "whois-expiration-date"
    WHOIS_REGISTRANT_EMAIL = "whois-registrant-email"
    WHOIS_REGISTRANT_NAME = "whois-registrant-name"
    WHOIS_REGISTRANT_ORG = "whois-registrant-org"
    WHOIS_REGISTRANT_PHONE = "whois-registrant-phone"
    WHOIS_REGISTRAR = "whois-registrar"
    WIKIDATAID = "wikidataId"
    WIKIPEDIAURL = "wikipediaUrl"
    WIN32_VERSION_VALUE = "win32-version-value"
    WINLOGON_KEY_LAST_WRITE_TIME = "winlogon-key-last-write-time"
    WINLOGON_KEY_PATH = "winlogon-key-path"
    WINSTATIONSDISABLED = "WinStationsDisabled"
    WIN_CV_PATH = "win-cv-path"
    X = "x"
    X509_FINGERPRINT_MD5 = "x509-fingerprint-md5"
    X509_FINGERPRINT_SHA1 = "x509-fingerprint-sha1"
    X509_FINGERPRINT_SHA256 = "x509-fingerprint-sha256"
    X_HEADER_NAME = "x-header-name"
    X_MAILER = "x-mailer"
    X_VALUE = "x-value"
    Y = "y"
    YARA = "yara"
    YARA_HUNT = "yara-hunt"
    YARA_RULE_MATCH = "yara-rule-match"
    YARA_RULE_NAME = "yara-rule-name"
    YEAR = "year"
    ZIPCODE = "zipcode"
    ZONE_IMPACTEE = "zone-impactee"
    ZONE_TIME_FIRST = "zone_time_first"
    ZONE_TIME_LAST = "zone_time_last"
    _0DAY_TODAY_ID = "0day-today-id"
    _5DS_OF_PROPAGANDA = "5Ds-of-propaganda"


# Object relation to attribute type mappings
OBJECT_RELATION_ATTRIBUTE_MAPPING: Dict[ObjectType, Dict[ObjectRelation, AttributeType]] = {
    ObjectType.ADS: {
        ObjectRelation.ACD_ELEMENT: AttributeType.TEXT,
        ObjectRelation.ADDITIONAL_RESOURCES: AttributeType.URL,
        ObjectRelation.BLIND_SPOTS_AND_ASSUMPTIONS: AttributeType.TEXT,
        ObjectRelation.CATEGORIZATION: AttributeType.TEXT,
        ObjectRelation.CATEGORIZATION_OTHERS: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.DATETIME,
        ObjectRelation.FALSE_POSITIVES_1: AttributeType.TEXT,
        ObjectRelation.GOAL: AttributeType.TEXT,
        ObjectRelation.PRIORITY: AttributeType.TEXT,
        ObjectRelation.RESPONSES: AttributeType.TEXT,
        ObjectRelation.SIGMA_RULE: AttributeType.SIGMA,
        ObjectRelation.STRATEGY_ABSTRACT: AttributeType.TEXT,
        ObjectRelation.TECHNICAL_CONTEXT: AttributeType.TEXT,
        ObjectRelation.VALIDATION: AttributeType.TEXT,
    },
    ObjectType.ABUSEIPDB: {
        ObjectRelation.ABUSE_CONFIDENCE_SCORE: AttributeType.INTEGER,
        ObjectRelation.IS_MALICIOUS: AttributeType.BOOLEAN,
        ObjectRelation.IS_PUBLIC: AttributeType.BOOLEAN,
        ObjectRelation.IS_TOR: AttributeType.BOOLEAN,
        ObjectRelation.IS_WHITELISTED: AttributeType.BOOLEAN,
    },
    ObjectType.AI_CHAT_PROMPT: {
        ObjectRelation.ACT_AS: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.PROMPT: AttributeType.TEXT,
        ObjectRelation.RESULT_1: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
    },
    ObjectType.AIL_LEAK: {
        ObjectRelation.DUPLICATE: AttributeType.TEXT,
        ObjectRelation.DUPLICATE_NUMBER: AttributeType.COUNTER,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.ORIGINAL_DATE: AttributeType.DATETIME,
        ObjectRelation.RAW_DATA: AttributeType.ATTACHMENT,
        ObjectRelation.SENSOR: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.AIS: {
        ObjectRelation.ETA: AttributeType.DATETIME,
        ObjectRelation.IMO_NUMBER: AttributeType.TEXT,
        ObjectRelation.MMSI: AttributeType.TEXT,
        ObjectRelation.CALL_SIGN: AttributeType.TEXT,
        ObjectRelation.COURSE_OVER_GROUND: AttributeType.FLOAT,
        ObjectRelation.DESTINATION: AttributeType.TEXT,
        ObjectRelation.DIMENSION_A: AttributeType.FLOAT,
        ObjectRelation.DIMENSION_B: AttributeType.FLOAT,
        ObjectRelation.DIMENSION_C: AttributeType.FLOAT,
        ObjectRelation.DIMENSION_D: AttributeType.FLOAT,
        ObjectRelation.DRAUGHT: AttributeType.FLOAT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAVIGATIONAL_STATUS: AttributeType.FLOAT,
        ObjectRelation.RATE_OF_TURN: AttributeType.TEXT,
        ObjectRelation.SPEED_OVER_GROUND: AttributeType.FLOAT,
        ObjectRelation.TRUE_HEADING: AttributeType.FLOAT,
        ObjectRelation.TRUE_HEADING_AT_OWN_POSITION: AttributeType.FLOAT,
        ObjectRelation.TYPE_OF_SHIP: AttributeType.TEXT,
    },
    ObjectType.AIS_INFO: {
        ObjectRelation.ADMINISTRATIVE_AREA: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.INDUSTRY: AttributeType.TEXT,
        ObjectRelation.ORGANISATION: AttributeType.TEXT,
    },
    ObjectType.ANDROID_APP: {
        ObjectRelation.APPID: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE: AttributeType.SHA1,
        ObjectRelation.CERTIFICATE_SHA256: AttributeType.SHA256,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
    },
    ObjectType.ANDROID_PERMISSION: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.PERMISSION: AttributeType.TEXT,
    },
    ObjectType.ANNOTATION: {
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.MODIFICATION_DATE: AttributeType.DATETIME,
        ObjectRelation.REF: AttributeType.LINK,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.ANONYMISATION: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENCRYPTION_FUNCTION: AttributeType.TEXT,
        ObjectRelation.IV: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEYED_HASH_FUNCTION: AttributeType.TEXT,
        ObjectRelation.LEVEL_OF_KNOWLEDGE: AttributeType.TEXT,
        ObjectRelation.METHOD: AttributeType.TEXT,
        ObjectRelation.REGEXP: AttributeType.TEXT,
    },
    ObjectType.APIVOID_EMAIL_VERIFICATION: {
        ObjectRelation.CHINA_FREE_EMAIL: AttributeType.BOOLEAN,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DIRTY_WORDS_DOMAIN: AttributeType.BOOLEAN,
        ObjectRelation.DIRTY_WORDS_USERNAME: AttributeType.BOOLEAN,
        ObjectRelation.DISPOSABLE: AttributeType.BOOLEAN,
        ObjectRelation.DMARC_CONFIGURED: AttributeType.BOOLEAN,
        ObjectRelation.DMARC_ENFORCED: AttributeType.BOOLEAN,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.DOMAIN_POPULAR: AttributeType.BOOLEAN,
        ObjectRelation.EDUCATIONAL_DOMAIN: AttributeType.BOOLEAN,
        ObjectRelation.EMAIL: AttributeType.EMAIL,
        ObjectRelation.FREE_EMAIL: AttributeType.BOOLEAN,
        ObjectRelation.GOVERNMENT_DOMAIN: AttributeType.BOOLEAN,
        ObjectRelation.HAS_A_RECORDS: AttributeType.BOOLEAN,
        ObjectRelation.HAS_MX_RECORDS: AttributeType.BOOLEAN,
        ObjectRelation.HAS_SPF_RECORDS: AttributeType.BOOLEAN,
        ObjectRelation.IS_SPOOFABLE: AttributeType.BOOLEAN,
        ObjectRelation.POLICE_DOMAIN: AttributeType.BOOLEAN,
        ObjectRelation.RISKY_TLD: AttributeType.BOOLEAN,
        ObjectRelation.ROLE_ADDRESS: AttributeType.BOOLEAN,
        ObjectRelation.RUSSIAN_FREE_EMAIL: AttributeType.BOOLEAN,
        ObjectRelation.SCORE: AttributeType.FLOAT,
        ObjectRelation.SHOULD_BLOCK: AttributeType.BOOLEAN,
        ObjectRelation.SUSPICIOUS_DOMAIN: AttributeType.BOOLEAN,
        ObjectRelation.SUSPICIOUS_EMAIL: AttributeType.BOOLEAN,
        ObjectRelation.SUSPICIOUS_USERNAME: AttributeType.BOOLEAN,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.VALID_FORMAT: AttributeType.BOOLEAN,
        ObjectRelation.VALID_TLD: AttributeType.BOOLEAN,
    },
    ObjectType.ARTIFACT: {
        ObjectRelation.DECRYPTION_KEY: AttributeType.TEXT,
        ObjectRelation.ENCRYPTION_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.MIME_TYPE_1: AttributeType.MIME_TYPE,
        ObjectRelation.PAYLOAD_BIN: AttributeType.ATTACHMENT,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA3_256: AttributeType.SHA3_256,
        ObjectRelation.SHA3_512: AttributeType.SHA3_512,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.TLSH_1: AttributeType.TLSH,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.ASN: {
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EXPORT: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IMPORT: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.MP_EXPORT: AttributeType.TEXT,
        ObjectRelation.MP_IMPORT: AttributeType.TEXT,
        ObjectRelation.SUBNET_ANNOUNCED: AttributeType.IP_SRC,
    },
    ObjectType.ATTACK_PATTERN: {
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PREREQUISITES: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.RELATED_WEAKNESS: AttributeType.WEAKNESS,
        ObjectRelation.SOLUTIONS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.ATTACK_STEP: {
        ObjectRelation.COMMAND_LINE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTIONS: AttributeType.TEXT,
        ObjectRelation.DST_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.DST_IP: AttributeType.IP_DST,
        ObjectRelation.DST_MISC: AttributeType.TEXT,
        ObjectRelation.EXPECTED_RESPONSE: AttributeType.TEXT,
        ObjectRelation.KEY_STEP: AttributeType.BOOLEAN,
        ObjectRelation.SOURCE_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.SOURCE_IP: AttributeType.IP_SRC,
        ObjectRelation.SOURCE_MISC: AttributeType.TEXT,
        ObjectRelation.SUCCESFUL: AttributeType.BOOLEAN,
    },
    ObjectType.ATTACKER_INFRA: {
        ObjectRelation.ARCHITECTURE: AttributeType.TEXT,
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.BEACON_HOST_1: AttributeType.TEXT,
        ObjectRelation.BEACON_HTTP_GET: AttributeType.TEXT,
        ObjectRelation.BEACON_HTTP_POST: AttributeType.TEXT,
        ObjectRelation.BEACON_TYPE_1: AttributeType.TEXT,
        ObjectRelation.BINARY_MD5_1: AttributeType.MD5,
        ObjectRelation.BINARY_SHA1_1: AttributeType.SHA1,
        ObjectRelation.BINARY_SHA256_1: AttributeType.SHA256,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.CONFIG_MD5_1: AttributeType.MD5,
        ObjectRelation.CONFIG_SHA1_1: AttributeType.SHA1,
        ObjectRelation.CONFIG_SHA256_1: AttributeType.SHA256,
        ObjectRelation.CONTENT_LENGTH_1: AttributeType.TEXT,
        ObjectRelation.CONTENT_TYPE_1: AttributeType.TEXT,
        ObjectRelation.ENCODED_DATA_1: AttributeType.TEXT,
        ObjectRelation.ENCODED_LENGTH_1: AttributeType.TEXT,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.HOSTNAME: AttributeType.TEXT,
        ObjectRelation.HOSTNAME_SOURCE: AttributeType.TEXT,
        ObjectRelation.HTTP: AttributeType.TEXT,
        ObjectRelation.HTTP_CODE_1: AttributeType.TEXT,
        ObjectRelation.HTTP_URL_1: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.LICENSE_ID_1: AttributeType.TEXT,
        ObjectRelation.NAICS: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.TEXT,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.REGION: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.TAG: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.DATETIME,
    },
    ObjectType.AUTHENTICATION_FAILURE_REPORT: {
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.TOTAL: AttributeType.COUNTER,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.AUTHENTICODE_SIGNERINFO: {
        ObjectRelation.CONTENT_TYPE: AttributeType.TEXT,
        ObjectRelation.DIGEST_BASE64: AttributeType.TEXT,
        ObjectRelation.DIGEST_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.ENCRYPTION_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.ISSUER: AttributeType.TEXT,
        ObjectRelation.PROGRAM_NAME: AttributeType.TEXT,
        ObjectRelation.SERIAL_NUMBER: AttributeType.TEXT,
        ObjectRelation.SIGNATURE_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.AV_SIGNATURE: {
        ObjectRelation.DATETIME: AttributeType.DATETIME,
        ObjectRelation.SIGNATURE: AttributeType.TEXT,
        ObjectRelation.SOFTWARE_1: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.AVAILABILITY_IMPACT: {
        ObjectRelation.AVAILABILITY_IMPACT: AttributeType.TEXT,
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
    },
    ObjectType.BANK_ACCOUNT: {
        ObjectRelation.ABA_RTN: AttributeType.ABA_RTN,
        ObjectRelation.ACCOUNT: AttributeType.BANK_ACCOUNT_NR,
        ObjectRelation.ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.BALANCE: AttributeType.TEXT,
        ObjectRelation.BENEFICIARY: AttributeType.TEXT,
        ObjectRelation.BENEFICIARY_COMMENT: AttributeType.TEXT,
        ObjectRelation.BRANCH: AttributeType.TEXT,
        ObjectRelation.CLIENT_NUMBER: AttributeType.TEXT,
        ObjectRelation.CLOSED: AttributeType.DATETIME,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.CURRENCY_CODE: AttributeType.TEXT,
        ObjectRelation.DATE_BALANCE: AttributeType.DATETIME,
        ObjectRelation.IBAN: AttributeType.IBAN,
        ObjectRelation.INSTITUTION_CODE: AttributeType.TEXT,
        ObjectRelation.INSTITUTION_NAME: AttributeType.TEXT,
        ObjectRelation.NON_BANKING_INSTITUTION: AttributeType.BOOLEAN,
        ObjectRelation.OPENED: AttributeType.DATETIME,
        ObjectRelation.PERSONAL_ACCOUNT_TYPE: AttributeType.TEXT,
        ObjectRelation.REPORT_CODE: AttributeType.TEXT,
        ObjectRelation.STATUS_CODE: AttributeType.TEXT,
        ObjectRelation.SWIFT: AttributeType.BIC,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.BGP_HIJACK: {
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTED_ASN: AttributeType.AS,
        ObjectRelation.END: AttributeType.DATETIME,
        ObjectRelation.EXPECTED_ASN: AttributeType.AS,
        ObjectRelation.START: AttributeType.DATETIME,
        ObjectRelation.SUBNET_ANNOUNCED: AttributeType.IP_SRC,
    },
    ObjectType.BGP_RANKING: {
        ObjectRelation.ADDRESS_FAMILY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.DATETIME,
        ObjectRelation.POSITION: AttributeType.FLOAT,
        ObjectRelation.RANKING: AttributeType.FLOAT,
    },
    ObjectType.BLOG: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MODIFICATION_DATE: AttributeType.DATETIME,
        ObjectRelation.POST: AttributeType.TEXT,
        ObjectRelation.REMOVAL_DATE: AttributeType.DATETIME,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
        ObjectRelation.VERIFIED_USERNAME: AttributeType.TEXT,
    },
    ObjectType.BOLETO: {
        ObjectRelation.BENEFICIARY: AttributeType.TEXT,
        ObjectRelation.BENEFICIARY_BANK_ACCOUNT: AttributeType.BANK_ACCOUNT_NR,
        ObjectRelation.BENEFICIARY_BANK_AGENCY: AttributeType.BANK_ACCOUNT_NR,
        ObjectRelation.BOLETO_NUMBER: AttributeType.TEXT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.FEBRABAN_CODE: AttributeType.TEXT,
        ObjectRelation.GENERATOR_FINANCIAL_INSTITUTION: AttributeType.TEXT,
        ObjectRelation.PAYMENT_DUE_DATE: AttributeType.DATETIME,
        ObjectRelation.PAYMENT_STATUS: AttributeType.TEXT,
        ObjectRelation.PAYMENT_VALUE: AttributeType.FLOAT,
        ObjectRelation.REQUESTER: AttributeType.TEXT,
    },
    ObjectType.BTC_TRANSACTION: {
        ObjectRelation.BTC_ADDRESS: AttributeType.BTC,
        ObjectRelation.TIME: AttributeType.DATETIME,
        ObjectRelation.TRANSACTION_NUMBER: AttributeType.TEXT,
        ObjectRelation.VALUE_BTC: AttributeType.FLOAT,
        ObjectRelation.VALUE_EUR: AttributeType.FLOAT,
        ObjectRelation.VALUE_USD: AttributeType.FLOAT,
    },
    ObjectType.BTC_WALLET: {
        ObjectRelation.BTC_RECEIVED: AttributeType.FLOAT,
        ObjectRelation.BTC_SENT: AttributeType.FLOAT,
        ObjectRelation.BALANCE_BTC: AttributeType.FLOAT,
        ObjectRelation.TIME: AttributeType.DATETIME,
        ObjectRelation.WALLET_ADDRESS: AttributeType.BTC,
    },
    ObjectType.C2_LIST: {
        ObjectRelation.C2_IP: AttributeType.IP_SRC,
        ObjectRelation.C2_IPPORT: AttributeType.IP_SRC_PORT,
        ObjectRelation.REPORT_URL: AttributeType.LINK,
        ObjectRelation.THREAT: AttributeType.TEXT,
    },
    ObjectType.CAP_ALERT: {
        ObjectRelation.ADDRESSES: AttributeType.TEXT,
        ObjectRelation.CODE: AttributeType.TEXT,
        ObjectRelation.IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.INCIDENT: AttributeType.TEXT,
        ObjectRelation.MSGTYPE: AttributeType.TEXT,
        ObjectRelation.NOTE: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.TEXT,
        ObjectRelation.RESTRICTION: AttributeType.TEXT,
        ObjectRelation.SCOPE: AttributeType.TEXT,
        ObjectRelation.SENDER: AttributeType.TEXT,
        ObjectRelation.SENT: AttributeType.DATETIME,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
    },
    ObjectType.CAP_INFO: {
        ObjectRelation.AUDIENCE: AttributeType.TEXT,
        ObjectRelation.CATEGORY_1: AttributeType.TEXT,
        ObjectRelation.CERTAINTY: AttributeType.TEXT,
        ObjectRelation.CONTACT: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EFFECTIVE: AttributeType.DATETIME,
        ObjectRelation.EVENT: AttributeType.TEXT,
        ObjectRelation.EVENTCODE: AttributeType.TEXT,
        ObjectRelation.EXPIRES: AttributeType.DATETIME,
        ObjectRelation.HEADLINE: AttributeType.TEXT,
        ObjectRelation.INSTRUCTION: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.ONSET: AttributeType.DATETIME,
        ObjectRelation.PARAMETER: AttributeType.TEXT,
        ObjectRelation.RESPONSETYPE: AttributeType.TEXT,
        ObjectRelation.SENDERNAME: AttributeType.TEXT,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.URGENCY: AttributeType.TEXT,
        ObjectRelation.WEB: AttributeType.LINK,
    },
    ObjectType.CAP_RESOURCE: {
        ObjectRelation.DEREFURI: AttributeType.ATTACHMENT,
        ObjectRelation.DIGEST: AttributeType.SHA1,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.RESOURCEDESC: AttributeType.TEXT,
        ObjectRelation.SIZE: AttributeType.TEXT,
        ObjectRelation.URI: AttributeType.LINK,
    },
    ObjectType.CERT_PL_PHISHING: {
        ObjectRelation.FAVICON_MMH3: AttributeType.TEXT,
        ObjectRelation.HTML_STRUCTURE: AttributeType.TEXT,
        ObjectRelation.PHASH_DCT_BASE64: AttributeType.TEXT,
        ObjectRelation.TRUNCATED_HASH_HTML_STRUCTURE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.CLOTH: {
        ObjectRelation.BOTTOM_ACCESSORIES: AttributeType.TEXT,
        ObjectRelation.CLOTH_COLOR: AttributeType.TEXT,
        ObjectRelation.CLOTH_PICTURE: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.HEAD_ACCESSORIES: AttributeType.TEXT,
        ObjectRelation.TOP_ACCESSORIES: AttributeType.TEXT,
    },
    ObjectType.COIN_ADDRESS: {
        ObjectRelation.ADDRESS: AttributeType.BTC,
        ObjectRelation.ADDRESS_CRYPTO: AttributeType.TEXT,
        ObjectRelation.ADDRESS_XMR: AttributeType.XMR,
        ObjectRelation.CURRENT_BALANCE: AttributeType.FLOAT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_UPDATED: AttributeType.DATETIME,
        ObjectRelation.SYMBOL: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TOTAL_RECEIVED: AttributeType.FLOAT,
        ObjectRelation.TOTAL_SENT: AttributeType.FLOAT,
        ObjectRelation.TOTAL_TRANSACTIONS: AttributeType.TEXT,
    },
    ObjectType.COMMAND: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.TRIGGER: AttributeType.TEXT,
    },
    ObjectType.COMMAND_LINE: {
        ObjectRelation.COMMAND_LINE_1: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.SOFTWARE_1: AttributeType.TEXT,
    },
    ObjectType.CONCORDIA_MTMF_INTRUSION_SET: {
        ObjectRelation.ATTACKNAME: AttributeType.TEXT,
        ObjectRelation.CMTMF_ATCKID: AttributeType.INTEGER,
        ObjectRelation.FEEDBACKLOOP: AttributeType.INTEGER,
        ObjectRelation.PHNAME: AttributeType.TEXT,
        ObjectRelation.PHSEQUENCE: AttributeType.INTEGER,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
    },
    ObjectType.CONFIDENTIALITY_IMPACT: {
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.INFORMATION_TYPE: AttributeType.TEXT,
        ObjectRelation.LOSS_TYPE: AttributeType.TEXT,
        ObjectRelation.RECORD_COUNT: AttributeType.COUNTER,
        ObjectRelation.RECORD_SIZE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
    },
    ObjectType.COOKIE: {
        ObjectRelation.COOKIE: AttributeType.COOKIE,
        ObjectRelation.COOKIE_NAME: AttributeType.TEXT,
        ObjectRelation.COOKIE_VALUE: AttributeType.TEXT,
        ObjectRelation.EXPIRES: AttributeType.DATETIME,
        ObjectRelation.HTTP_ONLY: AttributeType.BOOLEAN,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.SECURE: AttributeType.BOOLEAN,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.CORTEX: {
        ObjectRelation.FULL: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SERVER_NAME: AttributeType.TEXT,
        ObjectRelation.START_DATE: AttributeType.DATETIME,
        ObjectRelation.SUCCESS: AttributeType.BOOLEAN,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.CORTEX_TAXONOMY: {
        ObjectRelation.CORTEX_URL: AttributeType.LINK,
        ObjectRelation.LEVEL: AttributeType.TEXT,
        ObjectRelation.NAMESPACE: AttributeType.TEXT,
        ObjectRelation.PREDICATE: AttributeType.TEXT,
        ObjectRelation.VALUE: AttributeType.TEXT,
    },
    ObjectType.COURSE_OF_ACTION: {
        ObjectRelation.COST: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EFFICACY: AttributeType.TEXT,
        ObjectRelation.IMPACT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.STAGE: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.COVID19_CSSE_DAILY_REPORT: {
        ObjectRelation.ACTIVE: AttributeType.COUNTER,
        ObjectRelation.CONFIRMED: AttributeType.COUNTER,
        ObjectRelation.COUNTRY_REGION: AttributeType.TEXT,
        ObjectRelation.COUNTY: AttributeType.INTEGER,
        ObjectRelation.DEATH: AttributeType.COUNTER,
        ObjectRelation.FIPS: AttributeType.INTEGER,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.PROVINCE_STATE: AttributeType.TEXT,
        ObjectRelation.RECOVERED: AttributeType.COUNTER,
        ObjectRelation.UPDATE: AttributeType.DATETIME,
    },
    ObjectType.COVID19_DXY_LIVE_CITY: {
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.CURRENT_CONFIRMED: AttributeType.COUNTER,
        ObjectRelation.TOTAL_CONFIRMED: AttributeType.COUNTER,
        ObjectRelation.TOTAL_CURED: AttributeType.COUNTER,
        ObjectRelation.TOTAL_DEATH: AttributeType.COUNTER,
        ObjectRelation.UPDATE: AttributeType.DATETIME,
    },
    ObjectType.COVID19_DXY_LIVE_PROVINCE: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.CURRENT_CONFIRMED: AttributeType.COUNTER,
        ObjectRelation.PROVINCE: AttributeType.TEXT,
        ObjectRelation.TOTAL_CONFIRMED: AttributeType.COUNTER,
        ObjectRelation.TOTAL_CURED: AttributeType.COUNTER,
        ObjectRelation.TOTAL_DEATH: AttributeType.COUNTER,
        ObjectRelation.UPDATE: AttributeType.DATETIME,
    },
    ObjectType.COWRIE: {
        ObjectRelation.COMPCS: AttributeType.TEXT,
        ObjectRelation.DST_IP_1: AttributeType.IP_DST,
        ObjectRelation.DST_PORT_1: AttributeType.PORT,
        ObjectRelation.ENCCS: AttributeType.TEXT,
        ObjectRelation.EVENTID_1: AttributeType.TEXT,
        ObjectRelation.HASSH: AttributeType.HASSH_MD5,
        ObjectRelation.INPUT: AttributeType.TEXT,
        ObjectRelation.ISERROR: AttributeType.TEXT,
        ObjectRelation.KEYALGS: AttributeType.TEXT,
        ObjectRelation.MACCS: AttributeType.TEXT,
        ObjectRelation.MESSAGE: AttributeType.TEXT,
        ObjectRelation.PASSWORD: AttributeType.TEXT,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SENSOR: AttributeType.TEXT,
        ObjectRelation.SESSION: AttributeType.TEXT,
        ObjectRelation.SRC_IP: AttributeType.IP_SRC,
        ObjectRelation.SRC_PORT_1: AttributeType.PORT,
        ObjectRelation.SYSTEM: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.DATETIME,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.CPE_ASSET: {
        ObjectRelation.CPE: AttributeType.CPE,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EDITION: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.OTHER: AttributeType.TEXT,
        ObjectRelation.PART: AttributeType.TEXT,
        ObjectRelation.PRODUCT: AttributeType.TEXT,
        ObjectRelation.SW_EDITION: AttributeType.TEXT,
        ObjectRelation.TARGET_HW: AttributeType.TEXT,
        ObjectRelation.TARGET_SW: AttributeType.TEXT,
        ObjectRelation.UPDATE: AttributeType.TEXT,
        ObjectRelation.VENDOR: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.CREDENTIAL: {
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.NOTIFICATION: AttributeType.TEXT,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.PASSWORD: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.CREDIT_CARD: {
        ObjectRelation.BANK_NAME: AttributeType.TEXT,
        ObjectRelation.CARD_SECURITY_CODE: AttributeType.TEXT,
        ObjectRelation.CC_NUMBER: AttributeType.CC_NUMBER,
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.EXPIRATION: AttributeType.DATETIME,
        ObjectRelation.IIN: AttributeType.TEXT,
        ObjectRelation.ISSUED: AttributeType.DATETIME,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.CROWDSEC_IP_CONTEXT: {
        ObjectRelation.AS_NAME: AttributeType.TEXT,
        ObjectRelation.AS_NUM: AttributeType.AS,
        ObjectRelation.ATTACK_DETAILS: AttributeType.TEXT,
        ObjectRelation.BACKGROUND_NOISE: AttributeType.FLOAT,
        ObjectRelation.BEHAVIORS: AttributeType.TEXT,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATIONS: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.COUNTRY_CODE: AttributeType.TEXT,
        ObjectRelation.CVES: AttributeType.TEXT,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FALSE_POSITIVES: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.IP_RANGE: AttributeType.IP_SRC,
        ObjectRelation.IP_RANGE_SCORE: AttributeType.FLOAT,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.MITRE_TECHNIQUES: AttributeType.TEXT,
        ObjectRelation.REPUTATION: AttributeType.TEXT,
        ObjectRelation.REVERSE_DNS: AttributeType.HOSTNAME,
        ObjectRelation.SCORES: AttributeType.TEXT,
        ObjectRelation.TARGET_COUNTRIES: AttributeType.TEXT,
        ObjectRelation.TRUST: AttributeType.FLOAT,
    },
    ObjectType.CROWDSTRIKE_REPORT: {
        ObjectRelation.COMMAND: AttributeType.TEXT,
        ObjectRelation.FILE_HASH: AttributeType.SHA256,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.FULLPATH: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.PARENT_COMMAND: AttributeType.TEXT,
        ObjectRelation.PROCESS_NAME: AttributeType.TEXT,
    },
    ObjectType.CRYPTO_MATERIAL: {
        ObjectRelation.GX: AttributeType.TEXT,
        ObjectRelation.GY: AttributeType.TEXT,
        ObjectRelation.B: AttributeType.TEXT,
        ObjectRelation.CURVE_LENGTH: AttributeType.TEXT,
        ObjectRelation.E: AttributeType.TEXT,
        ObjectRelation.ECDSA_TYPE: AttributeType.TEXT,
        ObjectRelation.G: AttributeType.TEXT,
        ObjectRelation.GENERIC_SYMMETRIC_KEY: AttributeType.TEXT,
        ObjectRelation.MODULUS: AttributeType.TEXT,
        ObjectRelation.N: AttributeType.TEXT,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.P: AttributeType.TEXT,
        ObjectRelation.PRIVATE: AttributeType.TEXT,
        ObjectRelation.PUBLIC: AttributeType.TEXT,
        ObjectRelation.Q: AttributeType.TEXT,
        ObjectRelation.RSA_MODULUS_SIZE: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.X: AttributeType.TEXT,
        ObjectRelation.Y: AttributeType.TEXT,
    },
    ObjectType.CRYPTOCURRENCY_TRANSACTION: {
        ObjectRelation.ADDRESS: AttributeType.BTC,
        ObjectRelation.SYMBOL: AttributeType.TEXT,
        ObjectRelation.TIME: AttributeType.DATETIME,
        ObjectRelation.TRANSACTION_NUMBER: AttributeType.TEXT,
        ObjectRelation.VALUE: AttributeType.FLOAT,
        ObjectRelation.VALUE_EUR: AttributeType.FLOAT,
        ObjectRelation.VALUE_USD: AttributeType.FLOAT,
    },
    ObjectType.CS_BEACON_CONFIG: {
        ObjectRelation.ARCHITECTURE: AttributeType.TEXT,
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.BEACON_HOST: AttributeType.IP_DST,
        ObjectRelation.BEACON_TYPE: AttributeType.TEXT,
        ObjectRelation.BINARY_MD5: AttributeType.MD5,
        ObjectRelation.BINARY_SHA1: AttributeType.SHA1,
        ObjectRelation.BINARY_SHA256: AttributeType.SHA256,
        ObjectRelation.C2: AttributeType.URL,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.CONFIG_MD5: AttributeType.MD5,
        ObjectRelation.CONFIG_SHA1: AttributeType.SHA1,
        ObjectRelation.CONFIG_SHA256: AttributeType.SHA256,
        ObjectRelation.CONTENT_LENGTH: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.CONTENT_TYPE: AttributeType.TEXT,
        ObjectRelation.ENCODED_DATA: AttributeType.ATTACHMENT,
        ObjectRelation.ENCODED_LENGTH: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.HTTP: AttributeType.TEXT,
        ObjectRelation.HTTP_CODE: AttributeType.INTEGER,
        ObjectRelation.HTTP_URL: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.JAR_MD5: AttributeType.MD5,
        ObjectRelation.LICENSE_ID: AttributeType.TEXT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.NAICS: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.VT_SHA256: AttributeType.SHA256,
        ObjectRelation.WATERMARK: AttributeType.TEXT,
    },
    ObjectType.CTF_CHALLENGE: {
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CATEGORY_1: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FLAG: AttributeType.TEXT,
        ObjectRelation.HINTS: AttributeType.TEXT,
        ObjectRelation.MAX_ATTEMPTS: AttributeType.COUNTER,
        ObjectRelation.POINTS: AttributeType.FLOAT,
        ObjectRelation.SOLVES: AttributeType.COUNTER,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.CYTOMIC_ORION_FILE: {
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATIONNAME: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.FILENAME,
        ObjectRelation.FILESIZE_1: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
    },
    ObjectType.CYTOMIC_ORION_MACHINE: {
        ObjectRelation.CLIENTCREATIONDATEUTC: AttributeType.DATETIME,
        ObjectRelation.CLIENTID: AttributeType.TEXT,
        ObjectRelation.CLIENTNAME: AttributeType.TARGET_ORG,
        ObjectRelation.CREATIONDATE: AttributeType.DATETIME,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LASTSEENUTC: AttributeType.DATETIME,
        ObjectRelation.MACHINEMUID: AttributeType.TEXT,
        ObjectRelation.MACHINENAME: AttributeType.TARGET_MACHINE,
        ObjectRelation.MACHINEPATH: AttributeType.TEXT,
    },
    ObjectType.DARK_PATTERN_ITEM: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.GAIN: AttributeType.TEXT,
        ObjectRelation.IMPLEMENTER: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.TIME: AttributeType.DATETIME,
        ObjectRelation.USER_1: AttributeType.TEXT,
    },
    ObjectType.DDOS: {
        ObjectRelation.BACKSCATTER_THRESHOLD: AttributeType.INTEGER,
        ObjectRelation.CAPTURE_ORIGIN: AttributeType.TEXT,
        ObjectRelation.DOMAIN_DST: AttributeType.DOMAIN,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SRC_PORT: AttributeType.PORT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TOTAL_BPS: AttributeType.INTEGER,
        ObjectRelation.TOTAL_BYTES_SENT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.TOTAL_PACKETS_SENT: AttributeType.COUNTER,
        ObjectRelation.TOTAL_PPS: AttributeType.INTEGER,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.DDOS_CLAIM: {
        ObjectRelation.CLAIM_VALIDITY: AttributeType.TEXT,
        ObjectRelation.PROOF: AttributeType.TEXT,
        ObjectRelation.PROOF_SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.TARGET: AttributeType.TEXT,
    },
    ObjectType.DDOS_CONFIG: {
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.DDOS_TOOL: AttributeType.TEXT,
        ObjectRelation.HEADERS: AttributeType.TEXT,
        ObjectRelation.HOST: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.METHOD: AttributeType.TEXT,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.REQUEST_ID: AttributeType.TEXT,
        ObjectRelation.TARGET_ID: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.USE_SSL: AttributeType.TEXT,
    },
    ObjectType.DEVICE: {
        ObjectRelation.MAC_ADDRESS: AttributeType.MAC_ADDRESS,
        ObjectRelation.OS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.ANALYSIS_DATE: AttributeType.DATETIME,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DEVICE_TYPE: AttributeType.TEXT,
        ObjectRelation.DNS_NAME: AttributeType.TEXT,
        ObjectRelation.HITS: AttributeType.COUNTER,
        ObjectRelation.INFECTION_TYPE: AttributeType.TEXT,
        ObjectRelation.IP_ADDRESS: AttributeType.IP_SRC,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.DIAMETER_ATTACK: {
        ObjectRelation.APPLICATIONID: AttributeType.TEXT,
        ObjectRelation.CMDCODE: AttributeType.TEXT,
        ObjectRelation.DESTINATION_HOST: AttributeType.TEXT,
        ObjectRelation.DESTINATION_REALM: AttributeType.TEXT,
        ObjectRelation.IDRFLAGS: AttributeType.TEXT,
        ObjectRelation.ORIGIN_HOST: AttributeType.TEXT,
        ObjectRelation.ORIGIN_HOST_COUNTRYISO2: AttributeType.TEXT,
        ObjectRelation.ORIGIN_HOST_OPERATORNAME: AttributeType.TEXT,
        ObjectRelation.ORIGIN_HOST_TADIG: AttributeType.TEXT,
        ObjectRelation.ORIGIN_REALM: AttributeType.TEXT,
        ObjectRelation.ORIGIN_REALM_COUNTRYISO2: AttributeType.TEXT,
        ObjectRelation.ORIGIN_REALM_OPERATORNAME: AttributeType.TEXT,
        ObjectRelation.ORIGIN_REALM_TADIG: AttributeType.TEXT,
        ObjectRelation.SESSIONID: AttributeType.TEXT,
        ObjectRelation.USERNAME: AttributeType.TEXT,
        ObjectRelation.CATEGORY_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.DIAMOND: {
        ObjectRelation.ADVESARY: AttributeType.TEXT,
        ObjectRelation.CAPABILITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION: AttributeType.TEXT,
        ObjectRelation.DIRECTION: AttributeType.TEXT,
        ObjectRelation.EVENTID: AttributeType.INTEGER,
        ObjectRelation.INFRASTRUCTURE: AttributeType.TEXT,
        ObjectRelation.METHODOLOGY: AttributeType.TEXT,
        ObjectRelation.PHASE: AttributeType.TEXT,
        ObjectRelation.RESOURCES: AttributeType.TEXT,
        ObjectRelation.RESULT: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP: AttributeType.DATETIME,
        ObjectRelation.VICTIM: AttributeType.TEXT,
        ObjectRelation.IOC: AttributeType.TEXT,
        ObjectRelation.TEXTFIELD: AttributeType.TEXT,
    },
    ObjectType.DIRECTORY: {
        ObjectRelation.ACCESS_TIME: AttributeType.DATETIME,
        ObjectRelation.CREATION_TIME: AttributeType.DATETIME,
        ObjectRelation.MODIFICATION_TIME: AttributeType.DATETIME,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.PATH_ENCODING: AttributeType.TEXT,
    },
    ObjectType.DKIM: {
        ObjectRelation.D: AttributeType.DOMAIN,
        ObjectRelation.DKIM: AttributeType.DKIM,
        ObjectRelation.H: AttributeType.TEXT,
        ObjectRelation.K: AttributeType.TEXT,
        ObjectRelation.N: AttributeType.TEXT,
        ObjectRelation.PUBLIC_KEY: AttributeType.TEXT,
        ObjectRelation.S: AttributeType.TEXT,
        ObjectRelation.T: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.DNS_RECORD: {
        ObjectRelation.A_RECORD: AttributeType.IP_DST,
        ObjectRelation.AAAA_RECORD: AttributeType.IP_DST,
        ObjectRelation.CNAME_RECORD: AttributeType.DOMAIN,
        ObjectRelation.MX_RECORD: AttributeType.DOMAIN,
        ObjectRelation.NS_RECORD: AttributeType.DOMAIN,
        ObjectRelation.PTR_RECORD: AttributeType.DOMAIN,
        ObjectRelation.QUERIED_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.SOA_RECORD: AttributeType.DOMAIN,
        ObjectRelation.SPF_RECORD: AttributeType.IP_DST,
        ObjectRelation.SRV_RECORD: AttributeType.DOMAIN,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TXT_RECORD: AttributeType.TEXT,
    },
    ObjectType.DOM_HASH: {
        ObjectRelation.DOM_HASH: AttributeType.DOM_HASH,
        ObjectRelation.REF: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.DOMAIN_CRAWLED: {
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.DOMAIN_IP: {
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.REGISTRATION_DATE: AttributeType.DATETIME,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.EDR_REPORT: {
        ObjectRelation.ADDITIONAL_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.COMMAND: AttributeType.ATTACHMENT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DRIVERS: AttributeType.ATTACHMENT,
        ObjectRelation.ENDPOINT_ID: AttributeType.TEXT,
        ObjectRelation.EVENT: AttributeType.ATTACHMENT,
        ObjectRelation.EXECUTABLE: AttributeType.ATTACHMENT,
        ObjectRelation.HOSTNAME: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.MODULES: AttributeType.ATTACHMENT,
        ObjectRelation.PROCESSES: AttributeType.ATTACHMENT,
        ObjectRelation.PRODUCT: AttributeType.TEXT,
    },
    ObjectType.ELF: {
        ObjectRelation.ARCH: AttributeType.TEXT,
        ObjectRelation.ENTRYPOINT_ADDRESS: AttributeType.TEXT,
        ObjectRelation.NUMBER_SECTIONS: AttributeType.COUNTER,
        ObjectRelation.OS_ABI: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.ELF_SECTION: {
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.FLAG: AttributeType.TEXT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SHA512_224: AttributeType.SHA512_224,
        ObjectRelation.SHA512_256: AttributeType.SHA512_256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.EMAIL: {
        ObjectRelation.ATTACHMENT: AttributeType.EMAIL_ATTACHMENT,
        ObjectRelation.BCC: AttributeType.EMAIL_DST,
        ObjectRelation.BCC_DISPLAY_NAME: AttributeType.EMAIL_DST_DISPLAY_NAME,
        ObjectRelation.CC: AttributeType.EMAIL_DST,
        ObjectRelation.CC_DISPLAY_NAME: AttributeType.EMAIL_DST_DISPLAY_NAME,
        ObjectRelation.EMAIL_BODY: AttributeType.EMAIL_BODY,
        ObjectRelation.EMAIL_BODY_ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.EML: AttributeType.ATTACHMENT,
        ObjectRelation.FROM: AttributeType.EMAIL_SRC,
        ObjectRelation.FROM_DISPLAY_NAME: AttributeType.EMAIL_SRC_DISPLAY_NAME,
        ObjectRelation.FROM_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.HEADER: AttributeType.EMAIL_HEADER,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.MESSAGE_ID: AttributeType.EMAIL_MESSAGE_ID,
        ObjectRelation.MIME_BOUNDARY: AttributeType.EMAIL_MIME_BOUNDARY,
        ObjectRelation.MSG: AttributeType.ATTACHMENT,
        ObjectRelation.RECEIVED_HEADER_HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.RECEIVED_HEADER_IP: AttributeType.IP_SRC,
        ObjectRelation.REPLY_TO: AttributeType.EMAIL_REPLY_TO,
        ObjectRelation.REPLY_TO_DISPLAY_NAME: AttributeType.EMAIL_DST_DISPLAY_NAME,
        ObjectRelation.RETURN_PATH: AttributeType.EMAIL_SRC,
        ObjectRelation.SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.SEND_DATE: AttributeType.DATETIME,
        ObjectRelation.SUBJECT: AttributeType.EMAIL_SUBJECT,
        ObjectRelation.THREAD_INDEX: AttributeType.EMAIL_THREAD_INDEX,
        ObjectRelation.TO: AttributeType.EMAIL_DST,
        ObjectRelation.TO_DISPLAY_NAME: AttributeType.EMAIL_DST_DISPLAY_NAME,
        ObjectRelation.USER_AGENT: AttributeType.TEXT,
        ObjectRelation.X_MAILER: AttributeType.EMAIL_X_MAILER,
    },
    ObjectType.EMPLOYEE: {
        ObjectRelation.BUSINESS_UNIT: AttributeType.TARGET_ORG,
        ObjectRelation.EMAIL_ADDRESS_1: AttributeType.TARGET_EMAIL,
        ObjectRelation.EMPLOYEE_TYPE: AttributeType.TEXT,
        ObjectRelation.FIRST_NAME: AttributeType.FIRST_NAME,
        ObjectRelation.FULL_NAME: AttributeType.FULL_NAME,
        ObjectRelation.LAST_NAME: AttributeType.LAST_NAME,
        ObjectRelation.PRIMARY_ASSET: AttributeType.TARGET_MACHINE,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.USERID: AttributeType.TARGET_USER,
    },
    ObjectType.ERROR_MESSAGE: {ObjectRelation.MESSAGE: AttributeType.TEXT, ObjectRelation.SOURCE_1: AttributeType.TEXT},
    ObjectType.EVENT: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.EVENT_TYPE_1: AttributeType.TEXT,
        ObjectRelation.GOAL: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
    },
    ObjectType.EXPLOIT: {
        ObjectRelation._0DAY_TODAY_ID: AttributeType.TEXT,
        ObjectRelation.ACCESSIBILITY: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.CREDIT: AttributeType.TEXT,
        ObjectRelation.CVE_ID: AttributeType.VULNERABILITY,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EXPLOIT: AttributeType.TEXT,
        ObjectRelation.EXPLOIT_AS_ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.EXPLOITDB_ID: AttributeType.TEXT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.LEVEL: AttributeType.TEXT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.SOFTWARE_1: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.EXPLOIT_POC: {
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.POC: AttributeType.ATTACHMENT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.VULNERABLE_CONFIGURATION_1: AttributeType.TEXT,
    },
    ObjectType.EXTERNAL_IMPACT: {
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.IMPACT_TYPE: AttributeType.TEXT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
    },
    ObjectType.FACEBOOK_ACCOUNT: {
        ObjectRelation.ACCOUNT_ID: AttributeType.TEXT,
        ObjectRelation.ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_AVATAR: AttributeType.ATTACHMENT,
    },
    ObjectType.FACEBOOK_GROUP: {
        ObjectRelation.ADMINISTRATOR: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.GROUP_ALIAS: AttributeType.TEXT,
        ObjectRelation.GROUP_NAME: AttributeType.TEXT,
        ObjectRelation.GROUP_TYPE: AttributeType.TEXT,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PRIVACY: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.FACEBOOK_PAGE: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CONTACT_DETAIL: AttributeType.URL,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.EVENT: AttributeType.TEXT,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PAGE_ALIAS: AttributeType.TEXT,
        ObjectRelation.PAGE_ID: AttributeType.TEXT,
        ObjectRelation.PAGE_NAME: AttributeType.TEXT,
        ObjectRelation.PAGE_TYPE: AttributeType.TEXT,
        ObjectRelation.RELATED_PAGE_ID: AttributeType.TEXT,
        ObjectRelation.RELATED_PAGE_NAME: AttributeType.TEXT,
        ObjectRelation.TEAM_MEMBER: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.FACEBOOK_POST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_STATUS_ID: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_USER_ID: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.POST: AttributeType.TEXT,
        ObjectRelation.POST_ID: AttributeType.TEXT,
        ObjectRelation.POST_LOCATION: AttributeType.TEXT,
        ObjectRelation.REMOVAL_DATE: AttributeType.DATETIME,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_ID: AttributeType.TEXT,
        ObjectRelation.USER_NAME: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.FACEBOOK_REACTION: {
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.FACIAL_COMPOSITE: {
        ObjectRelation.FACIAL_COMPOSITE: AttributeType.ATTACHMENT,
        ObjectRelation.TECHNIQUE: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.FAIL2BAN: {
        ObjectRelation.ATTACK_TYPE: AttributeType.TEXT,
        ObjectRelation.BANNED_IP: AttributeType.IP_SRC,
        ObjectRelation.FAILURES: AttributeType.COUNTER,
        ObjectRelation.LOGFILE: AttributeType.ATTACHMENT,
        ObjectRelation.LOGLINE: AttributeType.TEXT,
        ObjectRelation.PROCESSING_TIMESTAMP: AttributeType.DATETIME,
        ObjectRelation.SENSOR: AttributeType.TEXT,
        ObjectRelation.VICTIM_1: AttributeType.TEXT,
    },
    ObjectType.FAVICON: {
        ObjectRelation.FAVICON: AttributeType.ATTACHMENT,
        ObjectRelation.FAVICON_MMH3: AttributeType.FAVICON_MMH3,
        ObjectRelation.LINK: AttributeType.LINK,
    },
    ObjectType.FILE: {
        ObjectRelation.ACCESS_TIME: AttributeType.DATETIME,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.AUTHENTIHASH: AttributeType.AUTHENTIHASH,
        ObjectRelation.CERTIFICATE: AttributeType.X509_FINGERPRINT_SHA1,
        ObjectRelation.COMPILATION_TIMESTAMP: AttributeType.DATETIME,
        ObjectRelation.CREATION_TIME: AttributeType.DATETIME,
        ObjectRelation.DOM_HASH: AttributeType.DOM_HASH,
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.FILE_ENCODING: AttributeType.TEXT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.FULLPATH: AttributeType.TEXT,
        ObjectRelation.IMPHASH: AttributeType.IMPHASH,
        ObjectRelation.MALWARE_SAMPLE: AttributeType.MALWARE_SAMPLE,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.MIMETYPE_1: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFICATION_TIME: AttributeType.DATETIME,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.PATTERN_IN_FILE: AttributeType.PATTERN_IN_FILE,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA3_224: AttributeType.SHA3_224,
        ObjectRelation.SHA3_256: AttributeType.SHA3_256,
        ObjectRelation.SHA3_384: AttributeType.SHA3_384,
        ObjectRelation.SHA3_512: AttributeType.SHA3_512,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SHA512_224: AttributeType.SHA512_224,
        ObjectRelation.SHA512_256: AttributeType.SHA512_256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.TELFHASH: AttributeType.TELFHASH,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TLSH_1: AttributeType.TLSH,
        ObjectRelation.VHASH: AttributeType.VHASH,
    },
    ObjectType.FLOWINTEL_CM_CASE: {
        ObjectRelation.CASE_OWNER_ORG_NAME: AttributeType.TEXT,
        ObjectRelation.CASE_OWNER_ORG_UUID: AttributeType.TEXT,
        ObjectRelation.CASE_UUID: AttributeType.TEXT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.DEADLINE: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FINISH_DATE: AttributeType.DATETIME,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.ORIGIN_URL: AttributeType.URL,
        ObjectRelation.RECURRING_TYPE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.FLOWINTEL_CM_TASK: {
        ObjectRelation.CASE_UUID: AttributeType.TEXT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.DEADLINE: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FILE: AttributeType.ATTACHMENT,
        ObjectRelation.FINISH_DATE: AttributeType.DATETIME,
        ObjectRelation.ORIGIN_URL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.TASK_UUID: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.FLOWINTEL_CM_TASK_NOTE: {
        ObjectRelation.NOTE: AttributeType.TEXT,
        ObjectRelation.NOTE_UUID: AttributeType.TEXT,
        ObjectRelation.ORIGIN_URL: AttributeType.URL,
        ObjectRelation.TASK_UUID: AttributeType.TEXT,
    },
    ObjectType.FORENSIC_CASE: {
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.ANALYSIS_START_DATE: AttributeType.DATETIME,
        ObjectRelation.CASE_NAME: AttributeType.TEXT,
        ObjectRelation.CASE_NUMBER: AttributeType.TEXT,
        ObjectRelation.NAME_OF_THE_ANALYST: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
    },
    ObjectType.FORENSIC_EVIDENCE: {
        ObjectRelation.ACQUISITION_METHOD: AttributeType.TEXT,
        ObjectRelation.ACQUISITION_TOOLS: AttributeType.TEXT,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.CASE_NUMBER: AttributeType.TEXT,
        ObjectRelation.EVIDENCE_NUMBER: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.FORGED_DOCUMENT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DOCUMENT_NAME: AttributeType.TEXT,
        ObjectRelation.DOCUMENT_TEXT: AttributeType.TEXT,
        ObjectRelation.DOCUMENT_TYPE: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.PURPOSE_OF_DOCUMENT: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.FTM_AIRPLANE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.BUILDDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ICAOCODE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MANUFACTURER: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONDATE: AttributeType.TEXT,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SERIALNUMBER: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_ASSESSMENT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.ASSESSMENTID: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHDATE: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_ASSET: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_ASSOCIATE: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RELATIONSHIP: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_AUDIO: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.DURATION: AttributeType.FLOAT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SAMPLINGRATE: AttributeType.FLOAT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_BANKACCOUNT: {
        ObjectRelation.ACCOUNTNUMBER: AttributeType.TEXT,
        ObjectRelation.ACCOUNTTYPE: AttributeType.TEXT,
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.BALANCE: AttributeType.FLOAT,
        ObjectRelation.BANKADDRESS: AttributeType.TEXT,
        ObjectRelation.BANKNAME: AttributeType.TEXT,
        ObjectRelation.BIC: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.IBAN: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_CALL: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.CALLERNUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DURATION: AttributeType.FLOAT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECEIVERNUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_COMPANY: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.BIKCODE: AttributeType.TEXT,
        ObjectRelation.BVDID: AttributeType.TEXT,
        ObjectRelation.CAEMCODE: AttributeType.TEXT,
        ObjectRelation.CAPITAL: AttributeType.TEXT,
        ObjectRelation.CIKCODE: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COATOCODE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISSOLUTIONDATE: AttributeType.TEXT,
        ObjectRelation.DUNSCODE: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.FNSCODE: AttributeType.TEXT,
        ObjectRelation.FSSCODE: AttributeType.TEXT,
        ObjectRelation.IBCRUC: AttributeType.TEXT,
        ObjectRelation.ICIJID: AttributeType.TEXT,
        ObjectRelation.IDNUMBER: AttributeType.TEXT,
        ObjectRelation.INCORPORATIONDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.INNCODE: AttributeType.TEXT,
        ObjectRelation.IPOCODE: AttributeType.TEXT,
        ObjectRelation.IRSCODE: AttributeType.TEXT,
        ObjectRelation.JIBCODE: AttributeType.TEXT,
        ObjectRelation.JURISDICTION: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.KPPCODE: AttributeType.TEXT,
        ObjectRelation.LEGALFORM: AttributeType.TEXT,
        ObjectRelation.MAINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.MBSCODE: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.OGRNCODE: AttributeType.TEXT,
        ObjectRelation.OKOPFCODE: AttributeType.TEXT,
        ObjectRelation.OKPOCODE: AttributeType.TEXT,
        ObjectRelation.OKSMCODE: AttributeType.TEXT,
        ObjectRelation.OKVEDCODE: AttributeType.TEXT,
        ObjectRelation.OPENCORPORATESURL: AttributeType.URL,
        ObjectRelation.PFRNUMBER: AttributeType.TEXT,
        ObjectRelation.PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SWIFTBIC: AttributeType.TEXT,
        ObjectRelation.TAXNUMBER: AttributeType.TEXT,
        ObjectRelation.TAXSTATUS: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.VATCODE: AttributeType.TEXT,
        ObjectRelation.VOENCODE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.URL,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_CONTRACT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.CANCELLED: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.CONTRACTDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRITERIA: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.METHOD: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.NOTICEID: AttributeType.TEXT,
        ObjectRelation.NUMBERAWARDS: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCEDURE: AttributeType.TEXT,
        ObjectRelation.PROCEDURENUMBER: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_CONTRACTAWARD: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.AMENDED: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.CPVCODE: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DECISIONREASON: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DOCUMENTNUMBER: AttributeType.TEXT,
        ObjectRelation.DOCUMENTTYPE: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.LOTNUMBER: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NUTSCODE: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_COURTCASE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.CASENUMBER: AttributeType.TEXT,
        ObjectRelation.CATEGORY_1: AttributeType.TEXT,
        ObjectRelation.CLOSEDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.COURT: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FILEDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_COURTCASEPARTY: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_DEBT: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_DIRECTORSHIP: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SECRETARY: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_DOCUMENT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_DOCUMENTATION: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_ECONOMICACTIVITY: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.CCDNUMBER: AttributeType.TEXT,
        ObjectRelation.CCDVALUE: AttributeType.TEXT,
        ObjectRelation.CUSTOMSAMOUNT: AttributeType.TEXT,
        ObjectRelation.CUSTOMSPROCEDURE: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DEPARTURECOUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DESTINATIONCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DIRECTIONOFTRANSPORTATION: AttributeType.TEXT,
        ObjectRelation.DOLLAREXCHRATE: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.GOODSDESCRIPTION: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INVOICEAMOUNT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.ORIGINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TRADINGCOUNTRY: AttributeType.TEXT,
        ObjectRelation.VEDCODE: AttributeType.TEXT,
        ObjectRelation.VEDCODEDESCRIPTION: AttributeType.TEXT,
    },
    ObjectType.FTM_EMAIL: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.BCC: AttributeType.TEXT,
        ObjectRelation.BODYHTML: AttributeType.TEXT,
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.CC: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.FROM: AttributeType.TEXT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.HEADERS: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INREPLYTO: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SENDER: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.THREADTOPIC: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TO: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_EVENT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.IMPORTANT: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_FAMILY: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RELATIONSHIP: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_FOLDER: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_HYPERTEXT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.BODYHTML: AttributeType.TEXT,
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_IMAGE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_LAND: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.AREA: AttributeType.FLOAT,
        ObjectRelation.CADASTRALCODE: AttributeType.TEXT,
        ObjectRelation.CENSUSBLOCK: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CREATEDATE: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENCUMBRANCE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANDTYPE: AttributeType.TEXT,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PROPERTYTYPE: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TENURE: AttributeType.TEXT,
        ObjectRelation.TITLENUMBER: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_LEGALENTITY: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BVDID: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISSOLUTIONDATE: AttributeType.TEXT,
        ObjectRelation.DUNSCODE: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.ICIJID: AttributeType.TEXT,
        ObjectRelation.IDNUMBER: AttributeType.TEXT,
        ObjectRelation.INCORPORATIONDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.INNCODE: AttributeType.TEXT,
        ObjectRelation.JURISDICTION: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LEGALFORM: AttributeType.TEXT,
        ObjectRelation.MAINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.OKPOCODE: AttributeType.TEXT,
        ObjectRelation.OPENCORPORATESURL: AttributeType.URL,
        ObjectRelation.PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SWIFTBIC: AttributeType.TEXT,
        ObjectRelation.TAXNUMBER: AttributeType.TEXT,
        ObjectRelation.TAXSTATUS: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.VATCODE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.URL,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_LICENSE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.AREA: AttributeType.TEXT,
        ObjectRelation.CANCELLED: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COMMODITIES: AttributeType.TEXT,
        ObjectRelation.CONTRACTDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRITERIA: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.METHOD: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.NOTICEID: AttributeType.TEXT,
        ObjectRelation.NUMBERAWARDS: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCEDURE: AttributeType.TEXT,
        ObjectRelation.PROCEDURENUMBER: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.REVIEWDATE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_MEMBERSHIP: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_MESSAGE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.BODYHTML: AttributeType.TEXT,
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INREPLYTO: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.METADATA: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.THREADTOPIC: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_ORGANIZATION: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BVDID: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISSOLUTIONDATE: AttributeType.TEXT,
        ObjectRelation.DUNSCODE: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.ICIJID: AttributeType.TEXT,
        ObjectRelation.IDNUMBER: AttributeType.TEXT,
        ObjectRelation.INCORPORATIONDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.INNCODE: AttributeType.TEXT,
        ObjectRelation.JURISDICTION: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LEGALFORM: AttributeType.TEXT,
        ObjectRelation.MAINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.OKPOCODE: AttributeType.TEXT,
        ObjectRelation.OPENCORPORATESURL: AttributeType.URL,
        ObjectRelation.PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SWIFTBIC: AttributeType.TEXT,
        ObjectRelation.TAXNUMBER: AttributeType.TEXT,
        ObjectRelation.TAXSTATUS: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.VATCODE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.URL,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_OWNERSHIP: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.LEGALBASIS: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.OWNERSHIPTYPE: AttributeType.TEXT,
        ObjectRelation.PERCENTAGE: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SHARESCOUNT: AttributeType.TEXT,
        ObjectRelation.SHARESCURRENCY: AttributeType.TEXT,
        ObjectRelation.SHARESTYPE: AttributeType.TEXT,
        ObjectRelation.SHARESVALUE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_PACKAGE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_PAGE: {
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.INDEX: AttributeType.FLOAT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
    },
    ObjectType.FTM_PAGES: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PDFHASH: AttributeType.SHA1,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_PASSPORT: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.AUTHORITY: AttributeType.TEXT,
        ObjectRelation.BIRTHDATE: AttributeType.TEXT,
        ObjectRelation.BIRTHPLACE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.GENDER: AttributeType.TEXT,
        ObjectRelation.GIVENNAME: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PASSPORTNUMBER: AttributeType.TEXT,
        ObjectRelation.PERSONALNUMBER: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SURNAME: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.FTM_PAYMENT: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PROGRAMME: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.PURPOSE: AttributeType.TEXT,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SEQUENCENUMBER: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TRANSACTIONNUMBER: AttributeType.TEXT,
    },
    ObjectType.FTM_PERSON: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BIRTHDATE: AttributeType.TEXT,
        ObjectRelation.BIRTHPLACE: AttributeType.TEXT,
        ObjectRelation.BVDID: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DEATHDATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISSOLUTIONDATE: AttributeType.TEXT,
        ObjectRelation.DUNSCODE: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.FATHERNAME: AttributeType.TEXT,
        ObjectRelation.FIRSTNAME: AttributeType.TEXT,
        ObjectRelation.GENDER: AttributeType.TEXT,
        ObjectRelation.ICIJID: AttributeType.TEXT,
        ObjectRelation.IDNUMBER: AttributeType.TEXT,
        ObjectRelation.INCORPORATIONDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.INNCODE: AttributeType.TEXT,
        ObjectRelation.JURISDICTION: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LASTNAME: AttributeType.TEXT,
        ObjectRelation.LEGALFORM: AttributeType.TEXT,
        ObjectRelation.MAINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.MIDDLENAME: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.MOTHERNAME: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NATIONALITY: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.OKPOCODE: AttributeType.TEXT,
        ObjectRelation.OPENCORPORATESURL: AttributeType.URL,
        ObjectRelation.PASSPORTNUMBER: AttributeType.TEXT,
        ObjectRelation.PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.POSITION: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SECONDNAME: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SWIFTBIC: AttributeType.TEXT,
        ObjectRelation.TAXNUMBER: AttributeType.TEXT,
        ObjectRelation.TAXSTATUS: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.VATCODE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.URL,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_PLAINTEXT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.BODYTEXT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_PUBLICBODY: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BVDID: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISSOLUTIONDATE: AttributeType.TEXT,
        ObjectRelation.DUNSCODE: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.ICIJID: AttributeType.TEXT,
        ObjectRelation.IDNUMBER: AttributeType.TEXT,
        ObjectRelation.INCORPORATIONDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.INNCODE: AttributeType.TEXT,
        ObjectRelation.JURISDICTION: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LEGALFORM: AttributeType.TEXT,
        ObjectRelation.MAINCOUNTRY: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.OKPOCODE: AttributeType.TEXT,
        ObjectRelation.OPENCORPORATESURL: AttributeType.URL,
        ObjectRelation.PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SWIFTBIC: AttributeType.TEXT,
        ObjectRelation.TAXNUMBER: AttributeType.TEXT,
        ObjectRelation.TAXSTATUS: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.VATCODE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.URL,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_REALESTATE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.AREA: AttributeType.FLOAT,
        ObjectRelation.CADASTRALCODE: AttributeType.TEXT,
        ObjectRelation.CENSUSBLOCK: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CREATEDATE: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENCUMBRANCE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANDTYPE: AttributeType.TEXT,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PROPERTYTYPE: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TENURE: AttributeType.TEXT,
        ObjectRelation.TITLENUMBER: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_REPRESENTATION: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_ROW: {
        ObjectRelation.CELLS: AttributeType.TEXT,
        ObjectRelation.INDEX: AttributeType.FLOAT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
    },
    ObjectType.FTM_SANCTION: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.AUTHORITY: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DURATION: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REASON: AttributeType.TEXT,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_SUCCESSION: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_TABLE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COLUMNS: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.CSVHASH: AttributeType.SHA1,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROWCOUNT: AttributeType.FLOAT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_TAXROLL: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.BIRTHDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.GIVENNAME: AttributeType.TEXT,
        ObjectRelation.INCOME: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.SURNAME: AttributeType.TEXT,
        ObjectRelation.TAXPAID: AttributeType.TEXT,
        ObjectRelation.WEALTH: AttributeType.TEXT,
    },
    ObjectType.FTM_UNKNOWNLINK: {
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENDDATE: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RECORDID: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.STARTDATE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
    },
    ObjectType.FTM_USERACCOUNT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.PASSWORD: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SERVICE: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_VEHICLE: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.BUILDDATE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONDATE: AttributeType.TEXT,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_VESSEL: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AMOUNT: AttributeType.FLOAT,
        ObjectRelation.AMOUNTEUR: AttributeType.FLOAT,
        ObjectRelation.AMOUNTUSD: AttributeType.FLOAT,
        ObjectRelation.BUILDDATE: AttributeType.TEXT,
        ObjectRelation.CALLSIGN: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRSNUMBER: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FLAG: AttributeType.TEXT,
        ObjectRelation.GROSSREGISTEREDTONNAGE: AttributeType.FLOAT,
        ObjectRelation.IMONUMBER: AttributeType.TEXT,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.MMSI_1: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMECHANGEDATE: AttributeType.TEXT,
        ObjectRelation.NAVIGATIONAREA: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PASTFLAGS: AttributeType.TEXT,
        ObjectRelation.PASTNAMES: AttributeType.TEXT,
        ObjectRelation.PASTTYPES: AttributeType.TEXT,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.REGISTRATIONDATE: AttributeType.TEXT,
        ObjectRelation.REGISTRATIONNUMBER: AttributeType.TEXT,
        ObjectRelation.REGISTRATIONPORT: AttributeType.TEXT,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TONNAGE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_VIDEO: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.DURATION: AttributeType.FLOAT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.FTM_WORKBOOK: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALEPHURL: AttributeType.URL,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOREDAT: AttributeType.TEXT,
        ObjectRelation.COMPANIESMENTIONED: AttributeType.TEXT,
        ObjectRelation.CONTENTHASH: AttributeType.SHA1,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CRAWLER: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTEDCOUNTRY: AttributeType.TEXT,
        ObjectRelation.DETECTEDLANGUAGE: AttributeType.TEXT,
        ObjectRelation.EMAILMENTIONED: AttributeType.EMAIL_SRC,
        ObjectRelation.ENCODING: AttributeType.TEXT,
        ObjectRelation.EXTENSION: AttributeType.TEXT,
        ObjectRelation.FILENAME_1: AttributeType.TEXT,
        ObjectRelation.FILESIZE_1: AttributeType.FLOAT,
        ObjectRelation.GENERATOR: AttributeType.TEXT,
        ObjectRelation.IBANMENTIONED: AttributeType.IBAN,
        ObjectRelation.INDEXTEXT: AttributeType.TEXT,
        ObjectRelation.INDEXUPDATEDAT: AttributeType.TEXT,
        ObjectRelation.IPMENTIONED: AttributeType.IP_SRC,
        ObjectRelation.KEYWORDS_1: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LOCATIONMENTIONED: AttributeType.TEXT,
        ObjectRelation.MESSAGEID: AttributeType.TEXT,
        ObjectRelation.MIMETYPE: AttributeType.MIME_TYPE,
        ObjectRelation.MODIFIEDAT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NAMESMENTIONED: AttributeType.TEXT,
        ObjectRelation.NOTES: AttributeType.TEXT,
        ObjectRelation.PEOPLEMENTIONED: AttributeType.TEXT,
        ObjectRelation.PHONEMENTIONED: AttributeType.PHONE_NUMBER,
        ObjectRelation.PREVIOUSNAME: AttributeType.TEXT,
        ObjectRelation.PROCESSINGERROR: AttributeType.TEXT,
        ObjectRelation.PROCESSINGSTATUS: AttributeType.TEXT,
        ObjectRelation.PROGRAM: AttributeType.TEXT,
        ObjectRelation.PUBLISHEDAT: AttributeType.TEXT,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.PUBLISHERURL: AttributeType.URL,
        ObjectRelation.RETRIEVEDAT: AttributeType.TEXT,
        ObjectRelation.SOURCEURL: AttributeType.URL,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TOPICS: AttributeType.TEXT,
        ObjectRelation.WEAKALIAS: AttributeType.TEXT,
        ObjectRelation.WIKIDATAID: AttributeType.TEXT,
        ObjectRelation.WIKIPEDIAURL: AttributeType.URL,
    },
    ObjectType.GAME_CHEAT: {
        ObjectRelation.AFFECTED_GAME: AttributeType.TEXT,
        ObjectRelation.CHEAT_NAME: AttributeType.TEXT,
        ObjectRelation.CHEAT_SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.CHEAT_TYPE: AttributeType.TEXT,
        ObjectRelation.CHEAT_VERSION: AttributeType.TEXT,
        ObjectRelation.COMPILATION_DATE: AttributeType.DATETIME,
        ObjectRelation.CREATOR: AttributeType.THREAT_ACTOR,
        ObjectRelation.IG_CHEAT_BEHAVIOUR: AttributeType.COMMENT,
        ObjectRelation.IMPLEMENTATION: AttributeType.TEXT,
        ObjectRelation.IMPLEMENTATION_DETAILS: AttributeType.TEXT,
        ObjectRelation.OPERATING_SYSTEM: AttributeType.TEXT,
        ObjectRelation.PRICING: AttributeType.TEXT,
        ObjectRelation.WEBPAGE: AttributeType.URL,
    },
    ObjectType.GENERALIZING_PERSUASION_FRAMEWORK: {
        ObjectRelation.ACTORS_RECEIVER: AttributeType.TEXT,
        ObjectRelation.ACTORS_SPEAKER_MOTIVATION: AttributeType.TEXT,
        ObjectRelation.ACTORS_SPEAKER_TYPE: AttributeType.TEXT,
        ObjectRelation.OUTCOMES_ATTITUDE: AttributeType.TEXT,
        ObjectRelation.OUTCOMES_BEHAVIOR: AttributeType.TEXT,
        ObjectRelation.OUTCOMES_EMOTION: AttributeType.TEXT,
        ObjectRelation.OUTCOMES_IDENTITY: AttributeType.TEXT,
        ObjectRelation.SETTINGS_COMPETITION_OBSERVERS: AttributeType.FLOAT,
        ObjectRelation.SETTINGS_COMPETITION_RECEIVERS: AttributeType.FLOAT,
        ObjectRelation.SETTINGS_COMPETITION_SPEAKERS: AttributeType.FLOAT,
        ObjectRelation.SETTINGS_CULTURE: AttributeType.TEXT,
        ObjectRelation.SETTINGS_PROCESS: AttributeType.TEXT,
        ObjectRelation.SETTINGS_SPACE: AttributeType.TEXT,
        ObjectRelation.SETTINGS_TIME: AttributeType.TEXT,
        ObjectRelation.TREATMENTS_MEDIUM: AttributeType.TEXT,
        ObjectRelation.TREATMENTS_MESSAGE_CONTENT: AttributeType.TEXT,
        ObjectRelation.TREATMENTS_TOPIC: AttributeType.TEXT,
    },
    ObjectType.GEOLOCATION: {
        ObjectRelation.ACCURACY_RADIUS: AttributeType.FLOAT,
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALTITUDE: AttributeType.FLOAT,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.COUNTRYCODE: AttributeType.TEXT,
        ObjectRelation.EPSG: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.NEIGHBORHOOD: AttributeType.TEXT,
        ObjectRelation.REGION: AttributeType.TEXT,
        ObjectRelation.SPACIAL_REFERENCE: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.ZIPCODE: AttributeType.TEXT,
    },
    ObjectType.GIT_VULN_FINDER: {
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.AUTHOR_EMAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.AUTHORED_DATE: AttributeType.DATETIME,
        ObjectRelation.BRANCHES: AttributeType.TEXT,
        ObjectRelation.COMMIT_ID: AttributeType.GIT_COMMIT_ID,
        ObjectRelation.COMMITTED_DATE: AttributeType.DATETIME,
        ObjectRelation.CVE_1: AttributeType.VULNERABILITY,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.MESSAGE: AttributeType.TEXT,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.ORIGIN_GITHUB_API: AttributeType.URL,
        ObjectRelation.PATTERN_MATCHES: AttributeType.TEXT,
        ObjectRelation.PATTERN_SELECTED: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.STATS_DELETIONS: AttributeType.COUNTER,
        ObjectRelation.STATS_FILES: AttributeType.COUNTER,
        ObjectRelation.STATS_INSERTIONS: AttributeType.COUNTER,
        ObjectRelation.STATS_LINES: AttributeType.COUNTER,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TAGS: AttributeType.TEXT,
    },
    ObjectType.GITHUB_USER: {
        ObjectRelation.AVATAR_URL: AttributeType.LINK,
        ObjectRelation.BIO: AttributeType.TEXT,
        ObjectRelation.BLOG: AttributeType.TEXT,
        ObjectRelation.COMPANY: AttributeType.TEXT,
        ObjectRelation.FOLLOWER: AttributeType.GITHUB_USERNAME,
        ObjectRelation.FOLLOWING: AttributeType.GITHUB_USERNAME,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.NODE_ID: AttributeType.TEXT,
        ObjectRelation.ORGANISATION: AttributeType.GITHUB_ORGANISATION,
        ObjectRelation.PROFILE_IMAGE: AttributeType.ATTACHMENT,
        ObjectRelation.PUBLIC_GISTS: AttributeType.TEXT,
        ObjectRelation.PUBLIC_REPOS: AttributeType.TEXT,
        ObjectRelation.REPOSITORY: AttributeType.GITHUB_REPOSITORY,
        ObjectRelation.SSH_PUBLIC_KEY: AttributeType.TEXT,
        ObjectRelation.TWITTER_USERNAME: AttributeType.TEXT,
        ObjectRelation.USER_FULLNAME: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.GITHUB_USERNAME,
        ObjectRelation.VERIFIED: AttributeType.TEXT,
    },
    ObjectType.GITLAB_USER: {
        ObjectRelation.AVATAR_URL: AttributeType.LINK,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.WEB_URL: AttributeType.LINK,
    },
    ObjectType.GOOGLE_SAFE_BROWSING: {
        ObjectRelation.MALICIOUS: AttributeType.BOOLEAN,
        ObjectRelation.PLATFORMS: AttributeType.TEXT,
        ObjectRelation.THREATS: AttributeType.TEXT,
    },
    ObjectType.GOOGLE_THREAT_INTELLIGENCE_REPORT: {
        ObjectRelation.DETECTION_RATIO: AttributeType.TEXT,
        ObjectRelation.FIRST_SUBMISSION: AttributeType.DATETIME,
        ObjectRelation.LAST_SUBMISSION: AttributeType.DATETIME,
        ObjectRelation.PERMALINK: AttributeType.LINK,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.THREAT_SCORE: AttributeType.INTEGER,
        ObjectRelation.VERDICT: AttributeType.TEXT,
    },
    ObjectType.GREYNOISE_IP: {
        ObjectRelation.ACTOR: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.NOISE: AttributeType.TEXT,
        ObjectRelation.PROVIDER: AttributeType.TEXT,
        ObjectRelation.RIOT: AttributeType.TEXT,
        ObjectRelation.TRUST_LEVEL: AttributeType.TEXT,
    },
    ObjectType.GTP_ATTACK: {
        ObjectRelation.GTPIMEI: AttributeType.TEXT,
        ObjectRelation.GTPIMSI: AttributeType.TEXT,
        ObjectRelation.GTPINTERFACE: AttributeType.TEXT,
        ObjectRelation.GTPMESSAGETYPE: AttributeType.TEXT,
        ObjectRelation.GTPMSISDN: AttributeType.TEXT,
        ObjectRelation.GTPSERVINGNETWORK: AttributeType.TEXT,
        ObjectRelation.GTPVERSION: AttributeType.TEXT,
        ObjectRelation.PORTDEST: AttributeType.TEXT,
        ObjectRelation.PORTSRC: AttributeType.PORT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IPDEST: AttributeType.IP_DST,
        ObjectRelation.IPSRC: AttributeType.IP_SRC,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.HASHLOOKUP: {
        ObjectRelation.FILENAME: AttributeType.FILENAME,
        ObjectRelation.FILESIZE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.KNOWNMALICIOUS: AttributeType.TEXT,
        ObjectRelation.MD5: AttributeType.MD5,
        ObjectRelation.PACKAGEARCH: AttributeType.TEXT,
        ObjectRelation.PACKAGEDESCRIPTION: AttributeType.TEXT,
        ObjectRelation.PACKAGEMAINTAINER: AttributeType.TEXT,
        ObjectRelation.PACKAGENAME: AttributeType.TEXT,
        ObjectRelation.PACKAGERELEASE: AttributeType.TEXT,
        ObjectRelation.PACKAGEVERSION: AttributeType.TEXT,
        ObjectRelation.SHA_1: AttributeType.SHA1,
        ObjectRelation.SHA_256: AttributeType.SHA256,
        ObjectRelation.SSDEEP: AttributeType.SSDEEP,
        ObjectRelation.TLSH: AttributeType.TLSH,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
    },
    ObjectType.HHHASH: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.HHHASH: AttributeType.TEXT,
        ObjectRelation.HHHASH_HEADERS: AttributeType.TEXT,
        ObjectRelation.HHHASH_QUERY_HEADERS: AttributeType.TEXT,
        ObjectRelation.HHHASH_TOOL: AttributeType.TEXT,
    },
    ObjectType.HTTP_REQUEST: {
        ObjectRelation.BASICAUTH_PASSWORD: AttributeType.TEXT,
        ObjectRelation.BASICAUTH_USER: AttributeType.TEXT,
        ObjectRelation.CONTENT_TYPE: AttributeType.OTHER,
        ObjectRelation.COOKIE: AttributeType.TEXT,
        ObjectRelation.HEADER: AttributeType.TEXT,
        ObjectRelation.HOST: AttributeType.HOSTNAME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.METHOD: AttributeType.HTTP_METHOD,
        ObjectRelation.PROXY_PASSWORD: AttributeType.TEXT,
        ObjectRelation.PROXY_USER: AttributeType.TEXT,
        ObjectRelation.REFERER: AttributeType.OTHER,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.URI: AttributeType.URI,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_AGENT: AttributeType.USER_AGENT,
    },
    ObjectType.IDENTITY: {
        ObjectRelation.CONTACT_INFORMATION: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.IDENTITY_CLASS: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.ROLES: AttributeType.TEXT,
        ObjectRelation.SECTORS: AttributeType.TEXT,
    },
    ObjectType.ILR_IMPACT: {
        ObjectRelation.DUREE: AttributeType.TEXT,
        ObjectRelation.NOMBRE_UTILISATEURS_TOUCHES: AttributeType.TEXT,
        ObjectRelation.POURCENTAGE_UTILISATEURS_TOUCHES: AttributeType.TEXT,
        ObjectRelation.SERVICE: AttributeType.TEXT,
    },
    ObjectType.ILR_NOTIFICATION_INCIDENT: {
        ObjectRelation.ACTIONS_CORRECTIVE: AttributeType.TEXT,
        ObjectRelation.ACTIONS_POSTERIEUR: AttributeType.TEXT,
        ObjectRelation.AUTRES_INFORMATIONS: AttributeType.TEXT,
        ObjectRelation.CAUSE_INITIALE_INCIDENT: AttributeType.TEXT,
        ObjectRelation.DATE_INCIDENT: AttributeType.DATETIME,
        ObjectRelation.DATE_PRE_NOTIFICATION: AttributeType.TEXT,
        ObjectRelation.DELIMITATION_GEOGRAPHIQUE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_INCIDENT: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_PROBLEME_SERVICES_URGENCE: AttributeType.TEXT,
        ObjectRelation.DETAILS_SERVICE: AttributeType.TEXT,
        ObjectRelation.EMAIL_CONTACT_INCIDENT: AttributeType.TEXT,
        ObjectRelation.IMPACT_SERVICESW_URGENCE: AttributeType.TEXT,
        ObjectRelation.INTERCONNECTIONS_AFFECTEES: AttributeType.TEXT,
        ObjectRelation.NOM_CONTACT_INCIDENT: AttributeType.TEXT,
        ObjectRelation.NOM_ENTREPRISE: AttributeType.TEXT,
        ObjectRelation.REMARQUES: AttributeType.TEXT,
        ObjectRelation.TELEPHONE_CONTACT_INCIDENT: AttributeType.TEXT,
        ObjectRelation.TRAITEMENT_INCIDENT: AttributeType.TEXT,
        ObjectRelation.ZONE_IMPACTEE: AttributeType.TEXT,
    },
    ObjectType.IMAGE: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.IMAGE_TEXT: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.IMPERSONATION: {
        ObjectRelation.ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.ACCOUNT_URL: AttributeType.URL,
        ObjectRelation.IMPERSONATED_ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.IMPERSONATED_ACCOUNT_URL: AttributeType.LINK,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.REAL_NAME: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.TYPE_OF_ACCOUNT: AttributeType.TEXT,
    },
    ObjectType.IMSI_CATCHER: {
        ObjectRelation.BRAND: AttributeType.TEXT,
        ObjectRelation.CELLID: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IMSI: AttributeType.TEXT,
        ObjectRelation.LAC: AttributeType.TEXT,
        ObjectRelation.MCC: AttributeType.TEXT,
        ObjectRelation.MNC: AttributeType.TEXT,
        ObjectRelation.OPERATOR: AttributeType.TEXT,
        ObjectRelation.SEQ: AttributeType.INTEGER,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TMSI_1: AttributeType.TEXT,
        ObjectRelation.TMSI_2: AttributeType.TEXT,
    },
    ObjectType.INCIDENT: {
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DETECTION_METHOD: AttributeType.TEXT,
        ObjectRelation.DETERMINATION: AttributeType.TEXT,
        ObjectRelation.INCIDENT_TYPE: AttributeType.TEXT,
        ObjectRelation.INVESTIGATION_STATUS: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.SCORE: AttributeType.TEXT,
    },
    ObjectType.INFRASTRUCTURE: {
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.INFRASTRUCTURE_TYPE: AttributeType.TEXT,
        ObjectRelation.KILL_CHAIN_PHASES: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
    },
    ObjectType.INSTANT_MESSAGE: {
        ObjectRelation.APP_USED: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.FROM_NAME: AttributeType.TEXT,
        ObjectRelation.FROM_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.FROM_USER: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.RECEIVED_DATE: AttributeType.DATETIME,
        ObjectRelation.SENT_DATE: AttributeType.DATETIME,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
        ObjectRelation.TO_NAME: AttributeType.TEXT,
        ObjectRelation.TO_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.TO_USER: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.INSTANT_MESSAGE_GROUP: {
        ObjectRelation.APP_USED: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.GROUP_ALIAS: AttributeType.TEXT,
        ObjectRelation.GROUP_NAME: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PERSON_NAME: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.INTEGRITY_IMPACT: {
        ObjectRelation.ALTERATION: AttributeType.TEXT,
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.INFORMATION_TYPE: AttributeType.TEXT,
        ObjectRelation.RECORD_COUNT: AttributeType.COUNTER,
        ObjectRelation.RECORD_SIZE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
    },
    ObjectType.INTEL471_VULNERABILITY_INTELLIGENCE: {
        ObjectRelation.ACTIVITY_LOCATION_OPEN_SOURCE: AttributeType.BOOLEAN,
        ObjectRelation.ACTIVITY_LOCATION_PRIVATE: AttributeType.BOOLEAN,
        ObjectRelation.ACTIVITY_LOCATION_UNDERGROUND: AttributeType.BOOLEAN,
        ObjectRelation.COUNTERMEASURES: AttributeType.TEXT,
        ObjectRelation.CVE_ID: AttributeType.TEXT,
        ObjectRelation.CVSS_SCORE_V2: AttributeType.FLOAT,
        ObjectRelation.CVSS_SCORE_V3: AttributeType.FLOAT,
        ObjectRelation.DETECTION: AttributeType.TEXT,
        ObjectRelation.EXPLOIT_STATUS_AVAILABLE: AttributeType.BOOLEAN,
        ObjectRelation.EXPLOIT_STATUS_NOT_OBSERVED: AttributeType.BOOLEAN,
        ObjectRelation.EXPLOIT_STATUS_PRODUCTIZED: AttributeType.BOOLEAN,
        ObjectRelation.EXPLOIT_STATUS_WEAPONIZED: AttributeType.BOOLEAN,
        ObjectRelation.INTEREST_LEVEL_DISCLOSED_PUBLICLY: AttributeType.BOOLEAN,
        ObjectRelation.INTEREST_LEVEL_EXPLOIT_SOUGHT: AttributeType.BOOLEAN,
        ObjectRelation.INTEREST_LEVEL_RESEARCHED_PUBLICLY: AttributeType.BOOLEAN,
        ObjectRelation.MODIFIED: AttributeType.DATETIME,
        ObjectRelation.PATCH_STATUS: AttributeType.TEXT,
        ObjectRelation.PRODUCT_NAME: AttributeType.TEXT,
        ObjectRelation.PROOF_OF_CONCEPT: AttributeType.TEXT,
        ObjectRelation.PUBLISHED: AttributeType.DATETIME,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.RISK_LEVEL: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.UNDERGROUND_ACTIVITY_STATUS: AttributeType.TEXT,
        ObjectRelation.UNDERGROUND_ACTIVITY_SUMMARY: AttributeType.TEXT,
        ObjectRelation.VENDOR_NAME: AttributeType.TEXT,
        ObjectRelation.VULNERABILITY_STATUS: AttributeType.TEXT,
        ObjectRelation.VULNERABILITY_TYPE: AttributeType.TEXT,
        ObjectRelation.VULNERABLE_CONFIGURATION: AttributeType.TEXT,
    },
    ObjectType.INTELMQ_EVENT: {
        ObjectRelation.CLASSIFICATION_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION_TAXONOMY: AttributeType.TEXT,
        ObjectRelation.CLASSIFICATION_TYPE: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DESTINATION_ABUSE_CONTACT: AttributeType.TEXT,
        ObjectRelation.DESTINATION_ACCOUNT: AttributeType.TEXT,
        ObjectRelation.DESTINATION_ALLOCATED: AttributeType.DATETIME,
        ObjectRelation.DESTINATION_AS_NAME: AttributeType.TEXT,
        ObjectRelation.DESTINATION_ASN: AttributeType.AS,
        ObjectRelation.DESTINATION_DOMAIN_SUFFIX: AttributeType.TEXT,
        ObjectRelation.DESTINATION_FQDN: AttributeType.DOMAIN,
        ObjectRelation.DESTINATION_GEOLOCATION_CC: AttributeType.TEXT,
        ObjectRelation.DESTINATION_GEOLOCATION_CITY: AttributeType.TEXT,
        ObjectRelation.DESTINATION_GEOLOCATION_COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESTINATION_GEOLOCATION_LATITUDE: AttributeType.FLOAT,
        ObjectRelation.DESTINATION_GEOLOCATION_LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.DESTINATION_GEOLOCATION_REGION: AttributeType.TEXT,
        ObjectRelation.DESTINATION_GEOLOCATION_STATE: AttributeType.TEXT,
        ObjectRelation.DESTINATION_IP: AttributeType.IP_DST,
        ObjectRelation.DESTINATION_LOCAL_HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.DESTINATION_LOCAL_IP: AttributeType.IP_DST,
        ObjectRelation.DESTINATION_NETWORK: AttributeType.IP_DST,
        ObjectRelation.DESTINATION_PORT: AttributeType.PORT,
        ObjectRelation.DESTINATION_REGISTRY: AttributeType.TEXT,
        ObjectRelation.DESTINATION_REVERSE_DNS: AttributeType.TEXT,
        ObjectRelation.DESTINATION_TOR_NODE: AttributeType.BOOLEAN,
        ObjectRelation.DESTINATION_URL: AttributeType.URL,
        ObjectRelation.DESTINATION_URLPATH: AttributeType.TEXT,
        ObjectRelation.EVENT_DESCRIPTION_TARGET: AttributeType.TEXT,
        ObjectRelation.EVENT_DESCRIPTION_TEXT: AttributeType.TEXT,
        ObjectRelation.EVENT_DESCRIPTION_URL: AttributeType.URL,
        ObjectRelation.EVENT_HASH: AttributeType.TEXT,
        ObjectRelation.EXTRA: AttributeType.TEXT,
        ObjectRelation.FEED_ACCURACY: AttributeType.FLOAT,
        ObjectRelation.FEED_CODE: AttributeType.TEXT,
        ObjectRelation.FEED_DOCUMENTATION: AttributeType.TEXT,
        ObjectRelation.FEED_NAME: AttributeType.TEXT,
        ObjectRelation.FEED_PROVIDER: AttributeType.TEXT,
        ObjectRelation.FEED_URL: AttributeType.URL,
        ObjectRelation.MALWARE_HASH_MD5: AttributeType.MD5,
        ObjectRelation.MALWARE_HASH_SHA1: AttributeType.SHA1,
        ObjectRelation.MALWARE_HASH_SHA256: AttributeType.SHA256,
        ObjectRelation.MALWARE_NAME: AttributeType.TEXT,
        ObjectRelation.MALWARE_VERSION: AttributeType.TEXT,
        ObjectRelation.MISP_ATTRIBUTE_UUID: AttributeType.TEXT,
        ObjectRelation.MISP_EVENT_UUID: AttributeType.TEXT,
        ObjectRelation.OUTPUT: AttributeType.TEXT,
        ObjectRelation.PROTOCOL_APPLICATION: AttributeType.TEXT,
        ObjectRelation.PROTOCOL_TRANSPORT: AttributeType.TEXT,
        ObjectRelation.RAW: AttributeType.TEXT,
        ObjectRelation.RTIR_ID: AttributeType.INTEGER,
        ObjectRelation.SCREENSHOT_URL: AttributeType.URL,
        ObjectRelation.SOURCE_ABUSE_CONTACT: AttributeType.TEXT,
        ObjectRelation.SOURCE_ACCOUNT: AttributeType.TEXT,
        ObjectRelation.SOURCE_ALLOCATED: AttributeType.DATETIME,
        ObjectRelation.SOURCE_AS_NAME: AttributeType.TEXT,
        ObjectRelation.SOURCE_ASN: AttributeType.AS,
        ObjectRelation.SOURCE_DOMAIN_SUFFIX: AttributeType.TEXT,
        ObjectRelation.SOURCE_FQDN: AttributeType.DOMAIN,
        ObjectRelation.SOURCE_GEOLOCATION_CC: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_CITY: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_COUNTRY: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_CYMRU_CC: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_GEOIP_CC: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_LATITUDE: AttributeType.FLOAT,
        ObjectRelation.SOURCE_GEOLOCATION_LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.SOURCE_GEOLOCATION_REGION: AttributeType.TEXT,
        ObjectRelation.SOURCE_GEOLOCATION_STATE: AttributeType.TEXT,
        ObjectRelation.SOURCE_IP_1: AttributeType.IP_SRC,
        ObjectRelation.SOURCE_LOCAL_HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.SOURCE_LOCAL_IP: AttributeType.IP_SRC,
        ObjectRelation.SOURCE_NETWORK: AttributeType.IP_SRC,
        ObjectRelation.SOURCE_PORT: AttributeType.PORT,
        ObjectRelation.SOURCE_REGISTRY: AttributeType.TEXT,
        ObjectRelation.SOURCE_REVERSE_DNS: AttributeType.TEXT,
        ObjectRelation.SOURCE_TOR_NODE: AttributeType.BOOLEAN,
        ObjectRelation.SOURCE_URL: AttributeType.URL,
        ObjectRelation.SOURCE_URLPATH: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.TIME_OBSERVATION: AttributeType.DATETIME,
        ObjectRelation.TIME_SOURCE: AttributeType.DATETIME,
        ObjectRelation.TLP: AttributeType.TEXT,
    },
    ObjectType.INTELMQ_REPORT: {
        ObjectRelation.EXTRA: AttributeType.TEXT,
        ObjectRelation.FEED_ACCURACY: AttributeType.FLOAT,
        ObjectRelation.FEED_CODE: AttributeType.TEXT,
        ObjectRelation.FEED_DOCUMENTATION: AttributeType.TEXT,
        ObjectRelation.FEED_NAME: AttributeType.TEXT,
        ObjectRelation.FEED_PROVIDER: AttributeType.TEXT,
        ObjectRelation.FEED_URL: AttributeType.URL,
        ObjectRelation.RAW: AttributeType.TEXT,
        ObjectRelation.RTIR_ID: AttributeType.INTEGER,
        ObjectRelation.TIME_OBSERVATION: AttributeType.DATETIME,
    },
    ObjectType.INTERNAL_REFERENCE: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.INTERPOL_NOTICE: {
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.CHARGES: AttributeType.TEXT,
        ObjectRelation.COLOUR_OF_EYES: AttributeType.TEXT,
        ObjectRelation.COLOUR_OF_HAIR: AttributeType.TEXT,
        ObjectRelation.DATE_OF_BIRTH: AttributeType.DATE_OF_BIRTH,
        ObjectRelation.DATE_OF_DISAPPEARANCE: AttributeType.TEXT,
        ObjectRelation.DISTINGUISHING_MARKS_AND_CHARACTERISTICS: AttributeType.TEXT,
        ObjectRelation.FATHER_S_FAMILY_NAME___FORENAME: AttributeType.TEXT,
        ObjectRelation.FORENAME: AttributeType.FIRST_NAME,
        ObjectRelation.HEIGHT: AttributeType.TEXT,
        ObjectRelation.LANGUAGE_SPOKEN: AttributeType.TEXT,
        ObjectRelation.MOTHER_S_FAMILY_NAME___FORENAME: AttributeType.TEXT,
        ObjectRelation.NATIONALITY: AttributeType.NATIONALITY,
        ObjectRelation.NOTICE_COLOR: AttributeType.TEXT,
        ObjectRelation.PLACE_OF_BIRTH: AttributeType.PLACE_OF_BIRTH,
        ObjectRelation.PLACE_OF_DISAPPEARANCE: AttributeType.TEXT,
        ObjectRelation.PORTRAIT: AttributeType.ATTACHMENT,
        ObjectRelation.PRESENT_FAMILY_NAME: AttributeType.LAST_NAME,
        ObjectRelation.SEX: AttributeType.GENDER,
        ObjectRelation.WEIGHT: AttributeType.TEXT,
    },
    ObjectType.INTRUSION_SET: {
        ObjectRelation.ALIASES: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.GOALS: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PRIMARY_MOTIVATION: AttributeType.TEXT,
        ObjectRelation.RESOURCE_LEVEL: AttributeType.TEXT,
        ObjectRelation.SECONDARY_MOTIVATION: AttributeType.TEXT,
    },
    ObjectType.IOT_DEVICE: {
        ObjectRelation.ARCHITECTURE: AttributeType.TEXT,
        ObjectRelation.BOOT_LOG: AttributeType.ATTACHMENT,
        ObjectRelation.FCC_ID: AttributeType.TEXT,
        ObjectRelation.JTAG_INTERFACE: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.PICTURE_DEVICE: AttributeType.ATTACHMENT,
        ObjectRelation.PICTURE_PCB: AttributeType.ATTACHMENT,
        ObjectRelation.PLATFORM: AttributeType.TEXT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.SERIAL_INTERFACE: AttributeType.TEXT,
        ObjectRelation.SPI_INTERFACE: AttributeType.TEXT,
        ObjectRelation.VENDOR: AttributeType.TEXT,
    },
    ObjectType.IOT_FIRMWARE: {
        ObjectRelation.BINWALK_ENTROPY_GRAPH: AttributeType.ATTACHMENT,
        ObjectRelation.BINWALK_OUTPUT: AttributeType.ATTACHMENT,
        ObjectRelation.BOOT_LOG: AttributeType.ATTACHMENT,
        ObjectRelation.FILENAME_2: AttributeType.TEXT,
        ObjectRelation.FIRMWARE: AttributeType.ATTACHMENT,
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.IP_API_ADDRESS: {
        ObjectRelation.ISP: AttributeType.TEXT,
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.COUNTRY_CODE: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LATITUDE: AttributeType.FLOAT,
        ObjectRelation.LONGITUDE: AttributeType.FLOAT,
        ObjectRelation.ORGANIZATION: AttributeType.TEXT,
        ObjectRelation.REGION: AttributeType.TEXT,
        ObjectRelation.REGION_CODE: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.ZIPCODE: AttributeType.TEXT,
    },
    ObjectType.IP_PORT: {
        ObjectRelation.AS: AttributeType.AS,
        ObjectRelation.COUNTRY_CODE: AttributeType.TEXT,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SRC_PORT: AttributeType.PORT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.IRC: {
        ObjectRelation.CHANNEL: AttributeType.TEXT,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.NICKNAME: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.JA3: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.JA3_FINGERPRINT_MD5: AttributeType.JA3_FINGERPRINT_MD5,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
    },
    ObjectType.JA3S: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.JA3_FINGERPRINT_MD5: AttributeType.JA3_FINGERPRINT_MD5,
        ObjectRelation.JA3S_FINGERPRINT_MD5: AttributeType.JA3_FINGERPRINT_MD5,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
    },
    ObjectType.JA4_PLUS: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.JA4_FINGERPRINT: AttributeType.TEXT,
        ObjectRelation.JA4_TYPE: AttributeType.TEXT,
    },
    ObjectType.JARM: {
        ObjectRelation.JARM: AttributeType.JARM_FINGERPRINT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.SCOPE: AttributeType.TEXT,
        ObjectRelation.TLS_IMPLEMENTATION: AttributeType.TEXT,
        ObjectRelation.TOOL: AttributeType.TEXT,
    },
    ObjectType.KEYBASE_ACCOUNT: {
        ObjectRelation.BIO: AttributeType.TEXT,
        ObjectRelation.CRYPTOCURRENCY_ADDRESSES: AttributeType.BTC,
        ObjectRelation.EMAILS: AttributeType.TEXT,
        ObjectRelation.FULL_NAME_1: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.PRIVATE_KEYS: AttributeType.TEXT,
        ObjectRelation.PUBLIC_KEYS: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.LANGUAGE_CONTENT: {
        ObjectRelation.CONTENT: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
    },
    ObjectType.LEAKED_DOCUMENT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DOCUMENT_NAME: AttributeType.TEXT,
        ObjectRelation.DOCUMENT_TEXT: AttributeType.TEXT,
        ObjectRelation.DOCUMENT_TYPE: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.PURPOSE_OF_DOCUMENT: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.LEGAL_ENTITY: {
        ObjectRelation.BUSINESS: AttributeType.TEXT,
        ObjectRelation.COMMERCIAL_NAME: AttributeType.TEXT,
        ObjectRelation.LEGAL_FORM: AttributeType.TEXT,
        ObjectRelation.LOGO: AttributeType.ATTACHMENT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.REGISTRATION_NUMBER: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.LINK,
    },
    ObjectType.LNK: {
        ObjectRelation.BIRTH_DROID_FILE_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.BIRTH_DROID_VOLUME_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.DROID_FILE_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.DROID_VOLUME_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.FULLPATH: AttributeType.TEXT,
        ObjectRelation.LNK_ACCESS_TIME: AttributeType.DATETIME,
        ObjectRelation.LNK_COMMAND_LINE_ARGUMENTS: AttributeType.TEXT,
        ObjectRelation.LNK_CREATION_TIME: AttributeType.DATETIME,
        ObjectRelation.LNK_DESCRIPTION: AttributeType.TEXT,
        ObjectRelation.LNK_DRIVE_SERIAL_NUMBER: AttributeType.TEXT,
        ObjectRelation.LNK_DRIVE_TYPE: AttributeType.TEXT,
        ObjectRelation.LNK_FILE_ATTRIBUTE_FLAGS: AttributeType.TEXT,
        ObjectRelation.LNK_FILE_SIZE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.LNK_HOT_KEY_VALUE: AttributeType.TEXT,
        ObjectRelation.LNK_ICON_INDEX: AttributeType.TEXT,
        ObjectRelation.LNK_LOCAL_PATH: AttributeType.TEXT,
        ObjectRelation.LNK_MODIFICATION_TIME: AttributeType.DATETIME,
        ObjectRelation.LNK_RELATIVE_PATH: AttributeType.TEXT,
        ObjectRelation.LNK_SHOW_WINDOW_VALUE: AttributeType.TEXT,
        ObjectRelation.LNK_VOLUME_LABEL: AttributeType.TEXT,
        ObjectRelation.LNK_WORKING_DIRECTORY: AttributeType.TEXT,
        ObjectRelation.MACHINE_IDENTIFIER: AttributeType.TEXT,
        ObjectRelation.MALWARE_SAMPLE: AttributeType.MALWARE_SAMPLE,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.PATTERN_IN_FILE: AttributeType.PATTERN_IN_FILE,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SHA512_224: AttributeType.SHA512_224,
        ObjectRelation.SHA512_256: AttributeType.SHA512_256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TLSH_1: AttributeType.TLSH,
    },
    ObjectType.MACHO: {
        ObjectRelation.ENTRYPOINT_ADDRESS: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.NUMBER_SECTIONS: AttributeType.COUNTER,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.MACHO_SECTION: {
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SHA512_224: AttributeType.SHA512_224,
        ObjectRelation.SHA512_256: AttributeType.SHA512_256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.MACTIME_TIMELINE_ANALYSIS: {
        ObjectRelation.ACTIVITYTYPE: AttributeType.TEXT,
        ObjectRelation.DATETIME: AttributeType.DATETIME,
        ObjectRelation.FILE: AttributeType.ATTACHMENT,
        ObjectRelation.FILE_PATH: AttributeType.TEXT,
        ObjectRelation.FILEPERMISSIONS: AttributeType.TEXT,
        ObjectRelation.FILE_SIZE: AttributeType.SIZE_IN_BYTES,
    },
    ObjectType.MALWARE: {
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.ARCHITECTURE_EXECUTION_ENV: AttributeType.TEXT,
        ObjectRelation.CAPABILITY_1: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.IMPLEMENTATION_LANGUAGE: AttributeType.TEXT,
        ObjectRelation.IS_FAMILY: AttributeType.BOOLEAN,
        ObjectRelation.LAST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.MALWARE_TYPE: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
    },
    ObjectType.MALWARE_ANALYSIS: {
        ObjectRelation.ANALYSIS_DEFINITION_VERSION: AttributeType.TEXT,
        ObjectRelation.ANALYSIS_ENGINE_VERSION: AttributeType.TEXT,
        ObjectRelation.CONFIGURATION_VERSION: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.MODULE: AttributeType.TEXT,
        ObjectRelation.PRODUCT: AttributeType.TEXT,
        ObjectRelation.RESULT_1: AttributeType.TEXT,
        ObjectRelation.RESULT_NAME: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.SUBMITTED_TIME: AttributeType.DATETIME,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.MALWARE_CONFIG: {
        ObjectRelation.CONFIG: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENCRYPTED: AttributeType.TEXT,
        ObjectRelation.FILE_CONFIG: AttributeType.ATTACHMENT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PASSWORD: AttributeType.TEXT,
    },
    ObjectType.MEME_IMAGE: {
        ObjectRelation._5DS_OF_PROPAGANDA: AttributeType.TEXT,
        ObjectRelation.A_B_TEST: AttributeType.BOOLEAN,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CROSSPOST: AttributeType.LINK,
        ObjectRelation.CROSSPOST_UNSAFE: AttributeType.URL,
        ObjectRelation.DOCUMENT_TEXT: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MEME_REFERENCE: AttributeType.LINK,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.MICROBLOG: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_STATUS_ID: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_USER_ID: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MODIFICATION_DATE: AttributeType.DATETIME,
        ObjectRelation.POST: AttributeType.TEXT,
        ObjectRelation.REMOVAL_DATE: AttributeType.DATETIME,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TWITTER_ID: AttributeType.TWITTER_ID,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
        ObjectRelation.VERIFIED_USERNAME: AttributeType.TEXT,
    },
    ObjectType.MONETARY_IMPACT: {
        ObjectRelation.CONVERSION_RATE: AttributeType.FLOAT,
        ObjectRelation.CONVERSION_TIME: AttributeType.DATETIME,
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.CURRENCY_ACTUAL: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.MAX_AMOUNT: AttributeType.FLOAT,
        ObjectRelation.MIN_AMOUNT: AttributeType.FLOAT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.VARIETY: AttributeType.TEXT,
    },
    ObjectType.MUTEX: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OPERATING_SYSTEM: AttributeType.TEXT,
    },
    ObjectType.NARRATIVE: {
        ObjectRelation._5DS_OF_PROPAGANDA: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.EXTERNAL_REFERENCES: AttributeType.LINK,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.NARRATIVE_DISPROOF: AttributeType.TEXT,
        ObjectRelation.NARRATIVE_SUMMARY: AttributeType.TEXT,
        ObjectRelation.OBJECTIVE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.NETFLOW: {
        ObjectRelation.BYTE_COUNT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.COMMUNITY_ID: AttributeType.COMMUNITY_ID,
        ObjectRelation.DIRECTION_1: AttributeType.TEXT,
        ObjectRelation.DST_AS: AttributeType.AS,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FIRST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.FLOW_COUNT: AttributeType.COUNTER,
        ObjectRelation.ICMP_TYPE: AttributeType.TEXT,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_PROTOCOL_NUMBER: AttributeType.INTEGER,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.IP_VERSION: AttributeType.INTEGER,
        ObjectRelation.LAST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.PACKET_COUNT: AttributeType.COUNTER,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SRC_AS: AttributeType.AS,
        ObjectRelation.SRC_PORT: AttributeType.PORT,
        ObjectRelation.TCP_FLAGS: AttributeType.TEXT,
    },
    ObjectType.NETWORK_CONNECTION: {
        ObjectRelation.COMMUNITY_ID: AttributeType.COMMUNITY_ID,
        ObjectRelation.COUNT: AttributeType.COUNTER,
        ObjectRelation.DST_BYTES_COUNT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.DST_PACKETS_COUNT: AttributeType.COUNTER,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FIRST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME_DST: AttributeType.HOSTNAME,
        ObjectRelation.HOSTNAME_SRC: AttributeType.HOSTNAME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAYER3_PROTOCOL: AttributeType.TEXT,
        ObjectRelation.LAYER4_PROTOCOL: AttributeType.TEXT,
        ObjectRelation.LAYER7_PROTOCOL: AttributeType.TEXT,
        ObjectRelation.MAC_DST: AttributeType.MAC_ADDRESS,
        ObjectRelation.MAC_SRC: AttributeType.MAC_ADDRESS,
        ObjectRelation.SRC_BYTES_COUNT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SRC_PACKETS_COUNT: AttributeType.COUNTER,
        ObjectRelation.SRC_PORT: AttributeType.PORT,
    },
    ObjectType.NETWORK_PROFILE: {
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.CERTIFICATE_COMMON_NAME: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_COUNTRY: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.CERTIFICATE_EXPIRY_DATE: AttributeType.DATETIME,
        ObjectRelation.CERTIFICATE_ISSUER: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_ORGANIZATION: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_ORGANIZATION_LOCALITY: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_ORGANIZATION_STATE: AttributeType.TEXT,
        ObjectRelation.CERTIFICATE_ORGANIZATION_UNIT: AttributeType.TEXT,
        ObjectRelation.DNS_SERVER: AttributeType.HOSTNAME,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.EVIDENCES: AttributeType.ATTACHMENT,
        ObjectRelation.GOOGLE_ANALYTICS_ID: AttributeType.TEXT,
        ObjectRelation.HOSTING_PROVIDER: AttributeType.TEXT,
        ObjectRelation.IP_ADDRESS: AttributeType.IP_SRC,
        ObjectRelation.JARM: AttributeType.JARM_FINGERPRINT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.QUERY_STRING: AttributeType.TEXT,
        ObjectRelation.RESOURCE_PATH: AttributeType.TEXT,
        ObjectRelation.SERVICE_ABUSE: AttributeType.TEXT,
        ObjectRelation.SUBDOMAIN: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.THREAT_ACTOR_INFRASTRUCTURE_PATTERN: AttributeType.TEXT,
        ObjectRelation.THREAT_ACTOR_INFRASTRUCTURE_VALUE: AttributeType.TEXT,
        ObjectRelation.TLD: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.WHOIS_CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.WHOIS_EXPIRATION_DATE: AttributeType.DATETIME,
        ObjectRelation.WHOIS_REGISTRANT_EMAIL: AttributeType.WHOIS_REGISTRANT_EMAIL,
        ObjectRelation.WHOIS_REGISTRANT_NAME: AttributeType.WHOIS_REGISTRANT_NAME,
        ObjectRelation.WHOIS_REGISTRANT_ORG: AttributeType.WHOIS_REGISTRANT_ORG,
        ObjectRelation.WHOIS_REGISTRANT_PHONE: AttributeType.WHOIS_REGISTRANT_PHONE,
        ObjectRelation.WHOIS_REGISTRAR: AttributeType.WHOIS_REGISTRAR,
    },
    ObjectType.NETWORK_SOCKET: {
        ObjectRelation.ADDRESS_FAMILY: AttributeType.TEXT,
        ObjectRelation.DOMAIN_FAMILY: AttributeType.TEXT,
        ObjectRelation.DST_BYTES_COUNT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.DST_PACKETS_COUNT: AttributeType.COUNTER,
        ObjectRelation.DST_PORT: AttributeType.PORT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.FIRST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME_DST: AttributeType.HOSTNAME,
        ObjectRelation.HOSTNAME_SRC: AttributeType.HOSTNAME,
        ObjectRelation.IP_DST: AttributeType.IP_DST,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.MAC_DST: AttributeType.MAC_ADDRESS,
        ObjectRelation.MAC_SRC: AttributeType.MAC_ADDRESS,
        ObjectRelation.OPTION: AttributeType.TEXT,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SOCKET_TYPE: AttributeType.TEXT,
        ObjectRelation.SRC_BYTES_COUNT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SRC_PACKETS_COUNT: AttributeType.COUNTER,
        ObjectRelation.SRC_PORT: AttributeType.PORT,
        ObjectRelation.STATE: AttributeType.TEXT,
    },
    ObjectType.NETWORK_TRAFFIC: {
        ObjectRelation.DST_BYTES_COUNT_1: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.DST_HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.DST_IP_1: AttributeType.IP_DST,
        ObjectRelation.DST_MAC: AttributeType.MAC_ADDRESS,
        ObjectRelation.DST_PACKETS: AttributeType.COUNTER,
        ObjectRelation.DST_PORT_1: AttributeType.PORT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.IS_ACTIVE: AttributeType.BOOLEAN,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.SRC_BYTES_COUNT_1: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SRC_HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.SRC_IP: AttributeType.IP_DST,
        ObjectRelation.SRC_MAC: AttributeType.MAC_ADDRESS,
        ObjectRelation.SRC_PACKETS: AttributeType.COUNTER,
        ObjectRelation.SRC_PORT_1: AttributeType.PORT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
    },
    ObjectType.NEWS_AGENCY: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.E_MAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.FAX_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.NEWS_MEDIA: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CONTENT: AttributeType.TEXT,
        ObjectRelation.E_MAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.FAX_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.SUB_TYPE: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TRANSCRIPTION: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.OPEN_DATA_SECURITY: {
        ObjectRelation.DESCRIPTION_1: AttributeType.COMMENT,
        ObjectRelation.FREQUENCY: AttributeType.TEXT,
        ObjectRelation.HUMAN_VALIDATED: AttributeType.TEXT,
        ObjectRelation.LICENSE: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MACHINE_VALIDATED: AttributeType.TEXT,
        ObjectRelation.PRODUCER: AttributeType.LINK,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.SUBTITLE: AttributeType.TEXT,
        ObjectRelation.TIME_PRECISION: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.OPENTIDE: {
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OPENTIDE_OBJECT: AttributeType.TEXT,
        ObjectRelation.OPENTIDE_RELATION: AttributeType.TEXT,
        ObjectRelation.OPENTIDE_TYPE: AttributeType.TEXT,
        ObjectRelation.UUID: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.ORGANIZATION: {
        ObjectRelation.VAT: AttributeType.TEXT,
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.CONTACT_INFORMATION: AttributeType.TEXT,
        ObjectRelation.DATE_OF_INCEPTION: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.E_MAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.FAX_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.MISP_UUID: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.REGISTRATION_NUMBER: AttributeType.TEXT,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.TYPE_OF_ORGANIZATION: AttributeType.TEXT,
    },
    ObjectType.ORIGINAL_IMPORTED_FILE: {
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.IMPORTED_SAMPLE: AttributeType.ATTACHMENT,
        ObjectRelation.URI: AttributeType.URI,
    },
    ObjectType.PALOALTO_THREAT_EVENT: {
        ObjectRelation.APP: AttributeType.TEXT,
        ObjectRelation.DIRECTION_1: AttributeType.TEXT,
        ObjectRelation.DPORT: AttributeType.PORT,
        ObjectRelation.DST: AttributeType.IP_DST,
        ObjectRelation.DSTLOC: AttributeType.TEXT,
        ObjectRelation.PROTO: AttributeType.TEXT,
        ObjectRelation.SPORT: AttributeType.PORT,
        ObjectRelation.SRC: AttributeType.IP_SRC,
        ObjectRelation.SRCLOC: AttributeType.TEXT,
        ObjectRelation.SUBTYPE: AttributeType.TEXT,
        ObjectRelation.THR_CATEGORY: AttributeType.TEXT,
        ObjectRelation.THREATID: AttributeType.TEXT,
        ObjectRelation.TIME_GENERATED: AttributeType.DATETIME,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.PARLER_ACCOUNT: {
        ObjectRelation.ACCOUNT_ID: AttributeType.TEXT,
        ObjectRelation.ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BADGE: AttributeType.FLOAT,
        ObjectRelation.BIO: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.COVER_PHOTO: AttributeType.ATTACHMENT,
        ObjectRelation.FOLLOWERS: AttributeType.TEXT,
        ObjectRelation.FOLLOWING: AttributeType.TEXT,
        ObjectRelation.HUMAN: AttributeType.BOOLEAN,
        ObjectRelation.INTERACTIONS: AttributeType.FLOAT,
        ObjectRelation.LIKES: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.POSTS: AttributeType.TEXT,
        ObjectRelation.PROFILE_PHOTO: AttributeType.ATTACHMENT,
        ObjectRelation.SCORE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.VERIFIED: AttributeType.BOOLEAN,
    },
    ObjectType.PARLER_COMMENT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BADGE: AttributeType.FLOAT,
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.COMMENT_DEPTH: AttributeType.FLOAT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.CONTROVERSY: AttributeType.FLOAT,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.CREATOR_ID: AttributeType.TEXT,
        ObjectRelation.DOWNVOTES: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_PARLEY_ID: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_USER_ID: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.POST_ID: AttributeType.TEXT,
        ObjectRelation.SCORE: AttributeType.TEXT,
        ObjectRelation.UPVOTES: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.PARLER_POST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ARTICLE: AttributeType.BOOLEAN,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BADGE: AttributeType.FLOAT,
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.CREATOR_ID: AttributeType.TEXT,
        ObjectRelation.DEPTH: AttributeType.FLOAT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.IMPRESSIONS: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_PARLEY_ID: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_USER_ID: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.POST_ID: AttributeType.TEXT,
        ObjectRelation.SHARE_LINK: AttributeType.LINK,
        ObjectRelation.UPVOTES: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.PASSIVE_DNS: {
        ObjectRelation.BAILIWICK: AttributeType.DOMAIN,
        ObjectRelation.COUNT: AttributeType.COUNTER,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.RAW_RDATA: AttributeType.TEXT,
        ObjectRelation.RDATA: AttributeType.TEXT,
        ObjectRelation.RRNAME: AttributeType.TEXT,
        ObjectRelation.RRTYPE: AttributeType.TEXT,
        ObjectRelation.SENSOR_ID: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TIME_FIRST: AttributeType.DATETIME,
        ObjectRelation.TIME_FIRST_MS: AttributeType.DATETIME,
        ObjectRelation.TIME_LAST: AttributeType.DATETIME,
        ObjectRelation.TIME_LAST_MS: AttributeType.DATETIME,
        ObjectRelation.ZONE_TIME_FIRST: AttributeType.DATETIME,
        ObjectRelation.ZONE_TIME_LAST: AttributeType.DATETIME,
    },
    ObjectType.PASSIVE_DNS_DNSDBFLEX: {
        ObjectRelation.RRNAME: AttributeType.TEXT,
        ObjectRelation.RRTYPE: AttributeType.TEXT,
    },
    ObjectType.PASSIVE_SSH: {
        ObjectRelation.BANNER: AttributeType.TEXT,
        ObjectRelation.BASE64: AttributeType.TEXT,
        ObjectRelation.FINGERPRINT: AttributeType.SSH_FINGERPRINT,
        ObjectRelation.FIRST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.HASSH: AttributeType.HASSH_MD5,
        ObjectRelation.HOST: AttributeType.IP_DST,
        ObjectRelation.LAST_SEEN_1: AttributeType.DATETIME,
        ObjectRelation.PORT: AttributeType.PORT,
    },
    ObjectType.PASTE: {
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.PASTE: AttributeType.TEXT,
        ObjectRelation.PASTE_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.PCAP_METADATA: {
        ObjectRelation.CAPTURE_INTERFACE: AttributeType.TEXT,
        ObjectRelation.CAPTURE_LENGTH: AttributeType.TEXT,
        ObjectRelation.FIRST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_PACKET_SEEN: AttributeType.DATETIME,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.PE: {
        ObjectRelation.AUTHENTIHASH: AttributeType.AUTHENTIHASH,
        ObjectRelation.CHARACTERISTICS: AttributeType.TEXT,
        ObjectRelation.CHARACTERISTICS_HEX: AttributeType.HEX,
        ObjectRelation.COMPANY_NAME: AttributeType.TEXT,
        ObjectRelation.COMPILATION_TIMESTAMP: AttributeType.DATETIME,
        ObjectRelation.ENTRYPOINT_ADDRESS: AttributeType.TEXT,
        ObjectRelation.ENTRYPOINT_SECTION_AT_POSITION: AttributeType.TEXT,
        ObjectRelation.FILE_DESCRIPTION: AttributeType.TEXT,
        ObjectRelation.FILE_VERSION: AttributeType.TEXT,
        ObjectRelation.IMPFUZZY: AttributeType.IMPFUZZY,
        ObjectRelation.IMPHASH: AttributeType.IMPHASH,
        ObjectRelation.INTERNAL_FILENAME: AttributeType.FILENAME,
        ObjectRelation.LANG_ID: AttributeType.TEXT,
        ObjectRelation.LEGAL_COPYRIGHT: AttributeType.TEXT,
        ObjectRelation.MACHINE_TYPE: AttributeType.TEXT,
        ObjectRelation.MACHINE_TYPE_HEX: AttributeType.HEX,
        ObjectRelation.NUMBER_OF_SYMBOLS: AttributeType.COUNTER,
        ObjectRelation.NUMBER_SECTIONS: AttributeType.COUNTER,
        ObjectRelation.ORIGINAL_FILENAME: AttributeType.FILENAME,
        ObjectRelation.PEHASH: AttributeType.PEHASH,
        ObjectRelation.POINTER_TO_SYMBOL_TABLE: AttributeType.HEX,
        ObjectRelation.PRODUCT_NAME: AttributeType.TEXT,
        ObjectRelation.PRODUCT_VERSION: AttributeType.TEXT,
        ObjectRelation.RICHPE: AttributeType.MD5,
        ObjectRelation.SIZE_OF_OPTIONAL_HEADER: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.PE_OPTIONAL_HEADER: {
        ObjectRelation.ADDRESS_OF_ENTRYPOINT: AttributeType.INTEGER,
        ObjectRelation.BASE_OF_CODE: AttributeType.INTEGER,
        ObjectRelation.BASE_OF_DATA: AttributeType.INTEGER,
        ObjectRelation.CHECKSUM: AttributeType.HEX,
        ObjectRelation.DLL_CHARACTERISTICS: AttributeType.TEXT,
        ObjectRelation.DLL_CHARACTERISTICS_HEX: AttributeType.HEX,
        ObjectRelation.FILE_ALIGNMENT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.IMAGE_BASE: AttributeType.INTEGER,
        ObjectRelation.LOADER_FLAGS: AttributeType.HEX,
        ObjectRelation.MAGIC: AttributeType.TEXT,
        ObjectRelation.MAGIC_HEX: AttributeType.HEX,
        ObjectRelation.MAJOR_IMAGE_VERSION: AttributeType.INTEGER,
        ObjectRelation.MAJOR_LINKER_VERSION: AttributeType.INTEGER,
        ObjectRelation.MAJOR_OS_VERSION: AttributeType.INTEGER,
        ObjectRelation.MAJOR_SUBSYSTEM_VERSION: AttributeType.INTEGER,
        ObjectRelation.MINOR_IMAGE_VERSION: AttributeType.INTEGER,
        ObjectRelation.MINOR_LINKER_VERSION: AttributeType.INTEGER,
        ObjectRelation.MINOR_OS_VERSION: AttributeType.INTEGER,
        ObjectRelation.MINOR_SUBSYSTEM_VERSION: AttributeType.INTEGER,
        ObjectRelation.NUMBER_OF_RVA_AND_SIZE: AttributeType.INTEGER,
        ObjectRelation.SECTION_ALIGNMENT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_CODE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_HEADERS: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_HEAP_COMMIT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_HEAP_RESERVE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_IMAGE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_INITIALISED_DATA: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_STACK_COMMIT: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_STACK_RESERVE: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SIZE_OF_UNINITIALISED_DATA: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SUBSYSTEM: AttributeType.TEXT,
        ObjectRelation.SUBSYSTEM_HEX: AttributeType.HEX,
        ObjectRelation.WIN32_VERSION_VALUE: AttributeType.HEX,
    },
    ObjectType.PE_SECTION: {
        ObjectRelation.CHARACTERISTIC: AttributeType.TEXT,
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OFFSET: AttributeType.HEX,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA224: AttributeType.SHA224,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SHA384: AttributeType.SHA384,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.SHA512_224: AttributeType.SHA512_224,
        ObjectRelation.SHA512_256: AttributeType.SHA512_256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.SSDEEP_1: AttributeType.SSDEEP,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.VIRTUAL_ADDRESS: AttributeType.HEX,
        ObjectRelation.VIRTUAL_SIZE: AttributeType.SIZE_IN_BYTES,
    },
    ObjectType.PERSNONA: {
        ObjectRelation.ACTIONS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BACKGROUND: AttributeType.TEXT,
        ObjectRelation.CONVERSATIONS: AttributeType.TEXT,
        ObjectRelation.CRITICAL_TASKS: AttributeType.TEXT,
        ObjectRelation.GOALS: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.MEDIA: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.FULL_NAME,
        ObjectRelation.OPPPORTUNITIES: AttributeType.TEXT,
        ObjectRelation.PHOTO: AttributeType.URL,
        ObjectRelation.QUESTIONS: AttributeType.TEXT,
        ObjectRelation.RESPONSI: AttributeType.TEXT,
    },
    ObjectType.PERSON: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ALIAS: AttributeType.TEXT,
        ObjectRelation.BIRTH_CERTIFICATE_NUMBER: AttributeType.TEXT,
        ObjectRelation.DATE_OF_BIRTH: AttributeType.DATE_OF_BIRTH,
        ObjectRelation.DNI: AttributeType.TEXT,
        ObjectRelation.E_MAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.FAX_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.FIRST_NAME: AttributeType.FIRST_NAME,
        ObjectRelation.FULL_NAME: AttributeType.FULL_NAME,
        ObjectRelation.FUNCTION: AttributeType.TEXT,
        ObjectRelation.GENDER: AttributeType.GENDER,
        ObjectRelation.HANDLE: AttributeType.TEXT,
        ObjectRelation.IDENTITY_CARD_NUMBER: AttributeType.IDENTITY_CARD_NUMBER,
        ObjectRelation.INSTANT_MESSAGING_USED: AttributeType.TEXT,
        ObjectRelation.IP_SRC: AttributeType.IP_SRC,
        ObjectRelation.LAST_NAME: AttributeType.LAST_NAME,
        ObjectRelation.MIDDLE_NAME: AttributeType.MIDDLE_NAME,
        ObjectRelation.MOTHERS_NAME: AttributeType.TEXT,
        ObjectRelation.NATIONALITY: AttributeType.NATIONALITY,
        ObjectRelation.NIC_HDL: AttributeType.TEXT,
        ObjectRelation.NIE: AttributeType.TEXT,
        ObjectRelation.NIF: AttributeType.TEXT,
        ObjectRelation.OCCUPATION: AttributeType.TEXT,
        ObjectRelation.OFAC_IDENTIFICATION_NUMBER: AttributeType.TEXT,
        ObjectRelation.PASSPORT_COUNTRY: AttributeType.PASSPORT_COUNTRY,
        ObjectRelation.PASSPORT_CREATION: AttributeType.DATETIME,
        ObjectRelation.PASSPORT_EXPIRATION: AttributeType.PASSPORT_EXPIRATION,
        ObjectRelation.PASSPORT_NUMBER: AttributeType.PASSPORT_NUMBER,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.PLACE_OF_BIRTH: AttributeType.PLACE_OF_BIRTH,
        ObjectRelation.PORTRAIT: AttributeType.ATTACHMENT,
        ObjectRelation.REDRESS_NUMBER: AttributeType.REDRESS_NUMBER,
        ObjectRelation.ROLE: AttributeType.TEXT,
        ObjectRelation.SOCIAL_SECURITY_NUMBER: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.PERSONIFICATION: {
        ObjectRelation.AGE_RANGE: AttributeType.FLOAT,
        ObjectRelation.BEARD: AttributeType.TEXT,
        ObjectRelation.BIRTHMARK: AttributeType.TEXT,
        ObjectRelation.BODY_TYPE: AttributeType.TEXT,
        ObjectRelation.COLOR_OF_EYES: AttributeType.TEXT,
        ObjectRelation.HAIR_CHARACTERISTICS: AttributeType.TEXT,
        ObjectRelation.HAIR_COLOR: AttributeType.TEXT,
        ObjectRelation.HAIRCUT: AttributeType.TEXT,
        ObjectRelation.HEIGHT: AttributeType.FLOAT,
        ObjectRelation.OTHER_FACIAL_FEATURES: AttributeType.TEXT,
        ObjectRelation.PORTRAIT: AttributeType.ATTACHMENT,
        ObjectRelation.SHAPE_OF_EYES: AttributeType.TEXT,
        ObjectRelation.SHOE_SIZE: AttributeType.FLOAT,
        ObjectRelation.SKIN_CHARATERISTICS: AttributeType.TEXT,
        ObjectRelation.SKIN_COMPLEXION: AttributeType.TEXT,
        ObjectRelation.WEIGHT: AttributeType.FLOAT,
    },
    ObjectType.PGP_META: {
        ObjectRelation.KEY_ID: AttributeType.TEXT,
        ObjectRelation.USER_ID_EMAIL: AttributeType.TEXT,
        ObjectRelation.USER_ID_NAME: AttributeType.TEXT,
    },
    ObjectType.PHISHING: {
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.INTERNAL_REFERENCE: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.ONLINE: AttributeType.TEXT,
        ObjectRelation.PHISHTANK_DETAIL_URL: AttributeType.LINK,
        ObjectRelation.PHISHTANK_ID: AttributeType.TEXT,
        ObjectRelation.SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.SUBMISSION_TIME: AttributeType.DATETIME,
        ObjectRelation.TAKEDOWN_REQUEST: AttributeType.DATETIME,
        ObjectRelation.TAKEDOWN_REQUEST_TO: AttributeType.TEXT,
        ObjectRelation.TAKEDOWN_TIME: AttributeType.DATETIME,
        ObjectRelation.TARGET: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.URL_REDIRECT: AttributeType.URL,
        ObjectRelation.VERIFICATION_TIME: AttributeType.DATETIME,
        ObjectRelation.VERIFIED: AttributeType.TEXT,
    },
    ObjectType.PHISHING_KIT: {
        ObjectRelation.DATE_FOUND: AttributeType.DATETIME,
        ObjectRelation.EMAIL_TYPE: AttributeType.TEXT,
        ObjectRelation.INTERNAL_REFERENCE: AttributeType.TEXT,
        ObjectRelation.KIT_MAILER: AttributeType.TEXT,
        ObjectRelation.KIT_NAME: AttributeType.TEXT,
        ObjectRelation.KIT_URL: AttributeType.URL,
        ObjectRelation.ONLINE: AttributeType.TEXT,
        ObjectRelation.PHISHING_DOMAIN: AttributeType.URL,
        ObjectRelation.REFERENCE_LINK: AttributeType.LINK,
        ObjectRelation.TARGET: AttributeType.TEXT,
        ObjectRelation.THREAT_ACTOR_1: AttributeType.TEXT,
        ObjectRelation.THREAT_ACTOR_EMAIL: AttributeType.EMAIL_SRC,
    },
    ObjectType.PHONE: {
        ObjectRelation.BRAND: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.GUMMEI: AttributeType.TEXT,
        ObjectRelation.GUTI: AttributeType.TEXT,
        ObjectRelation.IMEI: AttributeType.TEXT,
        ObjectRelation.IMSI: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.MSISDN: AttributeType.TEXT,
        ObjectRelation.SERIAL_NUMBER: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TMSI: AttributeType.TEXT,
    },
    ObjectType.PHONE_NUMBER: {
        ObjectRelation.COUNTRY_CODE: AttributeType.TEXT,
        ObjectRelation.COUNTRY_CODE_NUMERIC: AttributeType.TEXT,
        ObjectRelation.NATIONAL_DESTINATION_CODE: AttributeType.TEXT,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.SUBSCRIBER_NUMBER: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.PHYSICAL_IMPACT: {
        ObjectRelation.ASSET_TYPE: AttributeType.TEXT,
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.IMPACT_TYPE: AttributeType.TEXT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
    },
    ObjectType.POSTAL_ADDRESS: {
        ObjectRelation.APARTMENT: AttributeType.TEXT,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.NUMBER: AttributeType.TEXT,
        ObjectRelation.POSTAL_CODE: AttributeType.TEXT,
        ObjectRelation.PROVINCE: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.STREET: AttributeType.TEXT,
    },
    ObjectType.PROBABILISTIC_DATA_STRUCTURE: {
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PROBABILITY: AttributeType.FLOAT,
        ObjectRelation.TOTAL_BITS: AttributeType.INTEGER,
        ObjectRelation.TOTAL_CAPACITY: AttributeType.INTEGER,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.UPDATABLE: AttributeType.BOOLEAN,
        ObjectRelation.USED_CAPACITY: AttributeType.INTEGER,
        ObjectRelation.VENDOR_IMPLEMENTATION_REF: AttributeType.LINK,
    },
    ObjectType.PROCESS: {
        ObjectRelation.ARGS: AttributeType.TEXT,
        ObjectRelation.CHILD_PID: AttributeType.TEXT,
        ObjectRelation.COMMAND_LINE: AttributeType.TEXT,
        ObjectRelation.CREATION_TIME: AttributeType.DATETIME,
        ObjectRelation.CURRENT_DIRECTORY: AttributeType.TEXT,
        ObjectRelation.ENVIRONMENT_VARIABLES: AttributeType.TEXT,
        ObjectRelation.FAKE_PROCESS_NAME: AttributeType.BOOLEAN,
        ObjectRelation.GUID: AttributeType.TEXT,
        ObjectRelation.HIDDEN: AttributeType.BOOLEAN,
        ObjectRelation.IMAGE: AttributeType.FILENAME,
        ObjectRelation.INTEGRITY_LEVEL: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PARENT_COMMAND_LINE: AttributeType.TEXT,
        ObjectRelation.PARENT_GUID: AttributeType.TEXT,
        ObjectRelation.PARENT_IMAGE: AttributeType.FILENAME,
        ObjectRelation.PARENT_PID: AttributeType.TEXT,
        ObjectRelation.PARENT_PROCESS_NAME: AttributeType.TEXT,
        ObjectRelation.PARENT_PROCESS_PATH: AttributeType.TEXT,
        ObjectRelation.PGID: AttributeType.TEXT,
        ObjectRelation.PID: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.PROCESS_STATE: AttributeType.PROCESS_STATE,
        ObjectRelation.START_TIME_1: AttributeType.DATETIME,
        ObjectRelation.USER_CREATOR: AttributeType.TEXT,
        ObjectRelation.USER_PROCESS: AttributeType.TEXT,
    },
    ObjectType.PUBLICATION: {
        ObjectRelation.DOI: AttributeType.TEXT,
        ObjectRelation.ISBN: AttributeType.TEXT,
        ObjectRelation.ACADEMIC_INSTITUTION: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.CONTENT: AttributeType.TEXT,
        ObjectRelation.CONTRIBUTOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EDITION: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PUBLISHER: AttributeType.TEXT,
        ObjectRelation.SERIES: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.VOLUME: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.LINK,
        ObjectRelation.YEAR: AttributeType.TEXT,
    },
    ObjectType.PYTHON_ETVX_EVENT_LOG: {
        ObjectRelation.COMPUTER: AttributeType.TEXT,
        ObjectRelation.CORRELATION_ID: AttributeType.TEXT,
        ObjectRelation.EVENT_DATA: AttributeType.TEXT,
        ObjectRelation.KEYWORDS: AttributeType.TEXT,
        ObjectRelation.OPERATIONAL_CODE: AttributeType.TEXT,
        ObjectRelation.PROCESSOR_ID: AttributeType.TEXT,
        ObjectRelation.RELATIVE_CORRELATION_ID: AttributeType.TEXT,
        ObjectRelation.SESSION_ID: AttributeType.TEXT,
        ObjectRelation.THREAD_ID: AttributeType.TEXT,
        ObjectRelation.USER: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.EVENT_CHANNEL: AttributeType.TEXT,
        ObjectRelation.EVENT_DATE_TIME: AttributeType.DATETIME,
        ObjectRelation.EVENT_ID: AttributeType.TEXT,
        ObjectRelation.EVENT_TYPE: AttributeType.TEXT,
        ObjectRelation.KERNEL_TIME: AttributeType.DATETIME,
        ObjectRelation.LEVEL: AttributeType.TEXT,
        ObjectRelation.LOG: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.TASK_CATEGORY: AttributeType.TEXT,
        ObjectRelation.USER_TIME: AttributeType.DATETIME,
    },
    ObjectType.QUERY: {
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.FORMAT: AttributeType.TEXT,
        ObjectRelation.QUERY: AttributeType.TEXT,
        ObjectRelation.QUERY_RULE_NAME: AttributeType.TEXT,
    },
    ObjectType.R2GRAPHITY: {
        ObjectRelation.CALLBACK_AVERAGE: AttributeType.INTEGER,
        ObjectRelation.CALLBACK_LARGEST: AttributeType.INTEGER,
        ObjectRelation.CALLBACKS: AttributeType.COUNTER,
        ObjectRelation.CREATE_THREAD: AttributeType.COUNTER,
        ObjectRelation.DANGLING_STRINGS: AttributeType.COUNTER,
        ObjectRelation.GET_PROC_ADDRESS: AttributeType.COUNTER,
        ObjectRelation.GML: AttributeType.ATTACHMENT,
        ObjectRelation.LOCAL_REFERENCES: AttributeType.COUNTER,
        ObjectRelation.MEMORY_ALLOCATIONS: AttributeType.COUNTER,
        ObjectRelation.MISS_API: AttributeType.COUNTER,
        ObjectRelation.NOT_REFERENCED_STRINGS: AttributeType.COUNTER,
        ObjectRelation.R2_COMMIT_VERSION: AttributeType.TEXT,
        ObjectRelation.RATIO_API: AttributeType.FLOAT,
        ObjectRelation.RATIO_FUNCTIONS: AttributeType.FLOAT,
        ObjectRelation.RATIO_STRING: AttributeType.FLOAT,
        ObjectRelation.REFERENCED_STRINGS: AttributeType.COUNTER,
        ObjectRelation.REFSGLOBALVAR: AttributeType.COUNTER,
        ObjectRelation.SHORTEST_PATH_TO_CREATE_THREAD: AttributeType.INTEGER,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TOTAL_API: AttributeType.COUNTER,
        ObjectRelation.TOTAL_FUNCTIONS: AttributeType.COUNTER,
        ObjectRelation.UNKNOWN_REFERENCES: AttributeType.COUNTER,
    },
    ObjectType.RANSOM_NEGOTIATION: {
        ObjectRelation.REMARKS: AttributeType.TEXT,
        ObjectRelation.ANNUAL_REVENUE_EUR: AttributeType.FLOAT,
        ObjectRelation.CHATSITE: AttributeType.URL,
        ObjectRelation.CHATSITE_ID_PRIVATE: AttributeType.TEXT,
        ObjectRelation.CHATSITE_ID_PUBLIC: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.DATA_LEAKED: AttributeType.BOOLEAN,
        ObjectRelation.DATA_STOLEN: AttributeType.BOOLEAN,
        ObjectRelation.DISCOUNT: AttributeType.FLOAT,
        ObjectRelation.EMAIL_ADDRESS_2: AttributeType.TEXT,
        ObjectRelation.FINAL_RANSOM: AttributeType.FLOAT,
        ObjectRelation.INITIAL_RANSOM: AttributeType.FLOAT,
        ObjectRelation.NEGOTIATIONS_SCREENSHOT: AttributeType.ATTACHMENT,
        ObjectRelation.NEGOTIATIONS_TRANSCRIPT: AttributeType.TEXT,
        ObjectRelation.PAY_FOR_DELETION: AttributeType.BOOLEAN,
        ObjectRelation.PAY_FOR_ENCRYPTOR: AttributeType.BOOLEAN,
        ObjectRelation.PERCENTAGE_OF_REVENUE: AttributeType.FLOAT,
        ObjectRelation.TIME: AttributeType.DATETIME,
        ObjectRelation.URL_LEAKSITE: AttributeType.URL,
        ObjectRelation.VALUE_EUR: AttributeType.FLOAT,
        ObjectRelation.WALLET_ADDRESS: AttributeType.BTC,
    },
    ObjectType.RANSOMWARE_GROUP_POST: {
        ObjectRelation.ACTOR_GEO_STATS_30D: AttributeType.TEXT,
        ObjectRelation.ACTOR_TOTAL_STATS_30D: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.DATETIME,
        ObjectRelation.DATE_PUBLISHED: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ENTITY_NAME: AttributeType.TEXT,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.LEAK_SITE_URL: AttributeType.LINK,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.RANSOMWARE_GROUP: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.WEBSITE: AttributeType.LINK,
    },
    ObjectType.REDDIT_ACCOUNT: {
        ObjectRelation.ACCOUNT_AVATAR: AttributeType.ATTACHMENT,
        ObjectRelation.ACCOUNT_AVATAR_URL: AttributeType.URL,
        ObjectRelation.ACCOUNT_ID: AttributeType.TEXT,
        ObjectRelation.ACCOUNT_NAME: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MODERATOR_OF: AttributeType.TEXT,
        ObjectRelation.TROPHIES: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.REDDIT_COMMENT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.SUBREDDIT_NAME: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.REDDIT_POST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EDITED: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.POST_CONTENT: AttributeType.TEXT,
        ObjectRelation.POST_TITLE: AttributeType.TEXT,
        ObjectRelation.SUBREDDIT_NAME: AttributeType.TEXT,
        ObjectRelation.THUMBNAIL: AttributeType.ATTACHMENT,
        ObjectRelation.THUMBNAIL_URL: AttributeType.URL,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.REDDIT_SUBREDDIT: {
        ObjectRelation.ACTIVE_USER_COUNT: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BANNER_BACKGROUND_IMAGE: AttributeType.ATTACHMENT,
        ObjectRelation.BANNER_BACKGROUND_URL: AttributeType.URL,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.HEADER_TITLE: AttributeType.TEXT,
        ObjectRelation.ICON_IMG: AttributeType.ATTACHMENT,
        ObjectRelation.ICON_IMG_URL: AttributeType.URL,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MODERATOR: AttributeType.TEXT,
        ObjectRelation.PRIVACY: AttributeType.TEXT,
        ObjectRelation.RULES: AttributeType.TEXT,
        ObjectRelation.SUBMIT_TEXT: AttributeType.TEXT,
        ObjectRelation.SUBREDDIT_ALIAS: AttributeType.TEXT,
        ObjectRelation.SUBREDDIT_TYPE: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.REGEXP: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.REGEXP: AttributeType.TEXT,
        ObjectRelation.REGEXP_TYPE: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.REGISTRY_KEY: {
        ObjectRelation.DATA: AttributeType.TEXT,
        ObjectRelation.DATA_TYPE: AttributeType.TEXT,
        ObjectRelation.HIVE: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.REGKEY,
        ObjectRelation.LAST_MODIFIED: AttributeType.DATETIME,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.ROOT_KEYS: AttributeType.TEXT,
    },
    ObjectType.REGISTRY_KEY_VALUE: {
        ObjectRelation.DATA: AttributeType.TEXT,
        ObjectRelation.DATA_TYPE: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_NTUSER: {
        ObjectRelation.APPLICATIONS_INSTALLED: AttributeType.TEXT,
        ObjectRelation.APPLICATIONS_RUN: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.EXTERNAL_DEVICES: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.LOGON_USER_NAME: AttributeType.TEXT,
        ObjectRelation.MOUNT_POINTS: AttributeType.TEXT,
        ObjectRelation.NETWORK_CONNECTED_TO: AttributeType.TEXT,
        ObjectRelation.NUKEONDELETE: AttributeType.BOOLEAN,
        ObjectRelation.RECENT_FILES_ACCESSED: AttributeType.TEXT,
        ObjectRelation.RECENT_FOLDERS_ACCESSED: AttributeType.TEXT,
        ObjectRelation.TYPED_URLS: AttributeType.TEXT,
        ObjectRelation.USER_INIT: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SAM_HIVE_SINGLE_USER: {
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.FULL_USER_NAME: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.LAST_LOGIN_TIME: AttributeType.DATETIME,
        ObjectRelation.LOGIN_COUNT: AttributeType.COUNTER,
        ObjectRelation.PWD_FAIL_DATE: AttributeType.DATETIME,
        ObjectRelation.PWD_RESET_TIME: AttributeType.DATETIME,
        ObjectRelation.USER_NAME: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SAM_HIVE_USER_GROUP: {
        ObjectRelation.FULL_NAME: AttributeType.TEXT,
        ObjectRelation.GROUP_COMMENT: AttributeType.TEXT,
        ObjectRelation.GROUP_NAME: AttributeType.TEXT,
        ObjectRelation.GROUP_USERS: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.LAST_WRITE_DATE_TIME: AttributeType.DATETIME,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_BHO: {
        ObjectRelation.BHO_KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.BHO_NAME: AttributeType.TEXT,
        ObjectRelation.CLASS: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.MODULE: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_APPINIT_DLLS: {
        ObjectRelation.DLL_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.DLL_NAME: AttributeType.TEXT,
        ObjectRelation.DLL_PATH: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.REFERENCES: AttributeType.LINK,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_APPLICATION_PATHS: {
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.EXECUTABLE_FILE_NAME: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.PATH: AttributeType.TEXT,
        ObjectRelation.REFERENCES: AttributeType.LINK,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_APPLICATIONS_INSTALLED: {
        ObjectRelation.APP_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.APP_NAME: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_PATH: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_COMMAND_SHELL: {
        ObjectRelation.COMMAND: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.SHELL_1: AttributeType.TEXT,
        ObjectRelation.SHELL_PATH: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_SOFTWARE_RUN: {
        ObjectRelation.APPLICATION_NAME: AttributeType.TEXT,
        ObjectRelation.APPLICATION_PATH: AttributeType.TEXT,
        ObjectRelation.COMMENTS_2: AttributeType.TEXT,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_PATH: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.REFERENCES: AttributeType.LINK,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_USERPROFILE_WINLOGON: {
        ObjectRelation.AUTOADMINLOGON: AttributeType.BOOLEAN,
        ObjectRelation.AUTORESTARTSHELL: AttributeType.BOOLEAN,
        ObjectRelation.CACHEDLOGONCOUNT: AttributeType.COUNTER,
        ObjectRelation.COMMENTS_1: AttributeType.TEXT,
        ObjectRelation.DEFAULTUSERNAME: AttributeType.TEXT,
        ObjectRelation.DISABLECAD: AttributeType.BOOLEAN,
        ObjectRelation.LEGAL_NOTICE_CAPTION: AttributeType.TEXT,
        ObjectRelation.LEGAL_NOTICE_TEXT: AttributeType.TEXT,
        ObjectRelation.PASSWORDEXPIRYWARINING: AttributeType.COUNTER,
        ObjectRelation.POWERDOWNAFTERSHUTDOWN: AttributeType.BOOLEAN,
        ObjectRelation.PRECREATEKNOWNFOLDERS: AttributeType.TEXT,
        ObjectRelation.REPORTBOOTOK: AttributeType.BOOLEAN,
        ObjectRelation.SID: AttributeType.TEXT,
        ObjectRelation.SHELL: AttributeType.TEXT,
        ObjectRelation.SHUTDOWNFLAGS: AttributeType.COUNTER,
        ObjectRelation.SHUTDOWNWITHOUTLOGON: AttributeType.BOOLEAN,
        ObjectRelation.USERINIT: AttributeType.TEXT,
        ObjectRelation.WINSTATIONSDISABLED: AttributeType.BOOLEAN,
        ObjectRelation.USER_PROFILE_KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.USER_PROFILE_KEY_PATH: AttributeType.TEXT,
        ObjectRelation.USER_PROFILE_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.USER_PROFILE_PATH: AttributeType.TEXT,
        ObjectRelation.WINLOGON_KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.WINLOGON_KEY_PATH: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SOFTWARE_HIVE_WINDOWS_GENERAL_INFO: {
        ObjectRelation.BUILDGUID: AttributeType.TEXT,
        ObjectRelation.BUILDLAB: AttributeType.TEXT,
        ObjectRelation.BUILDLABEX: AttributeType.TEXT,
        ObjectRelation.CSDVERSION: AttributeType.TEXT,
        ObjectRelation.CURRENTBUILD: AttributeType.TEXT,
        ObjectRelation.CURRENTBUILDTYPE: AttributeType.TEXT,
        ObjectRelation.CURRENTVERSION: AttributeType.TEXT,
        ObjectRelation.EDITIONID: AttributeType.TEXT,
        ObjectRelation.INSTALLDATE: AttributeType.DATETIME,
        ObjectRelation.INSTALLATIONTYPE: AttributeType.TEXT,
        ObjectRelation.PATHNAME: AttributeType.TEXT,
        ObjectRelation.PRODUCTID: AttributeType.TEXT,
        ObjectRelation.PRODUCTNAME: AttributeType.TEXT,
        ObjectRelation.REGISTEREDORGANIZATION: AttributeType.TEXT,
        ObjectRelation.REGISTEREDOWNER: AttributeType.TEXT,
        ObjectRelation.SOFTWARETYPE: AttributeType.TEXT,
        ObjectRelation.SYSTEMROOT: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.WIN_CV_PATH: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SYSTEM_HIVE_FIREWALL_CONFIGURATION: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DISABLE_NOTIFICATION: AttributeType.BOOLEAN,
        ObjectRelation.ENBLED_FIREWALL: AttributeType.BOOLEAN,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.PROFILE: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SYSTEM_HIVE_GENERAL_CONFIGURATION: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.COMPUTER_NAME: AttributeType.TEXT,
        ObjectRelation.FDENYTSCONNECTIONS_: AttributeType.BOOLEAN,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.SHUTDOWN_TIME: AttributeType.DATETIME,
        ObjectRelation.TIMEZONE_BIAS: AttributeType.TEXT,
        ObjectRelation.TIMEZONE_DAYLIGHT_BIAS: AttributeType.TEXT,
        ObjectRelation.TIMEZONE_DAYLIGHT_DATE: AttributeType.DATETIME,
        ObjectRelation.TIMEZONE_DAYLIGHT_NAME: AttributeType.TEXT,
        ObjectRelation.TIMEZONE_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.TIMEZONE_STANDARD_BIAS: AttributeType.TEXT,
        ObjectRelation.TIMEZONE_STANDARD_DATE: AttributeType.DATETIME,
        ObjectRelation.TIMEZONE_STANDARD_NAME: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SYSTEM_HIVE_NETWORK_INFORMATION: {
        ObjectRelation.DHCP_IP_ADDRESS: AttributeType.IP_DST,
        ObjectRelation.DHCP_DOMAIN: AttributeType.TEXT,
        ObjectRelation.DHCP_NAME_SERVER: AttributeType.IP_DST,
        ObjectRelation.DHCP_SERVER: AttributeType.IP_DST,
        ObjectRelation.DHCP_SUBNET_MASK: AttributeType.IP_DST,
        ObjectRelation.TCPIP_KEY: AttributeType.TEXT,
        ObjectRelation.TCPIP_KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.INTERFACE_GUID: AttributeType.TEXT,
        ObjectRelation.INTERFACE_IPCHECKINGENABLED: AttributeType.BOOLEAN,
        ObjectRelation.INTERFACE_MEDIASUBTYPE: AttributeType.TEXT,
        ObjectRelation.INTERFACE_PNPINSTANCEID: AttributeType.TEXT,
        ObjectRelation.INTERFACE_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.INTERFACE_NAME: AttributeType.TEXT,
        ObjectRelation.NETWORK_KEY: AttributeType.TEXT,
        ObjectRelation.NETWORK_KEY_LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.NETWORK_KEY_PATH: AttributeType.TEXT,
    },
    ObjectType.REGRIPPER_SYSTEM_HIVE_SERVICES_DRIVERS: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DISPLAY: AttributeType.TEXT,
        ObjectRelation.GROUP: AttributeType.TEXT,
        ObjectRelation.IMAGE_PATH: AttributeType.TEXT,
        ObjectRelation.LAST_WRITE_TIME: AttributeType.DATETIME,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.START: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.REPORT: {
        ObjectRelation.CASE_NUMBER: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.REPORT_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.RESEARCH_SCANNER: {
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.CONTACT_EMAIL: AttributeType.EMAIL_DST,
        ObjectRelation.CONTACT_PHONE: AttributeType.PHONE_NUMBER,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.PROJECT: AttributeType.TEXT,
        ObjectRelation.PROJECT_URL: AttributeType.LINK,
        ObjectRelation.SCANNING_HOST: AttributeType.HOSTNAME,
        ObjectRelation.SCANNING_IP: AttributeType.IP_SRC,
        ObjectRelation.SCHEDULED_END: AttributeType.DATETIME,
        ObjectRelation.SCHEDULED_START: AttributeType.DATETIME,
    },
    ObjectType.RISK_ASSESSMENT_REPORT: {
        ObjectRelation.CASE_NUMBER: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.REPORT_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.ROGUE_DNS: {
        ObjectRelation.HIJACKED_DOMAIN: AttributeType.HOSTNAME,
        ObjectRelation.PHISHING_IP: AttributeType.IP_DST,
        ObjectRelation.ROGUE_DNS: AttributeType.IP_DST,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.DATETIME,
    },
    ObjectType.RTIR: {
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.CONSTITUENCY: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.QUEUE: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
        ObjectRelation.TICKET_NUMBER: AttributeType.TEXT,
    },
    ObjectType.SANDBOX_REPORT: {
        ObjectRelation.ON_PREMISE_SANDBOX: AttributeType.TEXT,
        ObjectRelation.PERMALINK: AttributeType.LINK,
        ObjectRelation.RAW_REPORT: AttributeType.TEXT,
        ObjectRelation.RESULTS: AttributeType.TEXT,
        ObjectRelation.SAAS_SANDBOX: AttributeType.TEXT,
        ObjectRelation.SANDBOX_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.SANDBOX_TYPE: AttributeType.TEXT,
        ObjectRelation.SCORE: AttributeType.TEXT,
        ObjectRelation.WEB_SANDBOX: AttributeType.TEXT,
    },
    ObjectType.SB_SIGNATURE: {
        ObjectRelation.DATETIME: AttributeType.DATETIME,
        ObjectRelation.SIGNATURE: AttributeType.TEXT,
        ObjectRelation.SOFTWARE_1: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.SCAN_RESULT: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.SCAN_END: AttributeType.DATETIME,
        ObjectRelation.SCAN_RESULT: AttributeType.ATTACHMENT,
        ObjectRelation.SCAN_RESULT_FORMAT: AttributeType.TEXT,
        ObjectRelation.SCAN_RESULT_QUERY: AttributeType.TEXT,
        ObjectRelation.SCAN_RESULT_TOOL: AttributeType.TEXT,
        ObjectRelation.SCAN_START: AttributeType.DATETIME,
        ObjectRelation.SCAN_TYPE: AttributeType.TEXT,
    },
    ObjectType.SCHEDULED_EVENT: {
        ObjectRelation.ADDRESS: AttributeType.TEXT,
        ObjectRelation.ADMINISTRATOR: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.E_MAIL: AttributeType.EMAIL_SRC,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.EVENT_ALIAS: AttributeType.TEXT,
        ObjectRelation.EVENT_LISTING: AttributeType.TEXT,
        ObjectRelation.EVENT_NAME: AttributeType.TEXT,
        ObjectRelation.FAX_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PERSON_NAME: AttributeType.TEXT,
        ObjectRelation.PHONE_NUMBER: AttributeType.PHONE_NUMBER,
        ObjectRelation.SCHEDULED_DATE: AttributeType.DATETIME,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.SCHEDULED_TASK: {
        ObjectRelation.START_TIME: AttributeType.DATETIME,
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.HIGHEST_PRIVILEGES: AttributeType.BOOLEAN,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PASSWORD_STORED: AttributeType.BOOLEAN,
        ObjectRelation.REPEAT: AttributeType.TEXT,
        ObjectRelation.RUN_WHEN_USER_LOGGED_ON_ONLY: AttributeType.BOOLEAN,
        ObjectRelation.RUNNING_ACCOUNT: AttributeType.TEXT,
        ObjectRelation.TRIGGER: AttributeType.TEXT,
    },
    ObjectType.SCRIPPSCO2_C13_DAILY: {
        ObjectRelation.C13_VALUE: AttributeType.FLOAT,
        ObjectRelation.FLAG: AttributeType.INTEGER,
        ObjectRelation.NUMBER_FLASK: AttributeType.COUNTER,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPPSCO2_C13_MONTHLY: {
        ObjectRelation.MONTHLY_C13: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_C13_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_C13_SMOOTHED: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_C13_SMOOTHED_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPPSCO2_CO2_DAILY: {
        ObjectRelation.CO2_VALUE: AttributeType.FLOAT,
        ObjectRelation.FLAG: AttributeType.INTEGER,
        ObjectRelation.NUMBER_FLASK: AttributeType.COUNTER,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPPSCO2_CO2_MONTHLY: {
        ObjectRelation.MONTHLY_CO2: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_CO2_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_CO2_SMOOTHED: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_CO2_SMOOTHED_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPPSCO2_O18_DAILY: {
        ObjectRelation.FLAG: AttributeType.INTEGER,
        ObjectRelation.NUMBER_FLASK: AttributeType.COUNTER,
        ObjectRelation.O18_VALUE: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPPSCO2_O18_MONTHLY: {
        ObjectRelation.MONTHLY_O18: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_O18_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_O18_SMOOTHED: AttributeType.FLOAT,
        ObjectRelation.MONTHLY_O18_SMOOTHED_SEASONAL_ADJUSTMENT: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_EXCEL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATE_FRACTIONAL: AttributeType.FLOAT,
        ObjectRelation.SAMPLE_DATETIME: AttributeType.DATETIME,
    },
    ObjectType.SCRIPT: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.SCRIPT: AttributeType.TEXT,
        ObjectRelation.SCRIPT_AS_ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.STATE: AttributeType.TEXT,
    },
    ObjectType.SECURITY_PLAYBOOK: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LABELS: AttributeType.TEXT,
        ObjectRelation.ORGANIZATION_TYPE: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_ABSTRACTION: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_BASE64: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_CREATION_TIME: AttributeType.DATETIME,
        ObjectRelation.PLAYBOOK_CREATOR: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_FILE: AttributeType.ATTACHMENT,
        ObjectRelation.PLAYBOOK_ID: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_IMPACT: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_MODIFICATION_TIME: AttributeType.DATETIME,
        ObjectRelation.PLAYBOOK_PRIORITY: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_SEVERITY: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_STANDARD: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_TYPE: AttributeType.TEXT,
        ObjectRelation.PLAYBOOK_VALID_FROM: AttributeType.DATETIME,
        ObjectRelation.PLAYBOOK_VALID_UNTIL: AttributeType.DATETIME,
        ObjectRelation.REVOKED: AttributeType.BOOLEAN,
    },
    ObjectType.SHADOWSERVER_MALWARE_URL_REPORT: {
        ObjectRelation.APPLICATION: AttributeType.TEXT,
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.HOST: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.NAICS: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.REGION: AttributeType.TEXT,
        ObjectRelation.RESOURCE_PATH: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.TAG: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.DATETIME,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.SHADOWSERVER_SCAN_HTTP_PROXY: {
        ObjectRelation.ASN: AttributeType.AS,
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.CONNECTION: AttributeType.TEXT,
        ObjectRelation.CONTENT_LENGTH_1: AttributeType.TEXT,
        ObjectRelation.CONTENT_TYPE_1: AttributeType.TEXT,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.HOSTNAME_SOURCE: AttributeType.TEXT,
        ObjectRelation.HTTP: AttributeType.TEXT,
        ObjectRelation.HTTP_CODE_1: AttributeType.TEXT,
        ObjectRelation.HTTP_DATE: AttributeType.TEXT,
        ObjectRelation.HTTP_REASON: AttributeType.TEXT,
        ObjectRelation.IP_1: AttributeType.IP_SRC,
        ObjectRelation.NAICS: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.PROTOCOL: AttributeType.TEXT,
        ObjectRelation.PROXY_AUTHENTICATE: AttributeType.TEXT,
        ObjectRelation.REGION: AttributeType.TEXT,
        ObjectRelation.SECTOR: AttributeType.TEXT,
        ObjectRelation.SERVER: AttributeType.TEXT,
        ObjectRelation.SEVERITY: AttributeType.TEXT,
        ObjectRelation.TAG: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.DATETIME,
        ObjectRelation.TRANSFER_ENCODING: AttributeType.TEXT,
        ObjectRelation.VIA: AttributeType.TEXT,
    },
    ObjectType.SHELL_COMMANDS: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.SCRIPT: AttributeType.TEXT,
        ObjectRelation.SHELL_COMMAND: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
    },
    ObjectType.SHODAN_REPORT: {
        ObjectRelation.BANNER: AttributeType.TEXT,
        ObjectRelation.HOSTNAME: AttributeType.DOMAIN,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.ORG: AttributeType.TEXT,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.SHORT_MESSAGE_SERVICE: {
        ObjectRelation.BODY: AttributeType.TEXT,
        ObjectRelation.FROM: AttributeType.PHONE_NUMBER,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PHONE_COMPANY: AttributeType.TEXT,
        ObjectRelation.RECEIVED_DATE: AttributeType.DATETIME,
        ObjectRelation.SENT_DATE: AttributeType.DATETIME,
        ObjectRelation.SMSC: AttributeType.PHONE_NUMBER,
        ObjectRelation.TO: AttributeType.PHONE_NUMBER,
        ObjectRelation.URL_RFC5724: AttributeType.URL,
    },
    ObjectType.SHORTENED_LINK: {
        ObjectRelation.CREDENTIAL: AttributeType.TEXT,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.REDIRECT_URL: AttributeType.URL,
        ObjectRelation.SHORTENED_URL: AttributeType.URL,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.SIGMA: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.CONTEXT: AttributeType.TEXT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.SIGMA: AttributeType.SIGMA,
        ObjectRelation.SIGMA_RULE_NAME: AttributeType.TEXT,
    },
    ObjectType.SIGMF_ARCHIVE: {ObjectRelation.SIGMF_ARCHIVE: AttributeType.ATTACHMENT},
    ObjectType.SIGMF_EXPANDED_RECORDING: {
        ObjectRelation.AUTHOR: AttributeType.TEXT,
        ObjectRelation.COLLECTION: AttributeType.TEXT,
        ObjectRelation.DATA_DOI: AttributeType.TEXT,
        ObjectRelation.DATASET: AttributeType.TEXT,
        ObjectRelation.DATATYPE: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FFT_PLOT: AttributeType.ATTACHMENT,
        ObjectRelation.GEOLOCATION_ALT: AttributeType.TEXT,
        ObjectRelation.GEOLOCATION_LAT: AttributeType.TEXT,
        ObjectRelation.GEOLOCATION_LONG: AttributeType.TEXT,
        ObjectRelation.HW: AttributeType.TEXT,
        ObjectRelation.IQ_SAMPLE: AttributeType.ATTACHMENT,
        ObjectRelation.LICENSE: AttributeType.TEXT,
        ObjectRelation.META_DOI: AttributeType.TEXT,
        ObjectRelation.METADATA_ONLY: AttributeType.BOOLEAN,
        ObjectRelation.NUM_CHANNELS: AttributeType.COUNTER,
        ObjectRelation.OFFSET: AttributeType.INTEGER,
        ObjectRelation.RECORDER: AttributeType.TEXT,
        ObjectRelation.SAMPLE_RATE: AttributeType.FLOAT,
        ObjectRelation.SHA512: AttributeType.SHA512,
        ObjectRelation.TRAILING_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.VERSION: AttributeType.TEXT,
        ObjectRelation.WATERFALL_PLOT: AttributeType.ATTACHMENT,
    },
    ObjectType.SIGMF_RECORDING: {
        ObjectRelation.SIGMF_DATA: AttributeType.ATTACHMENT,
        ObjectRelation.SIGMF_META: AttributeType.ATTACHMENT,
    },
    ObjectType.SOCIAL_MEDIA_GROUP: {
        ObjectRelation.ADMINISTRATOR: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.GROUP_ALIAS: AttributeType.TEXT,
        ObjectRelation.GROUP_NAME: AttributeType.TEXT,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PERSON_NAME: AttributeType.TEXT,
        ObjectRelation.PLATFORM: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.SOFTWARE: {
        ObjectRelation.CPE: AttributeType.CPE,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SWID: AttributeType.TEXT,
        ObjectRelation.VENDOR: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.SPAMBEE_REPORT: {
        ObjectRelation.FEEDBACK_REQUESTED: AttributeType.BOOLEAN,
        ObjectRelation.FEEDBACK_SENT: AttributeType.BOOLEAN,
        ObjectRelation.FEEDBACK_TIME: AttributeType.DATETIME,
        ObjectRelation.PRIVACY: AttributeType.BOOLEAN,
        ObjectRelation.REPORT_STATUS: AttributeType.TEXT,
        ObjectRelation.REPORT_UID: AttributeType.TEXT,
    },
    ObjectType.SPEARPHISHING_ATTACHMENT: {
        ObjectRelation.ARTIFACT_DROPPED_MD5: AttributeType.MD5,
        ObjectRelation.ARTIFACT_DROPPED_NAME: AttributeType.FILENAME,
        ObjectRelation.ARTIFACT_DROPPED_SHA1: AttributeType.SHA1,
        ObjectRelation.ARTIFACT_DROPPED_SHA256: AttributeType.SHA256,
        ObjectRelation.ATTACHMENT_MD5: AttributeType.MD5,
        ObjectRelation.ATTACHMENT_NAME: AttributeType.FILENAME,
        ObjectRelation.ATTACHMENT_SHA1: AttributeType.SHA1,
        ObjectRelation.ATTACHMENT_SHA256: AttributeType.SHA256,
        ObjectRelation.C2_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.C2_IP: AttributeType.IP_DST,
        ObjectRelation.C2_URL: AttributeType.URL,
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.EMAIL_SENDER: AttributeType.EMAIL_SRC,
        ObjectRelation.MALICIOUS_URL: AttributeType.URL,
        ObjectRelation.RESEARCH_LINKS: AttributeType.LINK,
        ObjectRelation.SENDER_IP: AttributeType.IP_SRC,
        ObjectRelation.SUBJECT: AttributeType.EMAIL_SUBJECT,
        ObjectRelation.SUPPORTING_EVIDENCE: AttributeType.TEXT,
    },
    ObjectType.SPEARPHISHING_LINK: {
        ObjectRelation.DATE: AttributeType.TEXT,
        ObjectRelation.EMAIL_SENDER: AttributeType.EMAIL_SRC,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.REDIRECT_URL: AttributeType.URL,
        ObjectRelation.RESEARCH_LINKS: AttributeType.LINK,
        ObjectRelation.SENDER_IP: AttributeType.IP_SRC,
        ObjectRelation.SUBJECT: AttributeType.EMAIL_SUBJECT,
        ObjectRelation.SUPPORTING_EVIDENCE: AttributeType.TEXT,
    },
    ObjectType.SPLUNK: {
        ObjectRelation.DESCRIPTION_1: AttributeType.COMMENT,
        ObjectRelation.DRILL_DOWN: AttributeType.TEXT,
        ObjectRelation.EARLIEST: AttributeType.TEXT,
        ObjectRelation.LATEST: AttributeType.TEXT,
        ObjectRelation.RESPONSE_ACTION: AttributeType.TEXT,
        ObjectRelation.SCHEDULE: AttributeType.OTHER,
        ObjectRelation.SEARCH: AttributeType.TEXT,
    },
    ObjectType.SS7_ATTACK: {
        ObjectRelation.CATEGORY: AttributeType.TEXT,
        ObjectRelation.GTASSIGNEE: AttributeType.TEXT,
        ObjectRelation.GTLESSEE: AttributeType.TEXT,
        ObjectRelation.GTLESSOR: AttributeType.TEXT,
        ObjectRelation.GTSUBLESSEE: AttributeType.TEXT,
        ObjectRelation.MAPAPPLICATIONCONTEXT: AttributeType.TEXT,
        ObjectRelation.MAPGMLC: AttributeType.TEXT,
        ObjectRelation.MAPGSMSCFGT: AttributeType.TEXT,
        ObjectRelation.MAPIMSI: AttributeType.TEXT,
        ObjectRelation.MAPMSCGT: AttributeType.TEXT,
        ObjectRelation.MAPMSISDN: AttributeType.TEXT,
        ObjectRelation.MAPOPCODE: AttributeType.TEXT,
        ObjectRelation.MAPSMSTP_DCS: AttributeType.TEXT,
        ObjectRelation.MAPSMSTP_OA: AttributeType.TEXT,
        ObjectRelation.MAPSMSTP_PID: AttributeType.TEXT,
        ObjectRelation.MAPSMSTEXT: AttributeType.TEXT,
        ObjectRelation.MAPSMSTYPENUMBER: AttributeType.TEXT,
        ObjectRelation.MAPSMSCGT: AttributeType.TEXT,
        ObjectRelation.MAPUSSDCODING: AttributeType.TEXT,
        ObjectRelation.MAPUSSDCONTENT: AttributeType.TEXT,
        ObjectRelation.MAPVERSION: AttributeType.TEXT,
        ObjectRelation.MAPVLRGT: AttributeType.TEXT,
        ObjectRelation.SCCPCDGT: AttributeType.TEXT,
        ObjectRelation.SCCPCDGT_COUNTRY: AttributeType.TEXT,
        ObjectRelation.SCCPCDGT_COUNTRYISO2: AttributeType.TEXT,
        ObjectRelation.SCCPCDGT_OPERATORNAME: AttributeType.TEXT,
        ObjectRelation.SCCPCDGT_TADIG: AttributeType.TEXT,
        ObjectRelation.SCCPCDPC: AttributeType.TEXT,
        ObjectRelation.SCCPCDSSN: AttributeType.TEXT,
        ObjectRelation.SCCPCGGT: AttributeType.TEXT,
        ObjectRelation.SCCPCGGT_COUNTRY: AttributeType.TEXT,
        ObjectRelation.SCCPCGGT_COUNTRYISO2: AttributeType.TEXT,
        ObjectRelation.SCCPCGGT_OPERATORNAME: AttributeType.TEXT,
        ObjectRelation.SCCPCGGT_TADIG: AttributeType.TEXT,
        ObjectRelation.SCCPCGPC: AttributeType.TEXT,
        ObjectRelation.SCCPCGSSN: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.SSH_AUTHORIZED_KEYS: {
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.FULL_LINE: AttributeType.TEXT,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.KEY: AttributeType.TEXT,
        ObjectRelation.KEY_ID: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.STAIRWELL: {
        ObjectRelation.ENTROPY: AttributeType.FLOAT,
        ObjectRelation.ENVIRONMENT: AttributeType.COMMENT,
        ObjectRelation.IMPHASH: AttributeType.IMPHASH,
        ObjectRelation.MAGIC: AttributeType.COMMENT,
        ObjectRelation.MALEVAL_PROBABILITY: AttributeType.COMMENT,
        ObjectRelation.MALEVAL_SEVERITY: AttributeType.COMMENT,
        ObjectRelation.MD5_1: AttributeType.MD5,
        ObjectRelation.MIME_TYPE: AttributeType.MIME_TYPE,
        ObjectRelation.SHA1_1: AttributeType.SHA1,
        ObjectRelation.SHA256_1: AttributeType.SHA256,
        ObjectRelation.SIZE_IN_BYTES: AttributeType.SIZE_IN_BYTES,
        ObjectRelation.STAIRWELL_FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TLSH_1: AttributeType.TLSH,
        ObjectRelation.YARA_RULE_MATCH: AttributeType.COMMENT,
    },
    ObjectType.STIX2_PATTERN: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.STIX2_PATTERN: AttributeType.STIX2_PATTERN,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.STOCK: {
        ObjectRelation.BLOOMBERG_EXCHANGE_CODE: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.CURRENCY: AttributeType.TEXT,
        ObjectRelation.EXCHANGE: AttributeType.TEXT,
        ObjectRelation.HIGH_PRICE: AttributeType.TEXT,
        ObjectRelation.ISO_MIC: AttributeType.TEXT,
        ObjectRelation.LOW_PRICE: AttributeType.TEXT,
        ObjectRelation.SYMBOL: AttributeType.TEXT,
    },
    ObjectType.SUBMARINE: {
        ObjectRelation.ACTIVE: AttributeType.COUNTER,
        ObjectRelation.ARMAMENT: AttributeType.TEXT,
        ObjectRelation.BEAM: AttributeType.FLOAT,
        ObjectRelation.BUILDERS: AttributeType.TEXT,
        ObjectRelation.CANCELLED: AttributeType.COUNTER,
        ObjectRelation.CLASS: AttributeType.TEXT,
        ObjectRelation.COMPLEMENT: AttributeType.INTEGER,
        ObjectRelation.COMPLETED: AttributeType.COUNTER,
        ObjectRelation.DISPLACEMENT: AttributeType.INTEGER,
        ObjectRelation.DRAUGHT: AttributeType.FLOAT,
        ObjectRelation.ENDURANCE: AttributeType.COUNTER,
        ObjectRelation.IN_SERVICE_FROM: AttributeType.INTEGER,
        ObjectRelation.IN_SERVICE_UNTIL: AttributeType.INTEGER,
        ObjectRelation.LENGTH: AttributeType.FLOAT,
        ObjectRelation.OPERATOR: AttributeType.TEXT,
        ObjectRelation.PLANNED: AttributeType.COUNTER,
        ObjectRelation.PREDECESSOR: AttributeType.TEXT,
        ObjectRelation.PROPULSION: AttributeType.TEXT,
        ObjectRelation.RETIRED: AttributeType.COUNTER,
        ObjectRelation.SPEED_SUBMERGED: AttributeType.FLOAT,
        ObjectRelation.SPEED_SURFACED: AttributeType.FLOAT,
        ObjectRelation.SUCCESSOR: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.SURICATA: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.REF: AttributeType.LINK,
        ObjectRelation.SURICATA: AttributeType.SNORT,
        ObjectRelation.VERSION: AttributeType.TEXT,
    },
    ObjectType.TARGET_SYSTEM: {
        ObjectRelation.TARGETED_IP_OF_SYSTEM: AttributeType.IP_SRC,
        ObjectRelation.TARGETED_MACHINE: AttributeType.TARGET_MACHINE,
        ObjectRelation.TIMESTAMP_SEEN: AttributeType.DATETIME,
    },
    ObjectType.TASK: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.ERROR: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OUTCOME: AttributeType.TEXT,
        ObjectRelation.PRIORITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.TASK_TYPE: AttributeType.TEXT,
    },
    ObjectType.TATTOO: {
        ObjectRelation.TATTOO_BODY_PART: AttributeType.TEXT,
        ObjectRelation.TATTOO_COLOR: AttributeType.TEXT,
        ObjectRelation.TATTOO_DESCRIPTION: AttributeType.TEXT,
        ObjectRelation.TATTOO_PICTURE: AttributeType.ATTACHMENT,
        ObjectRelation.TATTOO_SIZE: AttributeType.TEXT,
        ObjectRelation.TATTOO_STYLE: AttributeType.TEXT,
    },
    ObjectType.TELEGRAM_ACCOUNT: {
        ObjectRelation.FIRST_NAME_1: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LAST_NAME_1: AttributeType.TEXT,
        ObjectRelation.PHONE: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
        ObjectRelation.VERIFIED: AttributeType.TEXT,
    },
    ObjectType.TELEGRAM_BOT: {
        ObjectRelation.CHAT_ID: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.TOKEN: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.TEMPORAL_EVENT: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.THAICERT_GROUP_CARDS: {
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.MORE_INFORMATIONS: AttributeType.TEXT,
        ObjectRelation.MOTIVATION: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.OBSERVED: AttributeType.TEXT,
        ObjectRelation.SPONSOR: AttributeType.TEXT,
        ObjectRelation.TOOLS_USED: AttributeType.TEXT,
    },
    ObjectType.THREATGRID_REPORT: {
        ObjectRelation.ANALYSIS_SUBMITTED_AT: AttributeType.TEXT,
        ObjectRelation.HEURISTIC_RAW_SCORE: AttributeType.TEXT,
        ObjectRelation.HEURISTIC_SCORE: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.IOCS: AttributeType.TEXT,
        ObjectRelation.ORIGINAL_FILENAME_1: AttributeType.TEXT,
        ObjectRelation.PERMALINK: AttributeType.TEXT,
        ObjectRelation.THREAT_SCORE_1: AttributeType.TEXT,
    },
    ObjectType.TIMECODE: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_MARKER_TIMECODE: AttributeType.TEXT,
        ObjectRelation.END_TIMECODE: AttributeType.TEXT,
        ObjectRelation.RECORDING_DATE: AttributeType.DATETIME,
        ObjectRelation.START_MARKER_TIMECODE: AttributeType.TEXT,
        ObjectRelation.START_TIMECODE: AttributeType.TEXT,
    },
    ObjectType.TIMESKETCH_TIMELINE: {
        ObjectRelation.DATETIME: AttributeType.DATETIME,
        ObjectRelation.MESSAGE: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_1: AttributeType.TEXT,
        ObjectRelation.TIMESTAMP_DESC: AttributeType.TEXT,
    },
    ObjectType.TIMESKETCH_MESSAGE: {
        ObjectRelation.DATETIME: AttributeType.DATETIME,
        ObjectRelation.MESSAGE: AttributeType.TEXT,
    },
    ObjectType.TIMESTAMP: {
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PRECISION: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.TOR_HIDDENSERVICE: {
        ObjectRelation.ADDRESS: AttributeType.ONION_ADDRESS,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.TOR_NODE: {
        ObjectRelation.ADDRESS: AttributeType.IP_SRC,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DOCUMENT: AttributeType.TEXT,
        ObjectRelation.FINGERPRINT: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.FLAGS: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.NICKNAME: AttributeType.TEXT,
        ObjectRelation.PUBLISHED: AttributeType.DATETIME,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.VERSION: AttributeType.TEXT,
        ObjectRelation.VERSION_LINE: AttributeType.TEXT,
    },
    ObjectType.TRACEABILITY_IMPACT: {
        ObjectRelation.CRITICALITY: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.END_TIME: AttributeType.DATETIME,
        ObjectRelation.END_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.RECOVERABILITY: AttributeType.TEXT,
        ObjectRelation.START_TIME_2: AttributeType.DATETIME,
        ObjectRelation.START_TIME_FIDELITY: AttributeType.TEXT,
        ObjectRelation.TRACEABILITY_IMPACT: AttributeType.TEXT,
    },
    ObjectType.TRACKING_ID: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.HOSTNAME: AttributeType.HOSTNAME,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.TRACKER: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.TRANSACTION: {
        ObjectRelation.AMOUNT: AttributeType.TEXT,
        ObjectRelation.AUTHORIZED: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.DATETIME,
        ObjectRelation.DATE_POSTING: AttributeType.DATETIME,
        ObjectRelation.FROM_COUNTRY: AttributeType.TEXT,
        ObjectRelation.FROM_FUNDS_CODE: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.TELLER: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TO_COUNTRY: AttributeType.TEXT,
        ObjectRelation.TO_FUNDS_CODE: AttributeType.TEXT,
        ObjectRelation.TRANSACTION_NUMBER: AttributeType.TEXT,
        ObjectRelation.TRANSMODE_CODE: AttributeType.TEXT,
        ObjectRelation.TRANSMODE_COMMENT: AttributeType.TEXT,
    },
    ObjectType.TRANSLATION: {
        ObjectRelation.ORIGINAL_LANGUAGE: AttributeType.TEXT,
        ObjectRelation.ORIGINAL_TEXT: AttributeType.TEXT,
        ObjectRelation.TRANSLATED_TEXT: AttributeType.TEXT,
        ObjectRelation.TRANSLATION_LANGUAGE: AttributeType.TEXT,
        ObjectRelation.TRANSLATION_SERVICE: AttributeType.TEXT,
        ObjectRelation.TRANSLATION_TYPE: AttributeType.TEXT,
    },
    ObjectType.TRANSPORT_TICKET: {
        ObjectRelation.CLASS: AttributeType.TEXT,
        ObjectRelation.COMPANY: AttributeType.TEXT,
        ObjectRelation.COPY: AttributeType.ATTACHMENT,
        ObjectRelation.DATE_OF_ARRIVAL: AttributeType.DATETIME,
        ObjectRelation.DATE_OF_DEPARTURE: AttributeType.DATETIME,
        ObjectRelation.DATE_OF_PURCHASE: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DESTINATION: AttributeType.TEXT,
        ObjectRelation.ORIGIN: AttributeType.TEXT,
        ObjectRelation.TICKET_NUMBER: AttributeType.TEXT,
        ObjectRelation.TYPE_OF_TICKET: AttributeType.TEXT,
        ObjectRelation.TYPE_OF_TRANSPORT: AttributeType.TEXT,
    },
    ObjectType.TRUSTAR_REPORT: {
        ObjectRelation.BITCOIN_ADDRESS: AttributeType.BTC,
        ObjectRelation.CIDR_BLOCK: AttributeType.IP_SRC,
        ObjectRelation.COMMENTS: AttributeType.TEXT,
        ObjectRelation.CVE: AttributeType.VULNERABILITY,
        ObjectRelation.EMAIL_ADDRESS: AttributeType.EMAIL_SRC,
        ObjectRelation.INDICATOR_SUMMARY: AttributeType.TEXT,
        ObjectRelation.IP: AttributeType.IP_DST,
        ObjectRelation.MALWARE: AttributeType.MALWARE_TYPE,
        ObjectRelation.MD5: AttributeType.MD5,
        ObjectRelation.REGISTRY_KEY: AttributeType.REGKEY,
        ObjectRelation.REPORT_LINK: AttributeType.LINK,
        ObjectRelation.SHA1: AttributeType.SHA1,
        ObjectRelation.SHA256: AttributeType.SHA256,
        ObjectRelation.SOFTWARE: AttributeType.FILENAME,
        ObjectRelation.THREAT_ACTOR: AttributeType.THREAT_ACTOR,
        ObjectRelation.URL: AttributeType.URL,
    },
    ObjectType.TSK_CHATS: {
        ObjectRelation.SOURCE: AttributeType.TEXT,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.APP_USED: AttributeType.TEXT,
        ObjectRelation.ATTACHMENTS: AttributeType.LINK,
        ObjectRelation.DATETIME_RECEIVED: AttributeType.DATETIME,
        ObjectRelation.DATETIME_SENT: AttributeType.DATETIME,
        ObjectRelation.DESTINATION: AttributeType.TEXT,
        ObjectRelation.MESSAGE: AttributeType.TEXT,
        ObjectRelation.MESSAGE_TYPE: AttributeType.TEXT,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
    },
    ObjectType.TSK_WEB_BOOKMARK: {
        ObjectRelation.URL: AttributeType.LINK,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.BROWSER: AttributeType.TEXT,
        ObjectRelation.DATETIME_BOOKMARKED: AttributeType.DATETIME,
        ObjectRelation.DOMAIN_IP: AttributeType.IP_SRC,
        ObjectRelation.DOMAIN_NAME: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.TSK_WEB_COOKIE: {
        ObjectRelation.URL: AttributeType.LINK,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.BROWSER: AttributeType.TEXT,
        ObjectRelation.DATETIME_CREATED: AttributeType.DATETIME,
        ObjectRelation.DOMAIN_IP: AttributeType.IP_SRC,
        ObjectRelation.DOMAIN_NAME: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.VALUE: AttributeType.TEXT,
    },
    ObjectType.TSK_WEB_DOWNLOADS: {
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DATETIME_ACCESSED: AttributeType.DATETIME,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PATH_DOWNLOADEDTO: AttributeType.TEXT,
        ObjectRelation.PATHID: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.TSK_WEB_HISTORY: {
        ObjectRelation.URL: AttributeType.LINK,
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.BROWSER: AttributeType.TEXT,
        ObjectRelation.DATETIME_ACCESSED: AttributeType.DATETIME,
        ObjectRelation.DOMAIN_IP: AttributeType.IP_SRC,
        ObjectRelation.DOMAIN_NAME: AttributeType.TEXT,
        ObjectRelation.REFERRER: AttributeType.TEXT,
        ObjectRelation.TITLE: AttributeType.TEXT,
    },
    ObjectType.TSK_WEB_SEARCH_QUERY: {
        ObjectRelation.ADDITIONAL_COMMENTS: AttributeType.TEXT,
        ObjectRelation.BROWSER: AttributeType.TEXT,
        ObjectRelation.DATETIME_SEARCHED: AttributeType.DATETIME,
        ObjectRelation.DOMAIN: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.TWITTER_ACCOUNT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.BIO: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISPLAYED_NAME: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.FOLLOWERS: AttributeType.TEXT,
        ObjectRelation.FOLLOWING: AttributeType.TEXT,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.JOINED_DATE: AttributeType.DATETIME,
        ObjectRelation.LIKES: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.LISTED: AttributeType.TEXT,
        ObjectRelation.LOCATION: AttributeType.TEXT,
        ObjectRelation.MEDIA: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.PRIVATE: AttributeType.TEXT,
        ObjectRelation.PROFILE_BANNER: AttributeType.ATTACHMENT,
        ObjectRelation.PROFILE_BANNER_URL: AttributeType.URL,
        ObjectRelation.PROFILE_IMAGE: AttributeType.ATTACHMENT,
        ObjectRelation.PROFILE_IMAGE_URL: AttributeType.URL,
        ObjectRelation.TWEETS: AttributeType.TEXT,
        ObjectRelation.TWITTER_FOLLOWERS: AttributeType.TEXT,
        ObjectRelation.TWITTER_FOLLOWING: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.VERIFIED: AttributeType.TEXT,
    },
    ObjectType.TWITTER_LIST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MEMBER_COUNT: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.SUBSCRIBER_COUNT: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_ID: AttributeType.TEXT,
        ObjectRelation.USER_NAME: AttributeType.TEXT,
    },
    ObjectType.TWITTER_POST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CREATED_AT: AttributeType.DATETIME,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.FAVORITE_COUNT: AttributeType.TEXT,
        ObjectRelation.GEO: AttributeType.TEXT,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_STATUS_ID: AttributeType.TEXT,
        ObjectRelation.IN_REPLY_TO_USER_ID: AttributeType.TEXT,
        ObjectRelation.LANGUAGE: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.MEDIA: AttributeType.ATTACHMENT,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.POSSIBLY_SENSITIVE: AttributeType.TEXT,
        ObjectRelation.POSSIBLY_SENSITIVE_APPEALABLE: AttributeType.TEXT,
        ObjectRelation.POST: AttributeType.TEXT,
        ObjectRelation.POST_ID: AttributeType.TEXT,
        ObjectRelation.REMOVAL_DATE: AttributeType.DATETIME,
        ObjectRelation.RETWEET_COUNT: AttributeType.TEXT,
        ObjectRelation.SOURCE_1: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_ID: AttributeType.TEXT,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
    },
    ObjectType.TYPOSQUATTING_FINDER: {
        ObjectRelation.RESEARCH_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.VARIATIONS_FOUND_NUMBER: AttributeType.TEXT,
        ObjectRelation.VARIATIONS_NUMBER: AttributeType.TEXT,
    },
    ObjectType.TYPOSQUATTING_FINDER_RESULT: {
        ObjectRelation.A_RECORD: AttributeType.IP_DST,
        ObjectRelation.AAAA_RECORD: AttributeType.IP_DST,
        ObjectRelation.MX_RECORD: AttributeType.DOMAIN,
        ObjectRelation.NS_RECORD: AttributeType.DOMAIN,
        ObjectRelation.QUERIED_DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.RATIO_SIMILARITY: AttributeType.TEXT,
        ObjectRelation.WEBSITE_RESSOURCE_DIFF: AttributeType.TEXT,
        ObjectRelation.WEBSITE_SIMILARITY: AttributeType.TEXT,
        ObjectRelation.WEBSITE_TITLE: AttributeType.TEXT,
    },
    ObjectType.URL: {
        ObjectRelation.CREDENTIAL: AttributeType.TEXT,
        ObjectRelation.DOM_HASH: AttributeType.DOM_HASH,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.DOMAIN_WITHOUT_TLD: AttributeType.TEXT,
        ObjectRelation.FIRST_SEEN: AttributeType.DATETIME,
        ObjectRelation.FRAGMENT: AttributeType.TEXT,
        ObjectRelation.HOST: AttributeType.HOSTNAME,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.LAST_SEEN: AttributeType.DATETIME,
        ObjectRelation.PORT: AttributeType.PORT,
        ObjectRelation.QUERY_STRING: AttributeType.TEXT,
        ObjectRelation.RESOURCE_PATH: AttributeType.TEXT,
        ObjectRelation.SCHEME: AttributeType.TEXT,
        ObjectRelation.SUBDOMAIN: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.TLD: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.USER_ACCOUNT: {
        ObjectRelation.ACCOUNT_TYPE: AttributeType.TEXT,
        ObjectRelation.CAN_ESCALATE_PRIVS: AttributeType.BOOLEAN,
        ObjectRelation.CREATED: AttributeType.DATETIME,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DISABLED: AttributeType.BOOLEAN,
        ObjectRelation.DISPLAY_NAME: AttributeType.TEXT,
        ObjectRelation.EMAIL: AttributeType.EMAIL,
        ObjectRelation.EXPIRES: AttributeType.DATETIME,
        ObjectRelation.FIRST_LOGIN: AttributeType.DATETIME,
        ObjectRelation.GROUP: AttributeType.TEXT,
        ObjectRelation.GROUP_ID: AttributeType.TEXT,
        ObjectRelation.HOME_DIR: AttributeType.TEXT,
        ObjectRelation.IS_SERVICE_ACCOUNT: AttributeType.BOOLEAN,
        ObjectRelation.LAST_LOGIN: AttributeType.DATETIME,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PASSWORD: AttributeType.TEXT,
        ObjectRelation.PASSWORD_LAST_CHANGED: AttributeType.DATETIME,
        ObjectRelation.PRIVILEGED: AttributeType.BOOLEAN,
        ObjectRelation.SHELL_1: AttributeType.TEXT,
        ObjectRelation.USER_AVATAR: AttributeType.ATTACHMENT,
        ObjectRelation.USER_ID: AttributeType.TEXT,
        ObjectRelation.USERNAME_1: AttributeType.TEXT,
    },
    ObjectType.USER_ACTION: {
        ObjectRelation.ACTION: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
    },
    ObjectType.VEHICLE: {
        ObjectRelation.DATE_FIRST_REGISTRATION: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DYNO_POWER: AttributeType.TEXT,
        ObjectRelation.EXTERIOR_COLOR: AttributeType.TEXT,
        ObjectRelation.GEARBOX: AttributeType.TEXT,
        ObjectRelation.IMAGE: AttributeType.ATTACHMENT,
        ObjectRelation.IMAGE_URL: AttributeType.TEXT,
        ObjectRelation.INDICATIVE_VALUE: AttributeType.TEXT,
        ObjectRelation.INTERIOR_COLOR: AttributeType.TEXT,
        ObjectRelation.LICENSE_PLATE_NUMBER: AttributeType.TEXT,
        ObjectRelation.MAKE: AttributeType.TEXT,
        ObjectRelation.MODEL: AttributeType.TEXT,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
        ObjectRelation.VIN: AttributeType.TEXT,
    },
    ObjectType.VICTIM: {
        ObjectRelation.CLASSIFICATION: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.EMAIL: AttributeType.TARGET_EMAIL,
        ObjectRelation.EXTERNAL: AttributeType.TARGET_EXTERNAL,
        ObjectRelation.IP_ADDRESS: AttributeType.IP_DST,
        ObjectRelation.NAME: AttributeType.TARGET_ORG,
        ObjectRelation.NODE: AttributeType.TARGET_MACHINE,
        ObjectRelation.REFERENCE: AttributeType.TEXT,
        ObjectRelation.REGIONS: AttributeType.TARGET_LOCATION,
        ObjectRelation.ROLES: AttributeType.TEXT,
        ObjectRelation.SECTORS: AttributeType.TEXT,
        ObjectRelation.USER_1: AttributeType.TARGET_USER,
    },
    ObjectType.VIRUSTOTAL_GRAPH: {
        ObjectRelation.ACCESS: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.PERMALINK: AttributeType.LINK,
        ObjectRelation.SCREENSHOT: AttributeType.ATTACHMENT,
    },
    ObjectType.VIRUSTOTAL_REPORT: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.COMMUNITY_SCORE: AttributeType.TEXT,
        ObjectRelation.DETECTION_RATIO: AttributeType.TEXT,
        ObjectRelation.FIRST_SUBMISSION: AttributeType.DATETIME,
        ObjectRelation.LAST_SUBMISSION: AttributeType.DATETIME,
        ObjectRelation.PERMALINK: AttributeType.LINK,
    },
    ObjectType.VIRUSTOTAL_SUBMISSION: {
        ObjectRelation.CITY: AttributeType.TEXT,
        ObjectRelation.COUNTRY: AttributeType.TEXT,
        ObjectRelation.DATE: AttributeType.DATETIME,
        ObjectRelation.FILENAME_2: AttributeType.FILENAME,
        ObjectRelation.INTERFACE: AttributeType.TEXT,
        ObjectRelation.SUBMITTER_ID: AttributeType.TEXT,
    },
    ObjectType.VULNERABILITY: {
        ObjectRelation.CREATED: AttributeType.DATETIME,
        ObjectRelation.CREDIT: AttributeType.TEXT,
        ObjectRelation.CVSS_SCORE: AttributeType.FLOAT,
        ObjectRelation.CVSS_STRING: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.VULNERABILITY,
        ObjectRelation.MODIFIED: AttributeType.DATETIME,
        ObjectRelation.PUBLISHED: AttributeType.DATETIME,
        ObjectRelation.REFERENCES: AttributeType.LINK,
        ObjectRelation.STATE: AttributeType.TEXT,
        ObjectRelation.SUMMARY: AttributeType.TEXT,
        ObjectRelation.VULNERABLE_CONFIGURATION: AttributeType.CPE,
    },
    ObjectType.WEAKNESS: {
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.ID: AttributeType.WEAKNESS,
        ObjectRelation.NAME: AttributeType.TEXT,
        ObjectRelation.STATUS: AttributeType.TEXT,
        ObjectRelation.WEAKNESS_ABS: AttributeType.TEXT,
    },
    ObjectType.WHOIS: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.CREATION_DATE: AttributeType.DATETIME,
        ObjectRelation.DOMAIN: AttributeType.DOMAIN,
        ObjectRelation.EXPIRATION_DATE: AttributeType.DATETIME,
        ObjectRelation.IP_ADDRESS: AttributeType.IP_SRC,
        ObjectRelation.MODIFICATION_DATE: AttributeType.DATETIME,
        ObjectRelation.NAMESERVER: AttributeType.HOSTNAME,
        ObjectRelation.REGISTRANT_EMAIL: AttributeType.WHOIS_REGISTRANT_EMAIL,
        ObjectRelation.REGISTRANT_NAME: AttributeType.WHOIS_REGISTRANT_NAME,
        ObjectRelation.REGISTRANT_ORG: AttributeType.WHOIS_REGISTRANT_ORG,
        ObjectRelation.REGISTRANT_PHONE: AttributeType.WHOIS_REGISTRANT_PHONE,
        ObjectRelation.REGISTRAR: AttributeType.WHOIS_REGISTRAR,
        ObjectRelation.TEXT: AttributeType.TEXT,
    },
    ObjectType.WINDOWS_SERVICE: {
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DISPLAY: AttributeType.WINDOWS_SERVICE_DISPLAYNAME,
        ObjectRelation.GROUP: AttributeType.TEXT,
        ObjectRelation.IMAGE_PATH: AttributeType.TEXT,
        ObjectRelation.NAME: AttributeType.WINDOWS_SERVICE_NAME,
        ObjectRelation.START: AttributeType.TEXT,
        ObjectRelation.TYPE: AttributeType.TEXT,
    },
    ObjectType.X_HEADER: {ObjectRelation.X_HEADER_NAME: AttributeType.TEXT, ObjectRelation.X_VALUE: AttributeType.TEXT},
    ObjectType.X509: {
        ObjectRelation.DNS_NAMES: AttributeType.HOSTNAME,
        ObjectRelation.EMAIL: AttributeType.EMAIL_DST,
        ObjectRelation.IP_1: AttributeType.IP_DST,
        ObjectRelation.IS_CA: AttributeType.BOOLEAN,
        ObjectRelation.ISSUER: AttributeType.TEXT,
        ObjectRelation.PEM: AttributeType.TEXT,
        ObjectRelation.PUBKEY_INFO_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.PUBKEY_INFO_EXPONENT: AttributeType.TEXT,
        ObjectRelation.PUBKEY_INFO_MODULUS: AttributeType.TEXT,
        ObjectRelation.PUBKEY_INFO_SIZE: AttributeType.TEXT,
        ObjectRelation.RAW_BASE64: AttributeType.TEXT,
        ObjectRelation.RID: AttributeType.TEXT,
        ObjectRelation.SELF_SIGNED: AttributeType.BOOLEAN,
        ObjectRelation.SERIAL_NUMBER: AttributeType.TEXT,
        ObjectRelation.SIGNATURE_ALGORITHM: AttributeType.TEXT,
        ObjectRelation.SUBJECT: AttributeType.TEXT,
        ObjectRelation.TEXT: AttributeType.TEXT,
        ObjectRelation.URI: AttributeType.URI,
        ObjectRelation.VALIDITY_NOT_AFTER: AttributeType.DATETIME,
        ObjectRelation.VALIDITY_NOT_BEFORE: AttributeType.DATETIME,
        ObjectRelation.VERSION: AttributeType.TEXT,
        ObjectRelation.X509_FINGERPRINT_MD5: AttributeType.X509_FINGERPRINT_MD5,
        ObjectRelation.X509_FINGERPRINT_SHA1: AttributeType.X509_FINGERPRINT_SHA1,
        ObjectRelation.X509_FINGERPRINT_SHA256: AttributeType.X509_FINGERPRINT_SHA256,
    },
    ObjectType.YABIN: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.VERSION: AttributeType.COMMENT,
        ObjectRelation.WHITELIST: AttributeType.COMMENT,
        ObjectRelation.YARA: AttributeType.YARA,
        ObjectRelation.YARA_HUNT: AttributeType.YARA,
    },
    ObjectType.YARA: {
        ObjectRelation.COMMENT: AttributeType.COMMENT,
        ObjectRelation.CONTEXT: AttributeType.TEXT,
        ObjectRelation.REFERENCE: AttributeType.LINK,
        ObjectRelation.VERSION: AttributeType.TEXT,
        ObjectRelation.YARA: AttributeType.YARA,
        ObjectRelation.YARA_RULE_NAME: AttributeType.TEXT,
    },
    ObjectType.YOUTUBE_CHANNEL: {
        ObjectRelation.ABOUT: AttributeType.TEXT,
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CHANNEL_AVATAR: AttributeType.ATTACHMENT,
        ObjectRelation.CHANNEL_BANNER: AttributeType.ATTACHMENT,
        ObjectRelation.CHANNEL_ID: AttributeType.TEXT,
        ObjectRelation.CHANNEL_NAME: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.FEATURED_CHANNEL: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
    },
    ObjectType.YOUTUBE_COMMENT: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CHANNEL_NAME: AttributeType.TEXT,
        ObjectRelation.COMMENT: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USER_ACCOUNT: AttributeType.TEXT,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
        ObjectRelation.VIDEO_TITLE: AttributeType.TEXT,
    },
    ObjectType.YOUTUBE_PLAYLIST: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.PLAYLIST_ID: AttributeType.TEXT,
        ObjectRelation.PLAYLIST_NAME: AttributeType.TEXT,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.VIDEO_LINK: AttributeType.LINK,
    },
    ObjectType.YOUTUBE_VIDEO: {
        ObjectRelation.ARCHIVE: AttributeType.LINK,
        ObjectRelation.ATTACHMENT: AttributeType.ATTACHMENT,
        ObjectRelation.CHANNEL_NAME: AttributeType.TEXT,
        ObjectRelation.CREATOR: AttributeType.TEXT,
        ObjectRelation.DESCRIPTION_1: AttributeType.TEXT,
        ObjectRelation.EMBEDDED_LINK: AttributeType.URL,
        ObjectRelation.EMBEDDED_SAFE_LINK: AttributeType.LINK,
        ObjectRelation.HASHTAG: AttributeType.TEXT,
        ObjectRelation.LINK: AttributeType.LINK,
        ObjectRelation.URL_1: AttributeType.URL,
        ObjectRelation.USERNAME_QUOTED: AttributeType.TEXT,
        ObjectRelation.VIDEO_TITLE: AttributeType.TEXT,
        ObjectRelation.VIDEO_TRANSCRIPT: AttributeType.TEXT,
    },
}
