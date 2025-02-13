def list_operations():
    lst = [3, 1, 2, 2, 4]
    lst.append(5)
    lst.remove(2)
    lst.sort()
    print("List Operations:", lst)

def tuple_operations():
    tpl = (3, 1, 2, 2, 4)
    print("Tuple Count of 2:", tpl.count(2))
    print("Tuple Index of 4:", tpl.index(4))
    print("Tuple Max:", max(tpl))
    print("Tuple Min:", min(tpl))
    print("Tuple Length:", len(tpl))

def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.add(7)
    set1.remove(2)
    set_union = set1.union(set2)
    set_intersection = set1.intersection(set2)
    print("Set Operations:")
    print("Updated Set1:", set1)
    print("Union:", set_union)
    print("Intersection:", set_intersection)

def main():
    print("Executing List Operations...")
    list_operations()
    
    print("\nExecuting Tuple Operations...")
    tuple_operations()
    
    print("\nExecuting Set Operations...")
    set_operations()

if __name__ == "__main__":
    main()
