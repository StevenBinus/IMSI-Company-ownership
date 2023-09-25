from sqlalchemy.orm import Session
from src.entities.common.LandedCostTypeEntity import MtrLandedCostType

def get_landed_cost_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(MtrLandedCostType).order_by(MtrLandedCostType.landed_cost_type_id).offset(offset).limit(limit).all()


def get_landed_cost_type_cruds(db:Session,get_id:int):
    return  db.query(MtrLandedCostType).filter(MtrLandedCostType.landed_cost_type_id==get_id).first()
    

def post_landed_cost_type_cruds(db:Session, payload:MtrLandedCostType):
    return MtrLandedCostType(**payload.dict())

def delete_landed_cost_type_cruds(db:Session,get_id:int):
    return db.query(MtrLandedCostType).filter(MtrLandedCostType.landed_cost_type_id==get_id).delete(synchronize_session=False)
    
def put_landed_cost_type_cruds(db:Session,payload:MtrLandedCostType, get_id:int):
    edit_landed_cost_type = db.query(MtrLandedCostType).filter(MtrLandedCostType.landed_cost_type_id==get_id)
    edit_landed_cost_type.update(payload.dict())
    messages_landed_cost_type = edit_landed_cost_type.first()
    return edit_landed_cost_type, messages_landed_cost_type

def patch_landed_cost_type_cruds(db:Session, get_id:int):
    return db.query(MtrLandedCostType).filter(MtrLandedCostType.landed_cost_type_id==get_id).first()
