from typing import Callable, List, Optional, Dict
from pipedrive_api.pipedrive_api import PipedriveApi
from models.deals import Deal


class DealInterface:
    """
    Interface for interacting with the Deal data.
    """

    pipedrive_api: PipedriveApi

    def __init__(
        self,
        pipedrive_api: PipedriveApi,
    ):
        self.pipedrive_api = pipedrive_api

    def get_all(
        self,
        *,
        query_params: Optional[Dict] = None,
        filter_function: Optional[Callable[[Deal], bool]] = None,
    ) -> List[Deal]:
        """
        Retrieve all deals from Pipedrive and return them as a list of Deal objects.
        """

        retrieved_objs: List[Deal] = []
        query_params = query_params or {}

        data_bunch = self.pipedrive_api.get("deals", query_params=query_params)

        for data_point in data_bunch:
            obj_instance = Deal.from_dict(
                data_point
            )

            if filter_function is None or filter_function(obj_instance):
                retrieved_objs.append(obj_instance)

        return retrieved_objs
