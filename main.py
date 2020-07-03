import ast
from flask import Flask, request, render_template, Response
import jsonpickle
from voice_processing import speech_recognition_api 
from weather_crawler import crawl_weather
from gtts import gTTS
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/recognize', methods=['GET', 'POST'])
def recognize():
    print(request.get_json())
    AUDIO_FILE = request.get_json()['filePath']
    response = {
        'text': ''
    }
    
    text = speech_recognition_api.speech_to_text(AUDIO_FILE)
    if text == None:
        text = "Mời bạn nói lại"
        os.remove(AUDIO_FILE)
    else:
        text = text.lower()

    response['text'] = text
    os.remove(AUDIO_FILE)

    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/weather', methods=['GET'])
def weather():
    weather_data = crawl_weather.get_weather()
    print(weather_data)
    tts = gTTS(weather_data['title'] + weather_data['loc'] + weather_data['temp'] + weather_data['detail'], lang='vi')
    tts.save('/home/iamvon/Documents/desktop/Năm_3/Kì_2/Voice_Processing/smart_room_voice_control/src/weather/weather.mp3')
    response_pickled = jsonpickle.encode(weather_data)
    return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)