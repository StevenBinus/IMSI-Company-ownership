from sqlalchemy.orm import Session

def activation(db:Session,table_query:object):
    active_status = db.scalars(table_query).first()
    active_status.is_active = not active_status.is_active
    db.commit()
    db.refresh(active_status)
    return active_status