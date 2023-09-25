from starlette.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_get_areas():
    response = client.get(f"/api/general/areas?page=1&limit=2&sort_by=area_code&sort_of=asc")
    assert response.status_code == 200

'''
# MASTER
# UNIT TEST GET - ALL
def test_get_countries():
    client = TestClient(app)
    response = client.get(f"/api/general/countries")
    assert response.status_code in (200)

def test_get_job_positions():
    client = TestClient(app)
    response = client.get(f"/api/general/job-positions")
    assert response.status_code in (200, 404)

def test_get_job_titles():
    client = TestClient(app)
    response = client.get(f"/api/general/job-titles")
    assert response.status_code in (200, 404)

def test_get_master_cost_centers():
    client = TestClient(app)
    response = client.get(f"/api/general/get-master-cost-centers")
    assert response.status_code in (200, 404)

def test_get_skill_level_code():
    client = TestClient(app)
    response = client.get(f"/api/general/skill-level-codes")
    assert response.status_code in (200, 404)

def test_get_skill_levels():
    client = TestClient(app)
    response = client.get(f"/api/general/skill-levels")
    assert response.status_code in (200, 404)

def test_get_source_approval_documents():
    client = TestClient(app)
    response = client.get(f"/api/general/source-approval-documents")
    assert response.status_code in (200, 404)

def test_get_vat_company():
    client = TestClient(app)
    response = client.get(f"/api/general/vat-company")
    assert response.status_code in (200, 404)

def test_get_addresses():
    client = TestClient(app)
    response = client.get(f"/api/general/addresses")
    assert response.status_code in (200, 404)

def test_get_loggings():
    client = TestClient(app)
    response = client.get(f"/api/general/loggings")
    assert response.status_code in (200, 404)

# MASTER
# UNIT TEST GET - LIST
def test_get_areas():
    client = TestClient(app)
    response = client.get(f"/api/general/areas", params={"page": 0, "limit": 20})
    assert response.status_code in (200, 404)

def test_get_provinces():
    client = TestClient(app)
    response = client.get(f"/api/general/provinces", params={"page": 0, "page_limit": 20})
    assert response.status_code in (200, 404)

def test_get_regions():
    client = TestClient(app)
    response = client.get(f"/api/general/region", params={"page": 0, "limit": 20})
    assert response.status_code in (200, 404)

def test_get_supplier_list():
    client = TestClient(app)
    response = client.get(f"/api/general/supplier-master", params={"page": 0, "limit": 10})
    assert response.status_code == 200


# MASTER
# UNIT TEST GET - BY ID

def test_get_address_by_id():
    client = TestClient(app)
    address_id = 1
    response = client.get(f"/api/general/address/{address_id}")
    assert response.status_code in (200, 404)

def test_get_supplier_by_id():
    client = TestClient(app)
    supplier_id = 1
    response = client.get(f"/api/general/supplier-master/{supplier_id}")
    assert response.status_code == 200
# MASTER
# UNIT TEST POST
def test_post_countries():
    client = TestClient(app)
    response = client.post(f"/api/general/country", 
        json={
            "country_code": "TEST",
            "country_name": "TEST",
            "country_language": "TEST",
            "country_phone": "TEST",
            "currency_id": 123
        }
    )
    print(response.json())
    assert response.status_code in (409, 201)

# MASTER
# UNIT TEST DELETE
def test_delete_countries():
    client = TestClient(app)
    country_id = 1
    response = client.delete(f"/api/general/country/{country_id}")
    assert response.status_code in (404,204)

# MASTER
# UNIT TEST PUT
def test_put_countries():
    client = TestClient(app)
    country_id = 1
    response = client.put(f"/api/general/country/{country_id}", 
        json={
            "country_code": "test",
            "country_name": "test",
            "country_language": "test",
            "country_phone": "test",
            "currency_id": 123
        }
    )
    print(response.json())
    assert response.status_code in (422, 202)

# MASTER
# UNIT TEST PATCH

def test_patch_countries():
    client = TestClient(app)
    country_id = 1
    response = client.patch(f"/api/general/country/{country_id}")
    print(response.json())
    assert response.status_code in (422, 202)
'''