from mitmproxy import http
import time


class Demo:

    def __init__(self):
        self.unique_hosts = []

    def request(self, flow: http.HTTPFlow):
        request_host = flow.request.pretty_host

        if request_host not in self.unique_hosts:
            self.unique_hosts.append(request_host)

    def done(self):

        file = open("hosts-" + time.strftime("%Y-%m-%d-%H-%M-%S.txt"), "w")
        for unique_host in self.unique_hosts:
            file.write(str(unique_host) + "\n")
        file.close()


addons = [Demo()]
