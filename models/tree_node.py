from pydantic import BaseModel
from typing import List, Optional

class TreeNode(BaseModel):
    tag: str
    attributes: Optional[dict] = None
    children: Optional[List["TreeNode"]] = None

TreeNode.model_rebuild()


