# custom_filters.py

def netmask_subtract(cidr_netmask):
    netmask = []
    for octet in cidr_netmask.split("."):
        netmask.append(str(255 - int(octet)))
    return ".".join(netmask)

class FilterModule(object):
    def filters(self):
        return {
            'netmask_subtract': netmask_subtract,
        }
