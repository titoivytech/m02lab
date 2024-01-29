# jose Solis
#m02 LAB
#01/28/2024
# accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
def main():
    # Infinite loop to continuously process student records
    while True:
        # Prompt for the student's last name
        last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")
        
        # Check if the user wants to quit
        if last_name == 'ZZZ':
            print("Exiting program. Goodbye!")
            break  # Exit the loop if 'ZZZ' is entered

        # Prompt for the student's first name
        first_name = input("Enter the student's first name: ")
        
        # Prompt for the student's GPA as a float
        gpa = float(input("Enter the student's GPA: "))

        # Test if the student qualifies for the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        # Test if the student qualifies for the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        # If GPA is below 3.25, the student does not qualify
        else:
            print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()  # Call the main function when the script is run
