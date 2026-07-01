import langid
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
from config.constants import LANG_MAP


def english_text(text: str) -> str:
    language = detect_language(text)

    if language not in LANG_MAP:
        raise ValueError(f"Unsupported language: {language}")
    else:
        text = translate_to_english(language, text)
        
    return text


def detect_language(text: str) -> str:
    language, confidence = langid.classify(text)
    print(language, confidence)
    return language


tokenizer = AutoTokenizer.from_pretrained(
    "facebook/nllb-200-distilled-600M"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "facebook/nllb-200-distilled-600M"
)

def translate_to_english(language: str, text: str, ) -> str:
    tokenizer.src_lang = LANG_MAP[language]

    inputs = tokenizer(text, return_tensors="pt")

    generated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("eng_Latn")
    )

    return tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]


