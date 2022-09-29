arr1 = [2,4,6,10]
arr2 = [7,6,9,5,10,2,1,3,4,8]

def is_match(arr1,arr2):
    arr1Sort = sorted(arr1)
    arr2Sort = sorted(arr2)
    shiftCounter = 0
    counter = 0

    for i in arr1Sort:
        while True:
            if shiftCounter > len(arr2) and i != arr2Sort[shiftCounter]:
                return False
            elif i < arr2Sort[shiftCounter]:
                return False                
            elif i != arr2Sort[shiftCounter] and i > arr2Sort[shiftCounter]:
                shiftCounter += 1
                print("shift:" + str(shiftCounter))
            else:
                shiftCounter += 1
                print("shift:" + str(shiftCounter))
                counter += 1
                print(str(i) + " passed")
                break
        if counter == (len(arr1)):
            return True


print(is_match(arr1,arr2))


# def is_match(arr2,arr1):
#     arr1Sort = sorted(arr1)
#     arr2Sort = sorted(arr2)
#     shiftCounter = 0
#     counter = 0

#     if len(arr1) > len(arr2):
#         return False
#     else:
#         for i in arr1Sort:
#             while True:
#                 if shiftCounter > len(arr2) and i != arr2Sort[shiftCounter]:
#                     return False
#                 elif i < arr2Sort[shiftCounter]:
#                     return False                
#                 elif i != arr2Sort[shiftCounter] and i > arr2Sort[shiftCounter]:
#                     shiftCounter += 1
#                 else:
#                     shiftCounter += 1
#                     counter += 1
#                     break
#             if counter == (len(arr1)+1):
#                 return True