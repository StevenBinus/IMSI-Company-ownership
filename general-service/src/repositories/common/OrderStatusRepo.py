from sqlalchemy.orm import Session
from src.entities.common.OrderStatusEntity import MtrOrderStatus

def get_order_statuss_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(MtrOrderStatus).order_by(MtrOrderStatus.order_status_id).offset(offset).limit(limit).all()


def get_order_status_cruds(db:Session,get_id:int):
    return db.query(MtrOrderStatus).filter(MtrOrderStatus.order_status_id==get_id).first()
    

def post_order_status_cruds(db:Session, payload:MtrOrderStatus):
    return MtrOrderStatus(**payload.dict())

def delete_order_status_cruds(db:Session,get_id:int):
    return db.query(MtrOrderStatus).filter(MtrOrderStatus.order_status_id==get_id).delete(synchronize_session=False)
    
def put_order_status_cruds(db:Session,payload:MtrOrderStatus, get_id:int):
    edit_order_status = db.query(MtrOrderStatus).filter(MtrOrderStatus.order_status_id==get_id)
    edit_order_status.update(payload.dict())
    messages_order_status= edit_order_status.first()
    return edit_order_status, messages_order_status

def patch_order_status_cruds(db:Session, get_id:int):
    return db.query(MtrOrderStatus).filter(MtrOrderStatus.order_status_id==get_id).first()
