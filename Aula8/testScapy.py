from scapy.all import IP,ICMP,sr1,sniff

print("Scapy ok")

resposta = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=2, verbose=0)

print(resposta)