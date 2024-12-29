#12.4 Write a program which illustrates the concept of attributes of a constructor.

class Car:
    # Constructor with attributes (attributes initialized in the constructor)
    def __init__(self, make, model, year):
        self.make = make  # Attribute to store the make of the car
        self.model = model  # Attribute to store the model of the car
        self.year = year  # Attribute to store the year of manufacture

    # Method to display the car's details
    def display_info(self):
        print(f"Car Information:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    # Method to change the year (an example of modifying an attribute)
    def update_year(self, new_year):
        self.year = new_year
        print(f"Year updated to: {self.year}")


# Main program to demonstrate constructor attributes
def main():
    # Create a Car object and initialize its attributes
    car1 = Car("Audi", "Q7", 2024)

    # Display the car's information
    car1.display_info()

    # Modify one of the attributes (year)
    car1.update_year(2024)

    # Display the updated information
    car1.display_info()


if __name__ == "__main__":
    main()
