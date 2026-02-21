from fastapi import FastAPI
from fastapi.responses import FileResponse
from openpyxl import Workbook

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/generate")
def generate():
    wb = Workbook()
    ws = wb.active
    ws.title = "仕様書"
    ws.append(["大分類","メーカー","品番","カラー"])
    ws.append(["外壁","ニチハ","EFF222","ホワイト"])
    ws.append(["トイレ","TOTO","GG1","ホワイト"])

    filename = "spec.xlsx"
    wb.save(filename)

    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=filename
    )
