# 🧠 NeuroScan
NeuroScan is a deep learning–based computer vision application designed to detect and classify brain tumors from MRI scans using MobileNetV3Large and transfer learning. Built with Streamlit and TensorFlow, it provides a user-friendly interface for medical professionals and researchers to quickly assess potential abnormalities.The model is trained to distinguish among four distinct classes:

- Pituitary Tumors

- Glioma Tumors

- Meningioma Tumors
  
- No Tumor
## Project Background
The purpose of this project is ________. (Describe the main goals of the project and potential civic impact. Limit to a short paragraph, 3-6 Sentences)

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.


### Technologies Used
* Python
* TensorFlow
* Streamlit
* Pandas
* Numpy

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Data & Preprocessing
The data for this project was sourced from the Brain Tumor MRI Dataset on Kaggle.
### Image Augmentation
Image augmentation was used to improve model genralization while preserving critical diagnostic features in the MRI scans. The methods used for image augmentation include:

**1. Brightness Adjustment** -> Randomly increases or decreases the image brightness by ±20%.
   
   &emsp; Purpose: Mimics variations in scanner intensity and lighting conditions.
   
**2. Contrast Enhancement** -> Randomly adjusts the contrast, making details either more or less prominent.
   
   &emsp; Purpose: Helps the model learn to detect tumors even when the tumor region isn't sharply defined.

## Training the Model
Optimizer: Adam (lr=0.0001)
Loss: Sparse Categorical Crossentropy
Batch Size: 20
Epochs: 50
Fine-Tuning: Last 20 layers unfrozen

### Why Transfer Learning?
Transfer learning is crucial for medical imaging where:

- Labelled data is limited.
- Training deep CNNs from scratch is computationally expensive.
- Pretrained models can generalize well with minimal fine-tuning.

MobileNetV3Large, trained on millions of images, already understands basic visual features (edges, textures, shapes). By freezing these layers, the model adapts quickly to specialized medical data.

### MobileNetV3
<img width="700" height="450" alt="image" src="https://github.com/user-attachments/assets/93897077-3595-4f92-a6b4-b54e67618f26" />


## Results



## Demo




## References
Kumar, S., & Mankame, D. P. (2020). Optimization driven deep convolution neural network for brain tumor classification. Biocybernetics and Biomedical Engineering, 40(3), 1190-1204. https://doi.org/10.1016/j.bbe.2020.05.009

Mathivanan, S. K., Sonaimuthu, S., Murugesan, S., Rajadurai, H., Shivahare, B. D., & Shah, M. A. (2024). Employing deep learning and transfer learning for accurate brain tumor detection. Scientific reports, 14(1), 7232. https://doi.org/10.1038/s41598-024-57970-7

Msoud Nickparvar. (2021). Brain Tumor MRI Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/2645886

Woźniak, M., Siłka, J., & Wieczorek, M. (2023). Deep neural network correlation learning mechanism for CT brain tumor detection. Neural Computing and Applications, 35(20), 14611-14626. https://doi.org/10.1007/s00521-021-05841-x

