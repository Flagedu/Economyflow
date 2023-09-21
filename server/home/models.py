from turtle import st
import requests
import simplejson
import json

from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from modelcluster.fields import ParentalKey
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import RichTextBlock
from wagtail.api import APIField

from django.http import JsonResponse


from .blocks import *
from .forms import *
from .utils import get_country_code_from_ip


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class HomePage(Page):
    template = "home/home_page.html"

    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_image"),
            ],
            heading="Body",
        ),
    ]

    parent_page_types = []
    subpage_types = [
        "CollectionPage",
        "EvestPage",
        "Trade360",
        "LegacyFxPage",
        "IngotBrokerPage",
        "AlvexoPage",
        "TradersGCCPage",
        "DemoPage",
        "CapitalPage",
        "AvaPage",
    ]


class CollectionPage(Page):
    parent_page_types = [
        "HomePage",
    ]
    subpage_types = [
        "EvestPage",
        "Trade360",
        "LegacyFxPage",
        "IngotBrokerPage",
        "AlvexoPage",
        "TradersGCCPage",
        "DemoPage",
        "CapitalPage",
        "AvaPage",
        "CommonRedirectPage"
    ]


class EvestTeamplateChoice(models.TextChoices):
    RAMADAN = "ramadan", "Ramadan"
    ISLAMIC = "islamic", "Islamic"
    EF05 = "ef05", "Ef05"
    EF06 = "ef06", "Ef06"
    BTCNEWS_1 = "btcnews1", "BTCNews1"
    BTCNEWS_2 = "btcnews2", "BTCNews2"
    BTCNEWS_3 = "btcnews3", "BTCNews3"
    YOUTUBE = "youtube", "Youtube"
    CRYPTO = "crypto", "Crypto"
    BITCOIN = "bitcoin", "Bitcoin"


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


def get_country_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    r = requests.get(url)
    json_data = json.loads(r.content.decode("utf-8"))
    status = json_data["status"]
    if status == "fail":
        url = "https://ipinfo.io"
        r = requests.get(url)
        json_data = json.loads(r.content.decode("utf-8"))
        return json_data["country"]
    else:
        return json_data["countryCode"]


def prepare_redirection(page_model, ip, current_path=None):
    # country_code = get_country_info(ip)
    country_code = get_country_code_from_ip(ip)
    is_accepted = False
    rules = page_model.redirection.all()

    for r in rules:
        if r.is_active == True:
            rules_type = r.type
            if rules_type == "accepted":
                country_exist = r.redirection_rules.filter(name=country_code).exists()
                if country_exist:
                    is_accepted = True
                    return True

            if is_accepted == False:
                if rules_type == "redirect":
                    r_country_exist = r.redirection_rules.filter(
                        name=country_code
                    ).exists()
                    if r_country_exist:
                        red_url = r.redirect_url
                        if current_path == red_url:
                            return True
                        return red_url

                if rules_type == "other":
                    red_url = r.redirect_url
                    if current_path == red_url:
                        return True
                    return r.redirect_url


class CommonRedirectPage(Page):
    template_name = "home/common-redirection/common-redirection.html"

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        )
    ]
    parent_page_types = ["CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.COMMON_REDIRECT_PAGE)
        except:
            page_model = False

        ip = get_client_ip(request)
        country_code = get_country_code_from_ip(ip)


        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)
        return render(
            request,
            self.template_name,
            {
                "self": self,
                "country_code": country_code,
            },
        )


class EvestAccountChoice(models.IntegerChoices):
    MEDIA_BUY = 0, "Media Buy"
    PPC = 1, "PPC"

class EvestPage(Page):
    # template = "home/evest/evest-islamic.html"

    def get_template(self):
        if self.template_choice == "ramadan":
            return "home/evest/evest-ramadan.html"
        elif self.template_choice == "islamic":
            return "home/evest/evest-islamic.html"
        elif self.template_choice == "ef05":
            return "home/evest/ef05.html"
        elif self.template_choice == "ef06":
            return "home/evest/ef06.html"
        elif self.template_choice == "btcnews1":
            return "home/evest/btcnews1.html"
        elif self.template_choice == "btcnews2":
            return "home/evest/btcnews2.html"
        elif self.template_choice == "btcnews3":
            return "home/evest/btcnews3.html"
        elif self.template_choice == "youtube":
            return "home/evest/youtube.html"
        elif self.template_choice == "crypto":
            return "home/evest/crypto.html"
        elif self.template_choice == "bitcoin":
            return "home/evest/bitcoin.html"

    template_choice = models.CharField(
        max_length=100,
        choices=EvestTeamplateChoice.choices,
        default=EvestTeamplateChoice.RAMADAN,
    )
    parameters = models.CharField(max_length=255, null=True, blank=True)
    form_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    form_title = models.CharField(max_length=255, null=True, blank=True)
    email_placeholder = models.CharField(max_length=100, null=True, blank=True)
    password_placeholder = models.CharField(max_length=100, null=True, blank=True)
    firstName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    lastName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    phone_placeholder = models.CharField(max_length=100, null=True, blank=True)
    country_placeholder = models.CharField(max_length=100, null=True, blank=True)
    submit_button_text = models.CharField(max_length=50, null=True, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True
    )
    account_used = models.IntegerField(
        choices=EvestAccountChoice.choices,
        default=EvestAccountChoice.MEDIA_BUY,
    )

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    body = StreamField(
        [
            ("evest_left", EvestLeftContentBlock()),
            ("why_evest", WhyEvestBlock()),
            ("evest_title_text", EvestTitleText()),
            ("evest_title_img", EvestTitleImg()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_image"),
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("account_used"),
                FieldPanel("parameters"),
            ],
            heading="Parameters",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("body")],
            heading="Body",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("form_logo"),
                FieldPanel("form_title"),
                FieldPanel("email_placeholder"),
                FieldPanel("password_placeholder"),
                FieldPanel("firstName_placeholder"),
                FieldPanel("lastName_placeholder"),
                FieldPanel("phone_placeholder"),
                FieldPanel("country_placeholder"),
                FieldPanel("submit_button_text"),
            ],
            heading="Form Data",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.EVEST)
        except:
            page_model = False

        ip = get_client_ip(request)
        country_code = get_country_code_from_ip(ip)


        if page_model:
            ip = get_client_ip(request)
            current_path = f"https://economyflow.com{request.path}"
            redirect_url = prepare_redirection(page_model, ip, current_path)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        phone = ""
        if request.method == "POST":
            common_template_choices = ["ramadan", "ef05", "ef06", "crypto", "bitcoin"]
            if self.template_choice in common_template_choices:
                area_code = request.POST.get("areaCode")
                phone_number = request.POST.get("phonenumber")
                phone = "+" + area_code + phone_number
                # print("=======================")
                # print(area_code)
                # print(phone_number)
                # print(phone)
            elif self.template_choice == "islamic":
                phone = request.POST.get("phonenumber")
            elif self.template_choice in ["btcnews1", "btcnews2", "btcnews3"]:
                phone = request.POST.get("phone")

            form = EvestForm(
                request.POST or None,
                params=self.parameters,
                phone=phone,
                page_slug=self.slug,
                ip=ip,
                account_used=self.account_used
            )
            if form.is_valid():
                status, login_url = form.post_customer()
                # return JsonResponse(login_url)
                if status == True:
                    if login_url:
                        return redirect(f"/signup/complete/?red_url={login_url}")
                        # return redirect(login_url)
                else:
                    err_msg = login_url
                    return render(
                        request,
                        self.get_template(),
                        {"self": self, "form": form, "err_msg": err_msg},
                    )
            else:
                print(form.errors)
        else:
            form = EvestForm(
                params=self.parameters,
                phone=phone,
                page_slug=self.slug,
                ip=ip,
                account_used=self.account_used
            )

        return render(
            request,
            self.get_template(),
            {
                "self": self,
                "country_code": country_code,
                "form": form,
            },
        )


class Trade360(Page):
    template = "home/trade360.html"

    form_title = models.CharField(max_length=255, null=True, blank=True)
    firstName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    lastName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    email_placeholder = models.CharField(max_length=100, null=True, blank=True)
    password_placeholder = models.CharField(max_length=100, null=True, blank=True)
    phone_placeholder = models.CharField(max_length=100, null=True, blank=True)
    country_placeholder = models.CharField(max_length=100, null=True, blank=True)
    submit_button_text = models.CharField(max_length=50, null=True, blank=True)
    # hero_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    body = StreamField(
        [
            ("trade360_head_right", Trade360RightHead()),
            ("trade360_three_column_block", Trade360ThreeColumnBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("form_title"),
                FieldPanel("firstName_placeholder"),
                FieldPanel("lastName_placeholder"),
                FieldPanel("email_placeholder"),
                FieldPanel("password_placeholder"),
                FieldPanel("phone_placeholder"),
                FieldPanel("country_placeholder"),
                FieldPanel("submit_button_text"),
            ],
            heading="Form Data",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("body")],
            heading="Body",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        if request.method == "POST":
            form = Trade360Form(request.POST or None)
            if form.is_valid():
                trade360 = form.post_customer()
                return render(
                    request,
                    self.template,
                    {
                        "self": self,
                        "form": form,
                    },
                )
        else:
            form = Trade360Form()

        return render(
            request,
            self.template,
            {
                "self": self,
                "form": form,
            },
        )


class LegacyFxPage(Page):
    template = "home/legacyfx.html"

    tag = models.CharField(
        max_length=255, default="ashraf_channel", null=True, blank=True
    )

    form_title = models.CharField(max_length=255, null=True, blank=True)
    email_placeholder = models.CharField(max_length=100, null=True, blank=True)
    firstName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    lastName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    phone_placeholder = models.CharField(max_length=100, null=True, blank=True)
    country_placeholder = models.CharField(max_length=100, null=True, blank=True)
    submit_button_text = models.CharField(max_length=50, null=True, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True
    )

    redirection = StreamField([("redirection", Redirection())], null=True)

    # body = StreamField([
    #     ("evest_left", EvestLeftContentBlock()),
    # ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_image"),
            ],
            heading="Background Image",
        ),
        # MultiFieldPanel(
        #     [
        #         StreamFieldPanel("body")
        #     ],
        #     heading="Body",
        # ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("tag"),
            ],
            heading="Tag",
        ),
        MultiFieldPanel(
            [
                FieldPanel("form_title"),
                FieldPanel("email_placeholder"),
                FieldPanel("firstName_placeholder"),
                FieldPanel("lastName_placeholder"),
                FieldPanel("phone_placeholder"),
                FieldPanel("country_placeholder"),
                FieldPanel("submit_button_text"),
            ],
            heading="Form Data",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.LEGACYFX)
        except:
            page_model = False

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":
            form = LegacyFxForm(request.POST or None, page_slug=self.slug, tag=self.tag)
            if form.is_valid():
                legacyfx = form.post_customer()
                if legacyfx:
                    return redirect(f"/signup/complete/?red_url={legacyfx}")
                    # return redirect(legacyfx)
                return render(
                    request,
                    self.template,
                    {
                        "self": self,
                        "form": form,
                    },
                )
        else:
            form = LegacyFxForm(page_slug=self.slug, tag=self.tag)

        return render(
            request,
            self.template,
            {
                "self": self,
                "form": form,
            },
        )


class IngotTeamplateChoice(models.TextChoices):
    CAMPAIGN1 = "camp1", "Campaign 1"
    CAMPAIGN2 = "camp2", "Campaign 2"


class IngotBrokerPage(Page):
    def get_template(self):
        if self.template_choice == IngotTeamplateChoice.CAMPAIGN1:
            return "home/ingot/camp-1.html"
        elif self.template_choice == IngotTeamplateChoice.CAMPAIGN2:
            return "home/ingot/camp-2.html"
        else:
            return "home/ingot/ingot.html"

    template_choice = models.CharField(
        max_length=100,
        choices=IngotTeamplateChoice.choices,
        default=IngotTeamplateChoice.CAMPAIGN1,
    )

    redirection = StreamField([("redirection", Redirection())], null=True)

    form_title = models.CharField(max_length=255, null=True, blank=True)
    email_placeholder = models.CharField(max_length=100, null=True, blank=True)
    password_placeholder = models.CharField(max_length=100, null=True, blank=True)
    firstName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    lastName_placeholder = models.CharField(max_length=100, null=True, blank=True)
    phone_placeholder = models.CharField(max_length=100, null=True, blank=True)
    post_code_placeholder = models.CharField(max_length=100, null=True, blank=True)
    country_placeholder = models.CharField(max_length=100, null=True, blank=True)
    submit_button_text = models.CharField(max_length=50, null=True, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_image"),
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("form_title"),
                FieldPanel("email_placeholder"),
                FieldPanel("password_placeholder"),
                FieldPanel("firstName_placeholder"),
                FieldPanel("lastName_placeholder"),
                FieldPanel("phone_placeholder"),
                FieldPanel("country_placeholder"),
                FieldPanel("post_code_placeholder"),
                FieldPanel("submit_button_text"),
            ],
            heading="Form Data",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.INGOT)
        except:
            page_model = False

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":

            form = IngotForm(request.POST or None, page_slug=self.slug)
            if form.is_valid():
                legacyfx = form.post_customer()
                if legacyfx:
                    return redirect(f"/signup/complete/?red_url=https://www.ingotbrokers.com/ar/login")
                    # return redirect("https://www.ingotbrokers.com/ar/login")
                return render(
                    request,
                    self.get_template(),
                    {
                        "self": self,
                        "form": form,
                    },
                )
            else:
                print(form.errors)
        else:
            form = IngotForm(page_slug=self.slug)

        return render(
            request,
            self.get_template(),
            {
                "self": self,
                "form": form,
            },
        )


#
# ──────────────────────────────────────────────────── I ──────────
#   :::::: A L V E X O : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────
#


class AlvexoTemplateChoice(models.TextChoices):
    STARTER_TEMPLATE = "starter-template", "Starter Template"


class AlvexoPage(Page):
    def get_template(self):
        if self.template_choice == "starter-template":
            return "home/alvexo/starter-template.html"

    template_choice = models.CharField(
        max_length=100,
        choices=AlvexoTemplateChoice.choices,
        default=AlvexoTemplateChoice.STARTER_TEMPLATE,
    )
    parameters = models.CharField(max_length=255, null=True, blank=True)

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("parameters"),
            ],
            heading="Parameters",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.ALVEXO)
        except:
            page_model = False

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":
            form = AlvexoForm(request.POST or None, page_slug=self.slug)
            if form.is_valid():
                alvexo = form.post_customer()
                if alvexo:
                    # return redirect(alvexo)
                    return redirect(f"/signup/complete/?red_url={alvexo}")
                return render(
                    request,
                    self.get_template(),
                    {
                        "self": self,
                        "form": form,
                    },
                )
            else:
                print(form.errors)
        else:
            form = AlvexoForm(page_slug=self.slug)

        return render(request, self.get_template(), {"self": self, "form": form})


def get_user_country(ip="167.172.41.255"):
    url = f"http://www.geoplugin.net/json.gp?ip={ip}"
    r = requests.get(url)
    json_data = json.loads(r.content.decode("utf-8"))
    return json_data["geoplugin_countryCode"]


class TradersGCCTemplateChoice(models.TextChoices):
    STARTER_TEMPLATE = "starter-template", "Starter Template"


class TradersGCCPage(Page):
    def get_template(self):
        if self.template_choice == "starter-template":
            return "home/tradersgcc/starter-template.html"

    template_choice = models.CharField(
        max_length=100,
        choices=TradersGCCTemplateChoice.choices,
        default=TradersGCCTemplateChoice.STARTER_TEMPLATE,
    )
    parameters = models.CharField(max_length=255, null=True, blank=True)

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("parameters"),
            ],
            heading="Parameters",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        client_ip = get_client_ip(request)
        country_code_from_server = get_user_country(client_ip)

        if country_code_from_server is None:
            country_code_from_server = "BD"
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.AXIA)
        except:
            page_model = False

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":
            form = TradersGCCForm(request.POST or None, page_slug=self.slug)
            if form.is_valid():
                tradersgcc = form.post_customer()
                if tradersgcc:
                    return redirect(f"/signup/complete/?red_url={tradersgcc}")
                    # return redirect(tradersgcc)
                    # return JsonResponse(tradersgcc, safe=False)
                return render(
                    request,
                    self.get_template(),
                    {
                        "self": self,
                        "form": form,
                        "country_code_from_server": country_code_from_server,
                        "client_ip": client_ip,
                    },
                )
            else:
                print(form.errors)
        else:
            form = TradersGCCForm(page_slug=self.slug)

        return render(
            request,
            self.get_template(),
            {
                "self": self,
                "form": form,
                "country_code_from_server": country_code_from_server,
                "client_ip": client_ip,
            },
        )


class CapitalemplateChoice(models.TextChoices):
    STARTER_TEMPLATE = "starter-template", "Starter Template"


class CapitalPage(Page):
    def get_template(self):
        if self.template_choice == "starter-template":
            return "home/capital/starter-template.html"

    template_choice = models.CharField(
        max_length=100,
        choices=CapitalemplateChoice.choices,
        default=CapitalemplateChoice.STARTER_TEMPLATE,
    )
    parameters = models.CharField(max_length=255, null=True, blank=True)

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("parameters"),
            ],
            heading="Parameters",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        client_ip = get_client_ip(request)
        country_code_from_server = get_country_code_from_ip(client_ip)

        if country_code_from_server is None:
            country_code_from_server = "SA"
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.CAPITAL)
        except:
            page_model = False

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        else:
            redirect_url = True

        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":
            form = CapitalForm(
                request.POST or None,
                page_slug=self.slug,
                user_ip=client_ip,
                country_code=country_code_from_server,
                params=self.parameters,
            )
            if form.is_valid():
                capital = form.post_customer()
                if capital is not None:
                    return redirect(f"/signup/complete/?red_url={capital}")
                    # return redirect(capital)
                return render(
                    request,
                    self.get_template(),
                    {
                        "self": self,
                        "form": form,
                        "country_code_from_server": country_code_from_server,
                        "client_ip": client_ip,
                    },
                )
            else:
                print(form.errors)
        else:
            form = CapitalForm(
                page_slug=self.slug,
                user_ip=client_ip,
                country_code=country_code_from_server,
                params=self.parameters,
            )

        return render(
            request,
            self.get_template(),
            {
                "self": self,
                "form": form,
                "country_code_from_server": country_code_from_server,
                "client_ip": client_ip,
            },
        )


#
# ──────────────────────────────────────────────────────────── I ──────────
#   :::::: A V A P A R T N E R : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────
#


class AVATemplateChoice(models.TextChoices):
    RAMADAN = "ramadan", "Ramadan"
    STOCK = "stock", "Stock"


class AvaPage(Page):
    def get_template(self):
        if self.template_choice == "ramadan":
            return "home/ava/ramadan.html"
        elif self.template_choice == "stock":
            return "home/ava/stock.html"

    template_choice = models.CharField(
        max_length=100,
        choices=AVATemplateChoice.choices,
        default=AVATemplateChoice.RAMADAN,
    )
    parameters = models.CharField(max_length=255, null=True, blank=True)

    redirection = StreamField([("redirection", Redirection())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("template_choice"),
            ],
            heading="Background Image",
        ),
        MultiFieldPanel(
            [StreamFieldPanel("redirection")],
            heading="Redirection",
        ),
        MultiFieldPanel(
            [
                FieldPanel("parameters"),
            ],
            heading="Parameters",
        ),
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def serve(self, request):
        try:
            page_model = Redirection.objects.get(page_type=TypeChoice.AVA)
        except:
            page_model = False

        client_ip = get_client_ip(request)
        country_code_from_server = get_country_code_from_ip(client_ip)

        if country_code_from_server is None:
            country_code_from_server = "BD"

        if page_model:
            ip = get_client_ip(request)
            redirect_url = prepare_redirection(page_model, ip)
        else:
            redirect_url = True

        if redirect_url == True:
            pass
        elif redirect_url is not None:
            red_url = f"/redirect/?red_url={redirect_url}"
            return redirect(red_url)

        if request.method == "POST":
            form = AvaForm(
                request.POST or None,
                page_slug=self.slug,
                user_ip=client_ip,
                country_code=country_code_from_server,
                params=self.parameters, # tag
            )
            if form.is_valid():
                error, ava = form.post_customer()
                if error == False:
                    return redirect(f"/signup/complete/?red_url={ava}")
                    # return redirect(ava)
                else:
                    return render(
                        request,
                        self.get_template(),
                        {
                            "self": self,
                            "form": form,
                            "country_code": country_code_from_server,
                            "client_ip": client_ip,
                            "error": ava
                        },
                    )
            else:
                return render(
                        request,
                        self.get_template(),
                        {
                            "self": self,
                            "form": form,
                            "country_code": country_code_from_server,
                            "client_ip": client_ip,
                        },
                    )
        else:
            pass
            # form = CapitalForm(
            #     page_slug=self.slug,
            #     user_ip=client_ip,
            #     country_code=country_code_from_server,
            #     params=self.parameters,
            # )

        return render(
            request,
            self.get_template(),
            {
                "self": self,
                "form": None,
                "country_code": country_code_from_server,
                "client_ip": client_ip,
            },
        )


#
# ────────────────────────────────────────────────────────────── I ──────────
#   :::::: C U S T O M   P A G E : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────
#


class ButtonLinkType(models.TextChoices):
    COUNTRY = "country", "Country"
    OTHER = "other", "Other"


class ButtonCountries(Orderable):
    name = models.CharField(max_length=10)
    rules = ParentalKey("ButtonLink", related_name="button_countries")

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name


class ButtonLink(Orderable, ClusterableModel):
    type = models.CharField(
        max_length=50, choices=ButtonLinkType.choices, default=ButtonLinkType.COUNTRY
    )
    is_active = models.BooleanField(default=True)
    redirect_url = models.URLField(max_length=255)
    button_link = ParentalKey("ButtonRules", related_name="button_link")

    panels = [
        MultiFieldPanel(
            [FieldPanel("type"), FieldPanel("is_active"), FieldPanel("redirect_url")],
            heading="Basic",
        ),
        MultiFieldPanel(
            [InlinePanel("button_countries", label="Country")], heading="Country"
        ),
    ]

    def __str__(self):
        return self.type


class ButtonRules(ClusterableModel):
    name = models.CharField(max_length=255)
    related_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                PageChooserPanel("related_page", page_type="home.DemoPage"),
            ],
            heading="Basic",
        ),
        MultiFieldPanel(
            [InlinePanel("button_link", label="Rules")], heading="Redirection"
        ),
    ]

    def __str__(self):
        return self.name


class DemoPage(Page):
    def get_template(self):
        return "home/demo/starter-template.html"

    investment_plan_link = models.URLField(max_length=250, null=True)
    page_title = models.CharField(max_length=255, null=True, blank=True)
    hero_title = models.CharField(max_length=255, null=True)
    desc = models.TextField(max_length=1000, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("page_title"),
                FieldPanel("investment_plan_link"),
                FieldPanel("hero_title"),
                FieldPanel("desc"),
            ],
            heading="Basic",
        )
    ]

    parent_page_types = ["HomePage", "CollectionPage"]
    subpage_types = []

    def __str__(self):
        return self.reference_name

    def get_btn_link(self, country_code="BD"):
        btn_rules = None
        try:
            btn_rules = ButtonRules.objects.get(related_page=self)
        except:
            btn_rules = None

        url = None
        if btn_rules:
            btn_links_country = btn_rules.button_link.filter(
                is_active=True, type=ButtonLinkType.COUNTRY
            )
            btn_links_other = btn_rules.button_link.filter(
                is_active=True, type=ButtonLinkType.OTHER
            )
            for btn_link_country in btn_links_country:
                country_exist = btn_link_country.button_countries.filter(
                    name__iexact=country_code
                ).exists()
                if country_exist:
                    url = btn_link_country.redirect_url
                    return url
            if btn_links_other:
                return btn_links_other[0].redirect_url
        return url

    def serve(self, request):
        client_ip = get_client_ip(request)
        try:
            country_code_from_server = get_user_country(client_ip)
        except:
            country_code_from_server = None

        if country_code_from_server is None:
            country_code_from_server = "BD"
        btn_url = self.get_btn_link(country_code=country_code_from_server)

        return render(request, self.get_template(), {"self": self, "btn_url": btn_url})


#
# ──────────────────────────────────────────────────────────────── I ──────────
#   :::::: C U S T O M   M O D E L : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────
#


class UserProfile(models.Model):
    firstName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    sign_up_id = models.CharField(max_length=150, null=True, blank=True)
    campaign = models.CharField(max_length=150, default="EF03", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    registered = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class TypeChoice(models.TextChoices):
    EVEST = "evest", "Evest" #
    TRADE360 = "trade360", "Trade360"
    LEGACYFX = "legacyfx", "LegacyFx" #
    INGOT = "ingot", "Ingot" #
    ALVEXO = "alvexo", "Alvexo"
    AXIA = "axia", "Axia" #
    CAPITAL = "capital", "Capital" #
    AVA = "ava", "Ava" #
    COMMON_REDIRECT_PAGE = "common_redirect", "Common Redirect Page"


class ApiRegistration(models.Model):
    is_active = models.BooleanField(default=True)
    type = models.CharField(
        max_length=50, choices=TypeChoice.choices, default=TypeChoice.EVEST
    )
    members = models.ManyToManyField(UserProfile, null=True, blank=True)

    def __str__(self):
        return self.type


class RedirectCountries(Orderable):
    name = models.CharField(max_length=10)
    rules = ParentalKey("RedirectionRules", related_name="redirection_rules")

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name


class RedirectionType(models.TextChoices):
    ACCEPTED = "accepted", "Accepted"
    REDIRECT = "redirect", "Redirect"
    OTHER = "other", "Other"


class RedirectionRules(Orderable, ClusterableModel):
    type = models.CharField(
        max_length=50, choices=RedirectionType.choices, default=RedirectionType.ACCEPTED
    )
    is_active = models.BooleanField(default=True)
    redirect_url = models.URLField(max_length=255)
    redirect = ParentalKey("Redirection", related_name="redirection")

    panels = [
        MultiFieldPanel(
            [FieldPanel("type"), FieldPanel("is_active"), FieldPanel("redirect_url")],
            heading="Basic",
        ),
        MultiFieldPanel(
            [InlinePanel("redirection_rules", label="Redirection Country")],
            heading="Rules",
        ),
    ]

    def __str__(self):
        return self.type


class Redirection(ClusterableModel):
    page_type = models.CharField(
        max_length=100, choices=TypeChoice.choices, default=TypeChoice.EVEST
    )
    panels = [
        MultiFieldPanel([FieldPanel("page_type")], heading="Page"),
        MultiFieldPanel(
            [InlinePanel("redirection", label="Redirection Rules")],
            heading="Redirection",
        ),
    ]

    def __str__(self):
        return self.page_type


class AcceptedMainParam(Orderable):
    name = models.CharField(max_length=10)
    central_redirect = ParentalKey(
        "CentralRedirection", related_name="accepted_main_params"
    )

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name


class CentralCountries(Orderable):
    name = models.CharField(max_length=10)
    rules = ParentalKey("CentralRedirection", related_name="central_country")

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name


class CentralRedirection(ClusterableModel):
    name = models.CharField(max_length=250)
    redirect_url = models.URLField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    redirect_msg = models.CharField(max_length=1000, null=True, blank=True)
    accepted_param = models.CharField(max_length=250, null=True, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("redirect_url"),
                FieldPanel("is_active"),
                FieldPanel("redirect_msg"),
                FieldPanel("accepted_param"),
            ],
            heading="Basic",
        ),
        MultiFieldPanel(
            [InlinePanel("central_country", label="Country")], heading="Country"
        ),
    ]

    def __str__(self):
        return self.name


#
# ──────────────────────────────────────────────────────────────────── I ──────────
#   :::::: I N C O M I N G   L E A D S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────
#


class Leads(models.Model):
    name = models.CharField(_("Name"), max_length=250)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    phone = models.CharField(_("Phone"), max_length=50)
    country = models.CharField(_("Country"), max_length=150)
    app_name = models.CharField(_("App name"), max_length=250)
    creation_time = models.DateTimeField(_("Creation time"), auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.email)