import sys

print("[LOG - PYTHON]: Inside py2/processor.py subsystem context.")

try:
    ### Variables
    base_value = float(input("Enter a base processing number: "))
    multiplier = 2.5
    
    ### Mathematical operator logic
    processed_result = base_value * multiplier
    print(f"[LOG - PROCESSING]: Calculation completed. Result is {processed_result}")

    ### Conditional statement
    if processed_result > 100.0:
        print("[LOG - OUTPUT]: High threshold system resource load detected.")
    else:
        print("[LOG - OUTPUT]: Nominal threshold resource load.")

except ValueError:
    print("[ERROR - PYTHON]: Numeric processing calculation failed.")
    sys.exit(1)
