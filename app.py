from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)

# Load your model (update the path accordingly)
model = load_model('marine_model.h5')

# Labels for prediction
labels = ['Non Oil Spill', 'Oil Spill']

def load_and_preprocess_image(image):
    try:
        img = Image.open(io.BytesIO(image))
        img = img.resize((150, 150))  # Resize the image
        img_array = np.array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return img_array
    except Exception as e:
        print(f"Error loading and processing image: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        
        if file:
            img = load_and_preprocess_image(file.read())
            if img is not None:
                try:
                    prediction = model.predict(img)
                    predicted_class = (prediction > 0.5).astype("int32")[0][0]
                    result_label = labels[predicted_class]
                    return render_template('index.html', prediction=result_label)
                except Exception as e:
                    print(f"Error during prediction: {e}")
                    return render_template('index.html', error="Error during prediction. Please try again.")
            else:
                return render_template('index.html', error="Error processing the image. Please ensure it's a valid image format.")
        else:
            return render_template('index.html', error="No file uploaded. Please upload an image.")
    
    return render_template('index.html')

if __name__ == '__main__':
    # Ensuring the app runs on the correct host and port provided by Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
