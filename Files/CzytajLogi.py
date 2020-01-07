"""
$ python czytaj_logi.py dane/input.txt
user-9: 3520 s
user-6: 2950 s
"""
from collections import defaultdict
logins = defaultdict(int)
logouts = defaultdict(int)
times = {}
with open("dane/logs.txt") as f:
    for line in f:
        user, action, time = line.split(";")
        time = int(time)

        if action == "LOGIN":
            logins[user] += time
        elif action == "LOGOUT":
            logouts[user] += time

        for k, v in logouts.items():
            times[k] = v - logins[k]


for u, t in sorted(times.items(), key=lambda x: x[1], reverse=True ):
    print(u, t)
