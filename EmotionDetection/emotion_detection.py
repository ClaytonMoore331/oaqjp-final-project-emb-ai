"""Extract emotion scores and handle invalid responses from embedded Watson NLP."""
import json
import requests

SERVICE_URL = (
    'https://sn-watson-emotion.labs.skills.network/v1/'
    'watson.runtime.nlp.v1/NlpService/EmotionPredict'
)
MODEL_HEADERS = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
}
EMOTIONS = ('anger', 'disgust', 'fear', 'joy', 'sadness')


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion, or None for invalid text."""
    invalid = dict.fromkeys((*EMOTIONS, 'dominant_emotion'))
    if not isinstance(text_to_analyze, str):
        return invalid
    try:
        response = requests.post(
            SERVICE_URL, headers=MODEL_HEADERS,
            json={'raw_document': {'text': text_to_analyze}}, timeout=30
        )
        if response.status_code == 400:
            return invalid
        if response.status_code != 200:
            return invalid
        emotion = json.loads(response.text)['emotionPredictions'][0]['emotion']
        scores = {name: emotion[name] for name in EMOTIONS}
        return {**scores, 'dominant_emotion': max(scores, key=scores.get)}
    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return invalid
