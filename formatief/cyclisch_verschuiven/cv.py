def shift(ch, n):
    if n == 0:
        return ch
    print(ch[-n:] + ch[:-n])


shift("ABCDEFG", 3)
