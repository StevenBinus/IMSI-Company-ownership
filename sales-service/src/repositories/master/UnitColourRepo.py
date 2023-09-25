from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.entities.master.UnitColourEntity import MtrColour
from src.entities.master.BrandEntity import MtrBrand
from src.payloads.schemas.master.UnitColourSchema import UnitColourRequest
from src.utils.Activation import activation
from src.utils.AddPagination import get_the_pagination_search_list
import math

async def get_unit_colour_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    try:
        query_set = select(MtrColour.colour_code,MtrColour.colour_commercial_name,MtrColour.colour_police_name,MtrBrand.brand_name,MtrColour.is_active).join(
            MtrBrand,MtrBrand.brand_id==MtrColour.brand_id
        )
        query_check,counter = await get_the_pagination_search_list(db,query_set,all_params)
        #for pagination purposes
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrColour.colour_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit)
        results = db.execute(query_final).all()

        total_rows = len(results)
        total_pages = math.ceil(counter/limit)

        final_results = []

        for colour_code, colour_commercial_name, colour_police_name, brand_name, is_active in results:
            result = {
                "colour_code" : colour_code,
                "colour_commercial_name" : colour_commercial_name,
                "colour_police_name" : colour_police_name,
                "brand_name":brand_name,
                "record_status":is_active
            }
            final_results.append(result)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return final_results, page_results, None
    except Exception as err:
        return None, None, err
    
async def get_unit_colour_by_id(db:Session,id:int):
    try:
        query_check = select(MtrColour).where(MtrColour.colour_id==id)
        result = db.scalars(query_check).first()
        return result, None
    except Exception as err:
        return None, err
    
async def post_unit_colour(db:Session,req:UnitColourRequest):
    try:
        db.begin()
        created_data = MtrColour()
        created_data.brand_id = req.vehicle_brand
        created_data.colour_code = req.colour_code
        created_data.colour_commercial_name = req.description_commercial
        created_data.colour_police_name = req.description_police
        db.add(created_data)
        db.commit()
        db.refresh(created_data)
        return created_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
async def patch_unit_colour(db:Session,id:int):
    try:
        db.begin()
        query_activate = select(MtrColour).where(MtrColour.colour_id==id)
        activation_status = activation(db,query_activate)
        return activation_status, None
    except Exception as err:
        db.rollback()
        return None, err
