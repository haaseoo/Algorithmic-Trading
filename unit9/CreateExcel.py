import openpyxl

# 엑셀 파일 생성
wb = openpyxl.Workbook()

# 활성 시트 잡기
ws = wb.active
ws.title = "Sheet1"

# 값 입력
ws.cell(row=1, column=1, value="hello world")

# 파일로 저장
wb.save("test.xlsx")