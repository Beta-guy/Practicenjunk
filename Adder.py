# Stephanie's adder 1.1
import calclib
import csv
counter = 1
#
# User enters numbers
#
print("*" * 25)
print("* Stephanie's Adder 1.1 *")
print("*" * 25)
#
# User inputs 2 numbers
#
a = input("Enter 2 numbers seperated by comma: ").strip()
#
# finds the char seperating the numbers
#
seperator = a.index(",")
#
# grabs string and converts it to float
#
first = float(a[:seperator])
second = float(a[seperator + 1:])
#
# Calclib adds the 2 numbers and retuns it to s
#
s = calclib.add(first, second)
#
#Opens adder.csv and writes the headers and values to the file.
#
with open("adder.csv", "a") as csv_file:
    csv_write = csv.writer(csv_file)
    if counter == 1:
        csv_write.writerow(["1st digit", "2nd digit", "Sum"])
    csv_write.writerow([first, second, s])

print(s)