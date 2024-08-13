num = int(input())

if num % 3 == 0 and num % 5 == 0 or num == 1:
    print("False")
elif num % 3 == 0:
    print("True")
elif num % 5 == 0:
    print("True")
else:
    print("False")