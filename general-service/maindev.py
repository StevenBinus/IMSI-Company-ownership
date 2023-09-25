from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.middlewares import Transaction,ProcessingTime
import src.utils.AddControllers
from src.utils.AddEntitiesEngine import addentitiesengine
from src.middlewares.logging_lib import RouterLoggingMiddleware, logging_config
#import logging.config

app = FastAPI(title="DMS Microservices - General",docs_url="/")

#logging.config.dictConfig(logging_config)

# utilized for incoming request from Front End / API Gateway
origins = [
    "http://localhost:3000",
]

# utilized for managing the middlewares
#app.add_middleware(Transaction.DBTransactionMiddleware)
app.add_middleware(ProcessingTime.ProcessTime)
#app.add_middleware(RouterLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

#add the entities engine automatically
addentitiesengine(False)

#including the router
app.include_router(src.utils.AddControllers.populate_router)