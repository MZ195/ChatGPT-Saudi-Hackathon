import http.client
import json

HEADERS = {
        'Content-Type': 'application/json',
        'customer-id': '1905674446',
        'x-api-key': 'zqt_cZZIzncr3qQYrfNyK-xnsqkQL0quDshqCb9gzA'
        }

class Controller:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("experimental.willow.vectara.io")

    def generate_dummy(self, col):
        result = {}
        try:
            payload = json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                "role": "user",
                "content": f"generate fake {col.col_name} in arabic"
                }
            ]
            })
            self.conn.request("POST", "/v1/chat/completions", payload, HEADERS)
            res = self.conn.getresponse()
            data = res.read()
            result = data.decode("utf-8")
            json_object = json.loads(result)
            res = json_object['choices'][0]['message']['content']

            data = [el.strip()[2:].strip() for el in res.split('\n')[2:]]

            return data, None

        except Exception as e:
            print("error", e)
            return res, e