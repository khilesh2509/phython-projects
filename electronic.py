import time

menu = {
    "television": 50000,
    "refrigerator": 40000,
    "laptop": 60000,
    "air conditioner": 70000,
    "washing machine": 50000,
}

discount = {
    "electronic50": 5000,

}


print("\nWELCOME TO ELECTRONIC SHOP ")
time.sleep(2)

name = input("Enter your name: ").capitalize()

print(f'hey, {name}')

order = input("Do you want to order anything: ").lower()
if order != "yes":
    quit()

else:
    print("cool, Here is our options: ")

time.sleep(2)
print("\nTELEVISION: 50000-/ \nREFRIGERATOR: 40000-/ \nLAPTOP: 60000-/ \nAIR CONDITIONER: 70000-/ \nWASHING "
      "MACHINE: 50000-/")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Item: {item_1} has been added! ')

else:
    print(f'Item: {item_1}, Not available right now. ')

another_order = input("Do you want to order anything more? ")

if another_order == "yes":
    print("\nOK, Here is our more option! ")
    print("\nTELEVISION: 50000-/ \nREFRIGERATOR: 40000-/ \nLAPTOP: 60000-/ \nAIR CONDITIONER: 70000-/ \nWASHING "
          "MACHINE: 50000-/")
    time.sleep(2)
    item_2 = input("Enter the name of the item you want to order = ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Item: {item_2} has been added! ')

    else:
        print(f'Item: {item_2}, Not available right now.')

coupon_input = input("Do you want to apply coupon code: ")

if coupon_input == "yes":
    special_code = input("\nEnter the coupon code: ").lower()

    if special_code in discount:
        discount_value = discount[special_code]
        order_total -= discount_value
        print(f'\nyou got: {discount_value} RS-/ discount')

    else:
        print("Invalid code! ")

else:
    print("Nevermind...")

print(f'Sir/Mam {name}, Your bill is processing... ')
time.sleep(2)
print(f'Total amount to pay: {order_total}')




