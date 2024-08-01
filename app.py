from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    date = request.form['date']
    
    # Call your Python script here
    # For example, let's create some dummy data
    df = pd.DataFrame({
        'Date': pd.date_range(start=date, periods=5, freq='D'),
        'Value': [10, 20, 15, 25, 30]
    })
    
    # Generate the graph
    img = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Value'])
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Graph')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('result.html', graph_url=graph_url, table=df.to_html(index=False))

if __name__ == '__main__':
    app.run(debug=True)
