import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

path = os.getcwd()
prev_path_mtr = path + "/src/controllers/master"
prev_path_trx = path + "/src/controllers/transaction"
router_mtr = os.listdir(prev_path_mtr)
router_trx = os.listdir(prev_path_trx)

#add the entire controllers
for ch in router_mtr:
    name,ext = os.path.splitext(ch)
    if ext == ".py":
        from_module = importlib.import_module("src.controllers.master." + name)
        populate_router.include_router(from_module.router)  

for ch in router_trx:
    name,ext = os.path.splitext(ch)
    if ext == ".py":
        from_module = importlib.import_module("src.controllers.transaction." + name)
        populate_router.include_router(from_module.router)  