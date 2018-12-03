
from .parser import parse

DATA = [
    {
        'produto1': 'ENERGIA ELET CONSUMO',
        'unidade': 'kWh',
        'grandezas_faturadas': '15156,00',
        'valor_unitario': '0,282481',
        'valor_total': '4.281,28',
        'base_de_calculo': '4.281,28',
        'aliquota_icms': '29,00'
    }, {
        'produto1': 'ENERGIA ELET USO SISTEMA',
        'unidade': 'kWh',
        'grandezas_faturadas': '15156,00',
        'valor_unitario': '0,031669',
        'valor_total': '479,97',
        'base_de_calculo': '479,97',
        'aliquota_icms': '29,00'
    }, {
        'produto1': 'ENERGIA REAT EXCED TE',
        'unidade': 'kWh',
        'grandezas_faturadas': '777,00',
        'valor_unitario': '0,282471',
        'valor_total': '219,48',
        'base_de_calculo': '219,48',
        'aliquota_icms': '29,00'
    }, {
        'produto1': 'DEMANDA USD',
        'unidade': 'kW',
        'grandezas_faturadas': '80,54',
        'valor_unitario': '29,593866',
        'valor_total': '2.383,49',
        'base_de_calculo': '2.383,49',
        'aliquota_icms': '29,00'
    }, {
        'produto1': 'ENERGIA CONS. B.VERMELHA',
        'unidade': 'kWh',
        'grandezas_faturadas': '',
        'valor_unitario': '',
        'valor_total': '330,77',
        'base_de_calculo': '330,77',
        'aliquota_icms': '29,00'
    }, {
        'produto2': 'ENERGIA ELET CONSUMO',
        'leitura_anterior': '6805367',
        'leitura_anual': '8037601',
        'medido': '15156,00',
        'contratado': '',
        'faturado': '15156,00',
        'tarifa': '0,282481',
        'total': '4.281,28'
    }, {
        'produto2': 'ENERGIA ELET USO SISTEMA',
        'leitura_anterior': '6805367',
        'leitura_anual': '8037601',
        'medido': '15156,00',
        'contratado': '',
        'faturado': '15156,00',
        'tarifa': '0,031669',
        'total': '479,97'
    }, {
        'produto2': 'ENERGIA REAT EXCED TE',
        'leitura_anterior': '',
        'leitura_anual': '',
        'medido': '777,00',
        'contratado': '',
        'faturado': '777,00',
        'tarifa': '0,282471',
        'total': '219,48'
    }, {
        'produto2': 'DEMANDA USD',
        'leitura_anterior': '1561',
        'leitura_anual': '1637',
        'medido': '80,54',
        'contratado': '80,00',
        'faturado': '80,54',
        'tarifa': '29,593866',
        'total': '2.383,49'
    }, {
        'produto2': 'ENERGIA CONS. B.VERMELHA',
        'leitura_anterior': '',
        'leitura_anual': '',
        'medido': '',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': '330,77'
    }, {
        'produto2': 'ENERGIA ELET CONSUMO PONTA',
        'leitura_anterior': '1083757',
        'leitura_anual': '1291854',
        'medido': '2559,00',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': ''
    }, {
        'produto2': 'ENERGIA ELET CONSUMO F PONTA',
        'leitura_anterior': '5721610',
        'leitura_anual': '6745747',
        'medido': '12596,00',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': ''
    }, {
        'produto2': 'ENERGIA REAT EXCED',
        'leitura_anterior': '15886',
        'leitura_anual': '18872',
        'medido': '36,00',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': ''
    }, {
        'produto2': 'ENERGIA REAT EXCED',
        'leitura_anterior': '311949',
        'leitura_anual': '372200',
        'medido': '741,00',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': ''
    }, {
        'produto2': 'ENER.REAT.INDUTIVA',
        'leitura_anterior': '3599505',
        'leitura_anual': '4283899',
        'medido': '8418,00',
        'contratado': '',
        'faturado': '',
        'tarifa': '',
        'total': ''
    }
]


def test_parse():
    assert parse(DATA) == [{}]
