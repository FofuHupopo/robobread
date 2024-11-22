from pydantic import BaseModel


class VendingMachine(BaseModel):
    id: int
    address: str
    name: str
    ip_address: str
    last_sync_date: str
    status: str


class VendingMachineSync(BaseModel):
    vending_machine: VendingMachine
    is_active: bool
