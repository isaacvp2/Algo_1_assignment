import sys

# Raises ValueError if invalid input, otherwise returns list of matchings
def parse_output():

    raw_lines = sys.stdin.readlines()
    
    matchings = []

    if not raw_lines:
        return []

    for i, line in enumerate(raw_lines):
        stripped = line.strip()
        
        if not stripped:
            raise ValueError
            
        parts = stripped.split()

        # Check: Exactly 2 numbers per line
        if len(parts) != 2:
            raise ValueError(f"Line {i+1}: Malformed output. Expected 2 integers (Hospital Student), found {len(parts)}.")

        try:
            # Parse integers and convert to 0-indexed
            h_id = int(parts[0]) - 1
            s_id = int(parts[1]) - 1
            
            matchings.append([h_id, s_id])

        except ValueError:
            raise ValueError(f"Line {i+1}: Non-integer values found in output: '{stripped}'")

    return matchings