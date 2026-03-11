import requests
import logging

# Configure logging
logging.basicConfig(
    filename='app_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Change this URL to your app URL
URL = "http://wisecow.devopshackarena.xyz"

def check_app_health():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            msg = f"Application is UP. Status code: {response.status_code}"
            print(msg)
            logging.info(msg)
        else:
            msg = f"Application is DOWN. Status code: {response.status_code}"
            print(msg)
            logging.warning(msg)
    except requests.exceptions.RequestException:
        msg = "Application is DOWN. Could not reach the server."
        print(msg)
        logging.error(msg)

if __name__ == "__main__":
    check_app_health()