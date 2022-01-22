print_devices = []
file = open("1.txt","r")

for item in file:
    item = item.strip()
    print_devices.append(item)

file.close()
print(print_devices[4])