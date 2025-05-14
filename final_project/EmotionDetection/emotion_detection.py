import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_text = json.loads(response.text)

    if response.status_code == 200:
        emotion_score_dictionary = formatted_text['emotionPredictions'][0]['emotion']
        anger_score = emotion_score_dictionary['anger']
        disgust_score = emotion_score_dictionary['disgust']
        fear_score = emotion_score_dictionary['fear']
        joy_score = emotion_score_dictionary['joy']
        sadness_score = emotion_score_dictionary['sadness']

        max = 0
        dominant_emotion = None
        for emotion in emotion_score_dictionary:
            if max < emotion_score_dictionary[emotion]:
                dominant_emotion = emotion
                max = emotion_score_dictionary[emotion]

        return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code == 400:
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    

    
    
    

    