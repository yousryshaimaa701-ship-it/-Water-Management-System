import streamlit as st
import matplotlib.pyplot as plt
import json
import os


# -------------------------
# Load users from JSON
# -------------------------

if "users" not in st.session_state:
    if os.path.exists("users.json"):

        with open("users.json", "r") as file:
            st.session_state.users = json.load(file)

    else:
        st.session_state.users = []


users = st.session_state.users


# -------------------------
# Save Users
# -------------------------

def save_users():

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    st.success("✅ Data saved successfully")


# -------------------------
# Add User
# -------------------------

def add_user():

    st.subheader("👤 Add User")

    user_name = st.text_input("Enter your name")
    user_id = st.number_input("Enter your ID", min_value=1, step=1)

    if st.button("Add User"):

        # Check if ID already exists
        for user in users:

            if user["id"] == user_id:
                st.error("❌ This ID already exists")
                return

        user = {
            "name": user_name,
            "id": user_id,
            "water": []
        }

        users.append(user)

        save_users()

        st.success("✅ User added successfully")


# -------------------------
# Search User
# -------------------------

def search_user():

    st.subheader("🔎 Search User")

    search_id = st.number_input(
        "Enter User ID",
        min_value=1,
        step=1,
        key="search_id"
    )

    if st.button("Search"):

        for user in users:

            if user["id"] == search_id:

                st.success("User found!")

                st.write("**Name:**", user["name"])
                st.write("**ID:**", user["id"])
                st.write("**Water usage:**", user["water"])

                return

        st.error("❌ User not found")


# -------------------------
# Water Usage
# -------------------------

def water_usage_page():

    st.subheader("💧 Water Usage")

    if len(users) == 0:

        st.warning("❌ No users available")
        return

    user_id = st.number_input(
        "Enter User ID",
        min_value=1,
        step=1,
        key="water_user_id"
    )

    selected_user = None

    for user in users:

        if user["id"] == user_id:
            selected_user = user
            break

    if selected_user is None:

        st.info("Enter a valid User ID")

        return

    st.write("### User:", selected_user["name"])

    usage = st.number_input(
        "Enter water usage",
        min_value=0.0,
        step=1.0
    )

    if st.button("Add Water Usage"):

        selected_user["water"].append(usage)

        save_users()

        st.success("✅ Usage added successfully")


    # -------------------------
    # Show Usage
    # -------------------------

    if len(selected_user["water"]) > 0:

        st.write("### 📋 Water Usage")

        st.write(selected_user["water"])


        # -------------------------
        # Average & Leak
        # -------------------------

        average = sum(selected_user["water"]) / len(selected_user["water"])

        st.write("### 📊 Average")

        st.write(average)

        high = 0

        for value in selected_user["water"]:

            if value > average * 4:
                high += 1


        if high >= 1:

            st.error("🚨 Possible Water Leak!")

        else:

            st.success("🟢 Normal Water Usage")


        # -------------------------
        # Bar Chart
        # -------------------------

        st.write("### 📊 Water Usage Chart")

        fig, ax = plt.subplots()

        ax.bar(
            range(len(selected_user["water"])),
            selected_user["water"]
        )

        ax.set_title("Water Usage")
        ax.set_xlabel("Reading")
        ax.set_ylabel("Water Usage")

        st.pyplot(fig)

    else:

        st.info("No water usage data yet")


# -------------------------
# Main App
# -------------------------

st.title("🚰 Water Management System")

st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Add User",
        "Search User",
        "Water Usage",
        "Show All Users",
        "Save Data"
    ]
)


if option == "Add User":

    add_user()


elif option == "Search User":

    search_user()


elif option == "Water Usage":

    water_usage_page()


elif option == "Show All Users":

    st.subheader("👥 All Users")

    if len(users) == 0:

        st.info("No users available")

    else:

        for user in users:

            st.write(
                f"**Name:** {user['name']} | "
                f"**ID:** {user['id']} | "
                f"Water readings: {len(user['water'])}"
            )


elif option == "Save Data":

    save_users()