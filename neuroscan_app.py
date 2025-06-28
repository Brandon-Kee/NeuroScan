import streamlit as st
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import base64
from PIL import Image

# Set page config
st.set_page_config(
    page_title="NeuroScan - Advanced Brain Analysis",
    page_icon="🧠",
    layout="wide"
)


# Load trained model
@st.cache_resource
def load_tumor_model():
    return load_model('model.keras')


model = load_tumor_model()

# Class labels
class_labels = ['pituitary', 'notumor', 'glioma', 'meningioma']


# Helper function to predict tumor type
def predict_tumor(image):
    IMAGE_SIZE = 224
    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = min(np.max(predictions, axis=1)[0], 0.9999)

    if class_labels[predicted_class_index] == 'notumor':
        return "No Tumor", confidence_score
    else:
        return f"Tumor: {class_labels[predicted_class_index]}", confidence_score


# Custom CSS
st.markdown("""
<style>
    :root {
        --primary: #4a6fa5;
        --secondary: #166088;
        --accent: #4fc3f7;
        --light: #f8f9fa;
        --dark: #212529;
        --success: #28a745;
        --info: #17a2b8;
    }

    .neuro-card {
        border: none;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background: white;
    }

    .neuro-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
        padding: 1.5rem;
        text-align: center;
        border-radius: 12px 12px 0 0;
        margin: -1.5rem -1.5rem 1.5rem -1.5rem;
    }

    .neuro-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: var(--accent);
    }

    .neuro-btn {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        border: none;
        color: white;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        border-radius: 8px;
        width: 100%;
    }

    .neuro-result {
        border-left: 4px solid var(--accent);
        background-color: rgba(79, 195, 247, 0.1);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }

    .neuro-confidence {
        font-weight: 600;
        color: var(--secondary);
    }

    .neuro-image-container {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
    }

    .file-upload-label {
        display: block;
        padding: 1.5rem;
        border: 2px dashed #d1d5db;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .file-upload-label:hover {
        border-color: var(--accent);
        background-color: rgba(79, 195, 247, 0.05);
    }

    .file-upload-icon {
        font-size: 2rem;
        color: var(--primary);
        margin-bottom: 0.5rem;
    }

    /* Style the analyze button */
    .stButton>button {
        background: linear-gradient(135deg, #4a6fa5 0%, #166088 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        border-radius: 8px !important;
        width: 100% !important;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 1rem;
    }

    .logo-image {
        width: 80px;
        height: 80px;
        object-fit: contain;
    }

    .title-text {
        text-decoration: none !important;
        color: inherit !important;
    }
</style>
""", unsafe_allow_html=True)


# Main app
def main():


    # Header Section
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div class="neuro-card">
                <div class="neuro-header">
                    <i class="fas fa-brain neuro-icon"></i>
                    <h1 class="display-5 fw-bold title-text">NeuroScan</h1>
                    <p class="mb-0">Advanced MRI Analysis for Brain Tumor Detection</p>
                </div>
                <div class="card-body text-center">
                    <p class="text-muted">
                        Upload an MRI scan to detect potential abnormalities with our AI-powered analysis system.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Upload Section
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div class="neuro-card">
                <h3 class="mb-4 text-center" style="color: var(--secondary);">
                    <i class="fas fa-upload me-2"></i>Upload MRI Scan
                </h3>
            </div>
            """, unsafe_allow_html=True)

            uploaded_file = st.file_uploader(
                "Choose an MRI image",
                type=["jpg", "jpeg", "png"],
                key="file_uploader",
                label_visibility="collapsed"
            )

            st.markdown("""
            <div class="file-upload mb-4">
                <label for="file_uploader" class="file-upload-label">
                    <i class="fas fa-cloud-upload-alt file-upload-icon"></i>
                    <h5>Drag & drop your MRI image or click to browse</h5>
                    <p class="text-muted">Supports JPG, PNG formats</p>
                </label>
            </div>
            """, unsafe_allow_html=True)

            analyze_clicked = st.button("Analyze Scan", key="analyze_btn")

    # Results Section
    if analyze_clicked and uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)

            with st.container():
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.markdown("""
                    <div class="neuro-card">
                        <h3 class="mb-4 text-center" style="color: var(--secondary);">
                            <i class="fas fa-clipboard-check me-2"></i>Analysis Results
                        </h3>
                    """, unsafe_allow_html=True)

                    result, confidence = predict_tumor(image)

                    if "No Tumor" in result:
                        icon = "fa-check-circle"
                        color = "text-success"
                    else:
                        icon = "fa-exclamation-triangle"
                        color = "text-warning"

                    st.markdown(f"""
                        <div class="neuro-result p-4 mb-4 rounded">
                            <h4 class="{color}">
                                <i class="fas {icon} me-2"></i>{result}
                            </h4>
                            <p class="neuro-confidence">
                                <i class="fas fa-chart-line me-2"></i>Confidence: {confidence * 100:.2f}%
                            </p>
                        </div>
                        <div class="neuro-image-container mx-auto">
                    """, unsafe_allow_html=True)

                    st.image(image, use_container_width=True)

                    st.markdown("""
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
    elif analyze_clicked and uploaded_file is None:
        st.error("Please upload an image first")

    # Footer
    st.markdown("""
    <div class="neuro-footer" style="text-align: center; margin-top: 2rem; color: #166088; font-size: 0.9rem;">
        <p>NeuroScan v1.0 | Advanced Brain Analysis Technology</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()