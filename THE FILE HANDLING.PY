# File Handling 

# Create    => x
# Write     => w
# Update    => a
# Read      => r
# Remove

# def writeData(filename, data, filemode):
#     file = open(filename, filemode)
#     file.write(data + "\n")

# def readData(filename):
#     file = open(filename, "r")
#     print("------------DATA--------------")
#     return file.read()

# # Create a new file
# extension = ".txt"
# name = input("Enter name: ")
# filename = f"{name}{extension}"

# import os
# if os.path.exists(filename):
#     mode = input("Enter your mode (e for EDIT and d for DELETE): ")
#     if mode == "e":
#         filedata = readData(filename)
#         data = input(f"Enter data to be written in {filename}: ")
#         if len(filedata) > 0:
#             writeData(filename, data, "a")
#         else:
#             writeData(filename, data)
#         print(readData(filename))
#     elif mode == "d":
#         os.remove(filename)
#         print(f"{filename} deleted")
#     else:
#         print("Not a valid option")
# else:
#     # Create a new file
#     file = open(filename, "x")
#     data = input(f"Enter data to be written in {filename}: ")
#     writeData(filename, data, "w")
#     print(readData(filename))


# Remove
# import os
# os.remove(filename)

# Create a list of dictionary
# Accept inputs for each key on each iteration of list from user

# employees.txt

# Number of employees: 2
# ID of employee: 1
# Name of employee: ABC
# Salary of employee: 20000
# ID of employee: 2
# Name of employee: PQR
# Salary of employee: 22000

# ID of employee: 1
# Name of employee: ABC
# Salary of employee: 20000
# --------------------------------
# ID of employee: 2
# Name of employee: PQR
# Salary of employee: 22000
# --------------------------------


# EXCEPTION HANDLING

# try       => actual code
# except    => catch the exception (multiple except => named except)
# else      => if no exception, else will execute
# finally   => always gets executed

try:
    number = int(input("Enter the number: "))
    divisor = int(input("Enter the divisior: "))
    print(f"{number} / {divisor} = {number / divisor}")

    brands = ["Apple", "Google", "Microsoft"]
    brand = int(input("Enter the position of element: "))
    print(brands[brand - 1])
except ZeroDivisionError:
    print("*********** CANNOT DIVIDE BY ZERO ***********")
except IndexError:
    print("*********** NO SUCH POSITION IN LIST ***********")
except ValueError:
    print("*********** CHECK YOUR DATA TYPE ***********")
except:
    print("*********** EXCEPTION RAISED ***********")
else:
    print("---------- PROGRAM EXECUTED SUCCESSFULLY ----------")
finally:
    print("//////////// PROGRAM ENDED ////////////")