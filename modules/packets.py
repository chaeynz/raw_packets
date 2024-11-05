from socket import AF_INET, SOCK_RAW, socket, IPPROTO_GRE

from modules.gre import get_gre_header
from modules.ip import get_ip_header
from modules.icmp import get_icmp_header
from modules.tcp import get_tcp_header
from modules.udp import get_udp_header

headers = [
    [
        get_ip_header(), # L3 - IP (0,0)
        get_icmp_header(), # L3 - ICMP (0,1)
        get_gre_header() # L3 - GRE (0,2)
    ],
    [
        get_ip_header() + get_tcp_header(), # L4 - TCP (1,0)
        get_ip_header() + get_udp_header() # L4 - UDP (1,1)
    ]
]

def send(dst_address, dst_port=None, data=None):
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_GRE)

    sock.sendto(data, (dst_address, dst_port))
    sock.close()
