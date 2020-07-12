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

### Set up via Docker
If you haven't already set up Docker. You can set it up [here](https://docs.docker.com/get-docker/)
```sh
docker build -t startpage:latest .
docker run -d -p 5000:5000 startpage:latest
```
Verify the deployment by navigating to your server address in your preferred browser.
```sh
http://<ip address>:9999
```
Now you can set your default home page to your new start page.