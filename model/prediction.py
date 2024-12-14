from model.model_handler import ModelHandler
from utils.audio_processor import AudioProcessor

class KeywordSpottingService:
    """Singleton class for keyword spotting."""

    _instance = None

    def __init__(self):
        self.model_handler = ModelHandler()
        self.audio_processor = AudioProcessor()

    def predict(self, file_path):
        """
        Predict the keyword from an audio file.

        :param file_path (str): Path to the audio file
        :return predicted_keyword (str): Predicted keyword
        """
        # Preprocess audio file
        mfccs = self.audio_processor.preprocess(file_path)

        # Use the model to predict
        return self.model_handler.predict(mfccs)


def Keyword_Spotting_Service():
    """Factory function for KeywordSpottingService."""

    if KeywordSpottingService._instance is None:
        KeywordSpottingService._instance = KeywordSpottingService()
    return KeywordSpottingService._instance


if __name__ == "__main__":
    # Test the service
    kss = Keyword_Spotting_Service()
    #prediction = kss.predict("/path/to/audio/file.wav")
    #print(f"Predicted Keyword: {prediction}")
