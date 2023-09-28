class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.coffee_beans = 1000
        self.money = 0

    def report(self):
        print(f"Water level: {self.water}ml")
        print(f"Milk level: {self.milk}ml")
        print(f"Coffee Beans level: {self.coffee_beans}g")
        print(f"Money earned: ${self.money}")

    def check_resources(self, required_water, required_milk, required_coffee_beans):
        if (
            self.water >= required_water
            and self.milk >= required_milk
            and self.coffee_beans >= required_coffee_beans
        ):
            return True
        else:
            return False

    def make_coffee(self, choice):
        if choice == "espresso":
            required_water = 250
            required_milk = 0
            required_coffee_beans = 16
            cost = 4
        elif choice == "latte":
            required_water = 350
            required_milk = 75
            required_coffee_beans = 20
            cost = 7
        elif choice == "cappuccino":
            required_water = 200
            required_milk = 100
            required_coffee_beans = 12
            cost = 6
        else:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")
            return

        if self.check_resources(required_water, required_milk, required_coffee_beans):
            print("Please insert coins.")
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.1
            nickels = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
            total_inserted = quarters + dimes + nickels + pennies

            if total_inserted < cost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                self.money += cost
                change = total_inserted - cost
                print(f"Making your {choice} ☕️. Enjoy!")
                if change > 0:
                    print(f"Don't forget your change: ${change:.2f}")
                self.water -= required_water
                self.milk -= required_milk
                self.coffee_beans -= required_coffee_beans
        else:
            print("Sorry, not enough resources to make this coffee.")

# Main program loop
coffee_machine = CoffeeMachine()
while True:
    action = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    if action == "exit":
        break
    elif action == "report":
        coffee_machine.report()
    else:
        coffee_machine.make_coffee(action)

