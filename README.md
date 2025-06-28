Synchrotron `.dat` File Processing with Temperature and Pressure Association

This project automates the processing of experimental `.dat` data files generated during synchrotron experiments. It extracts the first three relevant columns and associates them with the temperatures and pressures specified in a `tempres.txt` file. 
Returns an xxxx.opju (originpro proyect) in SynchrotronHandler.

Note: This project requires Windows because it depends on OriginPro, which is only available for Windows systems.

---

Quick Start

To run the entire processing pipeline automatically, simply execute the `Synchrotron.bat` file located in the root folder of the project. This batch script runs the processing workflow and installs all necessary dependencies.

---

PROJECT STRUCTURE

SynchrotronHandler/
├── data/
│   ├── xxx.dat
│   └── tempres.txt
├── lib/
│   ├── dataProcess.py
│   ├── originlib.py
│   └── main.py
│   └── README.md
├── Syncrotron.bat

---

Contents of the `data` Folder

- `.dat` files: Place here all synchrotron data files you wish to process.
- `tempres.txt`: A text file containing temperature or pressure data in the same order as the `.dat` files. Each line should contain one temperature or pressure.
    - Example:
        1
        2
        3
        4
        5
        6
        7

---

Processing Workflow

When executing `Syncrotron.bat`, the scripts inside the `lib/` folder will:

1. Load and list `.dat` files alongside the temperatures and pressures from `tempres.txt`.
2. Allow you to confirm the correct data assignment.
3. Prompt interactively for the valid starting line in each file to skip headers or unwanted data.
4. Offer the option to normalize intensity data.
5. Process and combine the data for further analysis.

---

Additional Notes

- Line numbering for data reading starts at 1.
- The project is designed to be user-friendly and requires minimal configuration thanks to the `Syncrotron.bat` script.
- Clear warnings and errors are provided in case of empty files or issues during processing to facilitate troubleshooting.

---

Author

Environment and project setup developed by Ferran Garcia Berenguer.
Contact: ferran.gberenguer@udc.es

Data processing code based on work by Victor Hernandez Piñeiro (victor.hernandez.pineiro@udc.es).

Released on June 27, 2025.
