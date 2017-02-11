# -*- coding: utf-8 -*-

from hello_world import app

from flask import render_template, jsonify, request

from hello_world.helpers import unit_description, unit_conversion

@app.route('/')
def index():
    """ opisuje ścieżkę do pliku z index.html
    """
    return render_template('index.html')


@app.route('/units')
def get_units():
    """
    """
    print("HELLO", request.args['type'])

    unit_type = request.args['type']
    unit_list = []
    if unit_type == 'temperature':
        unit_list = [
          'Celsius', 'Kelvin', 'Fahrenheit', 'Rankine'
        ]
    elif unit_type == 'lenght':
        unit_list = [
          'Sążen', 'Cracow elbow', 'Foot', 'Danish rod', 'Kilometre', 'Centimeter', 'Meter'
        ]
    elif unit_type == 'measure':
        unit_list = [
          'Prussian okseft', 'Log', 'Litre', 'Mililiter'
        ]
    elif unit_type == 'money':
        unit_list = [
          'Yuan', 'Baht', 'Euro', 'American dollar', 'Yen', 'Forint', 'Złoty'
        ]
    elif unit_type == 'weight':
        unit_list = [
          'Pound', 'Cetnar', 'Kilogram', 'Stone'
        ]

    return jsonify({'unit_list': unit_list})  # return JSON

@app.route('/convert')
def convert():
    value = request.args['value']  # str
    value = float(value) if value else 0
    _from = request.args['from']  # str
    _to = request.args['to']  # str
    convert_function = unit_conversion.get(_from, {}).get(_to)

    if not convert_function:
        return jsonify({'result': None, 'desc': 'error'})  # return JSON

    return jsonify({
        'result': convert_function(value),
        'unit_from': _from,
        'unit_to': _to,
        'desc_from': unit_description[_from][_from],
        'desc_to': unit_description[_to][_to]
        # 'desc_from': unit_description[_from]
        # 'desc_to': unit_description[_to]
    })


if __name__ == '__main__':
    app.run(debug=True)
