# que 1
# movies =  []
# mov1 = input("enter 1st movies: ")
# mov2 = input("enter 2nd movies: ")
# mov3 = input("enter 3rd movies: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

#que 2 palindrome mean which was same from dront and back like you shoud read from star and end it was come as same
# 1221= palindrome
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palidrome")
else:
    print("not palindrome")
    
    # que 3
    grade = ("C", "D", "A", "B", "B", "A" )
    print(grade.count("A"))