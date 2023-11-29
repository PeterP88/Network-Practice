import ipaddress
import subprocess
import platform


def is_ip_in_network(ip, network):
    return ip in network

def ping(ip):
    param = "-n" if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', str(ip)]


if __name__ == '__main__':

    network_cidr = "192.168.1.0/24"

    network = ipaddress.ip_network(network_cidr)

    for ip in network:
        print(f"IP {ip} is on the network: {is_ip_in_network(ip, network)}")
