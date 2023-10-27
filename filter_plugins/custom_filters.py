# custom_filters.py
import netaddr

def cidr_to_wildcard(cidr):
    cidr_netmask = netaddr.IPNetwork(cidr).hostmask
    # netmask = []
    # for octet in cidr_netmask.split("."):
    #     netmask.append(str(255 - int(octet)))
    # return ".".join(netmask)
    return cidr_netmask

def netmask_subtract(cidr_netmask):
    netmask = []
    for octet in cidr_netmask.split("."):
        netmask.append(str(255 - int(octet)))
    return ".".join(netmask)

class FilterModule(object):
    def filters(self):
        return {
            'netmask_subtract': netmask_subtract,
            'cidr_to_wildcard': cidr_to_wildcard
        }
