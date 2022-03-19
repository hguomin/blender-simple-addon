import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import debugpy as dbg
dbg.listen(5678)
dbg.wait_for_client()

import main

# This allows you to run the script directly from Blender's Text editor or command line
# to test the add-on without having to install it.
if __name__ == "__main__":
    main.register()