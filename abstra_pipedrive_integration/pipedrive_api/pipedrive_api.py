from typing import List, Dict, Union
import requests
import os

from config.envconfig import EnvConfig

PIPEDRIVE_API_KEY = os.getenv("PIPEDRIVE_API_KEY")
COMPANY_DOMAIN = os.getenv("COMPANY_DOMAIN")

LIMIT = 500


class PipedriveApi:
    envconfig: EnvConfig

    def __init__(self, envconfig: EnvConfig):
        self.envconfig = envconfig

    def __compose_endpoint(
        self,
        path: str,
        *,
        version: int = 2,
        query_params: Dict = {},
    ) -> str:
        """
        Compose the endpoint URL for the Pipedrive API.
        """

        base_url = f"https://{COMPANY_DOMAIN}.pipedrive.com/api/v{version}/{path}?api_token={PIPEDRIVE_API_KEY}"

        if "limit" not in query_params:
            query_params["limit"] = LIMIT

        query_string = "&".join(
            [f"{key}={value}" for key, value in query_params.items()]
        )
        base_url += f"&{query_string}"

        return base_url

    def get(
        self,
        path: str,
        *,
        version: int = 2,
        query_params: Dict = {},
    ) -> List[Dict]:
        """
        Make a GET request to the Pipedrive API and return the response data, handling pagination automatically.
        """

        data = []
        next_start: Union[int, str, None] = None

        while True:
            if next_start is not None:
                param_key = "start" if version == 1 else "cursor"
                query_params[param_key] = next_start

            url = self.__compose_endpoint(
                path, version=version, query_params=query_params
            )
            response = requests.get(url)
            response.raise_for_status()

            response_json = response.json()

            if not response_json.get("success"):
                break

            data_chunk = response_json.get("data", [])
            data.extend(data_chunk if data_chunk else [])

            additional_data = response_json.get("additional_data", {})
            if version == 1:
                next_start = additional_data.get("pagination", {}).get("next_start")
            else:
                next_start = additional_data.get("next_cursor")

            if not next_start:
                break

        return data
