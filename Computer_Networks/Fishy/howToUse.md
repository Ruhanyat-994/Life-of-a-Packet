
# Subnetting Python Script - Usage Guide

This Python script allows you to calculate subnet information such as subnet masks, network addresses, broadcast addresses, and usable IP ranges from a given IP address in CIDR notation. It can also divide networks into subnets based on the specified number of subnets.

## Prerequisites

Ensure you have Python 3 installed on your system. The script uses the `ipaddress` module, which is part of the Python standard library.

## How to Run the Script

1. **Clone or download the script** to your local machine.

2. **Run the script** using the following command format in a terminal:
   ```bash
   python3 subnetting.py <IP/CIDR> <subnet_count>
   ```

### Example 1: Finding Subnet Mask and Subnetting a Network

```bash
python3 subnetting.py 192.168.1.0/24 4
```

**Output:**
```bash
Subnet mask for 192.168.1.0/24: 255.255.255.0

Dividing into 4 subnets:

Subnet 1:
  Network Address: 192.168.1.0
  Broadcast Address: 192.168.1.63
  Range of Usable IPs: 192.168.1.1 - 192.168.1.62
  Subnet Mask: 255.255.255.192
  Usable Hosts: 62

Subnet 2:
  Network Address: 192.168.1.64
  Broadcast Address: 192.168.1.127
  Range of Usable IPs: 192.168.1.65 - 192.168.1.126
  Subnet Mask: 255.255.255.192
  Usable Hosts: 62

Subnet 3:
  Network Address: 192.168.1.128
  Broadcast Address: 192.168.1.191
  Range of Usable IPs: 192.168.1.129 - 192.168.1.190
  Subnet Mask: 255.255.255.192
  Usable Hosts: 62

Subnet 4:
  Network Address: 192.168.1.192
  Broadcast Address: 192.168.1.255
  Range of Usable IPs: 192.168.1.193 - 192.168.1.254
  Subnet Mask: 255.255.255.192
  Usable Hosts: 62
```

### Example 2: Subnetting with an Odd Number of Subnets

```bash
python3 subnetting.py 192.168.1.0/24 7
```

**Output:**
```bash
Subnet mask for 192.168.1.0/24: 255.255.255.0

Dividing into 7 subnets:

Subnet 1:
  Network Address: 192.168.1.0
  Broadcast Address: 192.168.1.31
  Range of Usable IPs: 192.168.1.1 - 192.168.1.30
  Subnet Mask: 255.255.255.224
  Usable Hosts: 30

... (other subnet details)
```

## Arguments

- **`<IP/CIDR>`**: The base IP address in CIDR notation, e.g., `192.168.1.0/24`.
- **`<subnet_count>`** *(optional)*: The number of subnets you want to divide the network into. If omitted, the script will simply provide the subnet mask and general details for the network.

## Output

For each subnet, the script will output:
- **Network Address**: The address identifying the subnet.
- **Broadcast Address**: The broadcast address for the subnet.
- **Range of Usable IPs**: The range of IPs available for devices (excluding the network and broadcast addresses).
- **Subnet Mask**: The subnet mask for each network.
- **Usable Hosts**: The number of usable IP addresses within the subnet.

## Example Problems Solved

This script can be used to solve a variety of subnetting problems, such as:
- Dividing a Class C or Class B network into multiple subnets.
- Calculating network and broadcast addresses, and usable hosts.
- Practicing subnetting with variable lengths (VLSM) or CIDR notation.

---
