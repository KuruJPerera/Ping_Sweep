# Ping Sweep Scanner in Python

This project demonstrates a simple Python script for scanning a subnet using ping requests. The script attempts to ping a specified range of IP addresses and prints a message for each host that responds, helping users identify active devices on a network.

---

## What is a Ping Sweep?

A ping sweep is a network reconnaissance technique used to discover which hosts on a network are reachable. By sending ICMP Echo Requests (ping), you can detect active devices and map out a network’s layout.

This script uses the **subprocess** module to run system-level `ping` commands and collect the responses directly in Python.

---

## How It Works

The script prompts the user to input:

- The starting IP address  
- The ending IP address  

It then loops through the specified range of IP addresses (in the **192.168.1.X** subnet), sending a single ping packet to each one:

- If the host responds, it prints that the host is **active**.  
- If the host does not respond or an error occurs, it skips to the next address.

This basic approach allows users to identify live hosts on a local network quickly.

---

## Getting Started

### Requirements

To run this project, you’ll need:

- Python 3 installed on your computer  
- Access to a terminal or command prompt  
- A local network environment for scanning  

If Python isn’t installed, download it here:  
https://www.python.org/downloads/

---

## Installation

1. Download or clone this repository to your local machine.  
2. Open the script file (`ping_sweep.py`) in a code editor.  
3. No external libraries are required—this script uses only the Python Standard Library.

---

## Running the Program

1. Open your terminal.  
2. Navigate to the script’s directory.  
3. Run the script with:  
   ```bash
   python ping_sweep.py
