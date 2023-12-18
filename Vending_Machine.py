#VENDING MACHINE

class VendingMachine:
    def __init__(self):
        self.products = {
            '1111': {'name': 'Coca Cola', 'price': 3.00},
            '2222': {'name': 'Water', 'price': 2.00},
            '3333': {'name': 'Snacks', 'price': 5.00},
            '4444': {'name': 'Soda Sprite', 'price': 3.00},
            '5555': {'name': 'Ice Cream', 'price': 6.50},
            '6666': {'name': 'Snickers', 'price': 4.00},
            '7777': {'name': 'Fresh Milk', 'price': 5.00}
            }

    def display_menu(self):
        print("\nWelcome to Goldy's Vending Machine\n")
        print(" Product   Price  Code")
        for code, product_info in self.products.items():
            print(f"{product_info['name']:<12}${product_info['price']:<4} {code}")

    def confirm_quit(self):
        user_input = input("\nDo you want to quit? (y/n): ").lower()
        return user_input == 'y'

    def select_product(self):
        while True:
            try:
                code = input("\nSelect a product by entering its code (enter 'q' to quit): ")
                if code == 'q':
                    if self.confirm_quit():
                        print("Thank you for using Goldy's Vending Machine. Goodbye!")
                        exit()
                    else:
                        continue
                elif code in self.products:
                    return code
                else:
                    print("Invalid code. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid code.")

    def process_payment(self, code):
        product_info = self.products[code]
        print(f"\nYou have selected {product_info['name']}. Please pay ${product_info['price']:.2f}")
        return product_info['price']

    def run(self):
        total_money_inserted = 0.0

        while True:
            self.display_menu()
            selected_code = self.select_product()
            price = self.process_payment(selected_code)

            while total_money_inserted < price:
                try:
                    money_inserted = float(input("Insert money (in dollars): "))
                    if money_inserted >= 1:
                        total_money_inserted += money_inserted
                    else:
                        print("Please enter a positive amount.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            change = total_money_inserted - price
            print(f"\nTransaction successful! Enjoy your {self.products[selected_code]['name']}!\n")
            print(f"Change: ${change:.2f}")
            total_money_inserted = 0.0


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()