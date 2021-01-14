def file():
    a = open(list[1], "r")       # opens the file in read mode
    b = a.readlines()            # stores the content of file in b
    a.close()                    # close the file
    return b                     # return the value of b


def result():
    if list[0] == "numrows":                # checking the command
        rows = 0
        for i in b:
            rows = rows + 1
        print(rows)                         # print the number of lines in the given file.
    else:
        col = [len(i.split()) for i in b]
        print(max(col))                     # print maximum number of words that a row has in the given file


try:
    while True:
        a = input()                                                 # enter the input
        if a == "exit":
            exit()                                                  # terminates the code

        list = a.split()                                            # splits the entered input

        if list[1] == "test.txt" or list[1] == "anothertest.txt":   # checks the filename
            b = file()                                              # call file function
        else:
            print("File Not Found")                                 # print if the filename is not found
            break

        if list[0] == "numrows" or list[0] == "numcols":            # checks the command
            result()                                                # call result function
        else:
            print("Incorrect command")                              # print if the command is not found
            break

except IndexError:                                                  # print if the syntax is not correct
    print('Incorrect command')
