from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router.rec import router as rec_router


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    title="OSINT API",
    description="OSINT API",
    version="0.1.0",

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rec_router)