print("Enter number: ")
number = input()

print("Enter start of range: ")
start_of_range = input()

print("Enter end of range: ")
end_of_range = input()


def in_range(number, start_of_range, end_of_range):
    if int(number) >= int(start_of_range) and int(number) <= int(end_of_range):
        print("Number is within given range")
    else:
        print("Number is not within given range")


in_range(int(number), int(start_of_range), int(end_of_range))