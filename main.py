from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from openpyxl import Workbook
import os
from datetime import datetime

app = FastAPI()

def build_excel(project: str, client: str):
    wb = Workbook()
    ws = wb.active
    ws.title = "仕様書"

    ws.append(["物件名", project])
    ws.append(["施主名", client])
    ws.append(["作成日", datetime.now().strftime("%Y-%m-%d %H:%M")])
    ws.append([])
    ws.append(["大分類", "メーカー", "品番", "カラー"])
    ws.append(["外壁", "ニチハ", "EFF222", "ホワイト"])
    ws.append(["トイレ", "TOTO", "GG1", "ホワイト"])

    filename = "spec.xlsx"
    wb.save(filename)
    return filename


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head>
        <meta charset="utf-8">
        <title>仕様書ダウンロード</title>
      </head>
      <body style="font-family: sans-serif; padding: 24px;">
        <h2>仕様書（Excel）自動生成</h2>

        <form action="/download" method="get">
          <div style="margin-bottom: 12px;">
            <label>物件名：</label><br/>
            <input name="project" style="width: 320px; padding: 8px;" placeholder="例）○○様邸" />
          </div>

          <div style="margin-bottom: 12px;">
            <label>施主名：</label><br/>
            <input name="client" style="width: 320px; padding: 8px;" placeholder="例）山田 太郎" />
          </div>

          <button type="submit" style="padding: 10px 16px;">
            Excelをダウンロード
          </button>
        </form>

        <p style="margin-top: 16px; color:#666;">
          ※テスト版です。入力してダウンロードを押してください。
        </p>
      </body>
    </html>
    """


@app.get("/download")
def download(project: str = "物件名未入力", client: str = "施主名未入力"):
    filename = build_excel(project, client)

    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="仕様書.xlsx"
    )


@app.post("/generate")
def generate():
    filename = build_excel("テスト物件", "テスト施主")

    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="仕様書.xlsx"
    )
