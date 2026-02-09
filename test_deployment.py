
import requests

# 🟢 STEP 1: Yahan Apna Render ka URL paste karein
# Example: "https://police-api.onrender.com"
base_url = input("Paste your Render API URL here (e.g. https://your-app.onrender.com): ").strip()

# Remove trailing slash if present
if base_url.endswith('/'):
    base_url = base_url[:-1]

print(f"\n🔍 Testing API at: {base_url} ...\n")

# 🟢 STEP 2: FIR Test Data
test_data = {
    "fir_text": "ek van ayi aur bache ko utha kar le gayi school ke bahar se"
}

try:
    # 🟢 STEP 3: Request bhejna
    response = requests.post(f"{base_url}/predict", json=test_data)
    
    # 🟢 STEP 4: Output dekhna
    if response.status_code == 200:
        print("✅ SUCCESS! API Response:")
        print("-----------------------------")
        print(response.json())
        print("-----------------------------")
    else:
        print(f"❌ Failed: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ Error: {e}")
    print("Check if the URL is correct and the app is running.")
