
octet1, octet2, octet3, octet4 = map(int, input("Enter the four octets: ").split())

ip_number = (octet1 << 24) | (octet2 << 16) | (octet3 << 8) | octet4


print("----------Output---------")
for _ in range(5):
    ip_number += 1
    new_octet1 = (ip_number >> 24) & 255
    new_octet2 = (ip_number >> 16) & 255
    new_octet3 = (ip_number >> 8) & 255
    new_octet4 = ip_number & 255
    print(new_octet1, new_octet2, new_octet3, new_octet4)
