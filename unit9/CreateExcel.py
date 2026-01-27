import openpyxl
import os

# 엑셀 파일 생성
wb = openpyxl.Workbook()

# 활성 시트 잡기
ws = wb.active
ws.title = "Sheet1"

# 값 입력
ws.cell(row=1, column=1, value="hello world")

# 저장 위치
current_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(current_dir, "..", "etc", "test.xlsx")

# 파일로 저장
try:
    wb.save("test.xlsx")
    print(f"저장 성공, 경로: {save_path}")
    # f : 변수를 문자열 안에 넣겠다
except FileNotFoundError:
    print("error 발생")