# MLE-Zoomcamp-M12-Car-Damage-Image-Classification-Capstone-Project

## Introduction

In the insurance industry, processing claims for vehicle damage is a common task.<br>
With advancements in AI and Computer Vision, settling claims online by uploading damaged car images is now possible.

## Dataset

> https://www.kaggle.com/datasets/imnandini/analytics-vidya-ripik-ai-hackfest
>> Training set (`train.zip`)<br>
>> Test set (`test.zip`)<br>
>> Sample submission (`sample_submission.csv`)

### Training Dataset

The training set contains a diverse dataset of car images with labels indicating the specific type of damage (e.g., dents, scratches, cracks).<br>
The `train.csv` file includes the following columns:

- `image_id`: Unique identifier of the image<br>
- `filename`: Filename of the image<br>
- `label`: Type of damage present in the car<br>
  1. Crack
  2. Scratch
  3. Tire Flat
  4. Dent
  5. Glass Shatter
  6. Lamp Broken

### Test Dataset

The test set contains only images, and the goal is to predict the type of damage for each image.<br>
The `test.csv` file includes the following columns:

- `image_id`: Unique identifier of the image
- `filename`: Filename of the image

### Sample Submission

The solution file must contain predictions for every `image_id` in the test set. It must contain only 2 columns - `image_id` and `label`.<br>
The solution file format must be similar to that of `sample_submission.csv`. `sample_submission.csv` contains 2 variables:

- `image_id`: Unique identifier of an image
- `label`: Type of damage present in the car {1:crack, 2:scratch, 3:tire flat, 4:dent, 5:glass shatter, 6:lamp broken}

## Evaluation Metric

The model will be evaluated based on the macro F1 score.

---

# Project Structure

The project is organized into CRISP-DM phases for effective development and documentation.

## Table of Contents

1. [Business Understanding](#business-understanding)
2. [Data Understanding](#data-understanding)
3. [Data Preparation](#data-preparation)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Deployment](#deployment)
7. [Conclusion](#conclusion)

---

## Business Understanding

### Project Name

- **GitHub Repo:** [Car Damage Image Classification Capstone Project](https://github.com/yourusername/multiclass-classification)
- **Project Notebook:** [Car_Damage Image_Multi_Class_Classification.ipynb](path/to/your/notebook.ipynb)

### Problem Statement
Identifying fraudulent claims, especially those exaggerating damage, poses a challenge. The goal is to develop a high-performance model for automatic car damage classification, enabling insurance companies to assess claim legitimacy accurately.

### Objective

Develop a model to automatically classify images of damaged cars into different types of damages for efficient claims processing and fraud detection.

### Stakeholders

- Insurance companies
- Claim processing teams

---

## Data Understanding

### Data Collection

- Description of dataset acquisition.
- Dataset statistics.

### Exploratory Data Analysis (EDA)

- Visualizations of image samples and their labels.
- Insights into class distribution.

---

## Data Preparation

### Data Preprocessing

- Image resizing and normalization.
- Augmentation techniques applied.

<!-- 
### Feature Engineering

- Any additional features or transformations.
-->

---

## Modeling

### Model Selection

- Keras offers pretrained models at [keras.io](https://keras.io/api/applications/)
- I use the [EfficientNetV2B0](https://keras.io/api/applications/convnext) model due to its fairly high Top-1 Accuracy and does not require depth.
- EfficientNetV2 models expect their inputs to be float tensors of pixels with values in the [0, 255] range.

### Hyperparameter Tuning

- Change Learning Rate
- Adding more layers
    - Conv2D
    - AveragePooling2D
    - SpatialDropout2D
    - Dropout
    - BatchNormalization

---

## Evaluation

### Performance Metrics

- Definition of evaluation metrics.
  - Submissions are evaluated using the [probabilistic F1 score](https://aclanthology.org/2020.eval4nlp-1.9.pdf) (pFbeta)
- Results on validation and test sets.

```sh
675/675 [==============================] - 598s 886ms/step - loss: 1.3841 - categorical_accuracy: 0.3993 - pFbeta: 0.3193 - precision: 0.5266 - recall: 0.1667 - val_loss: 1.5634 - val_categorical_accuracy: 0.3800 - val_pFbeta: 0.2988 - val_precision: 0.4104 - val_recall: 0.1400
```

<!-- 
### Model Interpretability

- Techniques used for model interpretability.
-->

---

## Deployment

### Model Deployment

#### Preparing Docker Image

- https://repost.aws/knowledge-center/lambda-container-images

Build docker image using the recommended public image for Lambda once Dockerfile has been created below:

```sh
docker build -t car-insurance-model .
```

To test first run image that was built:

```sh
docker run -it --rm -p 8080:8080 car-insurance-model:latest
```

#### Docker Hub

```sh
# Tag the Existing Image, username/car-insurance-model:new-tag
docker tag car-insurance-model:latest developerhost/car-insurance-model:latest

# Push the newly tagged image to Docker Hub:
developerhost/car-insurance-model:latest

# you can pull the image:
docker pull developerhost/car-insurance-model:latest
```

#### test.py created per AWS documentation for testing

lambda function a function must be added as below to the lambda_function.py file:

```py
def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
```

Run the file:

```sh
python client_to_docker_test.py
```

This is the output I recieved which clearly shows that the image was predicted as a "dent" which is correct:

```sh
{'crack': 0.006185653153806925,
 'scratch': 0.34056955575942993,
 'tire_flat': 0.021280569955706596,
 'dent': 0.5486962795257568,
 'glass_shatter': 0.0674322172999382,
 'lamp_broken': 0.01583569310605526}
```

#### Testing function for Lambda

output:

```sh
# python client_to_docker_test.py
# {"crack": 0.006185653153806925, "scratch": 0.34056955575942993, "tire_flat": 0.021280569955706596, "dent": 0.5486962795257568, "glass_shatter": 0.0674322172999382, "lamp_broken": 0.01583569310605526}
```

<!-- 
### Monitoring

- Continuous monitoring strategies.
-->

---

## Conclusion
<!-- 
### Summary

- Recap of the project.
- Achievements and challenges.
 -->
