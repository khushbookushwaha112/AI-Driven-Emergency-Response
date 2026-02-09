
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

# 1. Load the Dataset
csv_path = 'data/crime_logic_matrix.csv'
if not os.path.exists(csv_path):
    print(f"❌ Error: Dataset not found at {csv_path}")
    exit()

print(f"📂 Loading dataset from {csv_path}...")
df_matrix = pd.read_csv(csv_path)

# 2. Extract Logic and Keywords
crime_keywords = {}
crime_details = {}

for index, row in df_matrix.iterrows():
    crime_type = row['Crime_Type']
    # Keywords split by comma and strip whitespace
    keywords = [k.strip() for k in str(row['Keywords']).split(',')]
    crime_keywords[crime_type] = keywords
    
    # Save details for API response
    crime_details[crime_type] = {
        'Priority': row['Priority'],
        'Response_Units': row['Response_Units'],
        'Action': row['Action'],
        'Radius_km': row.get('Radius_km', 0)
    }

print(f"✅ Loaded {len(crime_keywords)} crime types: {list(crime_keywords.keys())}")

# 3. Automatic Data Generator (Synthetic Data based on CSV keywords)
aug_text, aug_label = [], []
print("⚙️ Generating synthetic training data...")

for crime, keywords in crime_keywords.items():
    # Generate 500 samples per crime type
    for _ in range(500):
        # Pick 2 random KEYWORDS from the list (if enough exist)
        if len(keywords) >= 2:
            selected = np.random.choice(keywords, size=2, replace=False)
            sentence = f"Emergency! {selected[0]} happened. {selected[1]} reported near my location."
        else:
            # Fallback if only 1 keyword exists
            selected = np.random.choice(keywords, size=1)
            sentence = f"Emergency! There is a {selected[0]} here. Please help."
            
        aug_text.append(sentence)
        aug_label.append(crime)

df_pro = pd.DataFrame({'text': aug_text, 'label': aug_label})

# 4. Vectorization
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=10000)
X = vectorizer.fit_transform(df_pro['text'])
y = df_pro['label']

# 5. Train Model
print("🚀 Training Random Forest Model...")
ml_model = RandomForestClassifier(n_estimators=300, max_depth=None, random_state=42)
ml_model.fit(X, y)

# 6. Save Files
print("💾 Saving models to disk...")
joblib.dump(ml_model, 'crime_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(crime_details, 'crime_details.pkl')  # Save logic for API

print("🔥 SUCCESS: Model trained on uploaded dataset and saved successfully!")
