import streamlit as st
# from transformers import pipeline
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES=True
import os
import predict
import time

st.title("ORTHO-ASSIST")

# Custom CSS styles
st.markdown(
    """
    <style>
    body {
         /* White background */
    }
    .stApp {
        max-width: 1200px; /* Limit app width */
    }
    </style>
    """,
    unsafe_allow_html=True
)

css = '''
<style>

</style>
'''
# Main content sections
st.header("x-ray assistant")

# Upload X-ray image
uploaded_image = st.file_uploader("Upload X-ray Image", type=["jpg", "jpeg", "png"])

# Input text box for patient history
default_text = "This portion is under developement....."

patient_history = st.text_area("Enter Patient Details",height=10,value=default_text)
# Button to trigger processing
if st.button("Process"):
    # Check if both image and patient history are uploaded/entered
    if uploaded_image is not None and patient_history:
        # Save image
        image_filename = os.path.join("images", uploaded_image.name)
        image = Image.open(uploaded_image)
        image.save(image_filename)
        time.sleep(1)
        predict.predict_xray()
        time.sleep(5)
        # Display resultant image from "images" directory
        resultant_image_path = os.path.join("FracAtlas/runs/detect/predict", uploaded_image.name)
        print(resultant_image_path)
        if os.path.exists(resultant_image_path):
            resultant_image = Image.open(resultant_image_path)
            st.subheader("Resultant Image")
            st.image(resultant_image, caption="Resultant Image", use_column_width=True)
        else:
            st.warning("Resultant image not found.")

        # Process patient history
        # summary = summarizer(patient_history, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

        # # Save text description
        # description_filename = os.path.join("description", uploaded_image.name.split('.')[0] + ".txt")
        # with open(description_filename, "w") as text_file:
        #     text_file.write(summary)

        # # Display uploaded image
        # st.image(image, caption="Uploaded X-ray Image", use_column_width=True)

        # # Display summarized patient history
        # st.subheader("Summarized Patient History")
        # st.write(summary)

        st.success("Image and description saved successfully.")
    
    else:
        st.warning("Please upload an X-ray image and enter patient history.")