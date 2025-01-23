print("Grasp the Contain Duplicate Problem")
print("Familarize yourself with pythoon lists")

# Activities:

# Coding Exercise:
# Create Python lists with various elements, including duplicates.
# Practice list operations: adding, removing, slicing, and accessing elements.
# Write a simple script to print each element in the list.

def showList(myList):
    for list in myList:
        print(list, end=' ')
    print()


myList = [0,2,3,4,5,9,1]


showList(myList)
myList.append(5)
showList(myList)
myList.remove(2)
showList(myList)
newlist = myList[0:4]
showList(newlist)
item = newlist[2]
print(item)

# Homework:

# Write a Python program that accepts user input to create a list 
# and then prints all elements

class MyList():
    def __init__(self):
        self.thisList = []

    def addList(self , item):
        self.thisList.append(item)

    def showList(self):
        for element in self.thisList:
            print(element, end=' ')
        print()


def main():

    newList = MyList()
    count = 0

    while count < 4:
        
        user_input = input("Enter a number to add to list")

        newList.addList(user_input)
        count += 1

    print("The Elements in the list")
    newList.showList()


if __name__ == "__main__":
    main()