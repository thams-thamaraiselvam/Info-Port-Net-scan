import socket
import os

# Network Details
def get_network_details(ip_address):
    hostname = socket.gethostbyaddr(ip_address)[0]
    return hostname

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

if __name__ == "__main__":
    main()
