from flask import Flask, render_template, request

app = Flask(__name__)

# Default Get
@app.route('/')
@app.route('/<room>')
def home(room):   
    return render_template('index.html')

# POST
@app.route('/api/chat/<room>', methods=['POST'])
def send(room):
    username = request.form['username']
    message = request.form['msg']
    # Print the values to the console for debugging
    print('Username:', username)
    print('Message:', message)
    # You can save the data as needed; here, we'll just render it in a response.
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
