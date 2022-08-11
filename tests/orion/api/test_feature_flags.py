from fastapi import status


class TestReadFeatureFlags:
    async def test_read_feature_flags_with_global_setting_off(self, client):
        response = await client.get(f"/feature_flags/")
        assert response.status_code == status.HTTP_200_OK
