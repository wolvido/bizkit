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

from data.search_data import USERS

def search_users(args):
    output = []
    if "id" in args:
        for x in USERS:
            if x["id"] == args["id"]:
                output.append(x)
    if "name" in args:
        for x in USERS:
            if args["name"].lower() in x["name"].lower():
                output.append(x)
    if "age" in args:
        for x in USERS:
            if (x["age"] == args["age"] or x["age"] == args["age"]-1 or x["age"] == args["age"]+1) and x not in output:
                output.append(x)
    if "occupation" in args:
        for x in USERS:
            if  args["occupation"].lower() in x["occupation"].lower():
                output.append(x)
    return output

print(search_users({
    "id":"5",
    "name":"Joe",
    "age": 30,
    "occupation":"Arc"
}))















# dragon = {
#   "id": "2",
#   "name": "John"
# }

# if "name" in dragon:
#     print(dragon["id"])

# test = [3]
# test2 = iter(test)

# print(next(test2))

# text = [1,3,'a','e']
## numbers = [x for x in text if x.isdigit()]

# output.append(next((x for x in USERS if x["age"] == args["age"]),None))

# age = []
# for x in USERS:
#     if x["age"] == args["age"]:
#         age.append(x)


# x for x in USERS if x["age"] == args["age"]



# numbers = []
# for x in text:
#     if isinstance(x, int):
#         numbers.append(x)

# print(numbers)