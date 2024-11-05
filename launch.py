# pylint: disable=missing-docstring
from modules.packets import send, headers

LAYER3_PROTOCOLS = """
1. IP
2. IPv6
3. ICMP
4. GRE
"""

LAYER4_PROTOCOLS = """
1. TCP
2. UDP
"""

def select(options):
    sel = input(f"Select: {options}")
    return sel

def main():
    sel_l3_proto = input(LAYER3_PROTOCOLS)
    sel_l4_proto = select(LAYER4_PROTOCOLS) if sel_l3_proto == '1' else None
    dst_address = input("Address: ")
    dst_port = input("Port") if sel_l4_proto else None


    send(dst_address, dst_port, data=headers[int(sel_l3_proto)-1][int(sel_l4_proto)-1] if sel_l4_proto else headers[int(sel_l3_proto)-1])



if __name__ == "__main__":
    main()
