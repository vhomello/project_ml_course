import json
import pickle
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import TunedThresholdClassifierCV, train_test_split
from sklearn.pipeline import Pipeline


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


def create_lightgbm_pipeline(params: dict) -> Pipeline:
    """Create LightGBM pipeline with preprocessing steps."""
    # Get parameters
    lightgbm_params = params.get("lightgbm", {})
    tuned_threshold_params = params["tuned_threshold"]
    random_state = params["random_state"]

    # Create LightGBM classifier with default parameters if not specified
    lgb_params = {
        "n_estimators": lightgbm_params.get("n_estimators", 100),
        "learning_rate": lightgbm_params.get("learning_rate", 0.1),
        "num_leaves": lightgbm_params.get("num_leaves", 31),
        "max_depth": lightgbm_params.get("max_depth", -1),
        "min_child_samples": lightgbm_params.get("min_child_samples", 20),
        "subsample": lightgbm_params.get("subsample", 1.0),
        "class_weight": "balanced",
        "random_state": random_state,
        "verbose": -1,
    }

    lightgbm_clf = lgb.LGBMClassifier(**lgb_params)

    # Create pipeline steps
    pipeline_steps = []

    # Add LightGBM classifier
    pipeline_steps.append(("lightgbm", lightgbm_clf))

    # Create pipeline
    pipeline = Pipeline(pipeline_steps)

    # Wrap with threshold tuning
    model = TunedThresholdClassifierCV(
        estimator=pipeline,
        thresholds=np.arange(0, 1.0, 0.01),
        cv=tuned_threshold_params["cv"],
        scoring=tuned_threshold_params["metric"],
        random_state=random_state,
    )

    return model


def main():
    """Main training function."""
    # Load parameters
    params = load_params("src/project_ml_course/lgbm_params.json")

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
    model = create_lightgbm_pipeline(params)

    # Fit the model
    print("Training LightGBM model...")
    model.fit(X_train, y_train)
    print("Training completed!")

    # Evaluate on test set
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"LightGBM F1 score on test set: {f1:.4f}")

    # Create models directory if it doesn't exist
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    # Save the trained model
    model_path = models_dir / "lightgbm_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
