# Global constants for the simulation

OS_TYPES = [
    "windows",
    "ubuntu",
    "centos",
    "freebsd"
]

OS_VERSION_DICT = {
    "windows" : ["10", "8.1", "8", "7", "vista", "xp"],
    "ubuntu" : ["20.04", "18.04", "16.04", "14.04", "12.04", "10.04"],
    "centos" : ["8", "7", "6", "5", "4", "3"],
    "freebsd" : ["13", "12", "11", "10", "9", "8"]
}

SERVICE_VERSIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

LARGE_INT = (1 << 100)

# No longer used and wordlists are included part of the package
# WORDLIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"
# NAME_LIST_URL = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"

# Constants for MTD strategies
MTD_MIN_TRIGGER_TIME = 1000
MTD_MAX_TRIGGER_TIME = 5000

# Constants for Network
NETWORK_HOST_DISCOVER_TIME = 1

# Constants for Hosts
HOST_SERVICES_MIN = 1
HOST_SERVICES_MAX = 11
HOST_INTERNAL_SERVICE_MIN = 0
HOST_PORT_RANGE = range(1, 65546)
HOST_USER_COMPROMISE_TIME = 5
HOST_AUTO_COMPROMISE_TIME = 1
HOST_MAX_PROB_FOR_USER_COMPROMISE = 0.01
HOST_PORT_SCAN_MIN_TIME = 10
HOST_PORT_SCAN_MAX_TIME = 50

VULN_PROB_DEPENDS_ON_OS = 0.1
VULN_PROB_DEPENDS_ON_OTHER_VULNS = 0.1
VULN_MIN_EXPLOIT_TIME = 10
VULN_MAX_EXPLOIT_TIME = 200

SERVICE_COMPROMISED_THRESHOLD = 7
SERVICE_DISCOVER_EACH_VULN_TIME = 10
SERVICE_TOP_X_VULNS_TO_RETURN = 5

HACKER_BLOCKED_BY_MTD_PENALITY = 300
HACKER_BLOCKED_BY_MTD_MAX_DISCOUNT = 0.9
HACKER_BLOCKED_BY_MTD_BLOCKS_TO_MAX_DISCOUNT = 100
HACKER_HOP_TIME = 5

def nothing():
    """
    Does nothing
    """
    pass