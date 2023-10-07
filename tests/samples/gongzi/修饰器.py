"""
Author:Qychui
DATE:2023/9/27 14:38
File:修饰器.py
"""
def funA(desA):
    print("It's funA")
    print('---')
    print(desA)
    desA()
    print('---')

def funB(desB):
    print("It's funB")

@funB
@funA
def funC():
    print("It's funC")

if __name__ == '__main__':
    funC