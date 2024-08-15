import socket
import os
import platform

# Network Details
def get_network_details(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "Hostname not found"

# OS Details
def get_os_details():
    os_name = platform.system()
    os_version = platform.version()
    return os_name, os_version

# Hardware Information
def get_hardware_info():
    # CPU information is not easily retrievable in a cross-platform way.
    cpu_info = "Not available"
    
    # RAM information
    try:
        ram_info = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        ram_info = ram_info / (1024 ** 3)  # Convert bytes to GB
    except AttributeError:
        ram_info = "Not available"
    
    # HDD information
    try:
        hdd_info = os.statvfs('/').f_frsize * os.statvfs('/').f_blocks
        hdd_info = hdd_info / (1024 ** 3)  # Convert bytes to GB
    except AttributeError:
        hdd_info = "Not available"

    return cpu_info, ram_info, hdd_info

# Port Scanner
def scan_ports(ip_address):
    open_ports = []
    for port in range(1, 1025):  # Scan common ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempts
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
    print(f"RAM: {ram_info} GB")
    print(f"HDD: {hdd_info} GB")

    open_ports = scan_ports(ip_address)
    print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    main()
