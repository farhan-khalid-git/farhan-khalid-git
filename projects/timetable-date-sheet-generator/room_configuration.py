from __future__ import annotations

import re
import unicodedata
from typing import Any


DEFAULT_ROOMS = [
    {"name": "AGRI-1.34", "type": "classroom"},
    {"name": "AGRI-1.36", "type": "classroom"},
    {"name": "Agronomy Library", "type": "overflow"},
]


def normalize_rooms(rooms: Any) -> list[dict[str, str]]:
    if not isinstance(rooms, list):
        raise ValueError("Rooms must be a list of room names.")
    unique = {}
    for room in rooms:
        if isinstance(room, str):
            room = {"name": room, "type": "classroom"}
        if not isinstance(room, dict) or not isinstance(room.get("name"), str):
            raise ValueError("Each room must have a name.")
        name = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", room["name"])).strip()
        kind = room.get("type", "classroom")
        if kind not in {"classroom", "overflow"}:
            raise ValueError("Room type must be classroom or overflow.")
        if not name or len(name) > 80:
            raise ValueError("Room names must contain between 1 and 80 characters.")
        if name.casefold() == "lab/field":
            raise ValueError("Lab/Field is reserved for practical classes. Enter a different room name.")
        key = name.casefold()
        if key in unique and unique[key]["type"] != kind:
            raise ValueError(f"{name} cannot be both a classroom and an overflow room.")
        unique.setdefault(key, {"name": name, "type": kind})
    if not unique:
        raise ValueError("Add at least one room before generating a timetable or date sheet.")
    return list(unique.values())


def resolve_rooms(options: dict[str, Any]) -> list[dict[str, str]]:
    if "rooms" in options:
        return normalize_rooms(options["rooms"])
    return normalize_rooms([
        {"name": options.get("roomOne") or options.get("bscRoom") or DEFAULT_ROOMS[0]["name"], "type": "classroom"},
        {"name": options.get("roomTwo") or DEFAULT_ROOMS[1]["name"], "type": "classroom"},
        {"name": options.get("libraryRoom") or options.get("mscRoom") or DEFAULT_ROOMS[2]["name"], "type": "overflow"},
    ])


def room_candidates_for_group(group: str, rooms: list[dict[str, str]]) -> list[str]:
    classrooms = [room["name"] for room in rooms if room["type"] == "classroom"]
    overflow = [room["name"] for room in rooms if room["type"] == "overflow"]
    if not classrooms:
        return overflow
    preferred = classrooms[0 if group in {"5th", "6th"} else min(1, len(classrooms) - 1)]
    return [preferred] + [name for name in classrooms if name != preferred] + overflow


def unique_room_name(name: str, used: set[str], *, sheet: bool = False) -> str:
    base = re.sub(r"[\[\]:*?/\\]", "_", name).strip("'") if sheet else re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_")
    base = base or "Room"
    limit = 31 if sheet else 100
    candidate = base[:limit]
    number = 2
    while candidate.casefold() in used:
        suffix = f"_{number}"
        candidate = base[:limit - len(suffix)] + suffix
        number += 1
    used.add(candidate.casefold())
    return candidate
