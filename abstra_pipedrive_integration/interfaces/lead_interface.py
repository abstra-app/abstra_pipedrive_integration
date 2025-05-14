from typing import Callable, Dict, List, Optional
from pipedrive_api.pipedrive_api import PipedriveApi

from models.leads import Lead


class LeadInterface:
    """
    Interface for interacting with the Lead data.
    """

    pipedrive_api: PipedriveApi

    def __init__(self, pipedrive_api: PipedriveApi):
        self.pipedrive_api = pipedrive_api

    def get_all(
        self,
        *,
        query_params: Optional[Dict] = None,
        filter_function: Optional[Callable[[Lead], bool]] = None,
    ) -> List[Lead]:
        """
        Retrieve all activities from Pipedrive and return them as a list of Lead objects.
        """

        retrieved_objs: List[Lead] = []
        query_params = query_params or {}

        data_bunch = self.pipedrive_api.get(
                "leads", 
                query_params=query_params,
                version=1
        )

        for data_point in data_bunch:
            obj_instance = Lead.from_dict(data_point)

            if filter_function is None or filter_function(obj_instance):
                retrieved_objs.append(obj_instance)

        return retrieved_objs
