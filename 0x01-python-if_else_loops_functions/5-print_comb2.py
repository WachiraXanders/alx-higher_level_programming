#!/usr/bin/python3
for x in range(100):
    if x <= 98:
        print('{},'.format(str(x).zfill(2)), end=' ')
    else:
        print('{}\n'.format(str(x).zfill(2)), end='')
