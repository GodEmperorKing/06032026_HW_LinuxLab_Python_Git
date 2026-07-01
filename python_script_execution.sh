#!/bin/bash

# Clear any broken system path mappings from the environment windows inplace repair 
unset PYTHONHOME
unset PYTHONPATH

echo "[LOG - BASH]: Script initialization successful."

### 1. Dynamic Variable: Capturing choice dynamically
read -p "Select an option (1: Validator, 2: Processor, 3: Logger): " choice

### Define the absolute path to for Python installation using clean forward slashes
PYTHON_EXE="C:/Users/The Boss/AppData/Local/Programs/Python/Python313/python.exe"

echo "[LOG - BASH]: Evaluation option context: $choice"

### 2. Conditional Logic: Selecting which directory script to fire based on input
if [ "$choice" == "1" ]; then
    echo "[LOG - BASH]: Context matched option 1. Launching sub-directory payload py1/validator.py"
    "$PYTHON_EXE" py1/validator.py

elif [ "$choice" == "2" ]; then
    echo "[LOG - BASH]: Context matched option 2. Launching sub-directory payload py2/processor.py"
    "$PYTHON_EXE" py2/processor.py

elif [ "$choice" == "3" ]; then
    echo "[LOG - BASH]: Context matched option 3. Launching sub-directory payload py3/logger.py"
    "$PYTHON_EXE" py3/logger.py

else
    echo "[ERROR - BASH]: Invalid context selection '$choice'. Execution aborted."
    exit 1
fi

echo "[LOG - BASH]: Orchestration lifecycle completed cleanly."
