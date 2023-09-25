from sqlalchemy import select
from sqlalchemy.orm import Session, load_only
from src.utils.AddPagination import get_the_pagination_search_list
from src.entities.master.ProspectSourceEntity import MtrProspectSource
from src.entities.master.ProspectGroupEntity import MtrProspectGroup
from src.payloads.schemas.master.ProspectSourceSchema import (
    ProspectSourceCreateRequest,
    ProspectSourceUpdateRequest,
)
import requests, pandas as pd
import math


async def get_prospect_source_all(db:Session, page: int, limit: int, all_params: dict()):
    try:
        query_init = select(
            MtrProspectSource, MtrProspectGroup.prospect_group_name
        ).join(
            MtrProspectGroup,
            MtrProspectSource.prospect_group_id == MtrProspectGroup.prospect_group_id,
        )
        query_check,counter = get_the_pagination_search_list(db, query_init, all_params)
        query_final = query_check.offset(page * limit).limit(limit)
        results = db.execute(query_final).all()
        # simpen variabel, .query() raw query, convert ke dict lagi

        finalize = []
        for mtr_prospect_source, group_name in results:
            # * Please change to your own local/prod url once it already deployed
            get_company_id = requests.get(
                f"http://10.1.32.26:8000/general-service/api/general/company/{mtr_prospect_source.company_id}"
            )

            company_name = get_company_id.json()["data"]["company_name"]
            if all_params["company_code"] == None:
                company_code = get_company_id.json()["data"]["company_code"]
                customized_json = {
                    "prospect_source_id": mtr_prospect_source.prospect_source_id,
                    "prospect_source_code": mtr_prospect_source.prospect_source_code,
                    "prospect_source_name": mtr_prospect_source.prospect_source_name,
                    "company_id": mtr_prospect_source.company_id,
                    "company_code": company_code,
                    "company_name": company_name,
                    "prospect_group_id": mtr_prospect_source.prospect_group_id,
                    "prospect_group_name": group_name,
                    "is_active": mtr_prospect_source.is_active,
                }
                finalize.append(customized_json)

            else:
                print(str(pd.DataFrame.from_dict(get_company_id.json())))
                dataframe_result = pd.DataFrame.from_dict(get_company_id.json())
                dict_result = dataframe_result.query(
                    'data == @all_params["company_code"]'
                ).to_dict()

                # print("company code result: " + str(dict_result["data"]["company_code"]))

                if dict_result["data"] != {}:
                    customized_json = {
                        "prospect_source_id": mtr_prospect_source.prospect_source_id,
                        "prospect_source_code": mtr_prospect_source.prospect_source_code,
                        "prospect_source_name": mtr_prospect_source.prospect_source_name,
                        "company_id": mtr_prospect_source.company_id,
                        "company_code": dict_result["data"]["company_code"],
                        "company_name": company_name,
                        "prospect_group_id": mtr_prospect_source.prospect_group_id,
                        "prospect_group_name": group_name,
                        "is_active": mtr_prospect_source.is_active,
                    }
                    finalize.append(customized_json)

        total_rows = len(finalize)
        total_pages = math.ceil(counter / limit)

        page_results = {"total_rows": total_rows, "total_pages": total_pages}
        return finalize, page_results, None

    except Exception as err:
        return None, None, err

async def get_prospect_source_drop_down(db:Session):
    try:
        query = select(MtrProspectSource).options(load_only(MtrProspectSource.prospect_source_name, MtrProspectSource.prospect_source_name))
        result = db.scalars(query).all()
        return result, None
    except Exception as err:
        return None, err

async def get_prospect_source_by_id(db:Session,id: int):
    try:
        query_init = select(MtrProspectSource, MtrProspectGroup)
        query_join = query_init.join(
            MtrProspectGroup,
            MtrProspectSource.prospect_group_id == MtrProspectGroup.prospect_group_id,
        ).filter(MtrProspectSource.prospect_source_id == id)
        results = db.execute(query_join).all()

        try:
            get_company_id = requests.get(
                f"http://127.0.0.1:8050/api/general/company/{results[0][0].company_id}"
            )

            company_code = get_company_id.json()["data"]["company_code"]
            company_name = get_company_id.json()["data"]["company_name"]
        except:
            company_code = "Dummy Code"
            company_name = "Dummy Name"
            
        finalize = {
            "prospect_source_id": results[0][0].prospect_source_id,
            "prospect_source_code": results[0][0].prospect_source_code,
            "prospect_source_name": results[0][0].prospect_source_name,
            "company_id": results[0][0].company_id,
            "company_code": company_code,
            "company_name": company_name,
            "prospect_group_id": results[0][0].prospect_group_id,
            "prospect_group_name": results[0][1].prospect_group_name,
            "is_active": results[0][0].is_active,
        }

        return finalize, None
    except Exception as err:
        return None, err


async def post_prospect_source(db:Session,req: ProspectSourceCreateRequest):
    try:
        new_prospect_source = MtrProspectSource(
            prospect_source_code=req.prospect_source_code,
            prospect_source_name=req.prospect_source_name,
            company_id=req.company_id,
            prospect_group_id=req.prospect_group_id,
            is_active=True,
        )
        db.add(new_prospect_source)
        db.commit()
        db.refresh(new_prospect_source)
        return new_prospect_source, None
    except Exception as err:
        db.rollback()
        return None, err


async def put_prospect_source(db:Session,id: int, req: ProspectSourceUpdateRequest):
    try:
        query_check = select(MtrProspectSource).where(
            MtrProspectSource.prospect_source_id == id
        )
        updated_data = db.scalars(query_check).first()
        updated_data.prospect_source_name = req.prospect_source_name
        updated_data.prospect_group_id = req.prospect_group_id
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err


async def patch_prospect_source(db:Session,id: int):
    check_active_status = select(MtrProspectSource).where(
        MtrProspectSource.prospect_source_id == id
    )
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
            db.commit()
            db.refresh(active_status)
            return active_status, None
        else:
            active_status.is_active = True
            db.commit()
            db.refresh(active_status)
            return active_status, None
    except Exception as err:
        db.rollback()
        return None, err