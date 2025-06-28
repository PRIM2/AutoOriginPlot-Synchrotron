# -*- coding: utf-8 -*-
'''
Main script to process data files, visualize results with OriginPro,
and save the project. Handles dependencies and error control.
'''

try:
    import sys
    import os
    import originpro as op
    import pandas as pd
    import numpy as np

except ImportError:
    import subprocess
    # Install necessary packages if not already installed and update pip
    packages = ["originpro", "pandas", "numpy"]
    print(f"Installing necessary packages: {', '.join(packages)} and upgrading pip...")

    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])
    except subprocess.CalledProcessError:
        print("\n\033[91mERROR: Unable to install packages. Check your internet connection or install packages manually.\033[0m")
        sys.exit(1)

    # Restart the script to ensure all imports are available
    os.execv(sys.executable, [sys.executable] + sys.argv)

import originlib as ol
import dataProcess as dp


print("***** Processing data *****")

try:
    tth, intensity, error, tempres = dp.process_files_dat()
except Exception as e:
    print(f"Error in dataProcess.process_files_dat(): {e}")
    sys.exit()

print("\n****** Processing completed successfully ****** \n")


# =============================
# ======== ORIGIN PRO =========
# =============================

print("***** Creating originpro environment *****\n")


# Automatic shutdown in case of error
def origin_shutdown_exception_hook(exctype, value, traceback):
    op.exit()
    sys.__excepthook__(exctype, value, traceback)

if op and op.oext:
    sys.excepthook = origin_shutdown_exception_hook
    try:
        op.set_show(False)
    except Exception as e:
        print("\033[91mERROR, CHECK ORIGINPRO INSTALLATION: https://www.originlab.com/\n", e, "\033[0m")
        sys.exit(1)

# Upload data into project
ol.uploadData(tth, intensity, error, tempres)

try:
    ol.contourFill()
except ValueError:
    print("Error in contourFill")


# =============================
# =========== Save ============
# =============================


# Get the absolute path of main.py
main_dir = os.path.dirname(os.path.abspath(__file__))

# Define the project name and save
fileName = input("Project name:\n")
ruta_opju = os.path.join(main_dir, '..', fileName + ".opju")
op.save(ruta_opju)
print(f"\033[92mProject saved successfully in {ruta_opju}\033[0m\n")

# Exit OriginPro
op.exit()
