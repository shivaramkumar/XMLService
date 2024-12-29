from fastapi import APIRouter

router = APIRouter()

@router.post("/transform")
def transform_data():
    return {"message": "Transform data endpoint"}
