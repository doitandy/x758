import datetime
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

def generate_inspection_report():
    # Questions for the inspection
    questions = [

                "내부/외부 - 조치해야할 내용이 있는가",
                "수염 가리개, 금속 장신구 및 손톱 장식 착용 금지 준수하고 있는가?",
                "식품 온도 관리 상태 시설 온도 및 온도계 작동여부 (냉장 41°F 이하, 냉동 0°F 이하, 열 조리된 식품 135°F 이상)",
                "식자재가 바닥에서 6인치 이상 정리되고 있는가?",
                "해동 과정이 규정에 맞게 진행하고 있는가? (흐르는 물에 70°F 이하, 4시간 이상 유지)",
                "교차 오염 방지를 위한 조치를 하고 있는가? (식품 및 도구의 분리 보관, 적절한 거리 유지)",
                "쓰레기 처리 시설의 청결 및 관리하고 있는가?",
                "화학용품 분리 보관상태 및 라벨링 관리상태?",
                "화장실/ 고객구역 청결상태는 어떤가?",
                "샐러드 바 온도 및 위생 관리는 어떻게 하고 있는가?",
                "알레르기 유발 식품 및 기타 주의 사항에 대한 경고문이 있는가?",
                "문제 요소가 있는 직원이 있는가? 있다면 매니저는 어떤조치를 하고 있는가",
                "직원안전관련 내용이 있는가? 뜨거운 물 / 미끄러운 바닥등 etc",
                "운영에 필요한 500불 이상 조치 필요내용이 있는가?",
                # ... (additional questions)
                ]

    store_location = input("Store location을 입력해주세요: ")
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H-%M-%S")

    # Define the directory path
    directory = "/home/doitandy/romeo/report"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the filename and filepath
    filename = f"{store_location}_visit_{date}_{time}.txt"
    filepath = os.path.join(directory, filename)

    # Write to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"Store Location: {store_location}\n")
        file.write(f"Date: {date}\n\n")

        # Write each question and its response to the file
        for question in questions:
            response = input(f"{question}: ")
            file.write(f"{question}\n- Response: {response}\n\n")

    print(f"Report saved as {filepath}")

# To run the script, simply call the function:
generate_inspection_report()
