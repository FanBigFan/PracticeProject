def get_count(s, ch):
    count = 0
    for j in s:
        if ch.upper() == j or ch.lower() == j:
            count += 1
    return count


if __name__ == '__main__':
    s = 'hello python'
    ch = input(' Input the character to count : ')
    count = get_count(s, ch)
    print(f' character ({ch}) counts [{count}] in (hello python)')
