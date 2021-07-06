import hex_funcs as hf
import sys

filename = sys.argv[1]
hex_string = hf.hex_out(filename)
hf.string_to_txt(hex_string, "test.txt")

