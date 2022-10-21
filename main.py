from functions import *

def main(input_file_name):
    schedules = file_to_dict(input_file_name)

    if schedules==None:
        print(input_file_name+" does not exist.")
        return 1

    employees_name = list(schedules.keys())
    if len(employees_name)<5:
        print("**Input file needs at least five sets of data.**")
        return 1

    i=0
    while i < len(employees_name):
        pivot = employees_name[i]
        for employee in employees_name:
            if pivot!= employee:
                match = is_a_match(pivot,employee,schedules)
                if match>0:
                    print("{}-{}: {}".format(pivot,employee,match))
        employees_name.remove(pivot)
        i+=1
    return 0

if __name__ == "__main__":

    input_file_name = input("Insert input filename: ")

    main(input_file_name)