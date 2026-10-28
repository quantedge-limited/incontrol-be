from pydantic import BaseModel, Field
import uuid

#Industry prices(service industry, product industry)
class Industry(BaseModel):
    id: str = Field(primary_key=True, default=uuid.uuid4().hex)
    name: str = Field(max_length=50)
    price: float = Field(max_digits=2, decimal_places=2)
    is_active: bool = Field(default=True)

    def __str__(self):
        return f"{self.name} {self.price}"

