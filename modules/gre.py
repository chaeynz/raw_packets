# pylint: disable=missing-docstring
#from modules.packets import send

def get_gre_header():
    gre_header  = b"\x00\x00" # 1 Bit Checksum bit + 12 Bit Reserved + 3 Bit Version
    gre_header += b"\x08\x00" # Protocol Type

    return gre_header

if __name__ == "__main__":
    print(get_gre_header())
    #send('1.1.1.1', '')
