from tkinter import Tk, Entry, Button, StringVar


# Create a Calculator class with a constructor that takes a master Tkinter window as input
class Calculator:
    def __init__(self, master):
        # Initialize the master window
        self.master = master
        self.master.title("Calculator")
        self.master.geometry('357x420+0+0')
        self.master.config(bg ='#17161b')
        self.master.resizable(False, False)

        # Create a StringVar object to store the value of the calculator's display
        self.equation = StringVar()
        # Initialize an empty string to store the current entry value
        self.entry_value = ''
        # Create an Entry widget with the specified properties and add it to the master window
        Entry(width=17, bg='lightgreen', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Create a CalculatorUI object and pass the master window and the Calculator object as input
        self.ui = CalculatorUI(self.master, self)

    # Define a method to display a value on the calculator's display
    def show(self, value):
        # Append the input value to the current entry value
        self.entry_value += str(value)
        # Update the StringVar object with the new entry value
        self.equation.set(self.entry_value)

    # Define a method to clear the calculator's display
    def clear(self):
        # Reset the entry value to an empty string
        self.entry_value = ''
        # Update the StringVar object with the new entry value
        self.equation.set(self.entry_value)

    # Define a method to evaluate the current entry value and display the result
    def solve(self):
        # Evaluate the entry value as a Python expression
        result = eval(self.entry_value)
        # Update the StringVar object with the result
        self.equation.set(result)