import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_text = json.loads(response.text)

    emotion_score_dictionary = formatted_text['emotionPredictions'][0]['emotion']
    anger_score = emotion_score_dictionary['anger']

    disgust_score = formatted_text['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_text['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_text['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_text['emotionPredictions'][0]['emotion']['sadness']

    max = 0
    dominant_emotion = None
    for emotion in emotion_score_dictionary:
        if max < emotion_score_dictionary[emotion]:
            dominant_emotion = emotion
            max = emotion_score_dictionary[emotion]
    print(dominant_emotion)
    print(emotion_score_dictionary)   

    
    
    

    