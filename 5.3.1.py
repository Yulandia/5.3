list_of_numbers = []

def print_sum_avg(my_list):
    summary = sum(my_list)
    av = summary / len(my_list)
    print("Summary is: ", summary)
    print("Average is: ", av)

def func():
    for i in range(1,4):
        user_input = int(input("Enter number " + str(i) + ": "))
        list_of_numbers.append(user_input)
    print_sum_avg(list_of_numbers)

func()