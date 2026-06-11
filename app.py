import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(
    page_title="Mandala Art Generator - Workshop",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Mandala Art Generator - New Things")
st.write("Generate black-and-white mandala coloring pages using OpenAI.")

# Secure API Key Input
api_key = st.text_input(
    "Enter OpenAI API Key",
    type="password"
)

character_name = st.text_input(
    "Character Name",
    placeholder="Example: Lion, Elephant, Krishna"
)

color_name = st.text_input(
    "Color Name",
    placeholder="Example: Blue, Red, Green"
)

generate_btn = st.button("Generate Mandala Art")

if generate_btn:

    if not api_key:
        st.error("Please enter your OpenAI API key.")
        st.stop()

    if not character_name:
        st.error("Please enter a character name.")
        st.stop()

    try:

        client = OpenAI(api_key=api_key)

        prompt = f"""
        Create a highly detailed black and white mandala coloring page.

        Main subject: {character_name}

        Theme inspiration color: {color_name}

        Requirements:
        - Pure black and white
        - No gray shades
        - Coloring book style
        - Thick clean outlines
        - Intricate mandala patterns
        - Symmetrical design
        - White background
        - Printable A4 coloring page
        - No text
        - Centered composition
        """

        with st.spinner("Generating image..."):

            result = client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )

            image_base64 = result.data[0].b64_json

            image_bytes = base64.b64decode(image_base64)

            image = Image.open(BytesIO(image_bytes))

            st.image(
                image,
                caption="Generated Mandala Art",
                use_container_width=True
            )

            st.download_button(
                label="Download Image",
                data=image_bytes,
                file_name=f"{character_name}_mandala.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")