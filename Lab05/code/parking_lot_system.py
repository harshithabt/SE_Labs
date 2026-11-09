"""Parking lot management demonstration used for Lab 5 static analysis."""

import hashlib
import json
import math
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, TypedDict


class ParkingSlot(TypedDict):
    """Stored information for one parking slot."""

    plate: str
    hours: int
    rate: float
    is_occupied: bool


@dataclass
class ParkingLotState:
    """Mutable state that belongs to the parking lot."""

    total_collections: float = 0.0


PARKING_SLOTS: dict[str, ParkingSlot] = {
    "P01": {
        "plate": "KA01AB1234", "hours": 2, "rate": 20.0, "is_occupied": True
    },
    "P02": {
        "plate": "TN07CD5678", "hours": 0, "rate": 20.0, "is_occupied": False
    },
    "P03": {
        "plate": "MH02EF9012", "hours": 4, "rate": 30.0, "is_occupied": True
    },
}
PARKING_STATE = ParkingLotState()


def park_vehicle(
    slot_id: str,
    plate_no: str,
    hours_booked: int = 1,
    entry_logs: list[str] | None = None,
) -> bool:
    """Park a vehicle in a vacant slot and record its charge."""
    if entry_logs is None:
        entry_logs = []
    if (
        slot_id not in PARKING_SLOTS
        or PARKING_SLOTS[slot_id]["is_occupied"]
    ):
        return False
    invalid_plate = not isinstance(plate_no, str) or not plate_no.strip()
    if invalid_plate or hours_booked <= 0:
        raise ValueError(
            "A valid plate number and positive booking duration are required."
        )

    slot = PARKING_SLOTS[slot_id]
    slot["plate"] = plate_no.strip().upper()
    slot["hours"] = hours_booked
    slot["is_occupied"] = True
    charge = slot["rate"] * hours_booked
    PARKING_STATE.total_collections += charge
    entry_logs.append(
        f"Vehicle {slot['plate']} parked at slot {slot_id} "
        f"for {hours_booked} hours; "
        f"total charge: {charge:.2f}"
    )
    return True


def release_slot(slot_id: str) -> bool:
    """Release an occupied slot; return False when the slot does not exist."""
    slot = PARKING_SLOTS.get(slot_id)
    if slot is None:
        return False
    slot["is_occupied"] = False
    slot["plate"] = ""
    slot["hours"] = 0
    return True


def check_slot_availability(slot_id: str) -> bool:
    """Return True when a known slot is vacant."""
    slot = PARKING_SLOTS.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(
    slot_id: str, surge_multiplier: float = 1.0
) -> float:
    """Calculate a fee with a caller-provided, validated surge multiplier."""
    if slot_id not in PARKING_SLOTS:
        raise ValueError(f"Unknown parking slot: {slot_id}")
    if not isinstance(surge_multiplier, (int, float)) or not math.isfinite(
        surge_multiplier
    ):
        raise ValueError("Surge multiplier must be a finite number.")
    if surge_multiplier < 0:
        raise ValueError("Surge multiplier cannot be negative.")
    slot = PARKING_SLOTS[slot_id]
    return slot["rate"] * slot["hours"] * surge_multiplier


def generate_vehicle_hash(plate_no: str) -> str:
    """Return a SHA-256 digest for a vehicle plate identifier."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin() -> int:
    """Generate a four-digit PIN using a cryptographically secure source."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename: str = "parking_manifest.json") -> Path:
    """Export the parking state as JSON without invoking a shell."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as manifest_file:
        json.dump(PARKING_SLOTS, manifest_file, indent=2)
    return output_path


def get_available_summary(
    slots: Mapping[str, ParkingSlot] | None = None,
) -> int:
    """Count vacant slots in the supplied mapping or the global parking lot."""
    if slots is None:
        slots = PARKING_SLOTS
    return sum(not details["is_occupied"] for details in slots.values())


def get_total_collections() -> float:
    """Return the total charges collected by this parking lot."""
    return PARKING_STATE.total_collections


def main() -> None:
    """Run a small parking-lot demonstration."""
    barrier_key = "[configured securely outside source code]"
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")
    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.5))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())
    print("Parking manifest exported to:", export_parking_manifest())
    print("Vacant slots:", get_available_summary())
    print("Barrier Key configured:", bool(barrier_key))


if __name__ == "__main__":
    main()
