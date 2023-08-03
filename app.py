from flask import Flask, render_template
import whisper

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html')

#if __name__ == "__main__":
#  app.run(host='0.0.0.0', debug=True)

print('Test')
model = whisper.load_model("base")
print('Test2')
result = model.transcribe("harvard.wav", verbose=True)
print('Test3')
#print(result['text'])