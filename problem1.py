import os

if __name__ == '__main__':
    print("Enter the string you want to reverse.")
    s = input()
    outs = list(map(lambda x: x[::-1], s.split()))
    for out in outs:
        print(out, end=' ')
    print()
    
