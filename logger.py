import sys

print("[LOG - PYTHON]: Inside py3/logger.py subsystem context.")

### Variables
disk_space_free = int(input("Enter mock available server storage space (GB): "))
critical_limit = 20

### Boolean operator comparison
is_low = disk_space_free <= critical_limit

### Conditional tracking
if is_low:
    print(f"[ALERT - OUTPUT]: Critical Warning! Only {disk_space_free}GB storage remains.")
else:
    print(f"[LOG - OUTPUT]: Storage allocations healthy. Status OK.")
