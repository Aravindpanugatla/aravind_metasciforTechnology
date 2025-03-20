import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Colorful Streamlit App", page_icon="🌟", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
        }
        .stSlider > div {
            color: #ff9800;
        }
        .stTitle {
            color: #2196f3;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🌈 Colorful & Professional Streamlit App")

# Slider
value = st.slider("Adjust Value", min_value=0, max_value=100, value=50)
st.write(f"Slider Value: {value}")

# Image with Caption
image = Image.open("sample.jpg")  # Ensure you have an image file named 'sample.jpg' in the working directory
st.image(image, caption="This is a sample image with a caption.", use_column_width=True)

# Button
if st.button("Click Me!"):
    st.success("You clicked the button!")
