from fastapi import FastAPI
from routes.user import user
app = FastAPI() 

app.include_router(user)

# # index.py or main file
# from fastapi import FastAPI
# from routes.user import user  # Ensure this import is correct

# app = FastAPI()

# app.include_router(user, prefix="/user", tags=["user"])


