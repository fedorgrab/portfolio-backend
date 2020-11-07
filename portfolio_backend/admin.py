from flask import Markup, redirect
from flask_admin import expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField, ImageUploadField
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from portfolio_backend import models
from portfolio_backend.application import admin, db
from portfolio_backend.application.settings import BackendSettings


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get("class"):
            kwargs["class"] += " ckeditor"
        else:
            kwargs.setdefault("class", "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


def display_image_list(_, __, model, *args, **kwargs):

    if not model.image_path:
        return ""

    return Markup(
        f'<img src="{BackendSettings.DATA_URL}{model.image_path}" '
        f'style="width:100px; height:100px">'
    )


class ProjectAdminView(ModelView):
    form_extra_fields = {
        "image_path": ImageUploadField(
            label="Image",
            base_path=f"{BackendSettings.DATA_DIR}/project_images",
            endpoint="data",
            relative_path="project_images",
            url_relative_path="",
        ),
        "notebook_path": FileUploadField(
            label="Notebook",
            base_path=f"{BackendSettings.DATA_DIR}/project_notebooks",
            relative_path="project_notebooks",
        ),
    }

    form_overrides = {"description": CKTextAreaField}
    column_labels = {"image_path": "Image", "notebook_path": "Notebook"}
    extra_js = ["//cdn.ckeditor.com/4.6.0/standard/ckeditor.js"]
    column_formatters = {"image_path": display_image_list}
    inline_models = (models.PortfolioLink,)

    @staticmethod
    def change_file_path_url(form_field, file):
        return f"{form_field.relative_path}/{file.filename}"

    def on_model_change(self, form, model, is_created):
        image_file = form.image_path.data
        notebook_file = form.notebook_path.data

        try:
            model.image_path = self.change_file_path_url(form.image_path, image_file)
        except AttributeError:
            print("Updating without new image")
        try:
            model.notebook_path = self.change_file_path_url(
                form.notebook_path, notebook_file
            )
        except AttributeError:
            print("Updating without new notebook")


class WebSiteInfoModelView(ModelView):
    form_extra_fields = {
        "avatar_image_path": ImageUploadField(
            label="image",
            base_path=f"{BackendSettings.DATA_DIR}",
            endpoint="data",
            relative_path="",
            url_relative_path="",
        )
    }

    @expose("/")
    def index_view(self):
        qs = models.WebSiteInfo.query.all()
        if qs:
            obj = qs[0]
            return redirect(
                f"/admin/websiteinfo/edit/?id={obj.id}&url=%2Fadmin%2Fwebsiteinfo%2F"
            )
        else:
            return redirect("/admin/websiteinfo/new/?url=%2Fadmin%2Fwebsiteinfo%2F")


admin.add_view(WebSiteInfoModelView(models.WebSiteInfo, db.session))
admin.add_view(ModelView(models.SocialLink, db.session))
admin.add_view(ProjectAdminView(models.PortfolioProject, db.session))
admin.add_view(ModelView(models.EducationSectionItem, db.session))
admin.add_view(ModelView(models.JobSectionItem, db.session))
admin.add_view(
    FileAdmin(BackendSettings.DATA_DIR, BackendSettings.DATA_URL, name="Media Files")
)
