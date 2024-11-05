# pylint: disable=missing-docstring

def get_ip_header():
    ip_header  = b"\x45" # Version + IHL
    ip_header += b"\x00" # Type of Service
    ip_header += b"\x00\x14" # Total Length
    ip_header += b"\xab\xcd" # Trusted Host ID
    ip_header += b"\x00\x00" # 3 Bit Flags + 13 bit Offset
    ip_header += b"\x40" # TTL
    ip_header += b"\x06" # Next Protocol (TCP)
    ip_header += b"\x00\xdb" # Checksum (I'm too lazy to calculate checksum)
    ip_header += b"\xc0\xa8\x00\x01" # Source address
    ip_header += b"\x01\x01\x01\x01" # Destination address

    return ip_header
