import ipaddress
import argparse
import sys
import math

def find_subnet_mask(ip_cidr):
    try:
        # Create an IPv4 network object from the CIDR input
        network = ipaddress.IPv4Network(ip_cidr, strict=False)
        return network.netmask
    except ValueError:
        return "Invalid input. Please enter a valid IP address with CIDR."

def subnet_info(ip_cidr, subnet_count=None):
    try:
        network = ipaddress.IPv4Network(ip_cidr, strict=False)
        if subnet_count:
            new_prefix = network.prefixlen + int(math.ceil(math.log(subnet_count, 2)))
            subnets = list(network.subnets(new_prefix=new_prefix))
        else:
            subnets = [network]

        subnet_details = []
        for subnet in subnets:
            details = {
                'network': subnet.network_address,
                'broadcast': subnet.broadcast_address,
                'range': f"{list(subnet.hosts())[0]} - {list(subnet.hosts())[-1]}",
                'subnet_mask': subnet.netmask,
                'usable_hosts': subnet.num_addresses - 2  # Exclude network and broadcast
            }
            subnet_details.append(details)

        return subnet_details
    except ValueError:
        return "Invalid input. Please enter a valid IP address with CIDR."

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Perform subnetting calculations.",
        usage="python %(prog)s <IP/CIDR> [<subnet_count>]\nExample: python %(prog)s 192.168.1.0/24 4"
    )
    
    parser.add_argument("ip_cidr", type=str, help="IP address with CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument("subnet_count", type=int, nargs='?', default=None, help="Number of subnets to divide into (optional)")

    # Parse the argument
    args = parser.parse_args()

    # Find subnet mask and subnet information
    subnet_mask = find_subnet_mask(args.ip_cidr)
    subnet_info_result = subnet_info(args.ip_cidr, args.subnet_count)

    print(f"Subnet mask for {args.ip_cidr}: {subnet_mask}\n")

    if args.subnet_count:
        print(f"Dividing into {args.subnet_count} subnets:")
        for i, info in enumerate(subnet_info_result):
            print(f"\nSubnet {i+1}:")
            print(f"  Network Address: {info['network']}")
            print(f"  Broadcast Address: {info['broadcast']}")
            print(f"  Range of Usable IPs: {info['range']}")
            print(f"  Subnet Mask: {info['subnet_mask']}")
            print(f"  Usable Hosts: {info['usable_hosts']}")
    else:
        print("Subnet info:")
        for info in subnet_info_result:
            print(f"  Network Address: {info['network']}")
            print(f"  Broadcast Address: {info['broadcast']}")
            print(f"  Range of Usable IPs: {info['range']}")
            print(f"  Subnet Mask: {info['subnet_mask']}")
            print(f"  Usable Hosts: {info['usable_hosts']}")
