from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_off = False
my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()


while not is_off:

    wish = input(f"What would you like? {my_menu.get_items()}?")

    if wish == "off":
        is_off = True


    elif wish == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    else:
        my_MenuItem = my_menu.find_drink(wish) #sadece print statement da gerceklesebilir
        can_make = my_coffee_maker.is_resource_sufficient(my_MenuItem)
        if not can_make:
            continue

        money_received = my_money_machine.make_payment(my_MenuItem.cost)
        if not money_received:
            continue

        my_coffee_maker.make_coffee(my_MenuItem)






