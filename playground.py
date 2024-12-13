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
    
user_entries = ['10', '19.2', '20', '3.2']
print(user_entries)
user_numbers = [float(number) for number in user_entries]

print(user_numbers)
