from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.AddControllers import populate_router
from src.utils.AddEntitiesEngine import addentitiesengine
from src.middlewares.LoggingLogger import RouterLoggingMiddleware, logging_config
import logging.config

# logging.config.dictConfig(logging_config)
app = FastAPI(title="DMS Microservices - Sales", docs_url="/")  # development

# utilized for managing the middlewares
# app.add_middleware(RouterLoggingMiddleware)
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# populates the entities/models
addentitiesengine(
    False
)  # True : to Migrate, default if False (CHECK BEFORE RUNNING THE SERVER)

# populates the router
app.include_router(populate_router)
