from datetime import datetime
import os
import sys

def create_visit_report():
    # 사용자 입력 받기
    print("방문 장소를 입력하세요: ", end='')
    place = sys.stdin.readline().strip()
    print("방문 목적을 입력하세요: ", end='')
    purpose = sys.stdin.readline().strip()
    print("특이사항을 입력하세요: ", end='')
    details = sys.stdin.readline().strip()

    # 현재 날짜 가져오기
    today_date = datetime.now().strftime("%Y년 %m월 %d일")
    current_time = datetime.now().strftime("%H시 %M분")

    # 보고서 작성
    report = f"""
방문보고서
{place}을(를) {today_date} {purpose}의 내용으로 방문했습니다.
{details}
"""

    return report, place, today_date, current_time

# 보고서 생성 및 출력
report_text, place, date, time = create_visit_report()
print(report_text)

# 저장할 경로 지정
save_path = "/home/doitandy/report/"

# 파일명 생성
filename = f"{date}_{time}_{place}.txt".replace(" ", "_").replace(":", "-")
full_path = os.path.join(save_path, filename)

# 경로가 존재하는지 확인하고, 없으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 파일 저장
try:
    with open(full_path, 'w', encoding='utf-8', errors='replace') as file:
        file.write(report_text)
    print(f"보고서가 '{full_path}' 파일로 저장되었습니다.")
except UnicodeDecodeError as e:
    print(f"인코딩 오류: {e}")
except Exception as e:
    print(f"파일 저장 중 오류 발생: {e}")
