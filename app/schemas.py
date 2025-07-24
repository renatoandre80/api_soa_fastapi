from pydantic import BaseModel


class UserCreate(BaseModel):
    """Classe para criar um usuário"""
    name: str
    email: str


class UserResponse(BaseModel):
    """Classe de resposta do usuário"""
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True