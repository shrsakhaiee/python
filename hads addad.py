import random
computer_number = random.randint(10, 40)
attempts = 0
while True:
    user_number = int(input())
    attempts = attempts + 1
    if user_number == computer_number:
        print("tabrikkkkkkkkkkkkkk")
        break
    elif user_number < computer_number:
        print("boro bala")
    elif user_number > computer_number:
        print("boro paeen")
print("tedad hads", attempts, "bar")