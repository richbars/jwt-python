import os

from dotenv import load_dotenv

from CreateJWT import CreateJWT

load_dotenv()

if __name__ == "__main__":
    # token = CreateJWT.create_token("richbars")
    # print(token)

    decode = CreateJWT.validate_token(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoicmljaGJhcnMiLCJleHAiOjE3NDUwMDA3MDF9._2aLdm1iNlDBvXMERxKdukUDrP_o-n57uyMudwsW0Os",
        os.getenv("SECRET_KEY"))

    print(decode)
