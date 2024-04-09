import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ConfigBase(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        
        
class HealtyResponse(ConfigBase):
    Message: str

class MessageBody(ConfigBase):
    Message: str
