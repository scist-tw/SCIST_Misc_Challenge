from time import sleep

print('''===== Welcome TO PPC CTF =====
Please wait for a few second, let me calculate the flag ''', end='\r')

for i in range(3):
    for j in range(3):
        print('Please wait for a few second, let me calculate the flag ' + '.' * (j + 1) + ' ' * (2 - j), end='\r', flush=True)
        sleep(0.5)
print()

print('flag : SCIST{jYznFW6xwQAqbu67XZKlRVDaTu95hJu5}')