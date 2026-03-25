
'''
a = int(input("입력 진수 결정(16/10/8/2) : "))
    b = int(input("값 입력 : "), a)

    print('16진수==> ', hex(b))
    print('10진수 ==> ', b)
    print('8진수 ==> ', oct(b))
    print('2진수 ==> ', bin(b))
'''


a = int(input("입력 진수 결정(16/10/8/2) : "))
b = input("값 입력 : ")

if a == 16:
    b = int(b,16)
elif a == 10:
    b = int(b,10)
elif a == 8:
    b = int(b,8)
elif a == 2:
    b = int(b,2)
else:
        ("숫자를 잘못 입력하셨습니다. 다시 시도해주세요.")

print('16진수==> ', hex(b))
print('10진수 ==> ', b)
print('8진수 ==> ', oct(b))
print('2진수 ==> ', bin(b))