import ipaddress
import argparse
import sys

def find_subnet_mask(ip_cidr):
    try:
        # Create an IPv4 network object from the CIDR input
        network = ipaddress.IPv4Network(ip_cidr, strict=False)
        # Get the subnet mask
        subnet_mask = network.netmask
        return subnet_mask
    except ValueError:
        return "Invalid input. Please enter a valid IP address with CIDR."

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Find the subnet mask from an IP address with CIDR notation.",
        usage="python %(prog)s <IP/CIDR>\nExample: python %(prog)s 192.168.1.0/24"
    )
    
    parser.add_argument("ip_cidr", type=str, nargs='?', help="IP address with CIDR notation (e.g., 192.168.1.0/24)")

    # Parse the argument
    args = parser.parse_args()
    
    if not args.ip_cidr:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Find subnet mask
    subnet_mask = find_subnet_mask(args.ip_cidr)
    print(f"The subnet mask for {args.ip_cidr} is: {subnet_mask}")
