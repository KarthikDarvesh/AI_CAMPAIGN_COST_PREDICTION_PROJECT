## ⚠️ Disclaimer

> This repository **does NOT contain or expose any real organizational, client, or campaign data**.
>
> The original dataset used in this project is **confidential and proprietary** and therefore **not included** in this repository due to organizational data privacy and confidentiality policies.
>
> All **examples, workflows, diagrams, model logic, API structures, and descriptions** provided here are shared **strictly for architectural, technical, and process explanation purposes only**.
>
> - No real business data is distributed  
> - No sensitive or confidential information is shared  
> - Any sample values (if present) are **synthetic or illustrative**
>
> This project is intended **solely for educational, learning, and demonstration purposes**, to showcase:
>
> - Machine learning workflow design  
> - Feature engineering approaches  
> - Model comparison strategies  
> - API deployment architecture using FastAPI  
>
> ❗ **This repository should NOT be considered a production-ready implementation** without proper data governance, security review, and validation using authorized datasets.
>
> - Learn from this project, but don’t deploy it in production as-is.

---
---

<img width="1942" height="809" alt="image" src="https://github.com/user-attachments/assets/c71aa673-4d55-4c6e-a1e0-aa182715e2a0" />

---
---

## 📁 Dataset

- **Source:** Google Sheets (CSV export link)
- **Name:** `New_AI_Final Data`
- **Path:**  
  `MyDrive/Colab Notebooks/1. Project 1: AI CAMPAIGN COST 2023-24 PROJECT (Done)/AI Cost Data.gsheet`

**Data Fetching Strategy:**  
Instead of using a downloaded CSV file with read.csv(), the dataset is fetched directly from a Google Sheets link.

Explanation:
A direct Google Sheets export URL is used to read the data. This allows the sheet to be read directly without manually downloading the file, ensuring the latest updated data is always available.

---

## 🧠 Feature Descriptions

| Feature                              | Description |
|--------------------------------------|-------------|
| `brand_name`                         | Advertiser running the campaign (e.g., mStock) |
| `product_name`                       | Product/service promoted |
| `yt_username`                        | YouTube influencer's channel name |
| `overall_videos_viewcount_of_channel`| Total video views on the channel |
| `channels_subscriber`                | Total number of subscribers |
| `first_five_avg_video_of_channel`    | Avg. metrics from first 5 videos |
| `engagement_rate_of_channel`         | Engagement rate from audience |
| `video_views`                        | Views on the campaign video |
| `video_duration`                     | Video length (in seconds) |
| `category`                           | Content type (e.g., Finance, Tech) |
| `video_type`                         | Video format (e.g., Dedicated, Shorts) |

---

## 🧰 Tools & Libraries

- **pandas** 
- **numpy**
- **matplotlib**, **seaborn**
- **scikit-learn**, **XGBoost**
- **FastAPI** 
- **joblib**

---

## 🔍 Data Analysis Workflow

1. **Data Cleaning With Pandas**  

2. **EDA (Exploratory Data Analysis):**
   **Co-Relation (HEATMAP):**
   - video_cost vs video_type
   - video_cost vs category
   - video_cost vs engagement_rate_of_channel

4. **Outlier Detection with Scatter & Box Plots**  
  
5. **Brand-Specific Outlier Cleaning**  
   - Each brand had its own subset of outliers removed using IQR (Interquartile Range)
   - Notable Features
     
       ● Outlier Removal Strategy:
         Each category of campaign is analyzed and cleaned individually.
         A sequence of before-and-after visuals highlights the effect of outlier filtering.

6. **Feature Engineering Before Feeding to Model**  
After testing with many models, both RandomForestRegressor and XGBRegressor
provided good accuracy for predicting campaign costs.

🧬 Feature Encoding Techniques
  - Tree-based models such as RandomForestRegressor and XGBRegressor can handle both One-Hot Encoding and Label Encoding effectively.
  - Both encodings were tested independently on the same dataset using the same models, to normalize the comparison and identify the better fit for cost prediction.
  - Here strategy to try both encodings and compare results was absolutely correct and aligned with best practices in machine learning


## 🧠 ML Model Learning & Evaluation

Several regression models were applied and evaluated using multiple error metrics to determine their effectiveness in predicting campaign costs.

### 🔍 Models Tested & Performance Comparison

#### 📌 Linear Regression
❌ Poor accuracy on test data  
❌ Not suitable for accurate campaign cost prediction

---
#### 📌 Ensemble Models – Bagging

**RandomForestRegressor**  
✅ Provided stable and accurate results  
🏆 Performed best among tested models  
🧪 Tested on:
- One-Hot Encoded dataset  
- Label Encoded dataset  

**ExtraTreesRegressor**  
✅ Similar performance to RandomForestRegressor  
✅ Stable prediction behavior  
⚠️ No major improvement over RandomForest  

---
#### 📌 Ensemble Models – Boosting

**GradientBoostingRegressor**  
❌ Poor accuracy on test data  
📉 Underperformed compared to bagging models  

**XGBRegressor**  
✅ Strong performance overall  
⚠️ Slightly lower accuracy than RandomForestRegressor  
🧪 Evaluated using:
- One-Hot Encoding  
- Label Encoding  

---
#### 📌 Support Vector Regression (SVR)
❌ Poor accuracy on test data  
❌ Not effective for this dataset  
 
---

### ✅ Best Performing Model

**🎯 RandomForestRegressor** using **Label Encoding** delivered the **best overall performance** across all models and evaluation metrics.

### 📈 Model Performance & Encoding Strategy
- R2 Score, MAE, RMSE, MSE

---

### 🔄 Encoding Strategy Comparison

In this project, both **One-Hot Encoding** and **Label Encoding** strategies were tested to evaluate their impact on:

- Feature space size  
- Model training time  
- Prediction error metrics  
- Model generalization capability
  
---

### 💡 Why Label Encoding Was Preferred:

- **Label Encoding** offers a **compact feature set**, making it more efficient in terms of memory and performance.
- **One-Hot Encoding** increases the number of features significantly, which:
  - May lead to **overfitting** if the dataset is not large enough  
  - Increases model complexity and training time unnecessarily

As a result, Label Encoding was selected for final model deployment.

---

### 🏆 Final Result

- **Best Model:** `RandomForestRegressor`  
- **Best Encoding Strategy:** `Label Encoding`

---

### 🔬 6. Model Testing

In the final model testing phase, the trained **RandomForestRegressor** model was:

- **Loaded** from the serialized `.pkl` file
- **Provided with new input data**
- **Used to predict campaign costs**

✅ The predictions confirmed the model’s **effectiveness** and **readiness for deployment** in a real-time environment.

---


### 🌐 7. API Endpoint Details

- **Route:** `/predict`  
- **Method:** `GET`  
- **Test URL:** [http://localhost:8000/predict](http://localhost:8000/predict)

#### 📥 Input Parameters:
1. `brand_name`  
2. `product_name`  
3. `for_username`  
4. `overall_videos_viewcount_of_channel`  
5. `subscribers_channel`  
6. `first_five_avg_video_of_channel`  
7. `engagement_rate_of_channel`  
8. `video_views`  
9. `video_duration` (in `HH:MM:SS`)  
10. `category`  
11. `video_type`

#### 📤 Output:
- Returns the **predicted `video_cost`** (in `float` format)

<img width="1265" height="403" alt="image" src="https://github.com/user-attachments/assets/5685ea77-1ae8-478d-b078-6d54e99cec27" />

---

### 📁 Project Structure

AI_Campaign_Cost_Prediction_Project/

├── app.py # FastAPI app with /predict endpoint

├── Dockerfile # For containerizing the API

├── requirements.txt # Python dependencies

├── RF_trained_model.pkl # Trained RandomForestRegressor model

---

### ⚙️ Key Features

- ✅ Trained model loaded from `RF_trained_model.pkl`  
- 🔄 Input preprocessing includes:
  - Duration conversion (`HH:MM:SS` → seconds)
  - Label encoding for categorical fields  
- ❗ Handles unseen category values using fallback encoding (`-1`)  
- 🧰 Built using `joblib`, `pandas`, and `FastAPI`

---

### ▶️ Run the API

#### 📦 Install Required Libraries

```bash
pip install -r requirements.txt

To start the FastAPI application locally, run the following command:

🚀 Launch the FastAPI Server
uvicorn app:app --reload
