from pydantic import BaseModel, validator, StrictStr


class UserValidator(BaseModel):
    account: StrictStr
    password: StrictStr
    confirm_password: StrictStr

    @validator("account")
    def account_must_not_empty(cls, v):
        if v == "":
            raise ValueError("account must not be empty.")
        return v

    @validator("password")
    def password_must_not_empty(cls, v):
        if v == "":
            raise ValueError("password must not be empty.")
