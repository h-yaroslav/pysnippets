


a = 0

def price(rub=a, kop=a):
    #print "%i, %i" % (rub, kop)
    return "%i, %i" % (rub, kop)

if __name__ == '__main__':
    
    print price(8, 50)
    print price(7)
    print price()
