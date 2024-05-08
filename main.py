from generator import viole_rcng as viole


def test():
    print('-------------------------TESTS------------------------------')

    for i in range(5):
        test=viole.gencode(name=viole.gencode())
        print(test)

    print(60*'-')

    for i in range(5):
        test=viole.gencode()
        print(test)

    print(60*'-')

    for i in range(5):
        test=viole.gencode(x=3)
        print(test)

    print(60*'-')

    for i in range(5):
        test=viole.gencode(name='Testin-Name')
        print(test)

test()