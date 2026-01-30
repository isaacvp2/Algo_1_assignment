import sys

def write_output(matchings):
    for matching in matchings:
        sys.stdout.write(f'{matching[0]} {matching[1]}\n')