from flask import Flask, render_template, request
import json

from .services import ProductService

app = Flask(__name__)


@app.route('/packing')
def packing():
    products = ProductService.get_products()

    cells = []
    
    for product in products:
        cells_ = product['cells']

        for cell_ in cells_:
            cells.append({
                'id': cell_["id"],
                'number': str(cell_['number']).zfill(3),
                'name': product['name'],
                'count': cell_['count'],
                'max_count': cell_['max_count'],
            })

    cells = sorted(cells, key=lambda x: x['number'])

    return render_template('packing.html', cells=cells)


@app.route('/packing-submit', methods=['POST'])
def packing_submit():
    items = json.loads(request.data).get('items', [])

    try:
        for item in items:
            ProductService.update_cell_count(item.get('id'), item.get('count'))
        
        return {"message": "success"}, 200
    except ValueError as e:
        return {"message": str(e)}, 400
