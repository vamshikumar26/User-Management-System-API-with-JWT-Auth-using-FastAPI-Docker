from fastapi import FastAPI
from routes import endpoints 
from routes import authentication

app=FastAPI()

#endpoints router
app.include_router(endpoints.router)

#authentication router
app.include_router(authentication.router)