from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class PipedriveApiPagination:
    start: int
    limit: int
    more_itens_in_collection: bool
    next_start: int

    @staticmethod
    def from_dict(data: Dict) -> "PipedriveApiPagination":
        return PipedriveApiPagination(
            start=data.get("start", 0),
            limit=data.get("limit", 0),
            more_itens_in_collection=data.get("more_itens_in_collection", False),
            next_start=data.get("next_start", 0),
        )

    def to_dict(self):
        return {
            "start": self.start,
            "limit": self.limit,
            "more_itens_in_collection": self.more_itens_in_collection,
            "next_start": self.next_start,
        }


@dataclass
class PipedriveApiAditionalDataV1:
    pagination: PipedriveApiPagination

    @staticmethod
    def from_dict(data: Dict) -> "PipedriveApiAditionalDataV1":
        return PipedriveApiAditionalDataV1(
            pagination=PipedriveApiPagination.from_dict(data.get("pagination", {}))
        )

    def to_dict(self) -> Dict:
        return {"pagination": self.pagination.to_dict()}


@dataclass
class PipedriveApiAditionalDataV2:
    next_cursor: str

    @staticmethod
    def from_dict(data: Dict) -> "PipedriveApiAditionalDataV2":
        if "next_cursor" not in data:
            raise Exception("Missing required response param: next_cursor")

        return PipedriveApiAditionalDataV2(next_cursor=data["next_cursor"])

    def to_dict(self) -> Dict:
        return {"next_cursor": self.next_cursor}


@dataclass
class ApiResponse:
    success: bool
    data: Union[Dict, List[Dict]]
    aditional_data: Union[PipedriveApiAditionalDataV1, PipedriveApiAditionalDataV2]

    @property
    def next_pagination_params(self) -> Dict:
        if isinstance(self.aditional_data, PipedriveApiAditionalDataV1):
            return {"start": self.aditional_data.pagination.next_start}

        elif isinstance(self.aditional_data, PipedriveApiAditionalDataV2):
            return {"cursor": self.aditional_data.next_cursor}

        else:
            return {"start": 0}
