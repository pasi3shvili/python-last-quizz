import random
import math

portfolio = ["BTC"]
amount = [0.5]
buy_price = [90000]
current_price = [90000]

while True:
    print("\n1- --მონეტის დამატება--")
    print("2- --ფასის განახლება--")
    print("3- --პორტფელის ნახვა--")
    print("4- --მოგება/ზარალის გამოთვლა--")
    print("5- --საუკეთესო ინვესტიცია--")
    print("0- --გამოსვლა--")
    choice = input("აირჩიე:")

    if choice == "0":
        break

    elif choice == "1":
        portfolio = portfolio + [input("მონეტა: ")]
        amount = amount + [float(input("რაოდენობა: "))]
        price_val = float(input("შესყიდვის ფასი: "))
        buy_price = buy_price + [price_val]
        current_price = current_price + [price_val]
        print("დაემატა!")

    elif choice == "2":
        coin_name = input("რომელი მონეტის ფასი განახლდეს?: ")

        idx = -1
        for i in range(len(portfolio)):
            if portfolio[i] == coin_name:
                idx = i

        if idx != -1:
            current_price[idx] = float(input("ახალი მიმდინარე ფასი: "))
            print("ფასი განახლდა!")
        else:
            print("ვერ მოიძებნა.")

    elif choice == "3":
        print("\n--- პორტფელი ---")
        for i in range(len(portfolio)):
            print(f"{portfolio[i]} - რაოდენობა: {amount[i]} | ფასი: {current_price[i]}")

    elif choice == "4":
        print("\n--- მოგება / ზარალი ---")
        for i in range(len(portfolio)):
            profit = (current_price[i] - buy_price[i]) * amount[i]
            print(f"{portfolio[i]}: {profit}$")

    else:
        print("არასწორია.")
