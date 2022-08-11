from typing import Generator

import pytest
from fastapi import status
from flipper.client import FeatureFlagClient

from prefect.settings import PREFECT_FEATURE_FLAGGING_ENABLED, temporary_settings
from prefect.utilities.feature_flags import create_if_missing, get_feature_flag_client


@pytest.fixture
def features() -> Generator[FeatureFlagClient, None, None]:
    """
    A feature flag client fixture.

    NOTE: When used in a test, this fixture turns on feature flagging.
    """
    with temporary_settings({PREFECT_FEATURE_FLAGGING_ENABLED: "true"}):
        yield get_feature_flag_client()


@pytest.fixture(autouse=True)
def delete_test_flags(features: FeatureFlagClient):
    for flag in features.list():
        features.destroy(flag.name)


@pytest.fixture
def enabled_flag(features: FeatureFlagClient):
    with temporary_settings({PREFECT_FEATURE_FLAGGING_ENABLED: "true"}):
        flag = create_if_missing("enabled_flag", is_enabled=True)
    yield flag


@pytest.fixture
def disabled_flag(features: FeatureFlagClient):
    with temporary_settings({PREFECT_FEATURE_FLAGGING_ENABLED: "true"}):
        flag = create_if_missing("disabled_flag", is_enabled=False)
    yield flag


class TestReadFeatureFlags:
    async def test_read_feature_flags_with_global_setting_off(
        self, client, enabled_flag
    ):
        with temporary_settings({PREFECT_FEATURE_FLAGGING_ENABLED: "false"}):
            response = await client.get(f"/feature_flags/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    async def test_read_feature_flags_with_global_setting_on(
        self, client, enabled_flag, disabled_flag
    ):
        expected_enabled_date = enabled_flag.get_meta()["created_date"]
        expected_disabled_date = disabled_flag.get_meta()["created_date"]

        response = await client.get(f"/feature_flags/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {
                "name": "disabled_flag",
                "is_enabled": False,
                "data": {
                    "client_data": {},
                    "created_date": expected_disabled_date,
                    "conditions": [],
                    "bucketer": {"type": "NoOpBucketer"},
                },
            },
            {
                "data": {
                    "bucketer": {"type": "NoOpBucketer"},
                    "client_data": {},
                    "conditions": [],
                    "created_date": expected_enabled_date,
                },
                "is_enabled": True,
                "name": "enabled_flag",
            },
        ]
