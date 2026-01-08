sandwich_orders = ['Ham', 'Vegetarian', "Classic", "Tuna"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("The following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)