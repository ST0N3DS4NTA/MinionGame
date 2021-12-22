def minion_game(string):
    kCount = 0
    sCount = 0
    length = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(length):
        if string[i] in vowels:
            kCount += length - i
        else:
            sCount += length - i

    if kCount > sCount:
        print("Kevin", kCount)

    elif kCount < sCount:
        print("Stuart", sCount)

    elif kCount == sCount:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)