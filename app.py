import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :

@app.route("/contact")
def MaPremiereAPI():
    return render_template("contact.html") 

@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.get("/paris-daily")
def api_paris_daily():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Paris"
    response = requests.get(url)
    data = response.json()

    dates = data.get("daily", {}).get("time", [])
    t_max = data.get("daily", {}).get("temperature_2m_max", [])
    t_min = data.get("daily", {}).get("temperature_2m_min", [])

    result = [
        {"date": dates[i], "temp_max": t_max[i], "temp_min": t_min[i]}
        for i in range(len(dates))
    ]
    return jsonify(result)

@app.route("/histogramme")
def histogramme():
    return render_template("histogramme.html")

@app.get("/montigny-meteo")
def api_montigny():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.7847&longitude=2.0335&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"
    response = requests.get(url)
    data = response.json()

    dates = data.get("daily", {}).get("time", [])
    t_max = data.get("daily", {}).get("temperature_2m_max", [])
    t_min = data.get("daily", {}).get("temperature_2m_min", [])
    precip = data.get("daily", {}).get("precipitation_sum", [])

    result = [
        {
            "date": dates[i],
            "temp_max": t_max[i],
            "temp_min": t_min[i],
            "precipitation": precip[i]
        }
        for i in range(len(dates))
    ]
    return jsonify(result)

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")

# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
