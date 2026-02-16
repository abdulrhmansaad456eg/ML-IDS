import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

def train():
    print("Training Smart Behavioral AI...")
    data = []

    
    for _ in range(1000):
        data.append([np.random.normal(1000, 200), np.random.choice([80, 443]), 6, 0])

    
    for _ in range(800):
        data.append([np.random.normal(60, 20), np.random.choice([53, 5353, 500, 123]), 17, 0])

    
    for _ in range(1000):
        data.append([np.random.normal(40, 5), np.random.randint(1024, 65535), 6, 1])

    
    for _ in range(500):
        data.append([np.random.normal(150, 20), 80, 6, 1])

    df = pd.DataFrame(data, columns=['packet_len', 'dst_port', 'protocol', 'label'])
    X = df.drop('label', axis=1)
    y = df['label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_scaled, y)

    joblib.dump(model, 'ids_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("✅ Model trained to recognize behavioral patterns!")

if __name__ == "__main__":
    train()