# numbers = []
# for i in range(5):
#     num = int(input("Enter number: "))
#     numbers.append(int)
# print(numbers)    

#insert():-
friends =[]
friends =(["Satya", "Tiger", "Shivali"])
print(friends)
friends.insert(1, "Nilam")
print(friends)
friends.insert(-1, "Nilakshi")
print(friends)

# REmove:-
friends = (["Satya", "Tiger", "Shivali"])
print(friends)
del friends[2]

if "Tiger" in friends:
    friends.remove("Tiger")
print(friends)    


# POP():-
# Remove an element with specified index and return the value which was removed.
friends = (["Satya", "Tiger", "Shivali"])
print(friends)

removed_friends = friends.pop(1)
print(friends)
print(f"The removed friend was {removed_friends}") 

# index():-
# GEt the the position of friend:-
friends =(["Satya", "Tiger", "Shivali"])
print(friends)
print(friends.index("Shivali"))

# Count():-Get the number of presence of an element in the list:-
friends =(["Satya", "Tiger", "Shivali"])
print(friends.count("Satya"))

# Sort():-
numbers = [5,7,6,4,7,3,5,6,6,5,3,4,5,7,3,5,6,8,6,2,4,5,1,3,4,2,2,3,3,8,5,6,9]
print(numbers)
# Ascending numbers:-
numbers.sort()
print(numbers)
# Descending Numbers:-
numbers.sort(reverse=True)
print(numbers)


# reverse():-
numbers = [7,8,6,2,4,5,1,3,4,2,2,9]
print(numbers)
numbers.reverse()
print(numbers)

# copy:-


# What is the meaning of "DEEP COPY":-
# "DEEP COPY" "SHALLOW COPY":-
