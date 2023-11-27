import subprocess
import ipaddress

if __name__ == '__main__':

    #saving network cidr
    network_cidr = "192.168.1.0/24"

    #creates a network object from the network cidr
    network = ipaddress.ip_network(network_cidr)




