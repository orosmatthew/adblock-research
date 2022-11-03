from python_hosts import Hosts
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("ads", help="The hosts file with the ads")
parser.add_argument("data", help="The domains recorded with the proxy")

args = parser.parse_args()

ad_hosts = []

hosts = Hosts(path=args.ads)
for entry in hosts.entries:
    if entry.entry_type == "ipv4":
        ad_hosts.append(str(entry.names[0]))

domains = []
with open(args.data) as file:
    for line in file:
        domains.append(line.rstrip())

total_count = 0
ad_count = 0

# The magic
for domain in domains:
    total_count += 1
    if domain in ad_hosts:
        ad_count += 1

print("Total domains: " + str(total_count))
print("Ad count: " + str(ad_count))
