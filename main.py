from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pathlib import Path
from starlette.staticfiles import StaticFiles

# fastapiの設定
app = FastAPI()

# 静的ファイル(HTMLファイル)を提供するためのディレクトリを指定
static_dir: Path = Path("static")
app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")

"""
HTMLを返す
"""
@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse(static_dir / "index.html")