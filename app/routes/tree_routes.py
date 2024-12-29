from fastapi import APIRouter

router = APIRouter()

@router.get("/tree")
def get_tree():
    return {"message": "Get tree endpoint"}
