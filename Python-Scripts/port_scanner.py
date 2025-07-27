import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            sock.close()
        except socket.error:
            print(f"Couldn't connect to {target}")
            break

if __name__ == "__main__":
    target_host = input("Enter target IP or hostname: ")
    common_ports = [22, 23, 80, 443, 3389]
    scan_ports(target_host, common_ports)
