import librosa
import numpy as np

SAMPLES_TO_CONSIDER = 16000

class AudioProcessor:
    """Handles audio preprocessing for speech recognition."""

    @staticmethod
    def preprocess(file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        """
        Extract MFCC features from an audio file.

        :param file_path (str): Path to the audio file
        :param num_mfcc (int): Number of MFCC coefficients to extract
        :param n_fft (int): Interval for STFT (measured in # of samples)
        :param hop_length (int): Sliding window for STFT (measured in # of samples)
        :return mfccs (ndarray): MFCC features of shape (# time steps, # coefficients)
        """
        # Load audio file
        signal, sample_rate = librosa.load(file_path,sr=16000)

        # Ensure audio length is consistent
        if len(signal) >= SAMPLES_TO_CONSIDER:
            signal = signal[:SAMPLES_TO_CONSIDER]

            # Extract MFCC features
            mfccs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
            return mfccs.T

        raise ValueError(f"Audio file {file_path} is too short for processing.")
