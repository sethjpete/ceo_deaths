from os.path import expanduser
from os import getcwd

# Get the current working directory
DATA_DIR = getcwd() + '/data/'
DATA_DIR = expanduser(DATA_DIR)

