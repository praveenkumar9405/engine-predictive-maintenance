# ⚙️ Industrial Engine Predictive Maintenance Dashboard

An enterprise-grade MLOps infrastructure project that utilizes machine learning to evaluate the **Remaining Useful Life (RUL)** of industrial turbofan engines. By processing real-time multi-channel sensor telemetry streams (including core temperature, fan speeds, and pressure metrics), this system flags operational degradation patterns to enable proactive asset management and prevent catastrophic mechanical failures.

---

## 🗺️ Project Framework & Architecture

This repository follows the core phases of the **MLOps Lifecycle (Machine Learning Engineering Framework)**:

1. **Data Engineering & Feature Ingestion**: Loaded space-separated text data simulating the industry-benchmark **NASA CMAPSS Turbofan Dataset**. Automatically calculated engine failure horizons by grouping unique `Engine_ID` entries and backwards-engineering the `RUL` target labels.
2. **Model Engineering**: Evaluated sensor collinearity and selected a robust **Random Forest Regressor** to perfectly handle the exponential, non-linear wear profiles of degrading assets without requiring excessive preprocessing scaling pipelines.
3. **Model Serving & Deployment**: Serialized the pipeline weights into a production artifact (`engine_model.pkl`) and wrapped the inference layer in an interactive **Streamlit** user interface for cloud deployment.

---

## 🛠️ Tech Stack & Requirements

* **Core Language**: Python (3.9 - 3.11)
* **Machine Learning**: Scikit-Learn (1.5.0)
* **Data Processing**: Pandas, NumPy
* **Model Serialization**: Joblib
* **Application Layer**: Streamlit (1.35.0)

---

## 🚀 How to Run Locally

### 1. Clone the Repository & Setup Environment
```bash
git clone https://github.com
cd engine-predictive-maintenance
python -m venv pdm_env
```
* Activate environment:
  * **Windows**: `pdm_env\Scripts\activate`
  * **Mac/Linux**: `source pdm_env/bin/activate`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate the Production Model Artifact
```bash
python train_model.py
```

### 4. Launch the Interactive Interface
```bash
streamlit run app.py
```

---

## 📊 Model Performance Evaluation

* **Root Mean Squared Error (RMSE)**: Evaluated within an incredibly tight window of cycles, ensuring highly precise warning flags prior to structural component failure points.
* **R² Variance Score**: Demonstrated strong performance in mapping the complex, correlation-heavy data paths across all 10 target engine sensors.
