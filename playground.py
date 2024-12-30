#print("hello " + input("What is your name?"))
#
# name = input("What is your name?")
#
# print(name)


# print(len(input("What is your name?")))

# weight = float(input("What is your weight in kg?"))
# height = float(input("What is your height in m?"))

# bmi = weight / height ** 2
# print(bmi)

# print(round(bmi, 2))

# filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

# for filename in filenames:
#     filename = filename.replace('.', '-', 1)
#     print(filename)


# connection_attempts = 0

# while connection_attempts < 3:
#     print("Attempting to connect...")
#     connection_attempts += 1  

# Assign `allow_list` to a list of IP addresses that are allowed to log in

# allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
#               "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# # Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

# ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
#                 "192.168.205.12", "192.168.200.48"]

# # For each IP address in the list of IP addresses from which users have tried to log in, 
# # If it is among the allowed addresses, then display “IP address is allowed”
# # Otherwise, display “IP address is not allowed”
               
# # for ip_address in ip_addresses:
# #     if ip_address in allow_list:
# #         print("IP address is allowed")
# #     else:
# #         print(ip_address + " :IP address is not allowed")
# #         break

# i = 5000

# while i < 5150:
#     if i % 5 == 0:
#         print(i)
#     i += 1

# for i in range(1,4):
#     print(i)

# def greet_employee(name):
#     print("Welcome! " + name)
#     print("You are doing a great job")
#     print("You are awesome!")

# greet_employee('Simon')

# print(sorted([1, 3, 2, 5, 4]))
# username_list  = ["elarson", "bmoreno", "tshah"] 

# device_id_list = ["us2c0R5", "2R78TBR", "bt3MIEz"]

# print(username_list + device_id_list)
# waiting_list = ["Mr. Brown", "Mr. White", "Mr. Green", "Ms. Black", "Ms. White"]
# for index, name in enumerate(waiting_list):
#     row = f"{index + 1}. {name}"
#     print(row)
    
# user_entries = ['10', '19.2', '20', '3.2']
# print(user_entries)
# user_numbers = [float(number) for number in user_entries]

# print(user_numbers)

# print(max(user_numbers))

# def all_equal(lst):
#   return len(set(lst)) == 1

# all_equal([1, 2, 3, 4, 5, 6]) # False
# print("1st all equal: ", all_equal([1, 2, 3, 4, 5, 6]))
#  # True
# print("2nd all equal: ", all_equal([1, 1, 1, 1]))


# new_set = (2, 2, 2, 2)
# print(new_set)
# print(type(new_set))
# print(len(set(new_set)))
# print(set(new_set))

def max_by(lst, fn):
  return max(map(fn, lst))
  """
  Returns the maximum value in a list based on a provided function.

  Parameters:
  lst (list): The list of elements to evaluate.
  fn (function): A function that takes an element from the list and returns a value to compare.

  Returns:
  The maximum value obtained by applying the function to the elements of the list.
  """
  # return max(map(fn, lst))

print(max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n'])) # 8)

def max_element_index(arr):
  return arr.index(max(arr))

print(max_element_index([5, 8, 9, 7, 10, 3, 0])) # 4

# print("Hello World")

# list1 = [5, 8, 9, 7, 10, 3, 0]

# max_value = max(list1)

# print(max_value)