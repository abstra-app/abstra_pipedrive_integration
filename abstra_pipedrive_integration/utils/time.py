from datetime import datetime, date, time
from typing import Union, Optional
from dateutil import parser
from dateutil.parser import ParserError


def time_string_to_datetime(time_string: Optional[str]) -> Optional[datetime]:
    """
    Convert a time string to a datetime object in a more fail-safe manner.

    1. Return None immediately if the input is None or not a string.
    2. Try parsing the time string using known datetime templates.
    3. If none of the templates work, fall back to the dateutil parser.
    4. Return None if all attempts fail.
    """

    if not time_string or not isinstance(time_string, str):
        return None

    try:
        return parser.parse(time_string)
    except (ParserError, ValueError):
        return None


def time_string_to_date(time_string: Union[str, None]) -> Union[date, None]:
    """
    Convert a time string to a date object.
    """

    if not time_string or not isinstance(time_string, str):
        return None

    try:
        return datetime.strptime(time_string, "%Y-%m-%d").date()
    except ValueError:
        return None


def time_string_to_time(time_string: Union[str, None]) -> Union[time, None]:
    """
    Convert a time string to a time object.
    """

    if not time_string or not isinstance(time_string, str):
        return None

    try:
        return datetime.strptime(time_string, "%H:%M:%S").time()
    except ValueError:
        return None


def datetime_obj_to_iso_format(
    dt: Optional[Union[datetime, date, time]],
) -> Optional[str]:
    """
    Convert a datetime object to ISO format.
    """

    if dt is None or not isinstance(dt, (datetime, date, time)):
        return None

    return dt.isoformat()
