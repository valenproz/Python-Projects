import psutil #Library used to check computer information

#CPU Speed
cpu = psutil.cpu_freq()
print(cpu)

#CPU cores
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

#Memory Information
memory = psutil.virtual_memory()
print(memory)

#Disk Information
disk = psutil.disk_partitions()
print(disk)

#Data sent and received through the network
net = psutil.net_io_counters
print(net)