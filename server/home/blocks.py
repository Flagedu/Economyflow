from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class EvestLeftContentBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)
    img = ImageChooserBlock()
    description = RichTextBlock()

    class Meta:
        template = "home/blocks/evest/evest-right-content.html"


class WhyEvestBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    images = blocks.ListBlock(ImageChooserBlock())

    class Meta:
        template = "home/blocks/evest/evest-why-block.html"

class EvestTitleText(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    description = RichTextBlock()
    class Meta:
        template = "home/blocks/evest/evest-title-text.html"


class EvestImgDesc(blocks.StructBlock):
    img = ImageChooserBlock()
    description = RichTextBlock(required=False)

class EvestTitleImg(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    img_desc = blocks.ListBlock(EvestImgDesc())
    
    class Meta:
        template = "home/blocks/evest/evest-title-img.html"


class Trade360RightHead(blocks.StructBlock):
    logo = ImageChooserBlock()
    background_img = ImageChooserBlock()
    subtitle = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=True)

    class Meta:
        template = "home/blocks/trade360-right-head.html"


class SingleColumn(blocks.StructBlock):
    logo = ImageChooserBlock()
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)

class Trade360ThreeColumnBlock(blocks.StructBlock):
    columns = blocks.ListBlock(SingleColumn())

    class Meta:
        template = "home/blocks/trade360-three-column-block.html"


class Country(blocks.StructBlock):
    name = blocks.CharBlock(max_length=10, required=False)


redirect_type_choice = (
    ("accepted", "Accepted"),
    ("redirect", "Redirect"),
    ("redirect2", "Redirect2"),
    ("other", "Other")
)

class RedirectRules(blocks.StructBlock):
    type = blocks.ChoiceBlock(
        choices=redirect_type_choice, 
        default="accepted", 
        required=False
    )
    is_active = blocks.BooleanBlock(required=False)
    redirect_url = blocks.URLBlock(required=False)
    countries = blocks.ListBlock(Country, required=False)

class Redirection(blocks.StructBlock):
    redirect = blocks.ListBlock(RedirectRules) 
    class Meta:
        template = "home/blocks/redirection.html"
