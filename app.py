from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/food-trucks', methods=['GET'])
def get_food_trucks():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    # URL da API do DataSF
    url = 'https://data.sfgov.org/resource/rqzj-sfat.json'
    
    # Parâmetros para filtrar os food trucks pela localização
    params = {
        '$where': f'within_circle(location, {latitude}, {longitude}, 1000)'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
