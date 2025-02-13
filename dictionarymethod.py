# Creating two sample sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. add(value) - Adds an element to the set
set1.add(7)
print("Add 7:", set1)

# 2. remove(value) - Removes a specific element (raises an error if not found)
set1.remove(2)
print("Remove 2:", set1)

# 3. clear() - Removes all elements from the set
set_clear = set1.copy()
set_clear.clear()
print("Clear:", set_clear)

# 4. pop() - Removes and returns a random element
popped_item = set1.pop()
print("Pop:", set1, "| Popped:", popped_item)

# 5. union(set) - Returns a new set containing all elements from both sets
set_union = set1.union(set2)
print("Union:", set_union)

# 6. intersection(set) - Returns a new set containing only common elements
set_intersection = set1.intersection(set2)
print("Intersection:", set_intersection)

# 7. symmetric_difference(set) - Returns a set with elements that are in either set, but not both
set_sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", set_sym_diff)

# 8. difference(set) - Returns a set with elements that are in the first set but not in the second
set_diff = set1.difference(set2)
print("Difference (set1 - set2):", set_diff)

# 9. isdisjoint(set) - Returns True if sets have no common elements
is_disjoint = set1.isdisjoint(set2)
print("Is Disjoint:", is_disjoint)
