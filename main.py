from fastapi import FastAPI, Request
import os
import socket

app = FastAPI(title="FastAPI Whoami")

@app.get("/")
async def read_root(request: Request):
    hostname = socket.gethostname()
    container_id = os.getenv("HOSTNAME", hostname)

    return {
        "hostname"    : container_id,                 # 컨테이너의 호스트명 (ID)
        "ip_address"  : request.client.host,          # 요청을 보낸 클라이언트의 IP 주소
        "headers"     : dict(request.headers),        # 모든 HTTP 헤더
        "method"      : request.method,               # HTTP 요청 메서드 (GET, POST 등)
        "path"        : request.url.path,             # 요청 경로
        "query_params": dict(request.query_params),   # 쿼리 파라미터
        "message"     : f"Hello from {container_id}!" # 환영 메시지
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}