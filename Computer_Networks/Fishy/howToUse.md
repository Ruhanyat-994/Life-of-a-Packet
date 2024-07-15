# Compiling
```sh
gcc -o script script.c -lws2_32
```
# Running
```sh
script <ip> <network_part>
```
## Example
```sh
script 207.21.54.240 27
```
## Output
```sh
IP Address: 207.21.54.240
Subnet Mask: 224.255.255.255
Network Address: 207.21.54.224
Broadcast Address: 207.21.54.255
IP Range: 207.21.54.225
 - 207.21.54.254
```
- Here For the subnet musk add the first octat to the last
	- A little coding issue
