import csv
a = 0
b = 1
def fib():
    global a, b
    c = a + b
    a = b
    b = c
    return(c)
limit = int(input("How many fibonacci numbers do you want me to count to? "))
counter = 2
with open("test.csv", "w") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(["Counter", "Numbers", "Digits"])
    csv_write.writerow([1, 1, 1])
    print("# 1  =  1 has  1  digits")
    while counter <= limit:
        c = fib()
        if counter == limit + 1:
            quit(0)
        digits = len(str(c))
        csv_write.writerow([counter, c, digits])
        print("#", counter, " = ", c, "has ", digits, " digits")
        counter +=1
