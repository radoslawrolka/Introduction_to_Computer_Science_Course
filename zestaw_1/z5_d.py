szukana = int(input("wpisz: "))

okolo = 0.5 * szukana
lepsza = 0.5 * (okolo + szukana/okolo)
while lepsza != okolo:
    okolo = lepsza
    lepsza = 0.5 * (okolo + szukana/okolo)
print(okolo)
