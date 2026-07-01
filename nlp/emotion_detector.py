from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def detect_emotion(text: str) -> list[dict[str, any]]:
    return emotion_model(text)[0]
