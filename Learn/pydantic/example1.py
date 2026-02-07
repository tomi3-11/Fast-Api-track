from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
        "id": "123",
        "signup_ts": "2017-06-01 14:34",
        "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > user id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 14, 34) friends=[1, 2, 3]
print(user.id)
# > 123
