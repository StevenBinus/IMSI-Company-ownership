import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

path = os.getcwd()
prev_path_common = path + "//src/controllers/common"
prev_path_master = path + "//src/controllers/master"
router_common = os.listdir(prev_path_common)
router_master = os.listdir(prev_path_master)

for ch in router_common:
    name,ext = os.path.splitext(ch)
    if ext == ".py":
        from_module = importlib.import_module("src.controllers.common." + name)
        populate_router.include_router(from_module.router)  

for ch in router_master:
    name,ext = os.path.splitext(ch)
    if ext == ".py":
        from_module = importlib.import_module("src.controllers.master." + name)
        populate_router.include_router(from_module.router)  