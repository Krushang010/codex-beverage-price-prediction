🧃 CodeX Beverage — Price Range Predictor

An end-to-end Machine Learning + Streamlit application that predicts consumer beverage price segments using behavioral and demographic data.

📊 Model Performance
Metric	Value
Algorithm	LightGBM
Test Accuracy	92.64%
Cross-Validation	92.17% ± 0.32
Features Used	15 (post feature selection)

🧠 Key Highlights
Engineered advanced features: CF_AB Score, ZAS, BSI, Age Group
Performed EDA, feature selection (VIF, correlation), and model optimization
Compared multiple models → selected LightGBM (best performer)
Integrated SHAP-based insights for interpretability
Built modular ML pipeline + interactive UI

🚀 Run Locally
## 🚀 How to Run

### Step 1 — Save the model from your notebook
Run `save_model.py` code inside your Jupyter notebook after training.
This creates `lgbm_model.pkl` in your project folder.

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

### Step 4 — Open in browser
Streamlit will open automatically at `http://localhost:8501`

## 📁 Project Structure
```
├── app.py               # Streamlit app (UI + controller)
├── ui.py                # UI components & styling
├── model_utils.py       # Feature engineering & prediction logic
├── config.py            # Encoding maps & constants
├── lgbm_model.pkl       # Trained LightGBM model
├── requirements.txt     # Dependencies
├── README.md
```

## 💡 Features
- Interactive consumer profile input dashboard
- Real-time price range prediction
- Class-wise confidence probability visualization
- Built-in feature-driven logic (behavior + income + zone)
- Demo mode support (runs without model file)



🎯 Business Use Case

Helps beverage companies:

- Identify customer price sensitivity
- Improve pricing strategies
- Enable targeted marketing & segmentation

🛠️ Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, LightGBM
- Streamlit
- MLflow (experiment tracking)


👨‍💻 Author
Krushang Patel
