from PIL import Image
from landingai.predict import Predictor 

# Enter your API Key
endpoint_id = "6fd6b818-b123-448d-ad0d-2043a99b1b0e"
api_key = "land_sk_43alES4BwK5YtK5IYZrYwqrHpB1bD07XyLjVTKLhBWEUz7L1Lg"

image_files = ["images/image1.jpg","images/image2.jpg","images/image3.jpg","images/image4.jpg","images/image5.jpg","images/image6.jpg","images/image7.jpg","images/image8.jpg","images/image9.jpg","images/image10.jpg","images/image11.jpg"]

predictor = Predictor(endpoint_id, api_key=api_key)

for i in image_files:
    image = Image.open(i)
    predictions = predictor.predict(image)
    print(predictions)