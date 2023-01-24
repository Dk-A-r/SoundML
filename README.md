# SoundML

В рамках настоящего проекта имплементирована модель speechbrain для
обработки аудиофайлов в рамках вебприложения. Функционал приложения: определение языка аудиофайла (в формате WAV), который загружается на сайт посредством встроенной формы. Для своего размера (~85 MB) модель сравнительно точна.

Для корректной работы требуется установка sound backend:

soundfile - аудио backend (для Windows);
sox - аудио backend (для Linux)

Ссылка на модель: https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa/tree/main

Для тестирования приложения использовались файлы из следующих датасетов:
 - Russian Single Speaker Speech Dataset (https://www.kaggle.com/datasets/bryanpark/russian-single-speaker-speech-dataset?resource=download)
 - Speech Emotion Recognition (en) (https://www.kaggle.com/datasets/dmitrybabko/speech-emotion-recognition-en?resource=download)



