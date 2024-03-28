from fastapi import FastAPI, Depends

from app.auth_helper import get_token
from app.routers import raw_material, common, production_detail, dispatch_detail


app = FastAPI(
    title="Test FastAPI with MySQL APIs",
    version="1.0.0",
    description="APIs for test FastAPI with MySQL",
)

# Mount routers
app.include_router(raw_material.router)
app.include_router(common.router)
app.include_router(production_detail.router)
app.include_router(dispatch_detail.router)


@app.get("/")
def check_server_status():
    return {"FastAPI Server is Running": True, "OpenAPI Docs": "/docs"}


@app.get("/protected")
async def protected_route(token: str = Depends(get_token)):
    return {"message": "This is a protected route", "token": token}
