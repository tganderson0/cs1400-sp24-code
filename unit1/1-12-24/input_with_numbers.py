user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print(type(user_age))
new_user_age = int(user_age)
print(type(new_user_age))

print("Hello,", user_name, ". In 10 years you will be", new_user_age + 10)