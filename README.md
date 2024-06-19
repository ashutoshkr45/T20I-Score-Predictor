# T20I-Score-Predictor

## Description

This project focuses on predicting the first innings score of Men's T20 International cricket matches using machine learning techniques. The models are trained on a comprehensive dataset obtained from Kaggle, encompassing ball-by-ball data from T20I matches spanning from 2003 to 2023.

## Dataset

- **Dataset Source**: [T20I Men's Cricket Match Data (2003 - 2023)](https://www.kaggle.com/datasets/jamiewelsh2/ball-by-ball-it20/data)
- **File Used**: ball_by_ball_it20.csv

The dataset provides detailed insights into each T20I match, capturing crucial match-specific attributes that influence the prediction of first innings scores.

## Overview

The project's primary goal is to develop an accurate regression model that predicts the final score of the first innings in T20I cricket matches. To achieve this, several preprocessing steps and feature engineering techniques were implemented to enhance model performance.

## Motivation

The motivation behind this project stems from the need to leverage machine learning to predict cricket match outcomes accurately. T20I cricket, known for its fast-paced and dynamic nature, presents a challenging yet exciting domain for predictive modeling.

## Technical Aspects

- **Feature Extraction and Engineering**:
  - Extracted relevant features from the dataset, focusing on match-specific attributes.
  - Filtered data to include matches from January 1, 2011, onwards to align with the contemporary pace of T20 cricket.
  - Incorporated venue-to-country mapping to enrich venue-based analysis.

- **Model Building**:
  - Developed two main regression models:
    - **XGBoost Regression**: Utilizes gradient boosting techniques with extensive hyperparameter tuning.
    - **Random Forest Regression**: Implemented for comparative analysis against XGBoost.
  - Conducted rigorous evaluation using metrics such as R2 Score and Mean Absolute Error (MAE) to assess model performance.

- **Model Selection**:
  - Selected XGBoost Regression based on superior predictive accuracy (higher R2 Score) compared to other models tested.
  - Demonstrated model predictions for sample match scenarios using both XGBoost and Random Forest models.

- **Deployment**:
  - Saved the trained XGBoost model using pickle for deployment in web application.

## Conclusion

This project underscores the efficacy of machine learning in predicting cricket match outcomes, specifically the first innings score in T20I matches. By leveraging advanced regression techniques and comprehensive dataset analysis, the models presented here demonstrate robust performance and potential applications in cricket analytics.

