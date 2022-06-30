def decode(e, n):
    #deduce the prime values of p and q
    for i in range(1, int(pow(n, 1 / 2))):
        if n % i == 0: #check to ensure that n is devisible by i so i can know i is a factor of n
            p = i
            q = int(n / i)
            #since i now know i is a factor of n,
            # deviding n by i will give the number multiplied by i which will give n

    print("p: ", p, " q: ", q)

    phi = (p - 1) * (q - 1) #calculate phi of n
    print("phi: ", phi)

    for i in range(200):
        p1 = i * phi + 1
        d = p1 / e
        # print(d, i)
        decimal_places = str(d - int(d))[1:] #get the decimal values of the numbers
        # print(decimal_places)
        if decimal_places == ".0": # filter numbers
            print("d: ", d, " k: ", i)


if __name__ == "__main__":
    decode(31, 377)
