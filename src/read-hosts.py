from python_hosts import Hosts

ad_hosts = []

hosts = Hosts(path="../hosts/hosts.txt")
for entry in hosts.entries:
    if entry.entry_type == "ipv4":
        ad_hosts.append(str(entry.names[0]))

for host in ad_hosts:
    print(host)
