import io
import streamlit as st
import torchaudio
from speechbrain.pretrained import EncoderClassifier


APP_NAME = 'Определение языка аудиофайла'
APP_ICON = 'logo.png'
APP_DESCRIPTION = '<i>Используемая модель: <a href="https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa/tree/main" target="_blank">Spoken Language Identification Model</a></i>'
APP_REP = '<i> <a href="https://github.com/Dk-A-r/SoundML" target="_blank">Репозиторий проекта</a></i>'


def load_audio():
    """Создание формы для загрузки аудио"""

    #Форма для загрузки средствами Streamlit

    uploaded_file = st.file_uploader(
        label='Загрузите аудиофайл для распознавания')

    if uploaded_file is not None:
        #Получение загруженного аудио
        audio_data = uploaded_file.getvalue()
        #st.write(audio_data)
        #Вывод аудиоплеера
        st.audio(audio_data)
        with open("temp.wav","wb") as f:
            f.write(uploaded_file.getbuffer())

@st.cache(allow_output_mutation=True)
def model_loading():
    return EncoderClassifier.from_hparams(source="speechbrain/lang-id-voxlingua107-ecapa", savedir="tmp")    


def identify(language_id):
    signal = language_id.load_audio("temp.wav")
    prediction =  language_id.classify_batch(signal)
    st.write(prediction[3][0] + ' with probability' + f" {prediction[1].exp().item()}")

def main():
    st.set_page_config(page_title=APP_NAME, page_icon=APP_ICON)
    st.title(APP_ICON + ' ' + APP_NAME)
    st.markdown(APP_DESCRIPTION, True)

    st.info('''Команда:  
        - Карпов Данил  
        - Репенко Диана''')

    load_audio()
    # Если кнопка нажата, то запускаем распознавание
    result = st.button('Распознать аудиофайл')

    if result:
        language_id = model_loading()
        identify(language_id)


if __name__ == "__main__":
    main()

    
