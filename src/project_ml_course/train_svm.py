import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import f1_score
from sklearn.model_selection import TunedThresholdClassifierCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def load_params(params_path: str) -> dict:
    """Load parameters from JSON file."""
    with open(params_path, "r") as f:
        params = json.load(f)
    return params


def load_and_preprocess_data(params: dict) -> tuple:
    """Load data and apply preprocessing according to parameters."""
    # Load raw data
    raw_df = pd.read_csv(params["training_input"], index_col="Unnamed: 0")

    # Separate features and target
    X = raw_df[params["features"]]
    y = raw_df["class"]

    return X, y


def create_svm_pipeline(params: dict) -> Pipeline:
    """Create SVM pipeline with preprocessing steps."""
    # Get parameters
    svm_params = params["svm"]
    tuned_threshold_params = params["tuned_threshold"]
    random_state = params["random_state"]

    # Create SVM classifier
    svm = SVC(
        C=svm_params["C"],
        kernel=svm_params["kernel"],
        probability=svm_params["probability"],
        class_weight="balanced",
        random_state=random_state,
    )

    # Create pipeline
    pipeline = Pipeline(
        [
            ("svm", svm),
        ]
    )

    model = TunedThresholdClassifierCV(
        estimator=pipeline,
        thresholds=np.arange(0, 1.0, 0.01),
        cv=tuned_threshold_params["cv"],
        scoring=tuned_threshold_params["metric"],
        random_state=params["random_state"],
    )

    return model


def main():
    """Main training function."""
    # Load parameters
    params = load_params("src/project_ml_course/svm_params.json")

    # Load and preprocess data
    X, y = load_and_preprocess_data(params)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=params["test_size"],
        random_state=params["random_state"],
        stratify=y,
    )

    # Create pipeline
    model = create_svm_pipeline(params)

    # Fit the model
    print("Training SVM model...")
    model.fit(X_train, y_train)
    print("Training completed!")
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"SVM F1 score on test set: {f1:.4f}")

    # Create models directory if it doesn't exist
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    # Save the trained model
    model_path = models_dir / "svm_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
