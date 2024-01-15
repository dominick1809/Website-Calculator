# Import the Tkinter module for creating the GUI window
import tkinter as tk

# Define the Calculator class
class Calculator:
    def __init__(self, master):
        # Initialize the entry_value as an empty string
        self.entry_value = ''
        
        # Initialize the Tkinter StringVar 'equation' to display the calculator input
        self.equation = tk.StringVar()

        # Create a Frame to hold the calculator buttons
        frame = tk.Frame(master)
        frame.pack()

        # Function to display a value on the calculator
        def show(value):
            # Concatenate the input value (converted to a string) to the existing entry_value
            self.entry_value += str(value)
            
            # Update the Tkinter StringVar 'equation' with the modified entry_value
            self.equation.set(self.entry_value)

        # Function to clear the calculator display
        def clear():
            # Reset the entry_value to an empty string
            self.entry_value = ''
            
            # Update the Tkinter StringVar 'equation' to reflect the cleared entry_value
            self.equation.set(self.entry_value)

        # Function to solve the current calculation
        def solve():
            # Evaluate the mathematical expression stored in entry_value and store the result
            result = eval(self.entry_value)
            
            # Update the Tkinter StringVar 'equation' with the result of the evaluation
            self.equation.set(result)

        # Create and place the calculator buttons
        Button(width = 11, height = 4, text = '3', relief = 'raised', bg = 'gray', command = lambda: show(3)).place(x=180, y=125)
        Button(width = 11, height = 4, text = '4', relief = 'raised', bg = 'gray', command = lambda: show(4)).place(x=0, y=200)
        Button(width = 11, height = 4, text = '5', relief = 'raised', bg = 'gray', command = lambda: show(5)).place(x=90, y=200)
        Button(width = 11, height = 4, text = '6', relief = 'raised', bg = 'gray', command = lambda: show(6)).place(x=180, y=200)
        Button(width = 11, height = 4, text = '7', relief = 'raised', bg = 'gray', command = lambda: show(7)).place(x=0, y=275)
        Button(width = 11, height = 4, text = '8', relief = 'raised', bg = 'gray', command = lambda: show(8)).place(x=90, y=275)
        Button(width = 11, height = 4, text = '9', relief = 'raised', bg = 'gray', command = lambda: show(9)).place(x=180, y=275)
        Button(width = 11, height = 4, text = '0', relief = 'raised', bg = 'gray', command = lambda: show(0)).place(x=90, y=350)
        Button(width = 11, height = 4, text = '.', relief = 'raised', bg = 'gray', command = lambda: show('.')).place(x=180, y=350)
        Button(width = 11, height = 4, text = '+', relief = 'raised', bg = 'gray', command = lambda: show('+')).place(x=270, y=350)
        Button(width = 11, height = 4, text = '-', relief = 'raised', bg = 'gray', command = lambda: show('-')).place(x=270, y=275)
        Button(width = 11, height = 4, text = '/', relief = 'raised', bg = 'gray', command = lambda: show('/')).place(x=270, y=50)
        Button(width = 11, height = 4, text = 'x', relief = 'raised', bg = 'gray', command = lambda: show('*')).place(x=270, y=125)
        Button(width = 11, height = 4, text = '=', relief = 'raised', bg = 'purple', command = solve).place(x=270, y=350)
        Button(width = 11, height = 4, text = 'C', relief = 'raised', bg = 'blue', command = clear).place(x=0, y=350)

# Initialize the Tkinter GUI window
root = tk.Tk()

# Create a Calculator instance and associate it with the GUI window
calculator = Calculator(root)

# Start the GUI window's main loop
root.mainloop()