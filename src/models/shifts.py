import datetime

from pydantic import BaseModel

from enums import ShiftType
from models.car_washes import CarWash
from models.staff import Staff, StaffIdAndName

__all__ = (
    'ShiftFinishResult',
    'ShiftsConfirmation',
    'Shift',
    'ShiftRegularCreateResult',
    'ShiftListItem',
    'ShiftListPage',
    'DirectShiftWebAppData',
    'SpecificShiftPickResult',
    'ShiftWithCarWashAndStaff',
    'ShiftFinishCarWashSummary',
    'ShiftExtraCreateResult',
    'ShiftTestCreateResult',
    'ShiftIdAndDate',
    'StaffWithoutShifts',
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
    trunk_vacuum_count: int


class ShiftFinishResult(BaseModel):
    shift_id: int
    is_first_shift: bool
    staff_id: int
    staff_full_name: str
    car_washes: list[ShiftFinishCarWashSummary]
    finish_photo_file_ids: list[str]


class ShiftsConfirmation(BaseModel):
    date: datetime.date
    staff_list: list[StaffIdAndName]


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


class ShiftIdAndDate(BaseModel):
    id: int
    date: datetime.date


class ShiftRegularCreateResult(BaseModel):
    staff_id: int
    staff_full_name: str
    shifts: list[ShiftIdAndDate]


class ShiftExtraCreateResult(BaseModel):
    staff_id: int
    staff_full_name: str
    shift_id: int
    shift_date: datetime.date


class ShiftTestCreateResult(BaseModel):
    staff_id: int
    staff_full_name: str
    shift_id: int
    shift_date: datetime.date


class ShiftListItem(BaseModel):
    id: int
    date: datetime.date
    car_wash_id: int | None
    car_wash_name: str | None
    staff_id: int | None
    staff_full_name: str | None
    started_at: datetime.datetime | None
    finished_at: datetime.datetime | None
    rejected_at: datetime.datetime | None
    created_at: datetime.datetime
    type: ShiftType


class ShiftListPage(BaseModel):
    shifts: list[ShiftListItem]
    is_end_of_list_reached: bool


class DirectShiftWebAppData(BaseModel):
    staff_ids: set[int]
    date: datetime.date


class SpecificShiftPickResult(BaseModel):
    staff_id: int
    shift_id: int


class StaffWithoutShifts(BaseModel):
    month: int
    year: int
    staff_list: list[StaffIdAndName]
