T=0
divide=0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
        try:
            n = int(num) 
            T=T+n
            divide=divide+1
        except ValueError:
            print('Invalid input')
print(T/divide)