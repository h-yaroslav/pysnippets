
def ip_range2cidr(start, end):
    """
    Convert an ip range to a cidr.
    """
    stack = []
    while True:
        h = 1
        p = 0
        x = start^end
        while x:
            x >>= 1
            h <<= 1
            p += 1
        if end - start + 1 == h:
            yield (start, 32 - p)
            if stack:
                start, end = stack.pop()
            else:
                break
        else:
            d = start | ((h >> 1) - 1)
            stack.append((d+1, end))
            end = d
if __name__ == '__main__':
    for i in ip_range2cidr(1178493772, 1178493772+256):
        print i

