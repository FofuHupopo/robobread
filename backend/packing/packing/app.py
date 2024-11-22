import json

from flask import Flask, render_template, request
from datetime import datetime, timedelta, timezone, UTC

from .services import ProductService, AccountingService


app = Flask(__name__)


def parse_timedelta_string(time_string: str):
    parts = time_string.split()
    
    if len(parts) == 2:
        days = int(parts[0])
        time_part = parts[1]
    elif len(parts) == 1:
        days = 0
        time_part = parts[0]
    else:
        raise ValueError("Неверный формат строки")

    hours, minutes, seconds = map(int, time_part.split(':'))
    
    return timedelta(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )


def get_vending_machine(vending_machine_id: int):
    vending_machines_data = AccountingService.get_vending_machines()

    for vending_machine_data in vending_machines_data:
        vending_machine = vending_machine_data["vending_machine"]
        is_active = vending_machine_data["is_active"]

        if not is_active:
            continue

        if vending_machine_id == vending_machine.get("id"):
            return vending_machine
    
    return None


def get_cells_from_vending_machine(ip_address: str):
    products = ProductService(ip_address).get_products()

    cells = []
    
    for product in products:
        product_cells = product['cells']

        for cell in product_cells:
            needs_to_remove = 0

            for cell_product in cell['products']:
                upload_date_offseted =  datetime.fromisoformat(
                    cell_product["upload_date"]
                )

                offset = upload_date_offseted.utcoffset()

                upload_date = (upload_date_offseted - offset).replace(tzinfo=None)

                expiration_date = parse_timedelta_string(
                    cell_product["expiration_date"]
                )

                now = datetime.utcnow()

                if upload_date + expiration_date < now:
                    needs_to_remove += 1

            cells.append({
                'id': cell["id"],
                'number': str(cell['number']).zfill(3),
                'name': product['name'],
                'count': cell['count'],
                'max_count': cell['max_count'],
                'needs_to_remove': needs_to_remove,
            })

    cells = sorted(cells, key=lambda x: x['number'])

    return cells


@app.route("/packing/<int:vending_machine_id>")
def packing(vending_machine_id: int):
    vending_machine = get_vending_machine(vending_machine_id)

    cells = get_cells_from_vending_machine(vending_machine["ip_address"])

    return render_template('packing.html', cells=cells)


@app.route('/packing-submit', methods=['POST'])
def packing_submit():
    items = json.loads(request.data).get('items', [])
    vending_machine_id = int(json.loads(request.data).get('vending_machine_id', "0"))

    vending_machine = get_vending_machine(vending_machine_id)

    try:
        packing_result: dict = ProductService(vending_machine["ip_address"]).add_packing(items)

        AccountingService.add_packing({
            **packing_result,
            "vending_machine_id": vending_machine_id,
            "packing_date": str(datetime.now(UTC)),
        })

        return {"message": "success"}, 200
    except ValueError as e:
        return {"message": str(e)}, 400
