## Three way handshaking
1. syn
2. syn/ack
3. ack

```palintext
pc-1                   |          Server     |
----------------------------------------------
source ip - pc-1
destination ip - server

```

## Masking
###### ipV4

```plaintext

192.168.1.0 

-> Network part (this is common for all device in a network)
   - 192.168.1.0/24 so there are 24 bits are network part
   - 192.168.1 -> network part


-> Host part ( can't be same in one network) - 2^n numbers of host ip possible (n all the host bits) 
   - 8 bits are host part
   - 2^8 = 256
   - 192.168.1.0000 0000 -> 0 # Special ip # Network Address
   - 192.168.1.1111 1111 -> 255 # Special ip # Broadcast Ip
   - We can't give the special ip to any devices in my network
   - Broadcast address is same for all. It will be broadcasted

-> Useable Ip
   - Total host ip = 2^n
   - Usable Ip = 2^n - 2(net add and broadcast add)
   - 


``` 
##### If network bits are not given

```plaintext
 Subnet Mask . . . . . . . . . . . : 255.255.255.0

    - last octat is 0 so its binary is 0000 0000
    - its host part is 8 bit
    - previous bits are 
            - 255 - 1111 1111
            - 255 - 1111 1111
            - 255 - 1111 1111
                - 24 bits network part
    
    - 2^8 = 256 host ip
    - 2^8 -2 = 254 usable ip(without network and broadcast ip)


```
##### Tips
```plaintext
Host Address = Network address + Broadcast Address + Usable ip

Network  Address
      |
      |
      | - Usable ip
      |
      |
Boradcast Address
```

##### 192.168.1.0/27

```plaintext
 Subnet Mask . . . . . . . . . . . : 255.255.255.224

    - 192.168.1.1110 0000
    - 192.168.1.224 -> Network address
    - 192.168.1.255 -> broadcast address
    - 2^5 -> host ip
    - 2^5 - 2 -> usable ip
    
```
## Default Gateway

![alt text](image-1.png)

##### **Router is the default gateway between one and multiple networks**

## Using Packet Tracer

##### Part-3: Create a single-segment network using a Hub

![alt text](image.png)

![alt text](image-2.png)