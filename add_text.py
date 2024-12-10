member = input("Add a new member: ")

# with open("/Users/simonvargas/Downloads/members.txt", "a") as file:
#     file.write(member + "\n")
#     print("Member added")

# another way to do it
file = open("/Users/simonvargas/Downloads/members.txt", "r")
exitsting_members = file.readlines()
file.close()
print(exitsting_members)
print("\n")
exitsting_members.append(member + "\n") # add a new member
print(exitsting_members)
file = open("/Users/simonvargas/Downloads/members.txt", "w")
exitsting_members = file.writelines(exitsting_members)
file.close()
