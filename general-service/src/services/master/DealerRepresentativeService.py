from src.repositories.master import DealerRepresentativeRepo
from src.payloads.schemas.master import DealerRepresentativeSchema
from fastapi import Request

def get_all_dealers_representative(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = DealerRepresentativeRepo.get_all_dealers_representative(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_dealer_representative(id:int):
    result, err = DealerRepresentativeRepo.get_by_id_dealer_representative(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_dealer_representative(req:DealerRepresentativeSchema.MtrDealerRepresentativeSchema):
    created_data, err = DealerRepresentativeRepo.post_dealer_representative(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def put_dealer_representative(id:int, request:DealerRepresentativeSchema):
    updated_data, err = DealerRepresentativeRepo.put_dealer_representative(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_dealer_representative(id:int):
    delete_data, err = DealerRepresentativeRepo.delete_dealer_representative(id)
    if err == None:
        return delete_data, None
    else:
        return None, err