
def P3():
    q, e = 0, 0
    import random
    for _ in range(20):
        a = int(random.randint(1, 30))
        b = random.randint(1, 30)
        c = random.choice('+''-')

        i = a, c, b
        text = input(i)
        if str(c) == '+':
            if (int(a) + int(b)) == int(text):
                print("Верно")
                q += 1
            else:
                print("Неверно")
                e += 1
        if str(c) == "-":
            if (int(a) - int(b)) == int(text):
                print("Верно")
                q += 1
            else:
                print("Неверно")
                e += 1

    print("\nВерно:{}\nНеверно:{}".format(q, e))


if __name__ == '__main__':
    P3()