import csv

def getFileName():
    goodFile = False

    while goodFile == False:
        fileName = input("Enter file name: ")
        try:
            myFile = open(fileName, "r")
            myFile.close()
            print("File found.")
            goodFile = True
            return fileName
        except FileNotFoundError:
            print("File not found.\n ")
            createFile = input(f"Would you like to create a file named {fileName}? y/n ")
            if createFile == "y":
                goodFile = True
                newFileName = open(fileName, "a")
                newFileName.close()
                return fileName
            else:
                goodFile = False


def options():

    open = "open"
    write = "write"

    goodInput = False

    while goodInput == False:
        selected = int(input("0 to read assignments, 1 to add assignments: "))
        try:
            if selected == 0:
                goodInput = True
                return open
            elif selected == 1:
                goodInput = True
                return write
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input")


def OpenFile(fileName):
    print(f"Opening {fileName} to read.")
    with open(fileName, "r") as myFile:
        for line in myFile:
            line = line.strip()
            print(line)
    return


def writeToFile(fileName):
    with open(fileName, 'w') as myFile:
        endOfInput = False
        csvField = ["Class", "Task", "Due date"]
        rows = [
            []
        ]
        csvWriter = csv.writer(myFile)
        csvWriter.writerow(csvField)

        while endOfInput == False:
            subject = input("Enter class: ")
            rows[0].append(subject)
            task = input("Enter task: ")
            rows[0].append(task)
            dueDate = input("Enter due date(mm.dd): ")
            rows[0].append(dueDate)
            isEndInput = input("Any other tasks y/n? ")
            isEndInput.strip().lower()
            csvWriter.writerows(rows)
            if isEndInput == "n":
                endOfInput = True
            else:
                rows[0].clear()
                endOfInput = False
    return


def main():
    fileName = getFileName()
    option = options()
    if option == "open":
        OpenFile(fileName)
    elif option == "write":
        writeToFile(fileName)


main()
