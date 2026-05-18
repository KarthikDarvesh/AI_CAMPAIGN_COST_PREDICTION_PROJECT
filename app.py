from fastapi import FastAPI
import pandas as pd
import joblib
# from typing import Union

# Load the trained model
model_path = "/home/karthik22/ML_Project/AI_Campaign_Cost_Prediction_Project/RF_trained_model.pkl"
dataset_path = "/home/karthik22/ML_Project/AI_Campaign_Cost_Prediction_Project/cleanned_data.csv"

model = joblib.load(model_path)

# Load dataset (before label encoding)
df = pd.read_csv(dataset_path)

# Identify categorical columns for encoding
categorical_cols = ["brand_name", "product_name", "for_username", "category", "video_type"]

# Create encoding mappings
encoding_mappings = {col: {label: idx for idx, label in enumerate(df[col].astype(str).unique())} for col in categorical_cols}
def encode_input(data: dict):
    """Encodes input categorical values using precomputed mappings."""
    for col in categorical_cols:
        data[col] = encoding_mappings[col].get(data[col], -1)  # Assign -1 for unseen values
    return data

def convert_duration(duration: str) -> int:
    """Convert HH:MM:SS duration to total seconds."""
    h, m, s = map(int, duration.split(":"))
    return h * 3600 + m * 60 + s

# Initialize FastAPI
app = FastAPI()
@app.get("/predict")
def predict(
    brand_name: str,
    product_name: str,
    for_username: str,
    overall_videos_viewcount_of_channel: int,
    subscribers_channel: int,
    first_five_video_avg_of_channel: int,
    engagement_rate_of_channel: float,
    video_views: int,
    video_duration: str,  # Expecting string HH:MM:SS
    category: str,
    video_type: str
):
    # Convert input to dictionary
    input_dict = {
        "brand_name": brand_name,
        "product_name": product_name,
        "for_username": for_username,
        "overall_videos_viewcount_of_channel": overall_videos_viewcount_of_channel,
        "subscribers_channel": subscribers_channel,
        "first_five_video_avg_of_channel": first_five_video_avg_of_channel,
        "engagement_rate_of_channel": engagement_rate_of_channel,
        "video_views": video_views,
        "video_duration": convert_duration(video_duration),  # Convert duration
        "category": category,
        "video_type": video_type,
    }
    # Encode categorical values
    encoded_input = encode_input(input_dict)
    # Convert to DataFrame
    input_df = pd.DataFrame([encoded_input])
    # Predict video cost
    prediction = model.predict(input_df)[0]
    return {"predicted_video_cost": prediction}