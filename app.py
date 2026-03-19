from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return jsonify({
	"message":"My only try, working mostly with apis"
})


@app.route('/get')
def get():
  return jsonify({
	"get1":"Try 1",
	"get2":"Try 2"
})


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
