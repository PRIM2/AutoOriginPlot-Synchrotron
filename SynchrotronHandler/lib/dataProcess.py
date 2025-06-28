# -*- coding: utf-8 -*-
'''
Functions to load and preprocess .dat files,
associate data with temperature/pressure readings,
and normalize data if requested.
'''

import os
import numpy as np

def process_files_dat():
    # Current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Data directory (../data)
    data_dir = os.path.normpath(os.path.join(script_dir, '..', 'data'))

    # List .dat files inside data folder, excluding 'tempres.txt'
    file_list = sorted([f for f in os.listdir(data_dir) if f.endswith('.dat') and f != 'tempres.txt'])

    # Read temperatures from tempres.txt
    temps = []
    temp_path = os.path.join(data_dir, "tempres.txt")
    with open(temp_path, "r") as temp_file:
        for line in temp_file:
            try:
                temps.append(float(line.strip()))
            except:
                temps.append(0.0)

    print("List of files and their assigned temperatures:\n")
    for i, filename in enumerate(file_list):
        if i < len(temps):
            print(f"{filename} - {temps[i]}")
        else:
            print(f"{filename} - No T/P assigned")

    # Confirm assignments
    answer = input("\nIs this assignment correct? (y/n): ").strip().lower()
    if answer not in ['y', 'yes', 'si', 'sí', 's']:
        print("Process cancelled by user.")
        return None

    # Ask if data normalization is desired
    answer = input("Do you want to normalize the data? (y/n): ").strip().lower()
    normalize = answer in ['y', 'yes', 'si', 'sí', 's']

    # Get minimum number of lines among all files to validate starting line input
    min_lines = None
    for filename in file_list:
        file_path = os.path.join(data_dir, filename)
        with open(file_path, 'r') as f:
            line_count = sum(1 for _ in f)
            if min_lines is None or line_count < min_lines:
                min_lines = line_count

    print(f"\nStarting line of the files (first line = 1). Value must be between 1 and {min_lines}")

    # Ask for starting line once for all files
    while True:
        entry = input("Starting line: ").strip()
        try:
            start_line = int(entry)
            if start_line < 1 or start_line > min_lines:
                print(f"[Error] Number out of range, please enter a value between 1 and {min_lines}")
                continue
            break
        except ValueError:
            print(f"[Error] Invalid input '{entry}'")

    # Accumulators
    tth, intensity, error, tempres = [], [], [], []

    # Process each file using the defined starting line
    for idx, filename in enumerate(file_list):
        if idx >= len(temps):
            continue

        file_path = os.path.join(data_dir, filename)
        data = []
        with open(file_path, 'r') as f:
            lines = f.readlines()

        valid_lines = lines[start_line - 1:]

        for line in valid_lines:
            if line.strip().startswith('#'):
                continue
            try:
                numbers = [float(x) for x in line.strip().split()]
                if len(numbers) >= 3:
                    data.append(numbers[:3])
            except ValueError:
                continue

        if not data:
            print(f"[Warning] Empty file or no valid data: {filename}")
            continue

        data = np.array(data)
        col0, col1, col2 = data[:, 0], data[:, 1], data[:, 2]

        if normalize:
            vmax = np.max(col1)
            if vmax != 0:
                col1 = col1 / vmax
            else:
                print(f"[Warning] vmax = 0 in {filename}, skipping normalization.")

        tth.extend(col0)
        intensity.extend(col1)
        error.extend(col2)
        tempres.extend([temps[idx]] * len(col0))

    return [tth, intensity, error, tempres]
