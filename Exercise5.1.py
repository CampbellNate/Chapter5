num = input("Enter a number: ")
count=0
total=0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
        try:
            n = int(num) 
            count=count+1
            total=total+n
        except ValueError:
            print('bad data')
print(total,count,total/count)