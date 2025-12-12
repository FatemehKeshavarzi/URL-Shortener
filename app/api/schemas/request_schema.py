from typing import Literal, TypeVar
from pydantic import BaseModel

data_type = TypeVar('data_type')

class ResponseSchema[data_type](BaseModel):
    data: data_type
    status: Literal['success', 'failure'] = 'success'


class ErrorSchema(BaseModel):
    status: Literal['success', 'failure'] = 'failure'
    message: str | None = None