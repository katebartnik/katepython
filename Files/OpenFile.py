f = open("test")
print(f)
f.close()

# ASCII
# a-zA-Z0-9
# 7 bit - 128
# 1111111 = 1 + 2 + 4 + 8 +16 + 32 + 64
# Unicode
# UTF-8

f = open("test")
print(dir(f))
for _ in f:
    print(_)
f.close()

f = open("test")
print(f.read())
f.close()

try:
    f = open('test')
    # cos tu robimy
except Exception:
    print("Wyjatek")
finally:
    f.close()

#  manager kontekstu
with open("otwieranie_pliku.py", encoding='utf-8') as f: #tego uzywamy do otwierania pliku
    for l in f:
        print(l.upper())