import configuration
import data
import requests

def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             header=data.headers)

def post_new_client_kit(kit_body, auth_token):
    current_header = data.headers.copy()
    current_header["Authorization"] = "bearer" + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         jason=kit_body,
                         headers=current_header)

