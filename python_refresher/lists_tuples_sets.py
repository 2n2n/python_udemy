my_variable = "hello"

grades = [77, 80, 90, 95, 100] # most flexible of the three
tuple_grades = (77, 80, 90, 95, 100) # immutable
set_grades = { 77, 80, 90, 100, 100 } # unique & unordered

# grades.append(50)
# tuple_grades  = tuple_grades + (98,)
# print( grades )
# print( tuple_grades )

# grades[0] = 60
# print(grades)

## set operations

your_lottery_numbers = {1,2,3,4,5}
winning_number = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_number))
print(your_lottery_numbers.union(winning_number))
print({1,2,3,(1,2,),(3,4,)}.difference({(3,4,), 1}))



# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [50,100,-50]
# Create a tuple, called my_tuple, with a single value in it
my_tuple = (1,)
# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
set2 = set1.intersection(set2)
print(set2)
