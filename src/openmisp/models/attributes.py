# This mapping is automatically generated from MISP data

from enum import Enum
from typing import Dict, Set


class AttributeCategory(Enum):
    ANTIVIRUS_DETECTION = "Antivirus detection"
    ARTIFACTS_DROPPED = "Artifacts dropped"
    ATTRIBUTION = "Attribution"
    EXTERNAL_ANALYSIS = "External analysis"
    FINANCIAL_FRAUD = "Financial fraud"
    INTERNAL_REFERENCE = "Internal reference"
    NETWORK_ACTIVITY = "Network activity"
    OTHER = "Other"
    PAYLOAD_DELIVERY = "Payload delivery"
    PAYLOAD_INSTALLATION = "Payload installation"
    PAYLOAD_TYPE = "Payload type"
    PERSISTENCE_MECHANISM = "Persistence mechanism"
    PERSON = "Person"
    SOCIAL_NETWORK = "Social network"
    SUPPORT_TOOL = "Support Tool"
    TARGETING_DATA = "Targeting data"


class AttributeType(Enum):
    ABA_RTN = "aba-rtn"
    ANONYMISED = "anonymised"
    AS = "AS"
    ATTACHMENT = "attachment"
    AUTHENTIHASH = "authentihash"
    AZURE_APPLICATION_ID = "azure-application-id"
    BANK_ACCOUNT_NR = "bank-account-nr"
    BIC = "bic"
    BIN = "bin"
    BOOLEAN = "boolean"
    BRO = "bro"
    BTC = "btc"
    CAMPAIGN_ID = "campaign-id"
    CAMPAIGN_NAME = "campaign-name"
    CC_NUMBER = "cc-number"
    CDHASH = "cdhash"
    CHROME_EXTENSION_ID = "chrome-extension-id"
    COMMENT = "comment"
    COMMUNITY_ID = "community-id"
    COOKIE = "cookie"
    CORTEX = "cortex"
    COUNTER = "counter"
    COUNTRY_OF_RESIDENCE = "country-of-residence"
    CPE = "cpe"
    DASH = "dash"
    DATETIME = "datetime"
    DATE_OF_BIRTH = "date-of-birth"
    DKIM = "dkim"
    DKIM_SIGNATURE = "dkim-signature"
    DNS_SOA_EMAIL = "dns-soa-email"
    DOMAIN = "domain"
    DOMAIN_IP = "domain|ip"
    DOM_HASH = "dom-hash"
    EMAIL = "email"
    EMAIL_ATTACHMENT = "email-attachment"
    EMAIL_BODY = "email-body"
    EMAIL_DST = "email-dst"
    EMAIL_DST_DISPLAY_NAME = "email-dst-display-name"
    EMAIL_HEADER = "email-header"
    EMAIL_MESSAGE_ID = "email-message-id"
    EMAIL_MIME_BOUNDARY = "email-mime-boundary"
    EMAIL_REPLY_TO = "email-reply-to"
    EMAIL_SRC = "email-src"
    EMAIL_SRC_DISPLAY_NAME = "email-src-display-name"
    EMAIL_SUBJECT = "email-subject"
    EMAIL_THREAD_INDEX = "email-thread-index"
    EMAIL_X_MAILER = "email-x-mailer"
    EPPN = "eppn"
    FAVICON_MMH3 = "favicon-mmh3"
    FILENAME = "filename"
    FILENAME_AUTHENTIHASH = "filename|authentihash"
    FILENAME_IMPFUZZY = "filename|impfuzzy"
    FILENAME_IMPHASH = "filename|imphash"
    FILENAME_MD5 = "filename|md5"
    FILENAME_PATTERN = "filename-pattern"
    FILENAME_PEHASH = "filename|pehash"
    FILENAME_SHA1 = "filename|sha1"
    FILENAME_SHA224 = "filename|sha224"
    FILENAME_SHA256 = "filename|sha256"
    FILENAME_SHA384 = "filename|sha384"
    FILENAME_SHA3_224 = "filename|sha3-224"
    FILENAME_SHA3_256 = "filename|sha3-256"
    FILENAME_SHA3_384 = "filename|sha3-384"
    FILENAME_SHA3_512 = "filename|sha3-512"
    FILENAME_SHA512 = "filename|sha512"
    FILENAME_SHA512_224 = "filename|sha512/224"
    FILENAME_SHA512_256 = "filename|sha512/256"
    FILENAME_SSDEEP = "filename|ssdeep"
    FILENAME_TLSH = "filename|tlsh"
    FILENAME_VHASH = "filename|vhash"
    FIRST_NAME = "first-name"
    FLOAT = "float"
    FREQUENT_FLYER_NUMBER = "frequent-flyer-number"
    FULL_NAME = "full-name"
    GENDER = "gender"
    GENE = "gene"
    GITHUB_ORGANISATION = "github-organisation"
    GITHUB_REPOSITORY = "github-repository"
    GITHUB_USERNAME = "github-username"
    GIT_COMMIT_ID = "git-commit-id"
    HASSHSERVER_MD5 = "hasshserver-md5"
    HASSH_MD5 = "hassh-md5"
    HEX = "hex"
    HOSTNAME = "hostname"
    HOSTNAME_PORT = "hostname|port"
    HTTP_METHOD = "http-method"
    IBAN = "iban"
    IDENTITY_CARD_NUMBER = "identity-card-number"
    IMPFUZZY = "impfuzzy"
    IMPHASH = "imphash"
    INTEGER = "integer"
    IP_DST = "ip-dst"
    IP_DST_PORT = "ip-dst|port"
    IP_SRC = "ip-src"
    IP_SRC_PORT = "ip-src|port"
    ISSUE_DATE_OF_THE_VISA = "issue-date-of-the-visa"
    JA3_FINGERPRINT_MD5 = "ja3-fingerprint-md5"
    JABBER_ID = "jabber-id"
    JARM_FINGERPRINT = "jarm-fingerprint"
    KUSTO_QUERY = "kusto-query"
    LAST_NAME = "last-name"
    LINK = "link"
    MAC_ADDRESS = "mac-address"
    MAC_EUI_64 = "mac-eui-64"
    MALWARE_SAMPLE = "malware-sample"
    MALWARE_TYPE = "malware-type"
    MD5 = "md5"
    MIDDLE_NAME = "middle-name"
    MIME_TYPE = "mime-type"
    MOBILE_APPLICATION_ID = "mobile-application-id"
    MUTEX = "mutex"
    NAMED_PIPE = "named pipe"
    NATIONALITY = "nationality"
    ONION_ADDRESS = "onion-address"
    OTHER = "other"
    PASSENGER_NAME_RECORD_LOCATOR_NUMBER = "passenger-name-record-locator-number"
    PASSPORT_COUNTRY = "passport-country"
    PASSPORT_EXPIRATION = "passport-expiration"
    PASSPORT_NUMBER = "passport-number"
    PATTERN_IN_FILE = "pattern-in-file"
    PATTERN_IN_MEMORY = "pattern-in-memory"
    PATTERN_IN_TRAFFIC = "pattern-in-traffic"
    PAYMENT_DETAILS = "payment-details"
    PDB = "pdb"
    PEHASH = "pehash"
    PGP_PRIVATE_KEY = "pgp-private-key"
    PGP_PUBLIC_KEY = "pgp-public-key"
    PHONE_NUMBER = "phone-number"
    PLACE_OF_BIRTH = "place-of-birth"
    PLACE_PORT_OF_CLEARANCE = "place-port-of-clearance"
    PLACE_PORT_OF_ONWARD_FOREIGN_DESTINATION = "place-port-of-onward-foreign-destination"
    PLACE_PORT_OF_ORIGINAL_EMBARKATION = "place-port-of-original-embarkation"
    PORT = "port"
    PRIMARY_RESIDENCE = "primary-residence"
    PROCESS_STATE = "process-state"
    PRTN = "prtn"
    REDRESS_NUMBER = "redress-number"
    REGKEY = "regkey"
    REGKEY_VALUE = "regkey|value"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA3_224 = "sha3-224"
    SHA3_256 = "sha3-256"
    SHA3_384 = "sha3-384"
    SHA3_512 = "sha3-512"
    SHA512 = "sha512"
    SHA512_224 = "sha512/224"
    SHA512_256 = "sha512/256"
    SIGMA = "sigma"
    SIZE_IN_BYTES = "size-in-bytes"
    SNORT = "snort"
    SPECIAL_SERVICE_REQUEST = "special-service-request"
    SSDEEP = "ssdeep"
    SSH_FINGERPRINT = "ssh-fingerprint"
    STIX2_PATTERN = "stix2-pattern"
    TARGET_EMAIL = "target-email"
    TARGET_EXTERNAL = "target-external"
    TARGET_LOCATION = "target-location"
    TARGET_MACHINE = "target-machine"
    TARGET_ORG = "target-org"
    TARGET_USER = "target-user"
    TELFHASH = "telfhash"
    TEXT = "text"
    THREAT_ACTOR = "threat-actor"
    TLSH = "tlsh"
    TRAVEL_DETAILS = "travel-details"
    TWITTER_ID = "twitter-id"
    URI = "uri"
    URL = "url"
    USER_AGENT = "user-agent"
    VHASH = "vhash"
    VISA_NUMBER = "visa-number"
    VULNERABILITY = "vulnerability"
    WEAKNESS = "weakness"
    WHOIS_CREATION_DATE = "whois-creation-date"
    WHOIS_REGISTRANT_EMAIL = "whois-registrant-email"
    WHOIS_REGISTRANT_NAME = "whois-registrant-name"
    WHOIS_REGISTRANT_ORG = "whois-registrant-org"
    WHOIS_REGISTRANT_PHONE = "whois-registrant-phone"
    WHOIS_REGISTRAR = "whois-registrar"
    WINDOWS_SCHEDULED_TASK = "windows-scheduled-task"
    WINDOWS_SERVICE_DISPLAYNAME = "windows-service-displayname"
    WINDOWS_SERVICE_NAME = "windows-service-name"
    X509_FINGERPRINT_MD5 = "x509-fingerprint-md5"
    X509_FINGERPRINT_SHA1 = "x509-fingerprint-sha1"
    X509_FINGERPRINT_SHA256 = "x509-fingerprint-sha256"
    XMR = "xmr"
    YARA = "yara"
    ZEEK = "zeek"


# Category to type mappings
CATEGORY_TYPE_MAPPING: Dict[AttributeCategory, Set[AttributeType]] = {
    AttributeCategory.ANTIVIRUS_DETECTION: {
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.COMMENT,
        AttributeType.HEX,
        AttributeType.LINK,
        AttributeType.OTHER,
        AttributeType.TEXT,
    },
    AttributeCategory.ARTIFACTS_DROPPED: {
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.AUTHENTIHASH,
        AttributeType.CDHASH,
        AttributeType.COMMENT,
        AttributeType.COOKIE,
        AttributeType.FILENAME,
        AttributeType.FILENAME_PATTERN,
        AttributeType.FILENAME_AUTHENTIHASH,
        AttributeType.FILENAME_IMPFUZZY,
        AttributeType.FILENAME_IMPHASH,
        AttributeType.FILENAME_MD5,
        AttributeType.FILENAME_PEHASH,
        AttributeType.FILENAME_SHA1,
        AttributeType.FILENAME_SHA224,
        AttributeType.FILENAME_SHA256,
        AttributeType.FILENAME_SHA3_224,
        AttributeType.FILENAME_SHA3_256,
        AttributeType.FILENAME_SHA3_384,
        AttributeType.FILENAME_SHA3_512,
        AttributeType.FILENAME_SHA384,
        AttributeType.FILENAME_SHA512,
        AttributeType.FILENAME_SHA512_224,
        AttributeType.FILENAME_SHA512_256,
        AttributeType.FILENAME_SSDEEP,
        AttributeType.FILENAME_TLSH,
        AttributeType.FILENAME_VHASH,
        AttributeType.GENE,
        AttributeType.HEX,
        AttributeType.IMPFUZZY,
        AttributeType.IMPHASH,
        AttributeType.KUSTO_QUERY,
        AttributeType.MALWARE_SAMPLE,
        AttributeType.MD5,
        AttributeType.MIME_TYPE,
        AttributeType.MUTEX,
        AttributeType.NAMED_PIPE,
        AttributeType.OTHER,
        AttributeType.PATTERN_IN_FILE,
        AttributeType.PATTERN_IN_MEMORY,
        AttributeType.PDB,
        AttributeType.PGP_PRIVATE_KEY,
        AttributeType.PGP_PUBLIC_KEY,
        AttributeType.PROCESS_STATE,
        AttributeType.REGKEY,
        AttributeType.REGKEY_VALUE,
        AttributeType.SHA1,
        AttributeType.SHA224,
        AttributeType.SHA256,
        AttributeType.SHA3_224,
        AttributeType.SHA3_256,
        AttributeType.SHA3_384,
        AttributeType.SHA3_512,
        AttributeType.SHA384,
        AttributeType.SHA512,
        AttributeType.SHA512_224,
        AttributeType.SHA512_256,
        AttributeType.SIGMA,
        AttributeType.SSDEEP,
        AttributeType.STIX2_PATTERN,
        AttributeType.TELFHASH,
        AttributeType.TEXT,
        AttributeType.VHASH,
        AttributeType.WINDOWS_SCHEDULED_TASK,
        AttributeType.WINDOWS_SERVICE_DISPLAYNAME,
        AttributeType.WINDOWS_SERVICE_NAME,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
        AttributeType.YARA,
    },
    AttributeCategory.ATTRIBUTION: {
        AttributeType.ANONYMISED,
        AttributeType.CAMPAIGN_ID,
        AttributeType.CAMPAIGN_NAME,
        AttributeType.COMMENT,
        AttributeType.DNS_SOA_EMAIL,
        AttributeType.EMAIL,
        AttributeType.OTHER,
        AttributeType.TEXT,
        AttributeType.THREAT_ACTOR,
        AttributeType.WHOIS_CREATION_DATE,
        AttributeType.WHOIS_REGISTRANT_EMAIL,
        AttributeType.WHOIS_REGISTRANT_NAME,
        AttributeType.WHOIS_REGISTRANT_ORG,
        AttributeType.WHOIS_REGISTRANT_PHONE,
        AttributeType.WHOIS_REGISTRAR,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
    },
    AttributeCategory.EXTERNAL_ANALYSIS: {
        AttributeType.AS,
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.BRO,
        AttributeType.COMMENT,
        AttributeType.COMMUNITY_ID,
        AttributeType.CORTEX,
        AttributeType.CPE,
        AttributeType.DOM_HASH,
        AttributeType.DOMAIN,
        AttributeType.DOMAIN_IP,
        AttributeType.FILENAME,
        AttributeType.FILENAME_PATTERN,
        AttributeType.FILENAME_MD5,
        AttributeType.FILENAME_SHA1,
        AttributeType.FILENAME_SHA256,
        AttributeType.FILENAME_SHA3_224,
        AttributeType.FILENAME_SHA3_256,
        AttributeType.FILENAME_SHA3_384,
        AttributeType.FILENAME_SHA3_512,
        AttributeType.GITHUB_REPOSITORY,
        AttributeType.HASSH_MD5,
        AttributeType.HASSHSERVER_MD5,
        AttributeType.HOSTNAME,
        AttributeType.IP_DST,
        AttributeType.IP_DST_PORT,
        AttributeType.IP_SRC,
        AttributeType.IP_SRC_PORT,
        AttributeType.JA3_FINGERPRINT_MD5,
        AttributeType.JARM_FINGERPRINT,
        AttributeType.LINK,
        AttributeType.MAC_ADDRESS,
        AttributeType.MAC_EUI_64,
        AttributeType.MALWARE_SAMPLE,
        AttributeType.MD5,
        AttributeType.ONION_ADDRESS,
        AttributeType.OTHER,
        AttributeType.PATTERN_IN_FILE,
        AttributeType.PATTERN_IN_MEMORY,
        AttributeType.PATTERN_IN_TRAFFIC,
        AttributeType.REGKEY,
        AttributeType.REGKEY_VALUE,
        AttributeType.SHA1,
        AttributeType.SHA256,
        AttributeType.SHA3_224,
        AttributeType.SHA3_256,
        AttributeType.SHA3_384,
        AttributeType.SHA3_512,
        AttributeType.SNORT,
        AttributeType.TEXT,
        AttributeType.URL,
        AttributeType.USER_AGENT,
        AttributeType.VULNERABILITY,
        AttributeType.WEAKNESS,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
        AttributeType.ZEEK,
    },
    AttributeCategory.FINANCIAL_FRAUD: {
        AttributeType.ABA_RTN,
        AttributeType.ANONYMISED,
        AttributeType.BANK_ACCOUNT_NR,
        AttributeType.BIC,
        AttributeType.BIN,
        AttributeType.BTC,
        AttributeType.CC_NUMBER,
        AttributeType.COMMENT,
        AttributeType.DASH,
        AttributeType.HEX,
        AttributeType.IBAN,
        AttributeType.OTHER,
        AttributeType.PHONE_NUMBER,
        AttributeType.PRTN,
        AttributeType.TEXT,
        AttributeType.XMR,
    },
    AttributeCategory.INTERNAL_REFERENCE: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.GIT_COMMIT_ID,
        AttributeType.HEX,
        AttributeType.LINK,
        AttributeType.OTHER,
        AttributeType.TEXT,
    },
    AttributeCategory.NETWORK_ACTIVITY: {
        AttributeType.AS,
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.BRO,
        AttributeType.COMMENT,
        AttributeType.COMMUNITY_ID,
        AttributeType.COOKIE,
        AttributeType.DKIM,
        AttributeType.DKIM_SIGNATURE,
        AttributeType.DOM_HASH,
        AttributeType.DOMAIN,
        AttributeType.DOMAIN_IP,
        AttributeType.EMAIL,
        AttributeType.EMAIL_DST,
        AttributeType.EMAIL_SRC,
        AttributeType.EMAIL_SUBJECT,
        AttributeType.EPPN,
        AttributeType.FAVICON_MMH3,
        AttributeType.FILENAME_PATTERN,
        AttributeType.HASSH_MD5,
        AttributeType.HASSHSERVER_MD5,
        AttributeType.HEX,
        AttributeType.HOSTNAME,
        AttributeType.HOSTNAME_PORT,
        AttributeType.HTTP_METHOD,
        AttributeType.IP_DST,
        AttributeType.IP_DST_PORT,
        AttributeType.IP_SRC,
        AttributeType.IP_SRC_PORT,
        AttributeType.JA3_FINGERPRINT_MD5,
        AttributeType.JARM_FINGERPRINT,
        AttributeType.MAC_ADDRESS,
        AttributeType.MAC_EUI_64,
        AttributeType.ONION_ADDRESS,
        AttributeType.OTHER,
        AttributeType.PATTERN_IN_FILE,
        AttributeType.PATTERN_IN_TRAFFIC,
        AttributeType.PORT,
        AttributeType.SNORT,
        AttributeType.SSH_FINGERPRINT,
        AttributeType.STIX2_PATTERN,
        AttributeType.TEXT,
        AttributeType.URI,
        AttributeType.URL,
        AttributeType.USER_AGENT,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
        AttributeType.ZEEK,
    },
    AttributeCategory.OTHER: {
        AttributeType.ANONYMISED,
        AttributeType.BOOLEAN,
        AttributeType.COMMENT,
        AttributeType.COUNTER,
        AttributeType.CPE,
        AttributeType.DATETIME,
        AttributeType.FLOAT,
        AttributeType.HEX,
        AttributeType.INTEGER,
        AttributeType.OTHER,
        AttributeType.PGP_PRIVATE_KEY,
        AttributeType.PGP_PUBLIC_KEY,
        AttributeType.PHONE_NUMBER,
        AttributeType.PORT,
        AttributeType.SIZE_IN_BYTES,
        AttributeType.TEXT,
    },
    AttributeCategory.PAYLOAD_DELIVERY: {
        AttributeType.AS,
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.AUTHENTIHASH,
        AttributeType.AZURE_APPLICATION_ID,
        AttributeType.CDHASH,
        AttributeType.CHROME_EXTENSION_ID,
        AttributeType.COMMENT,
        AttributeType.CPE,
        AttributeType.DOMAIN,
        AttributeType.EMAIL,
        AttributeType.EMAIL_ATTACHMENT,
        AttributeType.EMAIL_BODY,
        AttributeType.EMAIL_DST,
        AttributeType.EMAIL_DST_DISPLAY_NAME,
        AttributeType.EMAIL_HEADER,
        AttributeType.EMAIL_MESSAGE_ID,
        AttributeType.EMAIL_MIME_BOUNDARY,
        AttributeType.EMAIL_REPLY_TO,
        AttributeType.EMAIL_SRC,
        AttributeType.EMAIL_SRC_DISPLAY_NAME,
        AttributeType.EMAIL_SUBJECT,
        AttributeType.EMAIL_THREAD_INDEX,
        AttributeType.EMAIL_X_MAILER,
        AttributeType.FILENAME,
        AttributeType.FILENAME_PATTERN,
        AttributeType.FILENAME_AUTHENTIHASH,
        AttributeType.FILENAME_IMPFUZZY,
        AttributeType.FILENAME_IMPHASH,
        AttributeType.FILENAME_MD5,
        AttributeType.FILENAME_PEHASH,
        AttributeType.FILENAME_SHA1,
        AttributeType.FILENAME_SHA224,
        AttributeType.FILENAME_SHA256,
        AttributeType.FILENAME_SHA3_224,
        AttributeType.FILENAME_SHA3_256,
        AttributeType.FILENAME_SHA3_384,
        AttributeType.FILENAME_SHA3_512,
        AttributeType.FILENAME_SHA384,
        AttributeType.FILENAME_SHA512,
        AttributeType.FILENAME_SHA512_224,
        AttributeType.FILENAME_SHA512_256,
        AttributeType.FILENAME_SSDEEP,
        AttributeType.FILENAME_TLSH,
        AttributeType.FILENAME_VHASH,
        AttributeType.HASSH_MD5,
        AttributeType.HASSHSERVER_MD5,
        AttributeType.HEX,
        AttributeType.HOSTNAME,
        AttributeType.HOSTNAME_PORT,
        AttributeType.IMPFUZZY,
        AttributeType.IMPHASH,
        AttributeType.IP_DST,
        AttributeType.IP_DST_PORT,
        AttributeType.IP_SRC,
        AttributeType.IP_SRC_PORT,
        AttributeType.JA3_FINGERPRINT_MD5,
        AttributeType.JARM_FINGERPRINT,
        AttributeType.LINK,
        AttributeType.MAC_ADDRESS,
        AttributeType.MAC_EUI_64,
        AttributeType.MALWARE_SAMPLE,
        AttributeType.MALWARE_TYPE,
        AttributeType.MD5,
        AttributeType.MIME_TYPE,
        AttributeType.MOBILE_APPLICATION_ID,
        AttributeType.ONION_ADDRESS,
        AttributeType.OTHER,
        AttributeType.PATTERN_IN_FILE,
        AttributeType.PATTERN_IN_TRAFFIC,
        AttributeType.PEHASH,
        AttributeType.SHA1,
        AttributeType.SHA224,
        AttributeType.SHA256,
        AttributeType.SHA3_224,
        AttributeType.SHA3_256,
        AttributeType.SHA3_384,
        AttributeType.SHA3_512,
        AttributeType.SHA384,
        AttributeType.SHA512,
        AttributeType.SHA512_224,
        AttributeType.SHA512_256,
        AttributeType.SIGMA,
        AttributeType.SSDEEP,
        AttributeType.STIX2_PATTERN,
        AttributeType.TELFHASH,
        AttributeType.TEXT,
        AttributeType.TLSH,
        AttributeType.URL,
        AttributeType.USER_AGENT,
        AttributeType.VHASH,
        AttributeType.VULNERABILITY,
        AttributeType.WEAKNESS,
        AttributeType.WHOIS_REGISTRANT_EMAIL,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
        AttributeType.YARA,
    },
    AttributeCategory.PAYLOAD_INSTALLATION: {
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.AUTHENTIHASH,
        AttributeType.AZURE_APPLICATION_ID,
        AttributeType.CDHASH,
        AttributeType.CHROME_EXTENSION_ID,
        AttributeType.COMMENT,
        AttributeType.CPE,
        AttributeType.FILENAME,
        AttributeType.FILENAME_PATTERN,
        AttributeType.FILENAME_AUTHENTIHASH,
        AttributeType.FILENAME_IMPFUZZY,
        AttributeType.FILENAME_IMPHASH,
        AttributeType.FILENAME_MD5,
        AttributeType.FILENAME_PEHASH,
        AttributeType.FILENAME_SHA1,
        AttributeType.FILENAME_SHA224,
        AttributeType.FILENAME_SHA256,
        AttributeType.FILENAME_SHA3_224,
        AttributeType.FILENAME_SHA3_256,
        AttributeType.FILENAME_SHA3_384,
        AttributeType.FILENAME_SHA3_512,
        AttributeType.FILENAME_SHA384,
        AttributeType.FILENAME_SHA512,
        AttributeType.FILENAME_SHA512_224,
        AttributeType.FILENAME_SHA512_256,
        AttributeType.FILENAME_SSDEEP,
        AttributeType.FILENAME_TLSH,
        AttributeType.FILENAME_VHASH,
        AttributeType.HEX,
        AttributeType.IMPFUZZY,
        AttributeType.IMPHASH,
        AttributeType.MALWARE_SAMPLE,
        AttributeType.MALWARE_TYPE,
        AttributeType.MD5,
        AttributeType.MIME_TYPE,
        AttributeType.MOBILE_APPLICATION_ID,
        AttributeType.OTHER,
        AttributeType.PATTERN_IN_FILE,
        AttributeType.PATTERN_IN_MEMORY,
        AttributeType.PATTERN_IN_TRAFFIC,
        AttributeType.PEHASH,
        AttributeType.SHA1,
        AttributeType.SHA224,
        AttributeType.SHA256,
        AttributeType.SHA3_224,
        AttributeType.SHA3_256,
        AttributeType.SHA3_384,
        AttributeType.SHA3_512,
        AttributeType.SHA384,
        AttributeType.SHA512,
        AttributeType.SHA512_224,
        AttributeType.SHA512_256,
        AttributeType.SIGMA,
        AttributeType.SSDEEP,
        AttributeType.STIX2_PATTERN,
        AttributeType.TELFHASH,
        AttributeType.TEXT,
        AttributeType.TLSH,
        AttributeType.VHASH,
        AttributeType.VULNERABILITY,
        AttributeType.WEAKNESS,
        AttributeType.X509_FINGERPRINT_MD5,
        AttributeType.X509_FINGERPRINT_SHA1,
        AttributeType.X509_FINGERPRINT_SHA256,
        AttributeType.YARA,
    },
    AttributeCategory.PAYLOAD_TYPE: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.OTHER,
        AttributeType.TEXT,
    },
    AttributeCategory.PERSISTENCE_MECHANISM: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.FILENAME,
        AttributeType.HEX,
        AttributeType.OTHER,
        AttributeType.REGKEY,
        AttributeType.REGKEY_VALUE,
        AttributeType.TEXT,
    },
    AttributeCategory.PERSON: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.COUNTRY_OF_RESIDENCE,
        AttributeType.DATE_OF_BIRTH,
        AttributeType.EMAIL,
        AttributeType.FIRST_NAME,
        AttributeType.FREQUENT_FLYER_NUMBER,
        AttributeType.FULL_NAME,
        AttributeType.GENDER,
        AttributeType.IDENTITY_CARD_NUMBER,
        AttributeType.ISSUE_DATE_OF_THE_VISA,
        AttributeType.LAST_NAME,
        AttributeType.MIDDLE_NAME,
        AttributeType.NATIONALITY,
        AttributeType.OTHER,
        AttributeType.PASSENGER_NAME_RECORD_LOCATOR_NUMBER,
        AttributeType.PASSPORT_COUNTRY,
        AttributeType.PASSPORT_EXPIRATION,
        AttributeType.PASSPORT_NUMBER,
        AttributeType.PAYMENT_DETAILS,
        AttributeType.PGP_PRIVATE_KEY,
        AttributeType.PGP_PUBLIC_KEY,
        AttributeType.PHONE_NUMBER,
        AttributeType.PLACE_OF_BIRTH,
        AttributeType.PLACE_PORT_OF_CLEARANCE,
        AttributeType.PLACE_PORT_OF_ONWARD_FOREIGN_DESTINATION,
        AttributeType.PLACE_PORT_OF_ORIGINAL_EMBARKATION,
        AttributeType.PRIMARY_RESIDENCE,
        AttributeType.REDRESS_NUMBER,
        AttributeType.SPECIAL_SERVICE_REQUEST,
        AttributeType.TEXT,
        AttributeType.TRAVEL_DETAILS,
        AttributeType.VISA_NUMBER,
    },
    AttributeCategory.SOCIAL_NETWORK: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.EMAIL,
        AttributeType.EMAIL_DST,
        AttributeType.EMAIL_SRC,
        AttributeType.EPPN,
        AttributeType.GITHUB_ORGANISATION,
        AttributeType.GITHUB_REPOSITORY,
        AttributeType.GITHUB_USERNAME,
        AttributeType.JABBER_ID,
        AttributeType.OTHER,
        AttributeType.PGP_PRIVATE_KEY,
        AttributeType.PGP_PUBLIC_KEY,
        AttributeType.TEXT,
        AttributeType.TWITTER_ID,
        AttributeType.WHOIS_REGISTRANT_EMAIL,
    },
    AttributeCategory.SUPPORT_TOOL: {
        AttributeType.ANONYMISED,
        AttributeType.ATTACHMENT,
        AttributeType.COMMENT,
        AttributeType.HEX,
        AttributeType.LINK,
        AttributeType.OTHER,
        AttributeType.TEXT,
    },
    AttributeCategory.TARGETING_DATA: {
        AttributeType.ANONYMISED,
        AttributeType.COMMENT,
        AttributeType.TARGET_EMAIL,
        AttributeType.TARGET_EXTERNAL,
        AttributeType.TARGET_LOCATION,
        AttributeType.TARGET_MACHINE,
        AttributeType.TARGET_ORG,
        AttributeType.TARGET_USER,
    },
}
