import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.youtube_analytics
collection = db.videos

# Convert to DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("YouTube Channel Analytics"),
    dcc.Graph(
        figure=px.bar(df, x="title", y="published_at", title="Videos by Publish Date")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
