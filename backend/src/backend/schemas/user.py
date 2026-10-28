from pydantic import BaseModel, Field, EmailStr
import uuid
import datetime 

#these are the businesses that sign up for the project
class User(BaseModel):
    id: str = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str =Field(max_length=50)
    email: EmailStr = Field(unique=True, max_length=100, alias="username")
    phone_number: str = Field(max_length=50)
    date_joined: str = Field(default_factory=datetime.datetime.today)
    is_active: bool = Field(default=True)

    def __str__(self):
        return f"{self.name} {self.phone_number}"

