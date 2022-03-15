import csv
#print out instructions for user

print("Enter 1 to enter task")
print("Enter 2 to list task")
print("Enter 3 to delete task")
print("Enter 4 to delete all item")
print("Enter 5 to an item")

SEPARATOR = " at "
FILE_NAME = "task.csv"

#prompt useri for task
option = input("enter any number within 1 - 5: ")
#save task for user
if option == "1":
    file = open(FILE_NAME, "a")

    task = input("Enter an activity: ")
    time = input("What time do you want to accomplish this?: ")

    writer = csv.writer(file)
    writer.writerow([task, time])
    file.close()


#list task for user
elif option == "2":
    file = open(FILE_NAME, "r")
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        print(index + 1, SEPARATOR.join(row))

elif option == "3":
    file = open(FILE_NAME, "r")
    csv_reader = csv.reader(file)
    lists_from_csv =[]
    for index, row in enumerate(csv_reader):
        print(index + 1, SEPARATOR.join(row))
        lists_from_csv.append(row)

elif option == "4":
	file = open(FILE_NAME, 'r+')
	file.truncate(0)
	file.close()

elif option == "5":
	file = open(FILE_NAME, 'r')
	csv_reader = csv.reader(file)
	todos = []
	for index, row in enumerate(csv_reader):
		print(index + 1, SEPARATOR.join(row))
		todos.append(row)
	delete_option = input('Enter the number of the item you want to delete: ')
	# type cast to int
	delete_option = int(delete_option)
	todos.pop(delete_option - 1)
print(todos)


    # confirm = input("Enter the number of the item you want to delete: ")
    # if confirm == "all":
    #     file.clear
    #     print(lists_from_csv)
    # elif confirm == ("one") or ("1"):
    #     print(lists_from_csv)
    #     remove = input("enter task to remove: ")
    #     if remove in lists_from_csv:
    #         lists_from_csv.remove(remove)
    #     print(lists_from_csv)














