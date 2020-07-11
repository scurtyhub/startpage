from flask import Flask, render_template, url_for
from publicip import get_ip_info
from weather import get_current_weather

app = Flask(__name__)

@app.route('/')
def index():
    public_ip, region, isp = get_ip_info()
    weather_info = get_current_weather()
    return render_template('index.html', ip=public_ip, region=region, isp=isp, location=weather_info['location'], description=weather_info['description'], temperature=weather_info['temperature']['now'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
