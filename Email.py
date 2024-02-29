from scapy.all import sniff, IP, TCP
import smtplib
from termcolor import cprint
import sys

cprint('Sniffing...', 'yellow')
syn_count, failed_attempts = 0, {}

def send_email(subject, body):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("hasmik.programmer@gmail.com", "gdodlylauoochqdf")
        server.sendmail("hasmik.programmer@gmail.com", "hash43338@gmail.com", f'Subject: {subject}\n\n{body}')

def detect_scan(pkt):
    global syn_count, failed_attempts

    if pkt.haslayer(TCP) and pkt[TCP].flags == 2:
        syn_count += 1
        if syn_count > 10:
            cprint('Scanning detected', 'red')
            send_email('IDSGuard: Security Alert!', f'Scanning detected. High probability of scan from {pkt[IP].src}')
            sys.exit()

    elif pkt.haslayer(TCP) and pkt[TCP].dport == 22:
        src_ip = pkt[IP].src
        failed_attempts[src_ip] = failed_attempts.get(src_ip, 0) + 1

        if failed_attempts[src_ip] > 3:
            cprint('Brute force attack', 'red')
            send_email('IDSGuard: Security Alert!', f'High probability of brute force attack from {src_ip}')
            sys.exit()

if __name__ == '__main__':
    sniff(prn=detect_scan, filter='tcp', store=0)
