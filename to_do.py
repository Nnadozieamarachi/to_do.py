import csv
#print out instructions for user

print("press 1 to enter task: ")
print("press 2 to list all your activities: ")
print("press 3 to delete activity: ")
#prompt user for task
option = input("enter command: ")
#save task for user
if option == "1":
    file = open("task.csv", "a")

    task = input("daily_activities: ")
    time = input("time: ")

    writer = csv.writer(file)
    writer.writerow([task, time])
    file.close()
            
    
#list task for user
elif option == "2":
    file = open("task.csv", "r")
    csv_reader = csv.reader(file)
    lists_from_csv =[]
    for row in csv_reader:
        lists_from_csv.append(row)
        
    print(lists_from_csv)
elif option == "3":
    file = open("task.csv", "r+")
    csv_reader = csv.reader(file)
    lists_from_csv =[]
    for row in csv_reader:
        lists_from_csv.append(row)
        
    print("type 'all' to delete all activities ")
    print("type 'one' to delete only one file")
    confirm = input("clear all task or one task?: ")
    if confirm == "all":
        # file = open("task.csv", "r+")
        file.truncate(0)
        file.close()
        print(lists_from_csv)
    elif confirm == ("one") or ("1"):
        print(lists_from_csv)
        remove = input("enter task to remove: ")
        if remove in lists_from_csv:
            lists_from_csv.remove(remove)
        print(lists_from_csv)