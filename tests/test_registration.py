import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tournaments", json={
            "name": "TestCup",
            "max_players": 2,
            "start_at": "2025-07-01T12:00:00Z"
        })
        tournament = response.json()
        res = await ac.post(f"/tournaments/{tournament['id']}/register", json={
            "name": "Tester",
            "email": "test@example.com"
        })
        assert res.status_code == 200