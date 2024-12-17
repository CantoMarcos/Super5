from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .config.config_db import origins
from .routes.routes import routes

""""
    @author     Marcos Canto <marcoscanto@super.ufam.edu.br>                                                                
    @since      Nov 27, 2024
"""

app = FastAPI(
    title="Super Application",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in routes:
    app.include_router(route)