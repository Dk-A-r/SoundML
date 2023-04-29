import pytest
from main import model_loading


@pytest.fixture
def language_id():
    return model_loading()


def test_predict_russian(language_id):
    signal = language_id.load_audio("shortstories_childrenadults_0008.wav")
    prediction = language_id.classify_batch(signal)
    assert prediction[3][0] == 'ru: Russian'


def test_predict_english(language_id):
    signal = language_id.load_audio("test2.wav")
    prediction = language_id.classify_batch(signal)
    assert prediction[3][0] == 'en: English'
