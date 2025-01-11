from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth

app = FastAPI(title="AlphaNode API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to AlphaNode API"} 