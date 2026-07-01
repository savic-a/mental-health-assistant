from nlp.normalization import normalize
from nlp.translation import english_text
from nlp.emotion_detector import detect_emotion

def start_chat():
    print("\nHow are you today?")
    text = input('>> ')

    # 1. normalize text
    text = normalize(text)

    # 2. translate input on english
    text = english_text(text)
    print("PREVOD: ", text)

    # 3. emotion detection (Hugging Face)
    emotion = detect_emotion(text)
    print("Emotion:", emotion)
