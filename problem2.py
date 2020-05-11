'''
Input:15
所有的數字是:1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
其中 3, 6, 9, 12 被剔除;5, 10 被剔除;但是 15 被保留
所以剩下來的數字是 1, 2, 4, 7, 8, 11, 13, 14, 15,因此
Output:9
'''
import os

if __name__ == '__main__':
    print('Input:', end='')
    number = int(input())
    print('所有的數字是:', end='')
    for i in range(number):
        if i != number-1:
            print(i+1,end=', ')
        else:
            print(i+1)
    l = []
    for i in range(1, number+1):
        if i%3 == 0 and i%5 == 0:
            l.append(i)
            continue
        else:
            if i%3 == 0 or i%5 == 0:
                continue
            else:
                l.append(i)
    print('剩下來的數字是:', end='')
    for n in l:
        if n != l[-1]:
            print(n, end=', ')
        else:
            print(n)
    print('Output:', end='')
    print(len(l))