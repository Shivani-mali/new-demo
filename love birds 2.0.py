from tkinter import *
import random

# Create GUI window
root = Tk()
root.geometry('400x500')
root.title('Love Calculator 💖')

# Set a solid color background for the main window
root.configure(bg='#f8e1e1')

# Function to calculate love percentage and display message
def calculate_love():
    name1_str = name1.get()
    name2_str = name2.get()
    
    if name1_str == "" or name2_str == "":
        result.config(text="Please enter both names.")
        message.config(text="")
        return
    
    # Generate a unique seed based on names
    random.seed(name1_str + name2_str)
    love_percentage = random.randint(0, 100)
    
    # Display the love percentage
    result.config(text=f"Love Percentage: {love_percentage}%")
    
    # Display a playful message based on the percentage
    if love_percentage > 80:
        msg = "A match made in heaven! 💕"
    elif love_percentage > 60:
        msg = "There's a strong connection! 💖"
    elif love_percentage > 40:
        msg = "There's some potential! 💞"
    elif love_percentage > 20:
        msg = "Keep working on it! 💘"
    else:
        msg = "It might need some more work! 💔"
    
    message.config(text=msg)

# Heading
heading = Label(root, text='Love Calculator - How much is he/she into you?', font=('Helvetica', 16, 'bold'), bg='#f8e1e1')
heading.pack(pady=10)

# Tagline
tagline = Label(root, text='Find out your love compatibility with a fun percentage!', font=('Helvetica', 12), bg='#f8e1e1', fg='#d1547d')
tagline.pack(pady=5)

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", font=('Helvetica', 12), bg='#f8e1e1')
slot1.pack(pady=5)
name1 = Entry(root, border=5, width=25)
name1.pack(pady=5)

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner's Name:", font=('Helvetica', 12), bg='#f8e1e1')
slot2.pack(pady=5)
name2 = Entry(root, border=5, width=25)
name2.pack(pady=5)

# Calculate button
bt = Button(root, text="Calculate", height=2, width=15, command=calculate_love, bg='#d1547d', fg='white', font=('Helvetica', 12, 'bold'))
bt.pack(pady=10)

# Result label
result = Label(root, text='Love Percentage will appear here.', font=('Helvetica', 14, 'bold'), bg='#f8e1e1')
result.pack(pady=10)

# Message label
message = Label(root, text='', font=('Helvetica', 12), bg='#f8e1e1', fg='#d1547d')
message.pack(pady=5)

# Start the GUI
root.mainloop()
