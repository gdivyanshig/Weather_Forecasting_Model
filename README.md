# 🌦️ Weather Forecast Dashboard

This is an interactive **Weather Forecast Dashboard** built using [Dash](https://dash.plotly.com/), [Plotly](https://plotly.com/), and [WeatherAPI](https://www.weatherapi.com/). Users can input a city name to fetch the **current weather**, **hourly temperature**, and **various metrics** such as humidity, wind speed, precipitation, pressure, and AQI (PM2.5).

---

## 💡 Features

- 🔍 Search weather by city and country (e.g., `London,UK` or `Noida,India`)
- 🌡️ Live temperature graph: actual vs feels-like
- 🌬️ Weather metrics graph: wind, humidity, precipitation, pressure, AQI (if available)
- 📍 Current weather summary: condition, temperature, and feels-like
- ⚠️ Error messages for invalid city names or API issues
- 🎨 Responsive layout with Plotly graphs and Dash UI

---

## 🧰 Technologies Used

- **Dash** for the web dashboard
- **Plotly** for graph visualizations
- **WeatherAPI** for fetching forecast data
- **Python 3.7+**

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure Python 3.7+ is installed. Install required packages:

```bash
pip install dash plotly requests
```

---

### ▶️ Run the App

1. Replace your own API key inside the script (from [WeatherAPI](https://www.weatherapi.com/)).
2. Run the app:

```bash
python Code.py
```

3. Open your browser and visit:  
   `http://127.0.0.1:8050/`

---

## 🧠 How It Works

- The app uses the `/forecast.json` endpoint of WeatherAPI to fetch hourly data for the next 24 hours.
- It displays:
  - A **temperature graph** comparing actual vs feels-like temperature.
  - A **weather metrics graph** showing wind speed, humidity, precipitation, pressure, and PM2.5 AQI (if available).
- The **current temperature and condition** are displayed above the graphs.

---

## 🌍 Example Cities

Try entering any of these formats in the input box:

- `New York,USA`
- `Mumbai,India`
- `Tokyo,Japan`
- `Paris,France`
- `Sydney,Australia`

---

## 📜 License

This project is open-sourced under the **MIT License**.  
You are free to use, share, and modify it.

---

> Feel free to ⭐ this repo if you find it helpful, and contributions are welcome!
