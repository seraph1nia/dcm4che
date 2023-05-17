from keycloak import KeycloakOpenID
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Keycloak server information
keycloak_url = "https://testing.local:8843/"
realm_name = "dcm4che"
client_id = "dcm4chee-arc-rs"
client_secret = "changeit"
username = "admin"
password = "changeit"

# Create a Keycloak client
keycloak = KeycloakOpenID(server_url=keycloak_url, realm_name=realm_name, client_id=client_id, client_secret_key=client_secret, verify=False)

# Get a token using username and password
token = keycloak.token(username=username, password=password, grant_type="password")

# Retrieve the access token
access_token = token["access_token"]

# Print the access token
print(access_token)


def api_test(access_token, path, base_url="https://testing.local:8443/dcm4chee-arc", **kwargs):
    session = requests.Session()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    url = base_url + path
    print(url)
    result = session.request(url=url, verify=False, headers=headers, **kwargs)
    print(result.status_code)
    #print(result.text)


api_test(access_token=access_token, path="/devices", method="GET")

api_test(access_token=access_token, path="/ui2", method="GET")


# https://testing.local:8843/realms/dcm4che/account
# user shit: https://github.com/dcm4che/dcm4chee-arc-light/wiki/Secure-Archive-UI-and-RESTful-Services-using-Keycloak#ldap-configuration-and-keycloak-user-federation

# admin had niet de goede role: https://groups.google.com/g/dcm4che/c/OV6sFEtjo-g

# add healthcheck containers