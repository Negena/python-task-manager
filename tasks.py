stop = False 
all_tasks = []

while stop == False: 
    task = input("s")
    all_tasks.append(task) 

    if (task == "stop"): 
        stop = True 
        break

    if(task == "view"):
        all_tasks.remove("view")
        print(all_tasks)

    if (task == "help"): 
        print("type: \n 'stop' to terminate the tasks \n 'view' to see all your tasks")
    
    if (task == "clear"): 
        stop = True
        confirm = input("are you sure you wanna delete all your records of task management ? \n y/n \n")
       
    
        if(confirm == 'y'): 
            all_tasks.clear()
            print("your tasks are cleared..") 
            stop = False      

        if(confirm == "n"):
            print("canceled")

        stop = False 
      

    else:
        task