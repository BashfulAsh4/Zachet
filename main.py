line_str = "Цифр в строке:"
n=int(input("Ввести цифры:"))
count=0
while n>0:
    count=count+1
    n=n//10
print(line_str,count)