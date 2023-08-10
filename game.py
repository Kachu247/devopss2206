name = input("enter your name here: ")
level = ["easy", "medium", "hard"]
user_input = ' '
input_message = "pick an option:\n"
print(f"hello {name} and welcome to the game")
for index, item in enumerate(level):
    input_message += f"{index+1}) {item}\n"
input_message += "your choice: "
while user_input.lower() not in level:
    user_input = input(input_message)

print('You picked: ' + user_input)