def count_upper_lower_case(input_string):
    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        
    return uppercase_count, lowercase_count

def main():
    input_string = input("Enter a string: ")

    uppercase_count, lowercase_count = count_upper_lower_case(input_string)

    print("تعداد حروف بزرگ:", uppercase_count)
    print("تعداد حروف کوچک:", lowercase_count)

if __name__ == "__main__":
    main()