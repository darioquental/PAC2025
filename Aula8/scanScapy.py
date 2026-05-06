from scapy.all import ARP,Ether,srp

arp = ARP(pdst="192.168.1.0/24")
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

pacote = ether/arp

respostas = srp(pacote, timeout=2, verbose=0)[0]

print(respostas.show())
for envio, recebido in respostas:
    print(recebido.psrc, recebido.hwsrc)