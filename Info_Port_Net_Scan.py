import socket
import os

# Network Details
def get_network_details(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "Hostname not found"

# OS Details
def get_os_details():
    os_name = os.name
    os_version = " ".join(os.uname())
    return os_name, os_version

# Hardware Information
def get_hardware_info():
    cpu_info = "Not available"  # CPU information may not be easily retrievable without external libraries
    ram_info = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # RAM information in bytes
    hdd_info = os.statvfs('/').f_frsize * os.statvfs('/').f_blocks  # Total HDD storage in bytes
    return cpu_info, ram_info, hdd_info

# Port Scanner
def scan_ports(ip_address):
    open_ports = []
    for port in range(1, 1025):  # Scan common ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Main function
def main():
    ip_address = input("Enter the IP address: ")
    hostname = get_network_details(ip_address)
    print(f"Hostname: {hostname}")

    os_name, os_version = get_os_details()
    print(f"Operating System: {os_name} {os_version}")

    cpu_info, ram_info, hdd_info = get_hardware_info()
    print(f"CPU: {cpu_info}")
    print(f"RAM: {ram_info} bytes")
    print(f"HDD: {hdd_info} bytes")

    open_ports = scan_ports(ip_address)
    print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    main()
