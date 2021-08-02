list_of_numbers = []

def print_sum_avg(*args):
    summary = 0
    for i in args:
        summary += i
    av = summary / len(args)
    print("Summary is: ", summary)
    print("Average is: ", av)

print_sum_avg(1,2, 4, 5)
print_sum_avg(66,77)

