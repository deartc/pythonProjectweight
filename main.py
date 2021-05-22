# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.def bmi_intro():
    print("Welcome to my BMI calculator!")
    print("If you can tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Let's Start!\n")

def main():
    bmi_intro()
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = float(input("Please enter your height in inches. "))
    get_weight = float(input("Please enter your weight in pounds. "))
    body_mass_index = (get_weight * 703) / (get_height ** 2)
    if body_mass_index < 18.5:
        print("A person with a BMI of " + str(body_mass_index ) + " is underweight ")
    elif body_mass_index < 24.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is normal weight ")
    else:
        print("A person with a BMI of " + str(body_mass_index ) + " is overweight ")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('BMI user')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
