from viole_rcng import *


def test():
    test=Viole.gencode()
    print(test)

    print(30*'-')
    print('--- Name change ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name')
    print(test)

    print(30*'-')
    print('--- Factor change ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name', factor=1)
    print(test)

    print(30*'-')
    print('--- No LowerUpper ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name', factor=1, lu=False)
    print(test)

    print(30*'-')
    print('--- No UpperLower ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name', factor=1, ul=False)
    print(test)

    print(30*'-')
    print('--- No UpperLower and LowerUpper ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name', factor=1, lu=False, ul=False)
    print(test)

    print(30*'-')
    print('--- No UpperLower, LowerUpper and custom separator ---')
    print(30*'-')

    test=Viole.gencode(name='Testing-name', factor=1, lu=False, ul=False, separator='-')
    print(test)

    print(30*'-')
    print('--- File extension added ---')
    print(30*'-')

    test=Viole.gencode(name='Waifu2z-Upscaled-image', factor=1, lu=False, ul=False, separator='-')
    print(f'{test}.png')

test()