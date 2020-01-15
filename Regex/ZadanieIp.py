import re


Error = "(\d{2}.\d{3}.\d{3}.\d{2}).*\"\s(404).*"

with open ("access.txt") as f:
    ip = f.read()

Error = re.compile(Error)
dataArray = Error.findall(ip)

for data in dataArray:
    print(data[0])

