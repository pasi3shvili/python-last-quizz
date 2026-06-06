import random
import math

names = ["Knight"]
hp = [120]
attack = [25]
gold = [50]

while True:
    print("\n1- --პერსონაჟის დამატება--")
    print("2- --შეტევა--")
    print("3- --ოქროს დამატება-- ")
    print("4- --სტატისტიკის ნახვა--")
    print("5- --ლიდერის ნახვა--")
    print("0- --გამოსვლა--")
    choice = input("აირჩიე:")

    if choice == "0":
        break

    elif choice == "1":
        names = names + [input("სახელი: ")]
        hp = hp + [int(input("HP: "))]
        attack = attack + [int(input("Attack: "))]
        gold = gold + [int(input("Gold: "))]
        print("დაემატა!")

    elif choice == "2":
        att_name = input("ვინ უტევს?: ")
        tar_name = input("ვის უტევს?: ")

        att_idx = -1
        tar_idx = -1
        for i in range(len(names)):
            if names[i] == att_name:
                att_idx = i
            if names[i] == tar_name:
                tar_idx = i

        if att_idx != -1 and tar_idx != -1:
            damage = attack[att_idx]

            if random.randint(1, 5) == 1:
                damage = damage * 2
                print("კრიტიკული დარტყმა!")

            hp[tar_idx] -= damage
            print(f"{att_name}-მა დააკლო {damage} HP {tar_name}-ს.")

            if hp[tar_idx] <= 0:
                print(f"{tar_name} დამარცხდა!")
                gold[att_idx] += 100
        else:
            print("მოთამაშე ვერ მოიძებნა.")

    elif choice == "3":
        name = input("ვის დავუმატოთ ოქრო?: ")

        idx = -1
        for i in range(len(names)):
            if names[i] == name:
                idx = i

        if idx != -1:
            gold[idx] += int(input("რამდენი ოქრო?: "))
        else:
            print("ვერ მოიძებნა.")

    elif choice == "4" or choice == "5":
        max_gold_idx = 0
        max_att_idx = 0
        max_hp_idx = 0

        for i in range(len(names)):
            if gold[i] > gold[max_gold_idx]:
                max_gold_idx = i
            if attack[i] > attack[max_att_idx]:
                max_att_idx = i
            if hp[i] > hp[max_hp_idx]:
                max_hp_idx = i

        if choice == "4":
            print(f"ყველაზე მდიდარი: {names[max_gold_idx]} ({gold[max_gold_idx]} ოქრო)")
            print(f"ყველაზე ძლიერი: {names[max_att_idx]} ({attack[max_att_idx]} attack)")
            print(f"ყველაზე მეტი HP: {names[max_hp_idx]} ({hp[max_hp_idx]} hp)")
        else:
            print(f"ლიდერია: {names[max_gold_idx]} ({gold[max_gold_idx]} ოქროთი)")

    else:
        print("არასწორია.")
