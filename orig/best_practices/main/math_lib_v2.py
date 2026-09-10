def list_sum(L):
    s = 0
    for l in L:
        s += l
    return s


def list_product(L):
    s = 1
    for l in L:
        s *= l
    return s

def main():
    V = [1, 2, 3, 4, 5, 6]

    print(list_sum(V))
    print(list_product(V))

if __name__ == '__main__':
    main()
