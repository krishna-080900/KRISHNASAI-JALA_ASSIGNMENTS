#3.12  Print gender (Male/Female) program according to given M/F using switch


def check_gender(gender_code):
    switch = {
        'M': "Male",  # 'M' maps to Male
        'F': "Female"  # 'F' maps to Female
    }
    return switch.get(gender_code.upper(), "Invalid input")

gender_code = input("Enter gender (M/F): ")

print(f"The gender is {check_gender(gender_code)}.")
