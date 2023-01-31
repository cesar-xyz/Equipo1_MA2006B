from requests.auth import HTTPBasicAuth

USER = ""
PASSWORD = ""


def send_info():
    basic = HTTPBasicAuth(USER, PASSWORD)
    r, json = requests.post("https://httpbin.org/basic-auth/user/pass", auth=basic)
    return r, json
