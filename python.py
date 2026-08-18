import matplotlib.pyplot as plt
import json
users = []


def check_water():

    water_usage = []

    user_name = input("Enter your name pls: ")
    user_id = int(input("Enter your ID pls: "))

    user = {
        "name": user_name,
        "id": user_id,
        "water": water_usage
    }

    users.append(user)

    while True:

        print("\n--- Water Usage Menu ---")
        print("1. Add water usage")
        print("2. Show water usage")
        print("3. Check average and leak")
        print("4. Search")
        print("5. show graph")
        print("6. save data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            usage = float(input("Enter water usage: "))
            water_usage.append(usage)

            print("✅ Usage added successfully")

        elif choice == "2":

            if len(water_usage) == 0:
                print("❌ No data available")

            else:
                print("Water usage:", water_usage)

        elif choice == "3":

            if len(water_usage) == 0:
                print("❌ Add some water usage first")

            else:
                average = sum(water_usage) / len(water_usage)

                high = 0

                for usage in water_usage:

                    if usage > average * 4:
                        high += 1

                print("Average:", average)

                if high >= 1:
                    print("🚨 Possible Water Leak")
                else:
                    print("🟢 Normal Water Usage")

        elif choice == "4":

            search_user()
        elif choice == "5":


            if len(water_usage) == 0:
                print("❌ No data available")

            else:
                    plt.bar(range(len(water_usage)), water_usage)

                    plt.title("Water Usage")
                    plt.xlabel("Reading")
                    plt.ylabel("Water Usage")

                    plt.show()

        elif choice == "6":
            save_users()


        elif choice=="7":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")


def search_user():

    search_id = int(input("Enter your ID: "))

    for user in users:

        if user["id"] == search_id:

            print("Name:", user["name"])
            print("ID:", user["id"])
            print("Water usage:", user["water"])

            return

    print("❌ User not found")

def save_users():
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        print("✅ Data saved successfully")


check_water()