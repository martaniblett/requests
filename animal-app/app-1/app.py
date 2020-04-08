from application import app

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')


'''
@app.route('/get/text', methods=['GET']) 
def get_text():
    return Response('Hello from Flask', mimetype='text/plain')

@app.route('/post/text', methods=['POST'])
def post_text():
    return Response("Data you sent: " + request.data.decode("utf-8"), mimetype='text/plain')

'''



