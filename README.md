# slack_webhook
자리 예약 알람
## 설정
- create_alarm.py 파일 수정
```python
    with open('<path to your directory>/config.yaml') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
```
- crontab 설정
  - shell 에서 실행
```
crontab -e
```
  - crontab 설정
```
#시간설정
<분> <시간> * * MON-FRI <path to python>/python3 <path to your directory>/create_alarm.py >> <path to your log directory>/logs/log_`date +\%Y\%m\%d`_`date +\%H\%M\%S`.log 2>&1
#example
55 14 * * MON-FRI /usr/bin/python3 /Users/dayoung/dev/onspace-alarm/create_alarm.py >> /Users/dayoung/dev/onspace-alarm/logs/log_`date +\%Y\%m\%d`_`date +\%H\%M\%S`.log 2>&1
```
