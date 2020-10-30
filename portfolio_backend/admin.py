from portfolio_backend.application import admin
from portfolio_backend.application import db
from portfolio_backend.models import PortfolioProject
from flask_admin.contrib.fileadmin import FileAdmin

from portfolio_backend.application.settings import BackendSettings

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from wtforms.validators import ValidationError
import imghdr


class UserAdminView(ModelView):

    def picture_validation(form, field):
        if field.data:
            filename = field.data.filename
            if filename[-4:] != '.jpg':
                raise ValidationError('file must be .jpg')
            if imghdr.what(field.data) != 'jpeg':
                raise ValidationError('file must be a valid jpeg image.')
        field.data = field.data.stream.read()
        return True

    form_columns = ['id', 'url_pic', 'pic']
    column_labels = dict(id='ID', url_pic="Picture's URL", pic='Picture')

    def pic_formatter(view, context, model, name):
        return 'NULL' if len(getattr(model, name)) == 0 else 'a picture'

    column_formatters = dict(pic=pic_formatter)
    form_overrides = dict(pic=FileUploadField)
    form_args = dict(pic=dict(validators=[picture_validation]))


admin.add_view(FileAdmin(BackendSettings.DATA_DIR, '/data/', name='Media Files'))
admin.add_view(ModelView(PortfolioProject, db.session))
