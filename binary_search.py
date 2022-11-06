

def binary_search(mylist, key):
    if len(mylist) > 0:
        mid = len(mylist) // 2

        if mylist[mid] == key:
            return True

        if key < mylist[mid]:
            return binary_search(mylist[:mid], key)

        if key > mylist[mid]:
            return binary_search(mylist[mid + 1:], key)

    else:
        return False


print(binary_search([5, 10, 25, 30, 40, 68], 68))

print(binary_search([35, 83, 89, 94, 99], 10))

print(binary_search([1, 1, 2, 3, 5, 8, 13, 21], 1))
