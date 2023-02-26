# import random


def base_conversion():
    num = int(input(' Input a metric num to conversion : '))
    print(f' ({num}) to binary      is : ', bin(num))
    print(f' ({num}) to octal       is : ', oct(num))
    print(f' ({num}) to hexadecimal is : ', hex(num))

    # guess number
    # rand = random.randint(1000, 1200)
    # a = int(input(' rand : '))
    # if a > rand:
    #     print(' big')
    # elif a < rand:
    #     print(' small')
    # else:
    #     print(a)
    # print(rand)


if __name__ == '__main__':
    while True:
        try:
            base_conversion()
            break
        except BaseException as e:
            print(e)
