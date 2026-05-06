from scapy.all import sniff

def analisa(p):
    print(p.summary())
    print(p.show())

sniff(iface="Wi-Fi",filter="udp",count=10,prn=analisa)