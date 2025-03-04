import streamlit as st
import random

# Conversion functions (unchanged)
def km_to_miles(km):
    return km / 1.609

def miles_to_km(miles):
    return miles * 1.609

def kg_to_lb(kg):
    return kg * 2.205

def lb_to_kg(lb):
    return lb / 2.205

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm / 0.092903

# Theme toggle
if 'theme' not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Custom CSS styling for improved responsiveness, modern UI, and theme support
def get_custom_css():
    return f"""
    <style>
    :root {{
        --primary-color: {("#3498db", "#2980b9")[st.session_state.theme == "dark"]};
        --background-color: {("#ffffff", "#1E1E1E")[st.session_state.theme == "dark"]};
        --text-color: {("#000000", "#ffffff")[st.session_state.theme == "dark"]};
        --secondary-bg-color: {("#f0f0f0", "#2D2D2D")[st.session_state.theme == "dark"]};
    }}
    body {{
        color: var(--text-color);
        background-color: var(--background-color);
    }}
    .main {{
        font-family: 'Arial', sans-serif;
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem;
    }}
    .stButton > button {{
        background-color: var(--primary-color);
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }}
    .stButton > button:hover {{
        opacity: 0.8;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .stSelectbox, .stNumberInput {{
        margin-bottom: 1rem;
    }}
    .result {{
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
        padding: 1.5rem;
        background-color: var(--secondary-bg-color);
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .header {{
        background-color: var(--primary-color);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .category-button {{
        background-color: var(--secondary-bg-color);
        color: var(--text-color);
        border: none;
        padding: 0.75rem 1.5rem;
        margin: 0.5rem;
        border-radius: 25px;
        font-size: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    .category-button:hover, .category-button.active {{
        background-color: var(--primary-color);
        color: white;
    }}
    .quick-reference {{
        background-color: var(--secondary-bg-color);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .fun-fact {{
        background-color: {("#e6f7ff", "#1E3A5F")[st.session_state.theme == "dark"]};
        color: var(--text-color);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
        font-style: italic;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .feedback-section {{
        background-color: var(--secondary-bg-color);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    @media (max-width: 768px) {{
        .header h1 {{
            font-size: 1.75rem;
        }}
        .result {{
            font-size: 1.25rem;
            padding: 1rem;
        }}
        .category-button {{
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
        }}
    }}
    </style>
    """

st.markdown(get_custom_css(), unsafe_allow_html=True)

# App header
st.markdown('<div class="header"><h1>🌐 Advanced Unit Converter</h1></div>', unsafe_allow_html=True)

# Theme toggle button with icon
theme_icon = "🌙" if st.session_state.theme == "light" else "☀️"
if st.button(f"{theme_icon} Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Categories
categories = ["Length", "Weight", "Temperature", "Volume", "Area"]
category = st.radio("Select a category:", categories, format_func=lambda x: f"📏 {x}" if x == "Length" else f"⚖️ {x}" if x == "Weight" else f"🌡️ {x}" if x == "Temperature" else f"🧊 {x}" if x == "Volume" else f"📐 {x}")

# Conversion options based on category
if category == "Length":
    options = ["Kilometers to Miles", "Miles to Kilometers", "Inches to Centimeters", "Centimeters to Inches"]
elif category == "Weight":
    options = ["Kilograms to Pounds", "Pounds to Kilograms"]
elif category == "Temperature":
    options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
elif category == "Volume":
    options = ["Liters to Gallons", "Gallons to Liters"]
elif category == "Area":
    options = ["Square Feet to Square Meters", "Square Meters to Square Feet"]

# Improved layout using columns
col1, col2 = st.columns([2, 1])
with col1:
    choice = st.selectbox("Choose a conversion:", options)
with col2:
    value = st.number_input("Enter value:", format="%.6f")

# Conversion button
if st.button("Convert", key="convert_button"):
    if choice == "Kilometers to Miles":
        result = km_to_miles(value)
        unit = "miles"
    elif choice == "Miles to Kilometers":
        result = miles_to_km(value)
        unit = "kilometers"
    elif choice == "Kilograms to Pounds":
        result = kg_to_lb(value)
        unit = "pounds"
    elif choice == "Pounds to Kilograms":
        result = lb_to_kg(value)
        unit = "kilograms"
    elif choice == "Inches to Centimeters":
        result = inches_to_cm(value)
        unit = "centimeters"
    elif choice == "Centimeters to Inches":
        result = cm_to_inches(value)
        unit = "inches"
    elif choice == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(value)
        unit = "°F"
    elif choice == "Fahrenheit to Celsius":
        result = fahrenheit_to_celsius(value)
        unit = "°C"
    elif choice == "Liters to Gallons":
        result = liters_to_gallons(value)
        unit = "gallons"
    elif choice == "Gallons to Liters":
        result = gallons_to_liters(value)
        unit = "liters"
    elif choice == "Square Feet to Square Meters":
        result = sqft_to_sqm(value)
        unit = "square meters"
    elif choice == "Square Meters to Square Feet":
        result = sqm_to_sqft(value)
        unit = "square feet"
    
    # Display result with improved formatting
    st.markdown(f'<div class="result">{value:.4f} {choice.split(" to ")[0]} = {result:.4f} {unit}</div>', unsafe_allow_html=True)

# Quick Reference
st.subheader("📚 Quick Reference")
reference_data = {
    "Length": ["1 kilometer ≈ 0.621371 miles", "1 inch = 2.54 centimeters"],
    "Weight": ["1 kilogram ≈ 2.20462 pounds"],
    "Temperature": ["0°C = 32°F", "100°C = 212°F"],
    "Volume": ["1 liter ≈ 0.264172 gallons"],
    "Area": ["1 square foot ≈ 0.092903 square meters"]
}
for ref in reference_data[category]:
    st.write(ref)

# Fun facts
fun_facts = [
    "The metric system is used by 95% of the world's population.",
    "The United States is one of only three countries that don't use the metric system.",
    "The kilogram was originally defined as the mass of one liter of water at 4°C.",
    "The inch was once defined as the length of three grains of barley laid end to end.",
    "The Fahrenheit scale was created by Daniel Gabriel Fahrenheit in 1724.",
    "A marathon is exactly 42.195 kilometers or 26.2 miles.",
    "The coldest temperature ever recorded on Earth was -128.6°F (-89.2°C) in Antarctica.",
    "One gallon of water weighs approximately 8.34 pounds (3.78 kilograms).",
    "The Great Pyramid of Giza originally had a height of 146.5 meters (480.6 feet).",
    "An Olympic-size swimming pool holds 2,500,000 liters (660,000 gallons) of water."
]
st.subheader("💡 Did you know?")
st.write(random.choice(fun_facts))

# Conversion history
if 'conversion_history' not in st.session_state:
    st.session_state.conversion_history = []

if st.button("Add to History", key="add_to_history") and 'result' in locals():
    st.session_state.conversion_history.append(f"{value:.4f} {choice.split(' to ')[0]} = {result:.4f} {unit}")

if st.session_state.conversion_history:
    st.subheader("🕒 Conversion History")
    for i, conversion in enumerate(reversed(st.session_state.conversion_history[-5:])):
        st.write(f"{i+1}. {conversion}")

# Save and Load History
if st.session_state.conversion_history:
    history_text = "\n".join(st.session_state.conversion_history)
    st.download_button(
        label="Download History",
        data=history_text,
        file_name="conversion_history.txt",
        mime="text/plain",
    )

uploaded_file = st.file_uploader("Upload Conversion History", type=["txt"])
if uploaded_file is not None:
    history_data = uploaded_file.read().decode("utf-8")
    st.session_state.conversion_history = history_data.split("\n")
    st.success("History loaded successfully!")

# Favorites
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

if st.button("Add to Favorites", key="add_to_favorites") and 'result' in locals():
    favorite_entry = f"{value:.4f} {choice.split(' to ')[0]} = {result:.4f} {unit}"
    if favorite_entry not in st.session_state.favorites:
        st.session_state.favorites.append(favorite_entry)
        st.success("Added to favorites!")
    else:
        st.warning("This conversion is already in your favorites.")

if st.session_state.favorites:
    st.subheader("⭐ Favorites")
    for i, favorite in enumerate(st.session_state.favorites):
        st.write(f"{i+1}. {favorite}")

# Feedback Section
st.subheader("📝 Feedback")

# Initialize feedback in session state
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# Feedback text area
feedback = st.text_area("How can we improve this converter? (Optional)", value=st.session_state.feedback, key="feedback_input")

# Submit feedback and reset the field
if st.button("Submit Feedback", key="feedback_button"):
    if feedback.strip() != "":
        st.success("Thank you for your feedback! We appreciate your input.")
        # Reset the feedback field
        st.session_state.feedback = ""
    else:
        st.warning("Please enter your feedback before submitting.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by MAARIJ KHAN MK | [GitHub](https://github.com/maarijkhan24)")