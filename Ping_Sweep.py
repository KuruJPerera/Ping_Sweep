# Ping Sweep (for a full subnet).

import subprocess  # Import subprocess module to handle system commands

def ping_sweep(start_ip, end_ip):
    """Pings hosts in the given IP range to check if they are active."""
    # Loop through the range of IP addresses
    for i in range(start_ip, end_ip + "1"):  
        ip = "192.168.1." + str(i)  # Combine the base subnet with the host IP end.
        response = subprocess.call(["ping", "-n", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Send one ping packet
        # and send the errors stdout and stderr to the subprocess (for organisation)
        
        # Host is up.
        if response == 0:
            print("Host " + ip + " is active")

# Usage
start_ip = input("Enter the starting IP number (e.g., 1 for 192.168.1.1): ")
end_ip = input("Enter the ending IP number (e.g., 254 for 192.168.1.254): ")

# Call the function.
ping_sweep(start_ip, end_ip)
