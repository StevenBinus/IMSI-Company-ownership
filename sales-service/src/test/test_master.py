from starlette.testclient import TestClient
import sys
sys.path.append("../..")
from maindev import app


client = TestClient(app)

#unit Brand
def get_all_unit_brands():
    responses = client.get(f"/api/sales/unit-brand?page=0&limit=10")
    assert responses == 200