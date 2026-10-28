from pydantic import BaseModel, Field
import uuid

class Brand(BaseModel):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(max_length=50)
    is_active: bool = Field(default=True)


class Product(BaseModel):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(max_length=50)
    brand: str = Brand.id
    is_active: bool = Field(default=True)

    def __str__(self):
        return f"{self.name}"

class Units(BaseModel):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)
    size: str = Field(max_length=50)
    is_active: bool = Field(default=True)

    def __str__(self):
        return f"{self.name}"


class ProductVariant(BaseModel):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(max_length=50)
    brand: str = Brand.id
    units: str = Units.id
    quantity: float = Field(max_digits=2)
    is_active: bool = Field(default=True)

    def __str__(self):
        return f"{self.name} {self.units} {self.quantity}"
