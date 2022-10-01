

import google.cloud.logging
import os


def authenticate():
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C://Users/abhiv/Downloads/gcp-logging-361702-eab65727f25c.json'

    client = google.cloud.logging.Client()

    # Alternatively, but not recommended. It's helpful when you can't set an environment variable.
    service_key_path = "C://Users/abhiv/Downloads/gcp-logging-361702-eab65727f25c.json"
    client = google.cloud.logging.Client.from_service_account_json(
        service_key_path)

    client.setup_logging()
    # logging.warning("This is a warning!")
    return 'Login success'
