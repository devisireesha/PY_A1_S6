# Example of a class
"""a class is a blueprint for creating objects that share a common structure and behavior."""
# Define a class called Person
class Person:
    # Define a constructor method that takes a name and age
    def __init__(self, name, age):
        # Set the name attribute to the name argument
        self.name = name
        # Set the age attribute to the age argument
        self.age = age

    # Define a method called introduce
    def introduce(self):
        # Print out a message that introduces the person's name and age
        print("Hi, my name is", self.name, "and I am", self.age, "years old.")


# Create a Person object with the name "John" and age 30
p1 = Person("John", 30)
# Call the introduce method on the p1 object
p1.introduce()

# Create another Person object with the name "Jane" and age 25
p2 = Person("Jane", 25)
# Call the introduce method on the p2 object
p2.introduce()
