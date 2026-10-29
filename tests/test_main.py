from fastapi.testclient import TestClient

from main import app
client = TestClient(app)

def test_read_sheep():
        response = client.get("/sheep/1")

        assert response.status_code == 200
        assert response.json() == {
            "id" : 1,
            "name" : "Spice",
            "breed" : "Gotland",
            "sex" : "ewe"
        }

def test_add_sheep():
        sheep_data = {
            "id" : 100,
            "name" : "Dolly",
            "breed" : "Gotland",
            "sex" : "ewe"

        }

        response = client.post("/sheep", json=sheep_data)

        assert response.status_code == 201

        for key, value in sheep_data.items():
            assert response.json()[key] == value


        sheep_id = response.json()["id"]
        get_response = client.get(f"/sheep/{sheep_id}")

        assert get_response.status_code == 200

        for key, value in sheep_data.items():
            assert get_response.json()[key] == value

def test_delete_sheep():
    sheep_data = {
        "id" : 100,
        "name" : "Dolly",
        "breed" : "Gotland",
        "sex" : "ewe"
    }

    response = client.post("/sheep", json=sheep_data)
    assert response.status_code == 201

    sheep_id = response.json()["id"]

    delete_response = client.delete(f"/sheep/{sheep_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/sheep/{sheep_id}")
    assert get_response.status_code == 404