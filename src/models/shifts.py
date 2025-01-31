import datetime

from pydantic import BaseModel

from models.car_washes import CarWash
from models.staff import Staff

__all__ = (
    'ShiftFinishResult',
    'ShiftsConfirmation',
    'Shift',
    'ShiftCreateResult',
    'ShiftListItem',
    'ShiftListPage',
    'DirectShiftWebAppData',
    'SpecificShiftPickResult',
    'ShiftWithCarWashAndStaff',
    'ShiftFinishCarWashSummary',
)


class ShiftFinishCarWashSummary(BaseModel):
    car_wash_id: int
    car_wash_name: str
    comfort_cars_count: int
    business_cars_count: int
    vans_count: int
    planned_cars_count: int
    urgent_cars_count: int
    dry_cleaning_count: int
    total_cars_count: int
    refilled_cars_count: int
    not_refilled_cars_count: int


class ShiftFinishResult(BaseModel):
    shift_id: int
    is_first_shift: bool
    staff_id: int
    staff_full_name: str
    car_washes: list[ShiftFinishCarWashSummary]
    finish_photo_file_ids: list[str]


class ShiftsConfirmation(BaseModel):
    date: datetime.date
    staff_ids: list[int]


class Shift(BaseModel):
    id: int
    date: datetime.date
    started_at: datetime.datetime | None
    finished_at: datetime.datetime | None
    created_at: datetime.datetime
    is_test: bool
    car_wash: CarWash | None


class ShiftWithCarWashAndStaff(BaseModel):
    id: int
    date: datetime.date
    car_wash: CarWash | None
    staff: Staff
    is_started: bool
    is_finished: bool
    created_at: datetime.datetime


class ShiftCreateResult(BaseModel):
    staff_id: int
    staff_full_name: str
    dates: list[datetime.date]


class ShiftListItem(BaseModel):
    id: int
    date: datetime.date
    car_wash: CarWash | None
    staff: Staff
    is_started: bool
    is_finished: bool
    created_at: datetime.datetime


class ShiftListPage(BaseModel):
    shifts: list[ShiftListItem]
    is_end_of_list_reached: bool


class DirectShiftWebAppData(BaseModel):
    staff_ids: set[int]
    date: datetime.date


class SpecificShiftPickResult(BaseModel):
    staff_id: int
    shift_id: int
