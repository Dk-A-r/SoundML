# SoundML

### В рамках настоящего проекта имплементирована модель speechbrain для
обработки аудиофайлов в рамках вебприложения. Функционал приложения: определение языка аудиофайла (в формате WAV), который загружается на сайт посредством встроенной формы. Для своего размера (~85 MB) модель сравнительно точна.

### Проект реализован с помощью Streamlit и развёрнут на Яндекс Облаке.

## <a href="https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa/tree/main" target="_blank">Ссылка на модель - Spoken Language Identification Model </a> 

## Состав команды:
- Карпов Данил
- Репенко Диана


### Для корректной работы требуется установка sound backend:
soundfile - аудио backend (для Windows);
sox - аудио backend (для Linux)


### Для тестирования приложения использовались файлы из следующих датасетов:
 - Russian Single Speaker Speech Dataset (https://www.kaggle.com/datasets/bryanpark/russian-single-speaker-speech-dataset?resource=download)
 - Speech Emotion Recognition (en) (https://www.kaggle.com/datasets/dmitrybabko/speech-emotion-recognition-en?resource=download)



