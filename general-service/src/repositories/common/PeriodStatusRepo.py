from sqlalchemy.orm import Session
from src.entities.common.PeriodStatusEntity import MtrPeriodStatus

def get_period_statuss_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(MtrPeriodStatus).order_by(MtrPeriodStatus.period_status_id).offset(offset).limit(limit).all()


def get_period_status_cruds(db:Session,get_id:int):
    return  db.query(MtrPeriodStatus).filter(MtrPeriodStatus.period_status_id==get_id).first()
    
def post_period_status_cruds(db:Session, payload:MtrPeriodStatus):
    return MtrPeriodStatus(**payload.dict())

def delete_period_status_cruds(db:Session,get_id:int):
    return db.query(MtrPeriodStatus).filter(MtrPeriodStatus.period_status_id==get_id).delete(synchronize_session=False)
    
def put_period_status_cruds(db:Session,payload:MtrPeriodStatus, get_id:int):
    edit_period_status = db.query(MtrPeriodStatus).filter(MtrPeriodStatus.period_status_id==get_id)
    edit_period_status.update(payload.dict())
    messages_period_status = edit_period_status.first()
    return edit_period_status, messages_period_status

def patch_period_status_cruds(db:Session, get_id:int):
    return db.query(MtrPeriodStatus).filter(MtrPeriodStatus.period_status_id==get_id).first()
