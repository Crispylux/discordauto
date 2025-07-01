import requests
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/여기에_붙여넣기"

now = datetime.now()
weekday = now.weekday()

message = {
    "content": "✨[자동화된 채팅입니다]✨\n{today_str} 스터디 끝! 다들 맛점심하시길... \n오늘 한 내용 내용공유방에 올리기!\n ~정세영 올림~"
}

#평일만
if weekday < 5:
    response = requests.post(WEBHOOK_URL, json=message)
    if response.status_code == 204:
        print("디스코드로 메시지 전송 성공")
    else:
        print(f"전송 실패: {response.status_code} - {response.text}")
else:
    print("오늘은 평일이 아니므로 메시지를 보내지 않습니다.")
