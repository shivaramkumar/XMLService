from fastapi import FastAPI
from app.routes import xml_routes, tree_routes, transform_routes

app = FastAPI(title="XML Service")

# Include routes
app.include_router(xml_routes.router, prefix="/xml", tags=["XML Operations"])
app.include_router(tree_routes.router, prefix="/tree", tags=["Tree Operations"])
app.include_router(transform_routes.router, prefix="/transform", tags=["Data Transformations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
