def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception(' Side can not be <= 0 ! ')

    if a + b > c and a + c > b and b + c > a:
        print(f' \033[:34m({a} {b} {c})\033[m \033[:35m can make\033[m a triangle')
    else:
        raise Exception(f' \033[:34m({a} {b} {c})\033[m can \033[:35mNOT\033[m make a triangle')


if __name__ == '__main__':
    try:
        a = int(input(' Input the 1st side : '))
        b = int(input(' Input the 2nd side : '))
        c = int(input(' Input the 3rd side : '))
        is_triangle(a, b, c)
    except Exception as e:
        print(e)
