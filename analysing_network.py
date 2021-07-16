import psutil


def Network():

    All = f"""
        {"="*40} Informações de Internet {"="*40} 
    """

    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:

            All2 = f"""  
        Interface: {interface_name} """

            if str(address.family) == 'AddressFamily.AF_INET':
                All3 = f""" 
        Endereço de IP: {address.address}
        Transmissão IP: {address.broadcast}
                """

    return All + All2 + All3
