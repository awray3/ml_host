"""
Simulates a production model that takes an api request and returns a prediction.
"""
import numpy as np
from typing import Dict
from app.data_model import ModelInput


def main(input_data: ModelInput) -> Dict[str, float]:
    """All of the good stuff happens here with your input data."""

    # silly mock example. Change this code to be whatever your use case model code is.
    mean_of_input = np.mean(input_data.x)
    return {"model_prediction": mean_of_input}
