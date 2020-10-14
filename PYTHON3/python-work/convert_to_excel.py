
import xlsxwriter


def publisher(dict_data,month):

    # Create a workbook and add a worksheet.
    file_name = 'Persnol Info :'+month+'.xlsx'
    workbook = xlsxwriter.Workbook('output/'+file_name)
    worksheet = workbook.add_worksheet()  

    row = 1
    col = 0
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})


    # Header
    worksheet.write('A1', 'KEY', bold)
    worksheet.write('B1', 'NAME', bold)
    worksheet.write('C1', 'AGE', bold)
    worksheet.write('D1', 'SEX', bold)
    worksheet.write('E1', 'ADDRESS', bold)
    worksheet.write('F1', 'PHONE', bold)

    try:  
        # Iterate over the data and write it out row by row.
        for  data in dict_data:
            worksheet.write(row, col,data)
            worksheet.write(row, col + 1, dict_data[data]['name'])
            worksheet.write(row, col + 2, dict_data[data]['age'])
            worksheet.write(row, col + 3, dict_data[data]['sex'])
            worksheet.write(row, col + 4, dict_data[data]['address'])
            worksheet.write(row, col + 5, dict_data[data]['phone'])
           
            row = row + 1
            col = 0

        workbook.close()
        print('Data Published Successfully.\n')

        #we can find sum avg ..so on
    except:
        print('Error in  Publisher :',dict_data)


dict_data = { 'key1': {'name': 'value_1','age': 'value_1','sex': 'value_1','address': 'value_1','phone': 'value_1'},
                'key2':{'name': 'value_1','age': 'value_1','sex': 'value_1','address': 'value_1','phone': 'value_1'}}
month = 'october'

publisher(dict_data,month)

