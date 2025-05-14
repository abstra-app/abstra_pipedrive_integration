from typing import Callable, Dict, List, Optional
from pipedrive_api.pipedrive_api import PipedriveApi

from models.activities import Activity


class ActivityInterface:
    """
    Interface for interacting with the Activity data.
    """

    pipedrive_api: PipedriveApi

    def __init__(self, pipedrive_api: PipedriveApi):
        self.pipedrive_api = pipedrive_api

    def get_all(
        self,
        *,
        query_params: Optional[Dict] = None,
        filter_function: Optional[Callable[[Activity], bool]] = None,
    ) -> List[Activity]:
        """
        Retrieve all activities from Pipedrive and return them as a list of Activity objects.
        """

        retrieved_objs: List[Activity] = []
        query_params = query_params or {}

        data_bunch = self.pipedrive_api.get("activities", query_params=query_params)

        for data_point in data_bunch:
            obj_instance = Activity.from_dict(data_point)

            if filter_function is None or filter_function(obj_instance):
                retrieved_objs.append(obj_instance)

        return retrieved_objs
