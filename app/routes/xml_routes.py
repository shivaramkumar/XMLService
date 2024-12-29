from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_xml():
    return {"message": "Upload XML endpoint"}
