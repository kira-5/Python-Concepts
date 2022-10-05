import logging

import google.cloud.logging
from google.logging.type import log_severity_pb2 as severity
from aunthentication.auth import authenticate


def googleLogger():
    authenticate()
    client = google.cloud.logging.Client()

    # textPayload
    logger = client.logger("python_application_name")
    logger.log_text(
        "This is a warning from 'python_application_name1'!", severity=severity.WARNING)

    # jsonPayload
    json_payload = {
        "message": "This is a warning from 'python_application_name2'!"}
    logger.log_struct(json_payload, severity=severity.WARNING)
