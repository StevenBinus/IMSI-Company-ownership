from src.repositories.master import SupplierReferenceRepo
from src.payloads.schemas.master import SupplierReferenceSchema
from src.payloads.schemas.master import SupplierReferencePicSchema
from src.payloads.schemas.master import SupplierReferenceBankReferenceSchema


def post_supplier_reference(req:SupplierReferenceSchema.MtrSupplierReferenceSchema):
    create_data,err = SupplierReferenceRepo.post_supplier_reference(req)
    if err == None:
        return create_data,None
    else:
        return None,err

def get_supplier_reference_by_id(id:int):
    get_data,pic_data,bank_reference,err = SupplierReferenceRepo.get_supplier_reference_by_id(id)
    if err == None:
        return get_data,pic_data,bank_reference,None
    else:
        return None,None,None,err

def get_all_supplier_references(page:int,limit:int,all_params:dict(),sort_params:dict()):
    get_all_data,pages,err=SupplierReferenceRepo.get_supplier_references(page,limit,all_params,sort_params)
    if err == None:
        return get_all_data,pages,None
    else:
        return None,None,err
    
def patch_supplier_references(id:int):
    updated_data,err = SupplierReferenceRepo.patch_supplier_reference(id)
    if err == None:
        return updated_data,None
    else:
        return None,err
    
def post_supplier_reference_pic(req:SupplierReferencePicSchema.MtrSupplierReferencePic):
    created_data,err = SupplierReferenceRepo.post_supplier_reference_pic(req)
    if err == None:
        return created_data,None
    else:
        return None,err
    
def patch_supplier_reference_pic(id:int):
    updated_data,err = SupplierReferenceRepo.patch_supplier_reference_pic(id)
    if err == None:
        return updated_data,None
    else:
        return None,err
    
def post_supplier_reference_bank_reference(req:SupplierReferenceBankReferenceSchema.MtrSupplierReferenceBankReference):
    created_data,err=SupplierReferenceRepo.post_supplier_reference_bank_reference(req)
    if err == None:
        return created_data,None
    else:
        return None,err

def put_supplier_reference(id:int):
    updated_data,err=SupplierReferenceRepo.put_supplier_reference(id)
    if err == None:
        return updated_data,None
    else:
        return None,err