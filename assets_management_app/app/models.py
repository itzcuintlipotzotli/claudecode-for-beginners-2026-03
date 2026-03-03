from datetime import datetime
from pydantic import BaseModel


class AssetCreate(BaseModel):
    name: str
    asset_type: str
    description: str = ""


class Asset(AssetCreate):
    id: str
    created_at: datetime
