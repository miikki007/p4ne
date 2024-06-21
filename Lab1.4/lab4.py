from ipaddress import IPv4Network
import random

class IPv4RandonNetwork(IPv4Network):
        def __init__(self):
                net = random.randint(0x0b000000, 0xdf000000)
                mask = random.randint(8,24)
                IPv4Network.__init__(self, (net, mask), strict=False)

net1 = IPv4RandonNetwork()
print(net1)
