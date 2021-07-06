import hex_funcs as hf
import sys

filename = sys.argv[1]
hex_string = hf.hex_out(filename)
print(hex_string)