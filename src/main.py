import input_parser
import output_writer


n, h, s = input_parser.parse_input()
if n:
    print(f"Success! n={n}")
    print(h)
    print(s)