# 🧠 NeuroScan
NeuroScan is a deep learning–based computer vision application designed to detect and classify brain tumors from MRI scans using MobileNetV3Large and transfer learning. Built with Streamlit and TensorFlow, it provides a user-friendly interface for medical professionals and researchers to quickly assess potential abnormalities. The model is trained to distinguish among four distinct classes:

- Pituitary Tumors

- Glioma Tumors

- Meningioma Tumors
  
- No Tumor
## Project Background
Brain tumors are abnormal growths of cells within the brain or its surrounding structures, which can be either **benign** (non-cancerous) or **malignant** (cancerous). They are classified into several types based on their origin and behavior, with the most common primary brain tumors including **gliomas** (arising from glial cells, often aggressive), **meningiomas** (typically benign, forming in the meninges), and **pituitary adenomas** (developing in the pituitary gland). Early and accurate detection is critical, as tumors can cause neurological deficits, seizures, or life-threatening complications depending on their size and location. Traditional diagnosis relies on MRI or CT scans analyzed by radiologists, but manual interpretation can be time-consuming and subjective. 

NeuroScan addresses these challenges by leveraging deep learning to **automate brain tumor classification**, providing rapid, standardized assessments of MRI scans. By distinguishing between tumor types and non-tumor cases with high accuracy, this system aids clinicians in **prioritizing urgent cases, reducing diagnostic delays, and improving patient outcomes**. The tool is particularly valuable in resource-limited settings where access to specialized neuroradiologists is scarce.

### Technologies Used
* Python
* TensorFlow
* Streamlit
* Pandas
* Numpy

## Getting Started

1. Access NeuroScan [here](https://neuro-scan.streamlit.app/).
2. Upload an MRI scan image (sample images are available in the `test_images` folder).
3. The model will automatically analyze the scan and display the predicted tumor classification.

### Demo



## ⚙️ Data & Preprocessing
The data for this project was sourced from the [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
 on Kaggle.

 #### Image Resizing & Normalization
- All MRI images were resized to **128×128 pixels** to reduce input complexity and speed up training.
- Pixel values were **normalized to the range [0, 1]**, which stabilizes gradient updates and accelerates convergence.
> ✅ *Standardized input scaling helps prevent the model from overfitting to intensity-based artifacts.*

#### Randomized Data Shuffling
- **Training and testing image paths were shuffled** prior to loading.
- This avoids the model learning any pattern related to file order or folder structure.
> ✅ *Introduces statistical randomness into batches, improving generalization.*

#### Dropout for Regularization
- A **dropout layer with rate 0.5** was added in the classification head
- During training, half the neurons are randomly deactivated, forcing the model to rely on multiple redundant features.
> ✅ Promotes robustness by preventing over-reliance on specific neurons.

### Image Augmentation

To improve model generalization without compromising important diagnostic features in MRI scans, several data augmentation techniques were applied:

#### Brightness Adjustment
- Randomly modifies image brightness by up to **±20%**.
> ✅  *Simulates real-world variations in scanner intensity and lighting conditions.*

#### Contrast Enhancement
- Randomly changes the **contrast** to make image details more or less prominent.
> ✅  *Helps the model recognize tumors even when tumor boundaries are faint or ambiguous.*

   
<img width="917" height="400" alt="Screenshot 2025-07-20 at 9 24 45 AM" src="https://github.com/user-attachments/assets/fb7b553e-ff87-4a4b-bced-75a53da020de" />


## Training the Model

### Training Configuration and Rationale

- **Transfer Learning Strategy**  
  Used **MobileNetV3Large** with transfer learning to leverage pretrained visual features

- **Optimizer**  
  Chose the **Adam optimizer** with a **low learning rate (0.0001)** to:  
  - Prevent large updates that could overwrite pretrained weights  
  - Allow gradual fine-tuning of the unfrozen layers

- **Loss Function**  
  Used **sparse categorical crossentropy** for multi-class classification:  
  - Suitable for classifying **glioma, meningioma, pituitary tumor, and no tumor**  
  - Efficient as it does not require one-hot encoding of labels

- **Batch Size**  
  Set to **20** to balance:  
  - **Memory constraints** from processing 224×224 MRI images  
  - **Gradient stability** during training

- **Epochs**  
  Trained for **50 epochs** to ensure the model **fully converges**

- **Layer Freezing**  
  Only the **last 20 layers** were unfrozen to:  
  - Retain early-layer features useful for general image recognition  
  - Specialize deeper layers for MRI-specific tumor detection


### Why Transfer Learning?
Transfer learning is crucial for medical imaging where:

- Labelled data is limited
- Training deep CNNs from scratch is computationally expensive
- Pretrained models can generalize well with minimal fine-tuning

MobileNetV3Large, trained on millions of images, already understands basic visual features (edges, textures, shapes). By freezing these layers, the model adapts quickly to specialized medical data.

### MobileNetV3
* **Optimized for Transfer Learning:** Pre-trained on ImageNet, making it highly effective when fine-tuned on medical imaging tasks

* **Fast Inference Time:** Ideal for real-time predictions in a web app environment

* **Small Model Size:** Easier to deploy and more memory-efficient than larger models like ResNet or Inception

* **High Accuracy on Limited Data:** Performs well even with smaller datasets, which is necessary for the brain tumor dataset

* **Robust Performance:** Balances speed, accuracy, and resource usage—key for user-facing tools

<img width="700" height="450" alt="image" src="https://github.com/user-attachments/assets/93897077-3595-4f92-a6b4-b54e67618f26" />


## Results
<img width="451" height="192" alt="Screenshot 2025-07-20 at 11 13 12 AM" src="https://github.com/user-attachments/assets/2acb0f5e-d8af-4a7f-90bb-ebdde97c7b17" />

<img width="700" height="545" alt="Screenshot 2025-07-20 at 9 25 21 AM" src="https://github.com/user-attachments/assets/399e6a67-9ae1-4ecf-b952-4ba3bc938504" />

<img width="700" height="545" alt="Screenshot 2025-07-20 at 11 13 42 AM" src="https://github.com/user-attachments/assets/3301b4a0-0905-40da-9209-c5f46128b7a4" />


## References
Kumar, S., & Mankame, D. P. (2020). Optimization driven deep convolution neural network for brain tumor classification. Biocybernetics and Biomedical Engineering, 40(3), 1190-1204. https://doi.org/10.1016/j.bbe.2020.05.009

Mathivanan, S. K., Sonaimuthu, S., Murugesan, S., Rajadurai, H., Shivahare, B. D., & Shah, M. A. (2024). Employing deep learning and transfer learning for accurate brain tumor detection. Scientific reports, 14(1), 7232. https://doi.org/10.1038/s41598-024-57970-7

Msoud Nickparvar. (2021). Brain Tumor MRI Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/2645886

Woźniak, M., Siłka, J., & Wieczorek, M. (2023). Deep neural network correlation learning mechanism for CT brain tumor detection. Neural Computing and Applications, 35(20), 14611-14626. https://doi.org/10.1007/s00521-021-05841-x

