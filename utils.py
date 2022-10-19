from pydantic import BaseModel

class Token(BaseModel):
    token: str

class Vote(BaseModel):
    userId: str
    orgCode: int

def takeOrgDetails() -> "dict[int, str]":
    details: "dict[int, str]" = {}
    while (True):
        orgDetail = input("Register Organisation: [name: code], ['q' -> exit] : ")
        if orgDetail == "q":
            break
        elif len(orgDetail.split(" ")) > 2:
            print("Enter valid details")
        else:
            n, c = orgDetail.split(" ")
            details[int(c)] = n
    return details