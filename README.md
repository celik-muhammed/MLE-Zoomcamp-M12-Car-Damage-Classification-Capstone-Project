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

## Sample Submission

The solution file must contain predictions for every `image_id` in the test set. It must contain only 2 columns - `image_id` and `label`.<br>
The solution file format must be similar to that of `sample_submission.csv`. `sample_submission.csv` contains 2 variables:

- `image_id`: Unique identifier of an image
- `label`: Type of damage present in the car {1:crack, 2:scratch, 3:tire flat, 4:dent, 5:glass shatter, 6:lamp broken}

## Evaluation Metric

The model will be evaluated based on the macro F1 score.

---

## Project Structure

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

### Feature Engineering

- Any additional features or transformations.

---

## Modeling

### Model Selection

- Explanation of chosen model(s).
- Training strategy.

### Hyperparameter Tuning

- Explanation of hyperparameter choices.
- Cross-validation approach.

---

## Evaluation

### Performance Metrics

- Definition of evaluation metrics.
- Results on validation and test sets.

### Model Interpretability

- Techniques used for model interpretability.

---

## Deployment

### Model Deployment

- Steps to deploy the model.
- Endpoint details.

### Monitoring

- Continuous monitoring strategies.

---

## Conclusion

### Summary

- Recap of the project.
- Achievements and challenges.
