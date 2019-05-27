def convert_dates_to_coconuts(count):
    if count < 0:
        return 0
    papaia = count // 7
    banaan = papaia // 5
    kookos = banaan*2 // 3
    return int(papaia) + int(banaan) + int(kookos)
