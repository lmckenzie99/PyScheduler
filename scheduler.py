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
            print("File not found.\n")


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
    with open(fileName, 'r') as myFile:
        for line in myFile:
            line = line.strip()
            print(line)
    return


def writeToFile():
    print("Write file")
    return


def main():
    fileName = getFileName()
    option = options()
    if option == "open":
        OpenFile(fileName)
    elif option == "write":
        writeToFile()


main()
