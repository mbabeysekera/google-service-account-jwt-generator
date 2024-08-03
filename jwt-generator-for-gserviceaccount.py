import json
import google.auth.crypt
import google.auth.jwt
import datetime
import pytz

# Load the service account JSON key file
with open("D:\Projetcs\Google APIs\Service Account for employee transfer.json") as f:
    service_account_info = json.load(f)

# Define the required scopes
scopes = ["https://www.googleapis.com/auth/forms.responses.readonly"]

# Create a signer using the private key
signer = google.auth.crypt.RSASigner.from_service_account_info(service_account_info)

colombo_tz = pytz.timezone("Asia/Colombo")

# Get the current time in the defined time zone
now = datetime.datetime.now(colombo_tz)
iat = int(now.timestamp())
exp = int(
    (now + datetime.timedelta(minutes=59)).timestamp()
)  # Token valid for 59 minutes

# Define the JWT claims
payload = {
    "iss": service_account_info["client_email"],
    "sub": service_account_info["client_email"],
    "aud": "https://oauth2.googleapis.com/token",
    "iat": iat,
    "exp": exp,
    "scope": " ".join(scopes),
}

# Encode the JWT
jwt = google.auth.jwt.encode(signer, payload)
print(jwt.decode("utf-8"))
