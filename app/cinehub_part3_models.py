from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class MovieCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str = Field(..., min_length=1, max_length=100, description="Movie title")
    rating: float = Field(..., ge=0.0, le=10.0, description="IMDB-like rating from 0 to 10")
    year: int = Field(..., ge=1888, le=2100, description="Release year")
    description: Optional[str] = Field(None, max_length=500, description="Optional short description")

class MovieUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    rating: Optional[float] = Field(None, ge=0.0, le=10.0)
    year: Optional[int] = Field(None, ge=1888, le=2100)
    description: Optional[str] = Field(None, max_length=500)

class MovieOut(BaseModel):
    id: int
    title: str
    rating: float
    year: int
    description: Optional[str] = None
    archived: bool = False
