import threading
import uvicorn
import bot.bot
from web.web import app

def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=12636)

def run_discord():
    bot.bot.start()

if __name__ == "__main__":
    # FastAPI를 백그라운드 스레드로 실행
    threading.Thread(target=run_fastapi, daemon=True).start()
    # 디스코드 봇을 메인 스레드에서 실행
    run_discord()
