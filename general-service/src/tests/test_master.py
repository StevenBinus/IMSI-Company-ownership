from starlette.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_get_areas():
    response = client.get(f"/api/general/areas?page=1&limit=2&sort_by=area_code&sort_of=asc")
    assert response.status_code == 200

def test_get_areas_by_id():
    response = client.get(f'/api/general/area/1')
    assert response.status_code == 200

def test_get_area_by_code():
    response = client.get(f"/api/general/area-by-code/A1")
    assert response.status_code == 200

def patch_status_area():
    response = client.patch(f"/api/general/area/2")
    assert response.status_code == 202

def put_area():
    response = client.put(f"/api/general/area/2",
                          json={
                                "area_code": "A2",
                                "description": "Coba",
                                "region_id": 1
                          })
    assert response.status_code == 202

def test_patch_countries():
    client = TestClient(app)
    country_id = 1
    response = client.patch(f"/api/general/country/{country_id}")
    print(response.json())
    assert response.status_code in (422, 202)


# MASTER
# UNIT TEST COMPANY REFERENCE GET BY ID

def test_get_company_references_by_id():
    client = TestClient(app)
    company_id = 1
    response = client.get(f"/api/general/address/{company_id}")
    assert response.status_code in (200, 404)

# MASTER
# UNIT TEST COMPANY REFERENCE GET ALL

def test_get_all_company_references():
    client = TestClient(app)
    response = client.get(f"/api/general/company_references", params={"page": 0, "limit": 20})
    assert response.status_code == 404

# MASTER
# UNIT TEST COMPANY REFERENCE GET BY ID

def test_get_all_is_use_tax_invoice():
    client = TestClient(app)
    company_id = 1
    response = client.get(f"/companyreference/{company_id}")
    assert response.status_code in (200,404)

# MASTER
# UNIT TEST COMPANY REFERENCE GET BY ID

def test_patch_company_reference():
    client = TestClient(app)
    company_id = 1
    response = client.patch(f"/api/general/country/{company_id}")
    print(response.json())
    assert response.status_code == 409



def get_regions():
    response = client.get(f"/api/general/region?page=1&limit=10&is_active=true&sort_by=region_code&sort_of=desc")
    assert response.status_code == 200

def get_region_by_id():
    response = client.get(f"/api/general/region/1")
    assert response.status_code == 200

def get_region_by_code():
    response = client.get(f"/api/general/region-by-code/R1")
    assert response.status_code == 200

def patch_status_region():
    response = client.patch(f"/api/general/region/1") 
    assert response.status_code == 202

def put_region():
    response = client.put(f"/api/general/region/?id=1",
                          json={
                                "region_code": "R1",
                                "region_name": "Region 1"
                          })
    assert response.status_code == 202

def get_all_comref():
    response = client.get(f"/api/general/company_references?page=0&limit=5")
    assert response.status_code == 200
