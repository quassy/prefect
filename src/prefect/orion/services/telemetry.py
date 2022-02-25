"""
The Telemetry service.
"""

import asyncio
import os
from uuid import uuid4

import httpx
import pendulum

import prefect
from prefect.orion.services.loop_service import LoopService


class Telemetry(LoopService):
    """
    This service sends basic telemetry back to Prefect
    """

    def __init__(self):
        super().__init__(loop_seconds=600)
        self.session_id = str(uuid4())
        self.session_start_timestamp = pendulum.now().to_iso8601_string()
        self.telemetry_environment = os.environ.get(
            "PREFECT_ORION_TELEMETRY_ENVIRONMENT", "production"
        )

    async def run_once(self):
        """
        Sends a heartbeat to the sens-o-matic
        """
        from prefect.orion.api.server import ORION_API_VERSION

        async with httpx.AsyncClient() as client:
            result = await client.post(
                "https://sens-o-matic.prefect.io/",
                json={
                    "source": "prefect_server",
                    "type": "orion_heartbeat",
                    "payload": {
                        "environment": self.telemetry_environment,
                        "api_version": ORION_API_VERSION,
                        "prefect_version": prefect.__version__,
                        "session_id": self.session_id,
                        "session_start_timestamp": self.session_start_timestamp,
                    },
                },
                headers={
                    "x-prefect-event": "prefect_server",
                },
            )
            self.logger.debug(f"Telemetry request result: {result.json()}")


if __name__ == "__main__":
    asyncio.run(Telemetry().start())
