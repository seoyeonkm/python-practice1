option = input("1. 입력한 수식 계산 2. 두 수 사이의 합계: ")


if option == '1':
    expr = input("*** 수식을 입력하세요: ")

    num = ""
    result = 0
    op = "+"

    for ch in expr:
        if ch in "+-*/":
            if op == "+":
                result += int(num)
            elif op == "-":
                result -= int(num)
            elif op == "*":
                result *= int(num)
            elif op == "/":
                result /= int(num)

            op = ch
            num = ""
        else:
            num += ch

    
    if op == "+":
        result += int(num)
    elif op == "-":
        result -= int(num)
    elif op == "*":
        result *= int(num)
    elif op == "/":
        result /= int(num)

    print("결과:", result)



elif option == '2':
    num1 = int(input("*** 첫 번째 숫자를 입력하세요: "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요: "))

    sum = 0
    for i in range(num1, num2 + 1):
        sum += i

    print("%d + ... + %d = %d" % (num1, num2, sum))



else:
    print("1 또는 2를 다시 입력해주세요.")

