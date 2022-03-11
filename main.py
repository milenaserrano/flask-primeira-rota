from flask import Flask
app = Flask('app')

@app.route('/')
def rota():
  return '<h1>Minha primeira rota!</h1>'

app.run(host='0.0.0.0', port=8080)