from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Kirov Secure Auth System API",
    description="Enterprise authentication system API",
    version="0.1.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy", "service": "kirov-secure-auth-system", "version": "0.1.0"}
