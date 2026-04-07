from pydantic import BaseModel, Field, field_validator


class Dimensions(BaseModel):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)

    def volume(self) -> float:
        return self.length * self.width * self.height


class Package(BaseModel):
    tracking_id: str
    weight: float = Field(gt=0, lt=100)
    dimensions: Dimensions
    fragile: bool = False

    @field_validator("tracking_id")
    @classmethod
    def tracking_must_be_valid(cls, tracking_id: str) -> str:
        if not tracking_id.startswith("PKG-"):
            raise ValueError("Must start with PKG-")
        return tracking_id


dim = Dimensions(length=10, width=5, height=3.3)
box = Package(tracking_id="PKG-123", weight=5, dimensions=dim, fragile=True)

data = {
    "tracking_id": "P999",
    "weight": 60,
    "dimensions": {"length": 30, "width": -5, "height": 15},
    "fragile": True,
}

try:
    Package.model_validate(data)
except Exception as e:
    print(e)
