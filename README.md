# Startpage
This is a startpage that has the shortcut links to selfhosted services, frequently used sites etc.

![alt text](static/images/sample.png)

### Download files
```sh
git clone git@github.com:scurtyhub/startpage.git
cd startpage/
```

### Set up confi.ini
This code uses [OpenWeather](https://openweathermap.org/) to get Weather information. You can get the API key from [here](https://openweathermap.org/api)

```sh
vi config.ini
```
Add your preferred values to the config file. Below is a sample file
```sh
[DEFAULT]
weather_location = Scranton
weather_api_key = <Place_your_OpenWeather_API_key_here>
weather_units = metric
default_value = -1
```

### Update index.html
Modify the links under selfhosted to point to your services. You can add any additional websites here.

### Set up
#### Docker:

If you haven't already set up Docker. You can set it up [here](https://docs.docker.com/get-docker/)
```sh
docker build -t startpage:latest .
docker run -d -p 5000:5000 startpage:latest
```
#### Virtual Environment
```sh
python3 -m venv .
source bin/activate
pip install -r requirements.txt
python app.py
```

Verify the deployment by navigating to your server address in your preferred browser.
```sh
http://localhost:5000
```
Now you can set your default home page to your new start page.