from typing import List

from prefect.orion import schemas
from prefect.orion.utilities.server import OrionRouter
from prefect.utilities.feature_flags import list_feature_flags

router = OrionRouter(prefix="/feature_flags", tags=["Feature Flags"])


@router.get("/", include_in_schema=False)
async def read_feature_flags() -> List[schemas.core.FeatureFlag]:
    return [
        schemas.core.FeatureFlag(
            name=flag.name, is_enabled=flag.is_enabled(), data=flag.get_meta()
        )
        for flag in list_feature_flags()
    ]
