#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
#else
#include <arpa/inet.h>
#endif

// Function to calculate the subnet mask from CIDR
unsigned int cidr_to_netmask(int cidr) {
    return htonl(~((1 << (32 - cidr)) - 1));
}

// Function to print the IP address in human-readable format
void print_ip(unsigned int ip) {
    struct in_addr ip_addr;
    ip_addr.s_addr = htonl(ip);
    printf("%s\n", inet_ntoa(ip_addr));
}

// Function to calculate network address
unsigned int calculate_network_address(unsigned int ip, unsigned int netmask) {
    return ip & netmask;
}

// Function to calculate broadcast address
unsigned int calculate_broadcast_address(unsigned int network_address, unsigned int netmask) {
    return network_address | ~ntohl(netmask);
}

// Function to calculate the range of IP addresses
void calculate_ip_range(unsigned int network_address, unsigned int broadcast_address) {
    printf("IP Range: ");
    print_ip(network_address + 1);
    printf(" - ");
    print_ip(broadcast_address - 1);
}

int main(int argc, char *argv[]) {
#ifdef _WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        fprintf(stderr, "WSAStartup failed.\n");
        return 1;
    }
#endif

    if (argc < 2 || argc > 3) {
        fprintf(stderr, "Usage: %s <IP> [CIDR]\n", argv[0]);
        return 1;
    }

    char *ip_str = argv[1];
    int cidr = argc == 3 ? atoi(argv[2]) : 24;  // Default to CIDR 24 if not provided

    struct in_addr ip_addr;
#ifdef _WIN32
    if (InetPton(AF_INET, ip_str, &ip_addr) <= 0) {
        fprintf(stderr, "Invalid IP address.\n");
        return 1;
    }
#else
    if (inet_aton(ip_str, &ip_addr) == 0) {
        fprintf(stderr, "Invalid IP address.\n");
        return 1;
    }
#endif

    unsigned int ip = ntohl(ip_addr.s_addr);
    unsigned int netmask = cidr_to_netmask(cidr);
    unsigned int network_address = calculate_network_address(ip, ntohl(netmask));
    unsigned int broadcast_address = calculate_broadcast_address(network_address, netmask);

    printf("IP Address: %s\n", ip_str);
    printf("Subnet Mask: ");
    print_ip(netmask);
    printf("Network Address: ");
    print_ip(network_address);
    printf("Broadcast Address: ");
    print_ip(broadcast_address);
    calculate_ip_range(network_address, broadcast_address);

#ifdef _WIN32
    WSACleanup();
#endif

    return 0;
}
