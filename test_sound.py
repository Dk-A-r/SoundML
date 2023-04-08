import pytest

from main import model_loading


class TestSoundRecognition:
    @pytest.fixture
    def setup_model(self):
        return model_loading()

    def test_english_recognition(self, setup_model):
        language_id = setup_model
        signal = language_id.load_audio("test2.wav")
        prediction = language_id.classify_batch(signal)
        assert prediction[3][0] == 'en: English'


    def test_russian_recognition(self, setup_model):
        language_id = setup_model
        signal = language_id.load_audio("shortstories_childrenadults_0008.wav")
        prediction = language_id.classify_batch(signal)
        assert prediction[3][0] == 'ru: Russian'
