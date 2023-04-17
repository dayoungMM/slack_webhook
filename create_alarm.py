from datetime import datetime
import requests
import yaml


def send_webhook(url, channel, username, message):
    payload = {
        'channel': channel,
        'username': username,
        'text': message
    }
    res = requests.post(url, json=payload)
    print(res)


def create_message():
    now = datetime.now()
    # now = datetime.strptime("20230327", "%Y%m%d")
    # print("현재 :", now)

    date_to_compare = datetime.strptime("20230313", "%Y%m%d")
    # print("비교할 날짜 :", date_to_compare)

    date_diff = now - date_to_compare
    # print("일 수 차이 :", date_diff.days)

    seats = [88, 75, 81]
    members_idx = {'강준형': 0, '문다영': 1, '김보경': 2}
    msg = ':alarm_clock: 오늘 예약할 자리 :alarm_clock: \n'
    for name in members_idx.keys():
        seat_idx = (((date_diff.days) // 7) + members_idx[name]) % 3
        msg += f"{name}: {seats[seat_idx]} \n"
        # print(f"{name} 의 자리: {seats[seat_idx]}")
    return msg


if __name__ == '__main__':
    with open('config.yaml') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)

    HOOK_URL = conf['url']
    SLACK_CHANNEL = conf['channel']
    USER_NAME = conf['username']

    message = create_message()
    send_webhook(HOOK_URL, SLACK_CHANNEL, USER_NAME, message)
