import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from streamlit_drawable_canvas import st_canvas
import tempfile
import os
import zipfile

st.title("Automatic Certificate Generator")

# Upload certificate template
uploaded_template = st.file_uploader("Upload Certificate Template Image", type=["png", "jpg", "jpeg"])
if uploaded_template is None:
    st.stop()

img = Image.open(uploaded_template).convert("RGB")
img_width, img_height = img.size

# Resize image for display (max width 700 px)
max_display_width = 700
scale = min(max_display_width / img_width, 1.0)
display_width = int(img_width * scale)
display_height = int(img_height * scale)
img_resized = img.resize((display_width, display_height))

st.write(f"Template size: {img_width} x {img_height} px")
st.write("Click on the image to select the name position:")

# Use drawable canvas with point mode to select position
canvas_result = st_canvas(
    fill_color="rgba(0,0,0,0)",
    stroke_width=5,
    stroke_color="#FF0000",
    background_image=img_resized,
    height=display_height,
    width=display_width,
    drawing_mode="point",
    key="canvas",
)

position = None
if canvas_result.json_data is not None:
    objects = canvas_result.json_data.get("objects", [])
    if objects:
        # Get last point coordinates (scaled)
        last_obj = objects[-1]
        # The coordinates are in displayed image scale
        x_disp = last_obj.get("left", 0)
        y_disp = last_obj.get("top", 0)
        # Convert back to original image scale
        x = int(x_disp / scale)
        y = int(y_disp / scale)
        position = (x, y)
        st.write(f"Selected position on original image: {position}")

# Upload names file
uploaded_names = st.file_uploader("Upload names text file (.txt)", type=["txt"])
if uploaded_names is None:
    st.stop()

names = uploaded_names.read().decode("utf-8").splitlines()
names = [n.strip() for n in names if n.strip()]

# Font size input
font_size = st.number_input("Font Size", min_value=10, max_value=200, value=70)

# Font file uploader or default
uploaded_font = st.file_uploader("Upload TTF font file (optional)", type=["ttf"])
if uploaded_font:
    font_path = tempfile.NamedTemporaryFile(delete=False, suffix=".ttf").name
    with open(font_path, "wb") as f:
        f.write(uploaded_font.read())
else:
    # Use default PIL font
    font_path = None

if st.button("Generate Certificates"):
    if position is None:
        st.error("Please select the position by clicking on the image.")
    else:
        output_dir = tempfile.mkdtemp()
        font = None
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()

        for name in names:
            cert_img = img.copy()
            draw = ImageDraw.Draw(cert_img)

            bbox = draw.textbbox((0, 0), name, font=font)
            text_width = bbox[2] - bbox[0]

            x = position[0] - text_width // 2
            y = position[1]

            draw.text((x, y), name, fill=(0, 0, 0), font=font)

            cert_img.save(os.path.join(output_dir, f"{name}.png"))

        # Zip the output folder
        zip_path = os.path.join(output_dir, "certificates.zip")
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for file in os.listdir(output_dir):
                if file.endswith(".png"):
                    zipf.write(os.path.join(output_dir, file), arcname=file)

        # Provide download link
        with open(zip_path, "rb") as f:
            st.download_button("Download Certificates ZIP", data=f, file_name="certificates.zip")

        st.success("Certificates generated successfully!")
