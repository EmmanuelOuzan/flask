from flask import Flask, render_template, request
import json
app = Flask(__name__)

# Default Get 1,2
@app.route('/')
@app.route('/<room>')
def home(room):   
    return render_template('index.html')

# GET 
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    with open('chat_data.json','r') as chats_file:
        chat_data = json.load(chats_file)
    
    room_data = chat_data.get(room, []) # Empty list if no room
    
    # Format each chat message according to the given format
    formatted_messages = [f'[{entry["timestamp"]}] {entry["username"]}: {entry["message"]}' for entry in room_data]

    # Join all messages with a newline to make it readable
    response_content = "\n".join(formatted_messages)

    return response_content, 200, {"Content-Type": "text/plain"}

# POST
@app.route('/chat/<room>')
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
