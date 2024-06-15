import pymongo
from flask import Flask, request

app = Flask(__name__)

password = "Angkasa1"
uri: LiteralString = f"mongodb+srv://Ninclaunya:<password>@sicpractice.1dr8jgg.mongodb.net/?retryWrites=true&w=majority&appName=SICPractice"

client = pymongo.MongoClient(uri)
db: Database[Any] = client.challange1
myCollection: Collection[Any] = db.sensor

@app.route("/", methods= ["GET"])
def hello_world():
    print("Hello World")
    
@app.route("/sensor1", methods= ["POST"])
def sensor1():
    temperature: str | None = request.argst.get("temperature")
    humidity: str | None = request.args.get("kelembapan")
    
    if temperature is not None:
        temperature = float(temperature)
    if humidity is not None:
        humidity = float(humidity)
        
    sensor: dict[float | None, float | ...]

if __name__ == "__main__":
    app.run(debug=True)