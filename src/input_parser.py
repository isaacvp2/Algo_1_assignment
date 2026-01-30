import sys

def parse_input():

    raw_lines = sys.stdin.readlines()

    if not raw_lines:
        print("Input is empty.")
        return None, None, None

    try:
        lines = []
        for i, line in enumerate(raw_lines):
            stripped_line = line.strip()
            
            # Check if a line just contains whitespaces or a newline
            if not stripped_line:
                raise ValueError(f"Line {i+1} is empty or contains only whitespace.")
                
            lines.append(stripped_line)

        try:
            n = int(lines[0])
            if n < 1:
                raise ValueError("n must be a positive integer.")
        except ValueError as e:
            if "positive" in str(e):
                raise e
            raise ValueError(f"Line 1: '{lines[0]}' is not a valid integer.")


        expected_lines = 2 * n + 1
        if len(lines) != expected_lines:
            raise ValueError(f"Expected {expected_lines} lines, found {len(lines)}.")
        
        hospital_prefs = []
        student_prefs = []
        
        for i in range(1, n + 1):
            parts = lines[i].split()

            if len(parts) != n:
                raise ValueError(f"Line {i+1} (Hospital {i}): Found {len(parts)} items, expected {n}.")
            
            current_prefs = []
            for val in parts:
                try:
                    current_prefs.append(int(val) - 1)
                except ValueError:
                    raise ValueError(f"Line {i+1}: Non-integer value '{val}' found.")

            # Bounds and Duplicate Checks
            if len(set(current_prefs)) != n:
                 raise ValueError(f"Line {i+1}: Preference list contains duplicates.")
            
            # Check bounds (1 to n)
            if any(p < 0 or p >= n for p in current_prefs):
                 raise ValueError(f"Line {i+1}: Values must be between 1 and {n}.")

            hospital_prefs.append(current_prefs)
        

        for i in range(n + 1, 2 * n + 1):
            parts = lines[i].split()

            if len(parts) != n:
                raise ValueError(f"Line {i+1} (Student {i-n}): Found {len(parts)} items, expected {n}.")
            
            current_prefs = []
            for val in parts:
                try:
                    current_prefs.append(int(val) - 1)
                except ValueError:
                    raise ValueError(f"Line {i+1}: Non-integer value '{val}' found.")

            if len(set(current_prefs)) != n:
                 raise ValueError(f"Line {i+1}: Preference list contains duplicates.")
            
            if any(p < 0 or p >= n for p in current_prefs):
                 raise ValueError(f"Line {i+1}: Values must be between 1 and {n}.")

            student_prefs.append(current_prefs)

        return n, hospital_prefs, student_prefs

    except ValueError as e:
        print(f"Input Error: {e}")
        return None, None, None