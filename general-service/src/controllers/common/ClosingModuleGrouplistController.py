from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import ClosingModuleGrouplistService
from src.payloads.schemas.common.ClosingModuleGrouplistSchema import MtrClosingModuleGrouplistGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Closing Module Grouplist"],prefix="/api/general")

@router.get("/closing-module-grouplists", status_code=200)
async def get_all_closing_module_grouplists(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = ClosingModuleGrouplistService.get_all_closing_module_grouplists(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/closing-module-grouplist/{closing_module_grouplist_id}", status_code=200)
async def get_by_id_closing_module_grouplist(closing_module_grouplist_id:int):
    get_result, err = ClosingModuleGrouplistService.get_by_id_closing_module_grouplist(closing_module_grouplist_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/closing-module-grouplist",status_code=201)
async def post_closing_module_grouplist(req:MtrClosingModuleGrouplistGetSchema):
    created_data, err = ClosingModuleGrouplistService.post_closing_module_grouplist(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/closing-module-grouplist/{closing_module_grouplist_id}",status_code=201)
async def put_closing_module_grouplist(closing_module_grouplist_id:int,req:MtrClosingModuleGrouplistGetSchema):
    updated_data, err = ClosingModuleGrouplistService.put_closing_module_grouplist(closing_module_grouplist_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/closing-module-grouplist/{closing_module_grouplist_id}",status_code=204)
async def delete_closing_module_grouplist(closing_module_grouplist_id:int):
    erase_data, err = ClosingModuleGrouplistService.delete_closing_module_grouplist(closing_module_grouplist_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/closing-module-grouplist/{closing_module_grouplist_id}",status_code=201)
async def patch_closing_module_grouplist(closing_module_grouplist_id:int):
    updated_data, err = ClosingModuleGrouplistService.patch_closing_module_grouplist(closing_module_grouplist_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



