from pydantic import BaseModel, Field, ConfigDict

class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='forbid')
    id: str = 'chikcjha'
    is_admin: bool = Field(default=False, alias='isAdmin')

#user = UserSchema(isAdmin=True)
user_2 = UserSchema()
print(user_2)