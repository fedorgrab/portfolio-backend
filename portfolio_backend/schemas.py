from portfolio_backend import models
from portfolio_backend.application import BackendSettings, ma


def get_media_data_callback(field_name):
    def get_data(obj):
        file_relative_path = getattr(obj, field_name)

        if not file_relative_path:
            return None
        return f"{BackendSettings.DATA_URL}{getattr(obj, field_name)}"

    return get_data


class FilePathField(ma.Function):
    def __init__(self, source, *args, **kwargs):
        super().__init__(get_media_data_callback(source), *args, **kwargs)


class WebSiteInfoSchema(ma.SQLAlchemySchema):
    avatar_image = FilePathField(source="avatar_image_path")

    class Meta:
        model = models.WebSiteInfo
        fields = (
            "id",
            "name",
            "role",
            "role_description",
            "about_me",
            "address",
            "website",
            "avatar_image",
        )


class PortfolioObjectSchema(ma.SQLAlchemySchema):
    image = FilePathField(source="image_path")
    notebook = FilePathField(source="notebook_path")

    class Meta:
        model = models.PortfolioProject
        fields = (
            "id",
            "name",
            "short_description",
            "description",
            "image",
            "notebook",
            "link",
            "source_link",
            "additional_link",
        )


class SocialLinkSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.SocialLink
        fields = ("name", "url", "class_name")


class EducationSectionItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.EducationSectionItem
        fields = ("school_name", "major", "graduation_month_year", "description")


class JobSectionItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.JobSectionItem
        fields = ("company_name", "position", "period_of_working", "description")
