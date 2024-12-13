member = input("Add a new member: ")

# with open("/Users/simonvargas/Downloads/members.txt", "a") as file:
#     file.write(member + "\n")
#     print("Member added")

# another way to do it
file = open("/Users/simonvargas/Downloads/members.txt", "r")
existing_members = file.readlines()
file.close()
print(existing_members)
print("\n")
existing_members.append(member + "\n") # add a new member
print(existing_members)
file = open("/Users/simonvargas/Downloads/members.txt", "w")
exitsting_members = file.writelines(existing_members)
file.close()
