from app import *


def test_home_route_returns_success_message():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello from Flask CI/CD demo!",
        "status": "ok",
    }


def test_health_route_returns_healthy_status():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_version_route_returns_app_metadata():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/version")

    assert response.status_code == 200
    assert response.get_json() == {
        "app": "flask-ci-cd-demo",
        "version": "1.0.0",
    }
