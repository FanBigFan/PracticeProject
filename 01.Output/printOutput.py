import os

ofs = open('output.txt', 'w')
print('hello python', file=ofs)
ofs.close()

with open('output1.txt', 'w') as ofs1:
    print('hello python 1111', file=ofs1)
