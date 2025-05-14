from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, date
from utils.time import (
    time_string_to_datetime,
    time_string_to_date,
    datetime_obj_to_iso_format,
)


@dataclass
class Deal:
    id: int
    title: Optional[str]
    creator_user_id: Optional[int]
    value: Optional[float]
    person_id: Optional[int]
    org_id: Optional[int]
    stage_id: Optional[int]
    currency: Optional[str]
    add_time: Optional[datetime]
    update_time: Optional[datetime]
    status: Optional[str]
    probability: Optional[str]
    lost_reason: Optional[str]
    visible_to: Optional[int]
    close_time: Optional[datetime]
    pipeline_id: Optional[int]
    won_time: Optional[datetime]
    lost_time: Optional[datetime]
    stage_change_time: Optional[datetime]
    local_won_date: Optional[date]
    local_lost_date: Optional[date]
    local_close_date: Optional[date]
    expected_close_date: Optional[date]
    owner_id: Optional[int]
    label_ids: Optional[List[int]]
    is_deleted: Optional[bool]
    origin: Optional[str]
    origin_id: Optional[str]
    channel: Optional[str]
    channel_id: Optional[str]
    acv: Optional[str]
    arr: Optional[str]
    mrr: Optional[str]
    is_archived: Optional[bool]
    archive_time: Optional[datetime]
    custom_fields: Optional[Dict]

    @staticmethod
    def from_dict(data: Dict) -> "Deal":
        """
        Create a Deal instance from a dictionary.
        """

        if "id" not in data:
            raise ValueError("Missing 'id' key in the data dictionary.")

        return Deal(
            id=data["id"],
            title=data.get("title"),
            creator_user_id=data.get("creator_user_id"),
            value=data.get("value"),
            person_id=data.get("person_id"),
            org_id=data.get("org_id"),
            stage_id=data.get("stage_id"),
            currency=data.get("currency"),
            add_time=time_string_to_datetime(data.get("add_time")),
            update_time=time_string_to_datetime(data.get("update_time")),
            status=data.get("status"),
            probability=data.get("probability"),
            lost_reason=data.get("lost_reason"),
            visible_to=data.get("visible_to"),
            close_time=time_string_to_datetime(data.get("close_time")),
            pipeline_id=data.get("pipeline_id"),
            won_time=time_string_to_datetime(data.get("won_time")),
            lost_time=time_string_to_datetime(data.get("lost_time")),
            stage_change_time=time_string_to_datetime(data.get("stage_change_time")),
            local_won_date=time_string_to_date(data.get("local_won_date")),
            local_lost_date=time_string_to_date(data.get("local_lost_date")),
            local_close_date=time_string_to_date(data.get("local_close_date")),
            expected_close_date=time_string_to_date(data.get("expected_close_date")),
            owner_id=data.get("owner_id"),
            label_ids=data.get("label_ids"),
            is_deleted=data.get("is_deleted"),
            origin=data.get("origin"),
            origin_id=data.get("origin_id"),
            channel=data.get("channel"),
            channel_id=data.get("channel_id"),
            acv=data.get("acv"),
            arr=data.get("arr"),
            mrr=data.get("mrr"),
            is_archived=data.get("is_archived"),
            archive_time=time_string_to_datetime(data.get("archive_time")),
            custom_fields=data.get("custom_fields", {}),
        )

    def to_dict(self) -> Dict:
        """
        Convert the Deal instance to a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "creator_user_id": self.creator_user_id,
            "value": self.value,
            "person_id": self.person_id,
            "org_id": self.org_id,
            "stage_id": self.stage_id,
            "currency": self.currency,
            "add_time": datetime_obj_to_iso_format(self.add_time),
            "update_time": datetime_obj_to_iso_format(self.update_time),
            "status": self.status,
            "probability": self.probability,
            "lost_reason": self.lost_reason,
            "visible_to": self.visible_to,
            "close_time": datetime_obj_to_iso_format(self.close_time),
            "pipeline_id": self.pipeline_id,
            "won_time": datetime_obj_to_iso_format(self.won_time),
            "lost_time": datetime_obj_to_iso_format(self.lost_time),
            "stage_change_time": datetime_obj_to_iso_format(self.stage_change_time),
            "local_won_date": datetime_obj_to_iso_format(self.local_won_date),
            "local_lost_date": datetime_obj_to_iso_format(self.local_lost_date),
            "local_close_date": datetime_obj_to_iso_format(self.local_close_date),
            "expected_close_date": datetime_obj_to_iso_format(self.expected_close_date),
            "owner_id": self.owner_id,
            "label_ids": self.label_ids,
            "is_deleted": self.is_deleted,
            "origin": self.origin,
            "origin_id": self.origin_id,
            "channel": self.channel,
            "channel_id": self.channel_id,
            "acv": self.acv,
            "arr": self.arr,
            "mrr": self.mrr,
            "is_archived": self.is_archived,
            "archive_time": datetime_obj_to_iso_format(self.archive_time),
            "custom_fields": self.custom_fields
            if self.custom_fields
            else {},
        }
