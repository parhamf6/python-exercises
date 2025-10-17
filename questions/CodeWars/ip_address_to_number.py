# https://www.codewars.com/kata/541a354c39c5efa5fa001372/python
def ip_to_num(ip):
    octets = ip.split(".")
    return (int(octets[0]) << 24) | (int(octets[1]) << 16) | (int(octets[2]) << 8) | int(octets[3])


def num_to_ip(num):
    octet1 = (num >> 24) & 255
    octet2 = (num >> 16) & 255
    octet3 = (num >> 8) & 255
    octet4 = num & 255
    return f"{octet1}.{octet2}.{octet3}.{octet4}"