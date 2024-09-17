import csv
import os


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
            createFile = input(
                f"Would you like to create a file named {fileName}? y/n "
            )
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
    remove = "remove"

    goodInput = False

    while goodInput == False:
        selected = int(
            input(
                "0 to read assignments, 1 to add assignments, 2 to remove assignments: "
            )
        )
        try:
            if selected == 0:
                goodInput = True
                return open
            elif selected == 1:
                goodInput = True
                return write
            elif selected == 2:
                goodInput = True
                return remove
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


def getLastId(fileName):
    if not os.path.exists(fileName):
        return 0  # If the file doesn't exist, start from 0

    with open(fileName, "r") as myFile:
        csvReader = csv.reader(myFile)
        rows = list(csvReader)

        if len(rows) > 1:  # Check if there are any data rows
            last_row = rows[-1]
            return int(last_row[0])  # Return the ID from the last row
        else:
            return 0  # If no data rows, start from 0


def writeToFile(fileName):
    previousID = getLastId(fileName)
    isOneClass = input("Is this for one class (y/n)")
    isOneClass.strip().lower()
    if isOneClass == "y":
        subject = input("Enter class: ")
        isClassTrue = True
    else:
        subject = subject
    with open(fileName, "w") as myFile:
        endOfInput = False
        csvField = ["ID", "Class", "Task", "Due date"]
        rows = [[]]
        csvWriter = csv.writer(myFile)
        csvWriter.writerow(csvField)

        while endOfInput == False:
            previousID += 1
            rows[0].append(previousID)
            if isClassTrue:
                rows[0].append(subject)
            else:
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


def removeFromFile(fileName, task_id):
    if not os.path.exists(fileName):
        print(f"File {fileName} does not exist.")
        return

    with open(fileName, "r") as myFile:
        csvReader = csv.reader(myFile)
        rows = list(csvReader)

    header = rows[0]
    updated_rows = [header]

    task_found = False
    for row in rows[1:]:
        row_id = int(row[0])

        if row_id == task_id:
            task_found = True
            adjust_ids = True
        elif adjust_ids:
            row[0] = str(row_id - 1)
            updated_rows.append(row)
        else:
            updated_rows.append(row)

    if task_found:
        with open(fileName, "w", newline="") as myFile:
            csvWriter = csv.writer(myFile)
            csvWriter.writerows(updated_rows)
        print(f"Task with ID {task_id} removed.")
    else:
        print(f"Task with ID {task_id} not found.")


def isStillWorking():
    isStillWorking = input("Anything else to modify y/n? ")
    isStillWorking.strip().lower()

    if isStillWorking == "y":
        return True
    else:
        return False


def main():
    stillWorking = True
    fileName = getFileName()
    while stillWorking:
        option = options()
        if option == "open":
            OpenFile(fileName)
            stillWorking = isStillWorking()
        elif option == "write":
            writeToFile(fileName)
            stillWorking = isStillWorking()
        elif option == "remove":
            task_id = int(input("Which task to remove?: "))
            removeFromFile(fileName, task_id)
            stillWorking = isStillWorking()


main()
