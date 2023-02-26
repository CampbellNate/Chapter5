largest = None
smallest = None
num = input("Enter a number: ")
try:
    n=int(num)
    largest=n
    smallest=n
except ValueError:
    print('Invalid input')
    num = input("Enter a number: ")
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
        try:
            n = int(num) 
            if n > largest:
                largest = n
            if n < smallest:
                smallest = n
        except ValueError:
            print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)