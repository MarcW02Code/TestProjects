
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[0:2].isalpha():
        return False
    first_number_index = -1    
    for i in range(len(s)):
        if s[i].isdigit():
            first_number_index = i
            break
    if first_number_index != -1:
        if s[first_number_index] == '0':
            return False
        right_part = s[first_number_index:]
        if not right_part.isdigit():
            return False
    
    if not s.isalnum():
        return False

    return True

    

main()
