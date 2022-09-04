a = int(input())
z = input()
b = int(input())
match z[0]:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)