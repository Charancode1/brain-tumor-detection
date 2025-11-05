import streamlit as st
from PIL import Image
import random

# List of tumor classes
classes = ['Glioma Tumor', 'Meningioma Tumor', 'Pituitary Tumor', 'No Tumor']

st.title("🧠 Brain Tumor Detection Demo")


# Upload section
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI Image', use_column_width=True)

    # Fake prediction button
    if st.button("Predict Tumor Type"):
        prediction = random.choice(classes)
        st.success(f"✅ Predicted Tumor Type: **{prediction}**")

