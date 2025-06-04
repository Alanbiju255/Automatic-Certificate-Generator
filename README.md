
# 🎓 Automatic Certificate Generator (Streamlit App)

## 📝 Overview

This project is a web-based application built with **Streamlit** that allows users to generate personalized certificates easily and quickly. By uploading a certificate template image, selecting where the recipient's name should appear, and providing a list of names, users can automatically create beautifully customized certificates ready for printing or digital sharing.

---

## ✨ Features

- 📁 **Upload Certificate Template:** Upload your own certificate background image in common formats such as PNG, JPEG, or JPG.
- 🎯 **Visual Position Selection:** View a scaled preview of the certificate template within the app and select the exact position where the recipient’s name will be placed by clicking on the image.
- 🧾 **Name List Input:** Upload a plain text file containing the names of recipients, one name per line.
- 🔤 **Custom Font Support:** Optionally upload a TrueType font file (.ttf) to customize the style of the name text.
- 🔎 **Font Size Control:** Adjust the font size dynamically to fit your template design.
- 📂 **Batch Certificate Generation:** Generate individual certificate images for each name in the list automatically.
- 📥 **Downloadable Output:** Download all generated certificates bundled into a ZIP file for easy access and distribution.
- 🖥️ **User-friendly Interface:** Simple and intuitive Streamlit web UI requiring no programming knowledge.

---
## example 
   ![Alt text](https://github.com/Alanbiju255/Automatic-Certificate-Generator/blob/main/Alan%20biju.png)

## 🛠️ Installation and Setup

To run this project locally, you need:

- 🐍 Python 3.x installed on your system.
- 🌐 A working internet connection to install dependencies.
- 📦 Streamlit, Pillow, and streamlit-drawable-canvas Python packages installed.

You can install the required dependencies using Python's package manager. Ensure you install the package `streamlit-drawable-canvas` for enabling image position selection.

---

## 🚀 How to Use

1. ▶️ **Start the App:** Launch the Streamlit application via command line or terminal.
2. 📤 **Upload Your Certificate Template:** Select and upload the background certificate image you want to use.
3. 🎯 **Select Text Position:** The app will display the template image. You click anywhere on the image where you want the names to appear. This point determines the exact text placement on all generated certificates.
4. 📄 **Upload Names File:** Provide a `.txt` file containing the recipient names, each on its own line.
5. ✍️ **Customize Font and Size:** Optionally upload a font file to personalize the text style, and choose an appropriate font size.
6. 🛠️ **Generate Certificates:** Once all inputs are provided, generate the certificates. The app automatically creates individual certificate images with the names positioned as selected.
7. 📦 **Download Certificates:** Download all generated certificates as a ZIP archive, making it easy to print or distribute digitally.

---

## 💡 Why Use This App?

- ⏳ **Saves Time:** Automates the tedious process of creating certificates one-by-one.
- 🎨 **No Design Skills Needed:** Simply upload your design and names list; the app handles text placement.
- 🔄 **Flexible:** Use any certificate template and any font you want.
- 🌍 **Accessible:** Runs on your local machine or any server with Streamlit support; accessible via web browser.
- 🔓 **Open Source:** You can customize and extend the app as needed.

---

## 🗂️ Project Structure

- 📄 **app.py:** The main Streamlit application file containing the app logic and UI.
- 📚 **README.md:** This documentation file describing the project.
- 📦 **Dependencies:** Python packages required are listed in documentation and installable via pip.
- 📂 **Uploads and Outputs:** Files such as certificate templates, fonts, and names are uploaded dynamically via the app UI. Generated certificates are temporarily saved and provided as downloadable ZIP files.

---

## ⚠️ Troubleshooting

- ✔️ Make sure Python 3.x is installed and accessible in your system PATH.
- ✔️ Verify that required Python packages are installed in the active Python environment.
- ❌ If you get errors related to missing modules, install them using pip.
- 🌐 Use the app on a modern web browser for best compatibility.
- 📸 Ensure your certificate template image is clear and of sufficient resolution for good print quality.

---

## 🤝 Contribution

Contributions are welcome! You can contribute by:

- 🐞 Reporting bugs or issues.
- 💡 Suggesting new features.
- 📝 Improving documentation.
- 🛠️ Adding new functionalities like PDF export, multiple text fields, or styling options.

Feel free to open an issue or a pull request in the repository.

---

## 🙏 Acknowledgments

- Built using **Streamlit** for easy web app creation.
- Image processing powered by **Pillow**.
- Interactive canvas functionality enabled via **streamlit-drawable-canvas**.

