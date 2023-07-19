import plotly.graph_objects as go

def plotData(data, label):
    figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"],
                                        high=data["High"],
                                        low=data["Low"],
                                        close=data["Close"])])
    figure.update_layout(title = label,
                     xaxis_rangeslider_visible=False)
    correlation = data.corr()
    figure.show()
    print(correlation["Close"].sort_values(ascending=False))

