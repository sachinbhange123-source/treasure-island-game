import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

st.title("🏝️ Treasure Island")
st.write("Your mission is to find the treasure.")

# Step 1
direction = st.radio("Where do you want to go?", ["-- Choose an option --", "Left", "Right"])

if direction == "Right":
    st.error("💀 You fall into a hole! Game Over.")
elif direction == "Left":
    # Step 2
    sea = st.radio("You come to a sea. What do you do?", ["-- Choose an option --", "Wait for boat", "Swim"])
    
    if sea == "Swim":
        st.error("🦈 A sea monster eats you! Game Over.")
    elif sea == "Wait for boat":
        # Step 3
        door = st.radio("Choose a door:", ["-- Choose an option --", "Red", "Blue", "Yellow"])
        
        if door == "Red":
            st.error("🔥 Burned by fire. Game Over!")
        elif door == "Blue":
            st.error("🐺 Eaten by beasts. Game Over!")
        elif door == "Yellow":
            st.success("🎉 You found the treasure! You Win!")
