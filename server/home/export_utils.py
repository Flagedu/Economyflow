import xlwt

from .models import ApiRegistration, Leads

def export_to_xlsx(company, start=None, end=None):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["First name", "Last name", "Email", "Phone", "Country"]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    data = ApiRegistration.objects.get(type=company)
    if start and end:
        rows = data.members.all().values_list("firstName", "lastName", "email", "phone", "country")[start:end]
    else:
        rows = data.members.all().values_list("firstName", "lastName", "email", "phone", "country")

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    if start and end:
        wb.save(f"{company}_{start}_{end}.xlsx")
    else:
        wb.save(f"{company}.xlsx")


def export_leads():
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Leads")

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["Name", "Email", "Phone", "Country", "Campaign name"]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Leads.objects.all().values_list("name", "email", "phone", "country", "app_name")

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(f"Leads.xlsx")
