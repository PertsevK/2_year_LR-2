import _2_year_LR_2

# Меню
choice = int(input("Please, choose the task 1-3 (0-EXIT): "))
while choice:
    if choice==1:
        _2_year_LR_2.task_if6()
    elif choice==2:
        _2_year_LR_2.task_geom19()
    elif choice==3:
        _2_year_LR_2.task_series10()
    else:
        print("Wrong task number!")
    choice = int(input("Please, choose the task again (0-EXIT): "))
print("Good bye!")
