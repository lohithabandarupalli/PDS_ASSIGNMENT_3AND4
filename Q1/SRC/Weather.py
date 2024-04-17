import dash
from dash import html, dcc, Input, Output
import requests
import json

# Initialize the Dash app
app = dash.Dash(__name__)

# Defining the layout of the dashboard
app.layout = html.Div([
    html.H1("Weather Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.H3("Enter City Name:"),
        dcc.Input(id='city-input', type='text', placeholder='Enter city name', debounce=True),
        html.Button('Submit', id='submit-button', n_clicks=0)
    ]),
    html.Div(id='output-container', style={'margin-top': '20px'})
])

# Defining a callback function to update the output based on user input
@app.callback(
    Output('output-container', 'children'),
    [Input('submit-button', 'n_clicks')],
    [Input('city-input', 'value')]
)
def update_output(n_clicks, city):
    if n_clicks > 0 and city:
        try:
            # Calling the Open Weather Map API to get weather data for the specified city
            api_key = '4fb1f2e4c90bb864df401d39859da7c6'  
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            data = response.json()

            # Saving the JSON data in a separate file 
            with open(f'{city}_data_json.json', 'w') as file:
                json.dump(data, file)

            # Extracting relevant weather information
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            visibility = data.get('visibility', 'N/A')

            # Displaying the weather information in a table with borders between columns and around headings
            return html.Table([
                html.Thead(
                    html.Tr([
                        html.Th("City", style={'border': '1px solid black'}),
                        html.Th("Description", style={'border': '1px solid black'}),
                        html.Th("Temperature (°C)", style={'border': '1px solid black'}),
                        html.Th("Humidity (%)", style={'border': '1px solid black'}),
                        html.Th("Wind Speed (m/s)", style={'border': '1px solid black'}),
                        html.Th("Visibility (m)", style={'border': '1px solid black'})
                    ])
                ),
                html.Tbody([
                    html.Tr([
                        html.Td(city, style={'border': '1px solid black'}),
                        html.Td(weather_description, style={'border': '1px solid black'}),
                        html.Td(temperature, style={'border': '1px solid black'}),
                        html.Td(humidity, style={'border': '1px solid black'}),
                        html.Td(wind_speed, style={'border': '1px solid black'}),
                        html.Td(visibility, style={'border': '1px solid black'})
                    ])
                ])
            ], style={'border-collapse': 'collapse'})
        except Exception as e:
            return html.Div(f"Error: {str(e)}")
    else:
        return html.Div("Enter a city name and click Submit to get weather information.")


if __name__ == '__main__':
    app.run_server(debug=True)
