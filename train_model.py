
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import os

# 1. Load the Dataset
csv_path = 'data/crime_logic_matrix.csv'
if not os.path.exists(csv_path):
    print(f"❌ Error: Dataset not found at {csv_path}")
    exit()

print(f"📂 Loading dataset from {csv_path}...")
df_matrix = pd.read_csv(csv_path)

# 2. Extract Logic and Enhanced Keywords
crime_keywords = {}
crime_details = {}

# Specific Hinglish/Hindi keywords mapping to boost accuracy
hinglish_boost = {
    "Kidnapping/Abduction": ["bacha utha liya", "gayab ho gaya", "missing", "van mein", "kidnap", "apharan", "beti nahi mil rahi", "school se", "zabardasti"],
    "Serious Road Accident": ["accident", "takkar", "crash", "khoon", "bhir gayi", "car lad gayi", "totka", "injured", "marr gaya", "blood"],
    "Armed Robbery": ["gun", "pistol", "chaku", "knife", "lutera", "loot", "dacoity", "hathiyar", "paise cheen liye"],
    "Murder/Homicide": ["murder", "hatya", "khoon", "lash", "body found", "dead body", "maar diya", "chakku maara", "goli maari"],
    "Chain Snatching": ["chain", "snatch", "gala", "mangalsutra", "jhamta", "cheen kar", "bike par", "bhaag gaye"],
    "Cyber Fraud": ["otp", "bank", "scam", "paise kat gaye", "online fraud", "hack", "account empty", "upi fraud"]
}

for index, row in df_matrix.iterrows():
    crime_type = row['Crime_Type']
    # Start with CSV keywords
    keywords = [k.strip().lower() for k in str(row['Keywords']).split(',')]
    
    # Add Hinglish boosters if available
    if crime_type in hinglish_boost:
        keywords.extend(hinglish_boost[crime_type])
        
    crime_keywords[crime_type] = list(set(keywords))  # Remove duplicates
    
    # Save details for API response
    crime_details[crime_type] = {
        'Priority': row['Priority'],
        'Response_Units': row['Response_Units'],
        'Action': row['Action'],
        'Radius_km': row.get('Radius_km', 0)
    }

print(f"✅ Loaded {len(crime_keywords)} crime types with Enhanced Hinglish Support.")

# 3. Enhanced Synthetic Data Generator
aug_text, aug_label = [], []
print("⚙️ Generating rigorous training data (1000 samples/crime)...")

templates = [
    "Emergency! {kw} happened here.",
    "Help! {kw} reported near my location.",
    "Police please come, {kw} ho gaya hai.",
    "There is a case of {kw}.",
    "Quickly send help for {kw}.",
    "Bohot bura hua, {kw} dekha maine.",
    "{kw} at visuals.",
    "Someone reported {kw} just now."
]

for crime, keywords in crime_keywords.items():
    # Generate 1000 samples per crime type for better learning
    for _ in range(1000):
        # Pick a random keyword
        kw = np.random.choice(keywords)
        # Pick a random template
        template = np.random.choice(templates)
        sentence = template.format(kw=kw)
        
        aug_text.append(sentence)
        aug_label.append(crime)

df_pro = pd.DataFrame({'text': aug_text, 'label': aug_label})

# 4. Better Vectorization (Character n-grams for spelling mistakes + Word n-grams)
vectorizer = TfidfVectorizer(ngram_range=(1, 4), analyzer='char_wb', max_features=20000)
X = vectorizer.fit_transform(df_pro['text'])
y = df_pro['label']

# 5. Train Stronger Model
print("🚀 Training Random Forest Model (High Accuracy Mode)...")
ml_model = RandomForestClassifier(n_estimators=500, max_depth=None, random_state=42, n_jobs=-1)
ml_model.fit(X, y)

# 6. Save Files
print("💾 Saving robust models to disk...")
joblib.dump(ml_model, 'crime_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(crime_details, 'crime_details.pkl')

print("🔥 SUCCESS: Retraining Complete! Model is now smarter with Hinglish.")
