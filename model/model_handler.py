import tensorflow as tf
import numpy as np

SAVED_MODEL_PATH = "model/model70.h5"

class ModelHandler:
    """Handles the loading and inference of the speech recognition model."""

    def __init__(self):
        # Load the pre-trained model
        self.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
        self._mapping = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]

    def predict(self, mfccs):
        """
        Make a prediction based on input MFCC features.

        :param mfccs (ndarray): Preprocessed MFCC features
        :return predicted_keyword (str): Keyword predicted by the model
        """
        # Reshape MFCCs to 4D array: (# samples, # time steps, # coefficients, 1)
        mfccs = mfccs[np.newaxis, ..., np.newaxis]

        # Get predictions
        predictions = self.model.predict(mfccs)
        predicted_index = np.argmax(predictions)
        return self._mapping[predicted_index]
