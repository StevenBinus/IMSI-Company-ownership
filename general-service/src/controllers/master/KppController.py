from fastapi import APIRouter, HTTPException, status, Query, Request,Depends
from src.payloads.schemas.master.KppSchema import MtrKppPost,MtrKppUpdate
from src.services.master import KppService
from src.repositories.master import KppRepo
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from sqlalchemy.orm import Session
from src.configs.database import get_db

router = APIRouter(tags=["kpp"],prefix="/api/general")

@router.get("/kpps",status_code=200)
async def get_kpps(page:int,limit:int,is_active:bool|None=None,kpp_code:str|None=None,kpp_name:str|None=None,kpp_phone_no:str|None=None,kpp_address_1:str|None=None,kpp_address_2:str|None=None,kpp_address_3:str|None=None,village_id:int|None=None,sort_by:str|None=None,sort_of:str|None=None,db=Depends(get_db)):
   get_all_params={"is_active":is_active,"kpp_code":kpp_code,"kpp_name":kpp_name,"kpp_phone_no":kpp_phone_no,"kpp_address_1":kpp_address_1,"kpp_address_2":kpp_address_2,"kpp_address_3":kpp_address_3,"village_id":village_id}
   sort_fields={"sort_by":sort_by,"sort_of":sort_of}

   get_results,pages,err =await KppService.get_all_kpps(db,page,limit,get_all_params,sort_fields)

   if get_results!=[] and err == None:
       return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
   else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/kpp/{kpp_id}",status_code=200)
async def get_kpp(kpp_id:int,db=Depends(get_db)):
    get_result,err = await KppService.get_kpp(db,kpp_id)
    if get_result==[] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    else:
        return payload_response(200, "Success",get_result)

@router.post("/kpp",status_code=201)
async def post_kpp(req:MtrKppPost,db=Depends(get_db)):
    created_data,err=await KppRepo.post_kpp(db,req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/kpp/{kpp_id}",status_code=202)
async def update_data(kpp_id:int, req:MtrKppUpdate,db=Depends(get_db)):
    update_kpp,err=await KppService.put_kpp(db,kpp_id,req)
    if err == None:
        return payload_response(201,"Updated", update_kpp)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    

@router.patch("/kpp/{kpp_id}",status_code=202)
async def patch_kpp(kpp_id:int,db=Depends(get_db)):
    updated_data, err =await KppService.patch_kpp(db,kpp_id)
    if err == None:
        return payload_response(202,"Updated", updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
