from typing import Callable, List, Optional, Dict
from pipedrive_api.pipedrive_api import PipedriveApi
from models.organizations import Organization


class OrganizationInterface:
    """
    Interface for interacting with the Organization data.
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
        filter_function: Optional[Callable[[Organization], bool]] = None,
    ) -> List[Organization]:
        """
        Retrieve all organizations from Pipedrive and return them as a list of Organization objects.
        """

        retrieved_objs: List[Organization] = []
        query_params = query_params or {}

        data_bunch = self.pipedrive_api.get("organizations", query_params=query_params)

        for data_point in data_bunch:
            obj_instance = Organization.from_dict(
                data_point
            )

            if filter_function is None or filter_function(obj_instance):
                retrieved_objs.append(obj_instance)

        return retrieved_objs
