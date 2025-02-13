
    # Creating a sample list
lst = [3, 1, 2, 2, 4]

# 1. append() - Adds an item to the end of the list
lst.append(5)
print("Append:", lst)

# 2. copy() - Returns a shallow copy of the list
lst_copy = lst.copy()
print("Copy:", lst_copy)

# 3. clear() - Removes all elements from the list
lst_clear = lst.copy()
lst_clear.clear()
print("Clear:", lst_clear)

# 4. count(value) - Returns the count of occurrences of a value
print("Count of 2:", lst.count(2))

# 5. extend(iterable) - Extends list by adding elements from an iterable
lst.extend([6, 7])
print("Extend:", lst)

# 6. index(value) - Returns the index of the first occurrence of a value
print("Index of 4:", lst.index(4))

# 7. insert(index, value) - Inserts an item at the given position
lst.insert(2, 10)
print("Insert at index 2:", lst)

# 8. pop(index) - Removes and returns item at given index (default is last)
popped_item = lst.pop()
print("Pop:", lst, "| Popped:", popped_item)

# 9. remove(value) - Removes the first occurrence of a value
lst.remove(2)
print("Remove first occurrence of 2:", lst)

# 10. reverse() - Reverses the list in place
lst.reverse()
print("Reverse:", lst)

# 11. sort() - Sorts the list in ascending order
lst.sort()
print("Sort:", lst)

# 12. min() - Returns the smallest element in the list
print("Min:", min(lst))

# 13. max() - Returns the largest element in the list
print("Max:", max(lst))
