import requests, json

data = [{"Nome": "Álvaro da Silva"}, {"Nome": "Fátima Santos"}, {"Nome": "Pedro Nogueira"}]

SPLUNK_SERVER = ""
SPLUNK_TOKEN = ""
SPLUNK_HEC_PORT = ""
SPLUNK_HEC_PROTOCOL = ""
SPLUNK_ENDPOINT = "{}://{}:{}/services/collector".format(SPLUNK_HEC_PROTOCOL, SPLUNK_SERVER, SPLUNK_HEC_PORT)


def send_hec(data):
    data_payload = []
    for event in data:
        event_data = {'event': event,
                'source': 'logLib',
                'sourcetype': 'jsonpt',
                'index': 'main'}

        data_payload.append(event_data)

    try:
        headers = {"Content-Type": "application/json; charset=ISO-8859-1"}
        data_send = requests.post(SPLUNK_ENDPOINT, data=json.dumps(data_payload),
                                  auth=('Splunk', SPLUNK_TOKEN), headers=headers)
        response = data_send.json()
    except requests.Timeout:
        print("TIMEOUT ERROR")

    if response['code'] == 0:
        print(data_send.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_hec(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
