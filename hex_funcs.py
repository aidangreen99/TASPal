
def hex_out(file_path):
    with open(file_path, 'rb') as f:
        hex_content = f.read().hex(' ')
        return hex_content


def string_to_txt(hex_strng, des_file_name):
    file1 = open(des_file_name, 'a')
    file1.write(hex_strng)
    file1.close()
