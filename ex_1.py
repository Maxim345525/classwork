try:
    a=int(input("Введіть ширину"))
    b=int(input("Введіть висоту"))
    for i in range(a):
        for j in range(a):
            print('*',end=" ")
        print()
except Exception as ex:
    print("Error information")
finally:
    print("Exit")


