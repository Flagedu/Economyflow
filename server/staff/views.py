import csv
import xlwt
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views import View
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.db.models import Q, Sum, F
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout

from staff.staff_menu import menus

from home.models import *
from .forms import *



class StaffPermissionMixin(object):
    def has_permissions(self, request):
        return request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions(request):
            return redirect("/staff/login/")
        return super(StaffPermissionMixin, self).dispatch(
            request, *args, **kwargs)


# ─── LOGOUT ─────────────────────────────────────────────────────────────────────
def logout_request(request):
    logout(request)
    return redirect("/staff/login/")


class Login(View):
    template_name = "staff/login.html"

    def get(self, request):
        form = LoginForm()

        variables = {
            "form": form,
        }
        return render(request, self.template_name, variables)
    def post(self, request):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            login_user = form.login()
            login(request, login_user)
            return redirect("staff:dashboard")

        variables = {
            "form": form,
        }
        return render(request, self.template_name, variables)


class Dashboard(StaffPermissionMixin, View):
    template_name = "staff/dashboard/dashboard.html"
    active_menu = "dashboard"
    activate_submenu_for = "#"
    
    def get(self, request):

        variables = {
            "menus": menus,
            "active_menu": self.active_menu,
            "activate_submenu_for": self.activate_submenu_for,
        }
        
        return render(request, self.template_name, variables)


class AllUser(StaffPermissionMixin, View):
    template_name = 'staff/users/users.html'
    active_menu = "all-user"
    activate_submenu_for = "users"

    def build_query(self, request):
        company_name = request.GET.get("company")
        page = request.GET.get("page")
        start = request.GET.get("start")
        end = request.GET.get("end")

        today = date.today()

        query_string = ""
        if company_name:
            query_string += f"?company={company_name}"
        else:
            types = TypeChoice.choices
            type_length = len(types)
            if type_length > 0:
                query_string += f"?company={types[0][0]}"
            else:
                query_string += f"?company=evest"
        
        if page:
            query_string += f"&page={page}"
        
        if start:
            query_string += f"&start={start}"
        else:
            query_string += f"&start={today}"
        
        if end:
            query_string += f"&end={end}"
        else:
            query_string += f"&end={today}"        

        return query_string
    
    def get(self, request):
        query_string = self.build_query(request)

        company_name = request.GET.get("company")
        start = request.GET.get("start")
        end = request.GET.get("end")
        country = request.GET.get("country")
        if not company_name or not start or not end:
            return redirect(f"/staff/users/{query_string}")
        api_obj = ApiRegistration.objects.get(type=company_name)

        users = api_obj.members.all()

        if start and end:
            users = users.filter(date__range=[start, end])
        
        if country:
            users = users.filter(country=country)

        users_count = users.count()
        
        #pagnation
        page = request.GET.get('page', 1)
        paginator = Paginator(users, 50)

        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        index = users.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index

        page_range = list(paginator.page_range)[start_index:end_index]
        
        currently_displayed_lower = users.start_index()
        currently_displayed_upper = users.end_index()
        #end pagination
                
        variables = {
            'menus': menus,
            'active_menu': self.active_menu,
            'activate_submenu_for': self.activate_submenu_for,
            
            "users": users,
            "users_count": users_count,
            "page_range": page_range,
            "currently_displayed_lower": currently_displayed_lower,
            "currently_displayed_upper": currently_displayed_upper,
        }
        
        return render(request, self.template_name, variables)

    def export_report(self, request, queryset, company):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(company)

        writer = csv.writer(response)
        writer.writerow(["Company Name", "Campaign", "First Name", "Last Name", "Email", "Phone", "Country", "IP", "Date"])
        for q in queryset:
            writer.writerow([company, q.campaign, q.firstName, q.lastName, q.email, q.phone, q.country, q.ip, q.date])
        return response

    def export_report_as_xls(self, request, queryset, company):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(company)

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("sheet1")

        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ["Company Name", "Campaign", "First Name", "Last Name", "Email", "Phone", "Country", "IP", "Date"]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        for q in queryset:
            row_num = row_num + 1
            ws.write(row_num, 0, company, font_style)
            ws.write(row_num, 1, q.campaign, font_style)
            ws.write(row_num, 2, q.firstName, font_style)
            ws.write(row_num, 3, q.lastName, font_style)
            ws.write(row_num, 4, q.email, font_style)
            ws.write(row_num, 5, q.phone, font_style)
            ws.write(row_num, 6, q.country, font_style)
            ws.write(row_num, 7, q.ip, font_style)
            ws.write(row_num, 8, str(q.date), font_style)
        wb.save(response)
        return response

    def post(self, request):
        company_name = request.GET.get("company")
        start = request.GET.get("start")
        end = request.GET.get("end")
        country = request.GET.get("country")
        if not company_name or not start or not end:
            return redirect(f"/staff/users/{query_string}")
        api_obj = ApiRegistration.objects.get(type=company_name)

        users = api_obj.members.all()

        if start and end:
            users = users.filter(date__range=[start, end])
        
        if country:
            users = users.filter(country=country)

        if request.POST.get("download") == "download":
            return self.export_report_as_xls(request, users, company_name)

        return redirect("staff:all_user")