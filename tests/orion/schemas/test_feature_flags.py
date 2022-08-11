import json

import pytest
from pydantic import ValidationError

from prefect.orion.schemas.core import FeatureFlag


def test_feature_flag_name_is_required():
    with pytest.raises(ValidationError, match="field required"):
        FeatureFlag()


def test_feature_flag_accepts_dict_for_data_field():
    flag = FeatureFlag(name="feature", is_enabled=True, data={"field": True})
    assert (
        flag.json()
        == '{"name": "feature", "is_enabled": true, "data": {"field": true}}'
    )


def test_feature_flag_parses_dict():
    flag_dict = {
        "name": "feature",
        "is_enabled": True,
        "data": {"thing": 1},
    }
    flag = FeatureFlag.parse_obj(flag_dict)
    assert flag.data["thing"] == 1


def test_feature_flag_parses_json_object_for_data_field():
    raw_json = json.dumps(
        {
            "name": "feature",
            "is_enabled": True,
            "data": {"thing": 1},
        }
    )
    flag = FeatureFlag.parse_raw(raw_json)
    assert flag.data["thing"] == 1


def test_feature_flag_rejects_non_dict_data_field():
    with pytest.raises(ValidationError, match="value is not a valid dict"):
        FeatureFlag(name="feature", is_enabled=True, data=False)


def test_feature_flag_rejects_raw_data_field_if_not_a_json_object():
    with pytest.raises(ValidationError, match="value is not a valid dict"):
        # "data" should be a JSON object here
        FeatureFlag.parse_raw('{"name": "test", "is_enabled": true, "data": true}')
