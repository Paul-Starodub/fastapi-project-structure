from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    # model_config = ConfigDict(from_attributes=True)  # used by default now
