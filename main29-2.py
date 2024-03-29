from ppadb.client import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037) 
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()

send_message = "안녕하세요 반갑습니다."
device.shell(f'am start -a android.intent.action.SENDTO -d sms:"01033112545" --es sms_body "{send_message}"')
time.sleep(1.0)
xyPosition = "1328 1823"
device.shell(f'input tap {xyPosition}')  # 전송버튼 클릭

time.sleep(3.0)