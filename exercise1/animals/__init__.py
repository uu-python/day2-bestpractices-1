# This directory is not in the system path:
# import sys
# for directory in sys.path:
#     print(directory)

# So we need to tell the program where the "mammals", "birds" files are in order to import their classes.
# Hence we use the "." in the front, to tell the program to look in the same directory as the "__init__" file    
from .mammals_old import Mammals
from .birds_old import Birds

from . import harmless
from . import dangerous