
from os import listdir

from xlsxwriter import Workbook

from scrapper import scrape

if __name__ == '__main__':
    workbook = Workbook('fatura.xlsx')
    worksheet = workbook.add_worksheet()
    # Headers
    worksheet.write('A1', 'produto1')
    worksheet.write('B1', 'unidade')
    worksheet.write('C1', 'grandezas_faturadas')
    worksheet.write('D1', 'valor_unitario')
    worksheet.write('E1', 'valor_total')
    worksheet.write('F1', 'base_de_calculo')
    worksheet.write('G1', 'aliquota_icms')
    worksheet.write('H1', 'produto2')
    worksheet.write('I1', 'leitura_anterior')
    worksheet.write('J1', 'leitura_anual')
    worksheet.write('K1', 'leitura_anual')
    worksheet.write('L1', 'medido')
    worksheet.write('M1', 'contratado')
    worksheet.write('N1', 'faturado')
    worksheet.write('O1', 'tarifa')
    worksheet.write('P1', 'total')

    pdfs = filter(
        lambda pdf: pdf.lower().endswith('.pdf'),
        listdir('pdfs/')
    )

    total_pdfs = 1
    index = 2
    for result in map(scrape, pdfs):
        print('PDF #{} was processed.'.format(total_pdfs))
        total_pdfs += 1
        for data in result:
            index += 1
            worksheet.write(
                'A{}'.format(index),
                data.get('produto1')
            )
            worksheet.write(
                'B{}'.format(index),
                data.get('unidade')
            )
            worksheet.write(
                'C{}'.format(index),
                data.get('grandezas_faturadas')
            )
            worksheet.write(
                'D{}'.format(index),
                data.get('valor_unitario')
            )
            worksheet.write(
                'E{}'.format(index),
                data.get('valor_total')
            )
            worksheet.write(
                'F{}'.format(index),
                data.get('base_de_calculo')
            )
            worksheet.write(
                'G{}'.format(index),
                data.get('aliquota_icms')
            )
            worksheet.write(
                'H{}'.format(index),
                data.get('produto2')
            )
            worksheet.write(
                'I{}'.format(index),
                data.get('leitura_anterior')
            )
            worksheet.write(
                'J{}'.format(index),
                data.get('leitura_anual')
            )
            worksheet.write(
                'K{}'.format(index),
                data.get('leitura_anual')
            )
            worksheet.write(
                'L{}'.format(index),
                data.get('medido')
            )
            worksheet.write(
                'M{}'.format(index),
                data.get('contratado')
            )
            worksheet.write(
                'N{}'.format(index),
                data.get('faturado')
            )
            worksheet.write(
                'O{}'.format(index),
                data.get('tarifa')
            )
            worksheet.write(
                'P{}'.format(index),
                data.get('total')
            )
    workbook.close()
