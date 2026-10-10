from app import app, get_greeting


def test_get_greeting():
    assert get_greeting("Анна") == "Добро пожаловать, Анна!"


def test_index_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Учебное Flask-приложение" in response.get_data(as_text=True)


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
