```
from dash import Dash, dcc, html, Input, Output, State
import requests
import plotly.graph_objs as go

app = Dash(__name__)
API_KEY = "8a2e3969e41e4289a4c54921252506" 

app.layout = html.Div([
    html.H1("Weather Forecast Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dcc.Input(id='city-input', type='text', placeholder='Enter city,country', value='Noida,India'),
        html.Button('Get Forecast', id='submit-button', n_clicks=0),
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),

    html.Div(id='current-temp', style={'textAlign': 'center', 'fontSize': '20px', 'marginBottom': '10px'}),

    dcc.Graph(id='forecast-graph'),  # Temperature
    dcc.Graph(id='weather-metrics-graph'),  # Other metrics

    html.Div(id='error-message', style={'color': 'red', 'textAlign': 'center', 'marginTop': '10px'})
])

def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=yes&alerts=no"
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"API Error: {response.status_code}"
    return response.json(), None

@app.callback(
    Output('forecast-graph', 'figure'),
    Output('weather-metrics-graph', 'figure'),
    Output('current-temp', 'children'),
    Output('error-message', 'children'),
    Input('submit-button', 'n_clicks'),
    State('city-input', 'value')
)
def update_forecast(n_clicks, city):
    if n_clicks == 0:
        return go.Figure(), go.Figure(), "", ""

    data, error = fetch_weather(city)
    if error:
        return go.Figure(), go.Figure(), "", error

    try:
        current = data['current']
        location = data['location']
        forecast = data['forecast']['forecastday'][0]
        hourly_data = forecast['hour']

        times = [h['time'] for h in hourly_data]
        temps = [h['temp_c'] for h in hourly_data]
        feels = [h['feelslike_c'] for h in hourly_data]
        wind = [h['wind_kph'] for h in hourly_data]
        humidity = [h['humidity'] for h in hourly_data]
        precip = [h['precip_mm'] for h in hourly_data]
        pressure = [h['pressure_mb'] for h in hourly_data]
        aqi = [
            round(h.get('air_quality', {}).get('pm2_5', None), 1) if isinstance(h.get('air_quality', {}).get('pm2_5'), (int, float)) else None
            for h in hourly_data
        ]

        # 1️⃣ Temp Graph
        temp_fig = go.Figure()
        temp_fig.add_trace(go.Scatter(x=times, y=temps, mode='lines+markers', name='Temp (°C)'))
        temp_fig.add_trace(go.Scatter(x=times, y=feels, mode='lines+markers', name='Feels Like (°C)'))
        temp_fig.update_layout(title=f"Temperature Forecast for {city}", xaxis_title="Time", yaxis_title="°C",hovermode='x unified')

        # 2️⃣ Weather Metrics Graph
        metrics_fig = go.Figure()
        metrics_fig.add_trace(go.Scatter(x=times, y=wind, mode='lines+markers', name='Wind (kph)'))
        metrics_fig.add_trace(go.Scatter(x=times, y=humidity, mode='lines+markers', name='Humidity (%)'))
        metrics_fig.add_trace(go.Scatter(x=times, y=precip, mode='lines+markers', name='Precipitation (mm)'))
        metrics_fig.add_trace(go.Scatter(x=times, y=pressure, mode='lines+markers', name='Pressure (mb)'))
        if any(aqi):
            metrics_fig.add_trace(go.Scatter(x=times, y=aqi, mode='lines+markers', name='AQI (PM2.5)'))

        metrics_fig.update_layout(title=f"Other Weather Metrics for {city}", xaxis_title="Time",hovermode='x unified')

        # Current summary
        current_summary = (
            f"Current in {city}: {current['temp_c']}°C ({current['condition']['text']}), "
            f"Feels like: {current['feelslike_c']}°C"
        )

        return temp_fig, metrics_fig, current_summary, ""

    except Exception as e:
        return go.Figure(), go.Figure(), "", f"Error processing data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
```
