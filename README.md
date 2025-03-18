# Oil Spill Detection AI

![Marine Life Savers](https://github.com/thilak-r/oil-spill-detection-AI/blob/main/sample_img.png) <!-- Add a relevant image link here if available -->

Demo (Only frontend) : [Click Here](https://thilak-r.github.io/oil-spill-detection-AI/)

## Overview
The **Oil Spill Detection AI** project leverages a convolutional neural network (CNN) model to detect oil spills in images. By automating this detection process, the system enables real-time monitoring and helps accelerate response times to protect marine ecosystems from oil pollution. The project is designed to assist in effective cleanup efforts by providing a fast and reliable tool for oil spill identification.


## Features
- **Real-time Oil Spill Detection:** Identifies oil spills in uploaded images using a pre-trained CNN model.
- **Web-Based Interface:** Provides a user-friendly web application for easy interaction.
- **Efficient and Reliable:** Helps monitor and alert users of potential oil spills promptly.
  
## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/thilak-r/oil-spill-detection-AI.git
   cd oil-spill-detection-AI
   
2. **Set up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
Download and Place the Model: Ensure marine_model.h5 is in the root directory of the project. This is the trained CNN model for detecting oil spills.

Usage

## Run the application:

   ```bash
   python app.py
```


Access the Web Interface: Open a browser and go to http://127.0.0.1:5000 to interact with the oil spill detection system.

Upload an Image: Use the upload feature to test the model by uploading an image. The system will analyze the image and display whether an oil spill is detected.

## Model

The marine_model.h5 is a CNN model specifically trained for oil spill detection using a dataset of images. The model uses advanced deep learning techniques to achieve accurate results in identifying oil spills from images.

## Technologies Used :

- **Python**: Core programming language.
- **Flask**: Web framework for building the web interface.
- **TensorFlow / Keras**: Frameworks used to develop and train the CNN model.
- **HTML/CSS**: Frontend development for the web interface.

## Contributing
Contributions are welcome! Please follow these steps to contribute:


Fork the repository :
  Create a new branch (git checkout -b feature-branch).
  Make your changes and commit them (git commit -m 'Add new feature').
  Push to the branch (git push origin feature-branch).
  Open a Pull Request.
  License
  This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments:
  Special thanks to the community and contributors for their valuable input and support in building this project.

  <br><br>
under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)


Thank you !
