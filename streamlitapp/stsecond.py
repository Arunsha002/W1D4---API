import streamlit as st
import time

st.title("வணக்கம் இறைமகிழன்")  # Vanakam Iraimagizhan
st.write("கீழே உள்ள வார்த்தைகளில் ஏதேனும் ஒன்றை கிளிக் செய்யவும்:")

# Dictionary of relationships
relations = {
    "அம்மா": "திவ்யா",
    "அப்பா": "அருண்",
    "அண்ணா": "ஆரோன்",
    "தம்பி": "நிலன்",
    "பாட்டி": "மீனா",
    "அப்பாத்தாத்தா": "சௌந்தர்",
    "பெரியப்பா": "ஆனந்த்",
    "அம்மம்மா": "சகிலா",
    "அம்மாத்தாத்தா": "செல்வம்",
    "மாமா": "தமிழ்",
    "அத்தை": "பிரிசில்லா"
}

# Arrange buttons horizontally in tiles
cols = st.columns(4)  # 4 buttons per row

# Placeholder for popup effect
popup = st.empty()

i = 0
for relation, name in relations.items():
    col = cols[i % 4]  # cycle through columns
    if col.button(relation):
        popup.success(f"{relation} - {name}")
        time.sleep(2)
        popup.empty()
    i += 1
