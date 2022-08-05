import requests, json

data = [{"Nome": "Álvaro da Silva"}, {"Nome": "Fátima Santos"}, {"Nome": "Pedro Nogueira"}]

SPLUNK_SERVER = "YOUR SPLUNK SERVER"
SPLUNK_TOKEN = "YOUR TOKEN"
SPLUNK_ENDPOINT = "http://{}:8088/services/collector".format(SPLUNK_SERVER)


def send_hec(data):
    data_payload = []
    for event in data:
        event_data = {'event': event,
                'source': 'logLib',
                'sourcetype': 'json',
                'index': 'main'}

        data_payload.append(event_data)

    try:
        data_send = requests.post(SPLUNK_ENDPOINT, data=json.dumps(data_payload),
                                  auth=('Splunk', SPLUNK_TOKEN))
        response = data_send.json()
    except requests.Timeout:
        print("TIMEOUT ERROR")

    if response['code'] == 0:
        print(data_send.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_hec(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
