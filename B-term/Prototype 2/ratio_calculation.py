
import xlsxwriter


def main():

    workbook = xlsxwriter.Workbook('Ratio_Calculation.xlsx')
    worksheet = workbook.add_worksheet()

    ratio_format = workbook.add_format({'num_format': '0.####'})
    teeth_format = workbook.add_format({'num_format': '##'})
    od_format = workbook.add_format({'num_format': '##'})
    pd_format = workbook.add_format({'num_format': '0.####'})

    worksheet.write('A1', 'OD_INTER')
    worksheet.write('B1', 'OD_FINGER')
    worksheet.write('C1', 'OD_TOP')
    worksheet.write('D1', 'OD_DRIVE')
    worksheet.write('E1', 'NO_TEETH_DRIVE_GEAR')
    worksheet.write('F1', 'NO_TEETH_TOP_GEAR',)
    worksheet.write('G1', 'NO_TEETH_FINGER_GEAR')
    worksheet.write('H1', 'NO_TEETH_INTERMEDIATE_GEAR')
    worksheet.write('I1', 'RATIO' )
    worksheet.write('J1', 'PD_INTERMEDIATE')
    worksheet.write('K1', 'PD_DRIVE')
    worksheet.write('L1', 'PD_TOP_GEAR')
    worksheet.write('M1', 'PD_FINGER_GEAR')

    smallest_ratio = 0.35
    row = 1

    for od_intermediate_gear in range(15, 22, 1):
        for od_finger_gear in range(35, 42, 1):
            for od_top_gear in range(28, 40, 1):
                for od_drive_gear in range(27, 35, 1):
                    for intermediate_gear in range(10, 30, 1):
                        for finger_gear in range(10, 30, 1):
                            for top_gear in range(10, 30, 1):
                                for drive_gear in range(10, 30, 1):
                                    ratio = (drive_gear / top_gear) * (intermediate_gear / finger_gear)
                                    pd_intermediate_gear = (intermediate_gear + 2) / od_intermediate_gear
                                    pd_drive_gear = (drive_gear + 2) / od_drive_gear
                                    pd_top_gear = (top_gear + 2) / od_top_gear
                                    pd_finger_gear = (finger_gear + 2) / od_finger_gear

                                    col = 0

                                    if (pd_top_gear * 0.995) <= pd_drive_gear <= (pd_top_gear * 1.005) or (pd_drive_gear * 0.995) <= pd_top_gear <= (pd_drive_gear * 1.005):
                                            if (pd_finger_gear * 0.995) <= pd_intermediate_gear <= (pd_finger_gear * 1.005) or (pd_intermediate_gear * 0.995) <= pd_finger_gear <= (pd_intermediate_gear * 1.005):
                                                if ratio <= 0.5:
                                                    worksheet.write_number(row, col, od_intermediate_gear, od_format)
                                                    worksheet.write_number(row, col + 1, od_finger_gear, od_format)
                                                    worksheet.write_number(row, col + 2, od_top_gear, od_format)
                                                    worksheet.write_number(row, col + 3, od_drive_gear, od_format)
                                                    worksheet.write_number(row, col + 4, drive_gear, teeth_format)
                                                    worksheet.write_number(row, col + 5, top_gear, teeth_format)
                                                    worksheet.write_number(row, col + 6, finger_gear, teeth_format)
                                                    worksheet.write_number(row, col + 7, intermediate_gear, teeth_format)
                                                    worksheet.write_number(row, col + 8, ratio, ratio_format)
                                                    worksheet.write_number(row, col + 9, pd_intermediate_gear, pd_format)
                                                    worksheet.write_number(row, col + 10, pd_drive_gear, pd_format)
                                                    worksheet.write_number(row, col + 11, pd_top_gear, pd_format)
                                                    worksheet.write_number(row, col + 12, pd_finger_gear, pd_format)

                                                    row += 1

                                                if ratio < smallest_ratio:
                                                    smallest_ratio = ratio

    worksheet.write(row + 2, 0, 'Smallest ratio')
    worksheet.write_number(row + 2, 1, smallest_ratio)

    workbook.close()


if __name__ == "__main__":
    main()