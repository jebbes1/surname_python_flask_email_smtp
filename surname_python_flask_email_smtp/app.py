from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configure your email credentials
EMAIL_ADDRESS = "healthhub973@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "uokopjfczuygiqwq"    # Replace with your email password
SMTP_SERVER = "smtp.gmail.com"          # Replace with your email provider's SMTP server
SMTP_PORT = 587                           # Common port for SMTP

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        recipient_email = data.get('email')
        message_content = data.get('message')

        if not recipient_email or not message_content:
            return jsonify({"error": "Both 'email' and 'message' fields are required"}), 400

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = "Message from Flask App"

        # Add the email body
        msg.attach(MIMEText(message_content, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
