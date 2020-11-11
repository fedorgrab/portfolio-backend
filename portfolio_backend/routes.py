from flask import send_from_directory

from portfolio_backend import models, schemas
from portfolio_backend.application import backend_application
from portfolio_backend.application.settings import BackendSettings


@backend_application.route("/portfolio-info", methods=["GET"])
def portfolio_info():
    website_info_schema = schemas.WebSiteInfoSchema()
    social_link_schema = schemas.SocialLinkSchema()
    portfolio_object_schema = schemas.PortfolioObjectSchema()
    education_section_item_schema = schemas.EducationSectionItemSchema()
    job_section_item_schema = schemas.JobSectionItemSchema()

    website_info = website_info_schema.dump(obj=models.WebSiteInfo.query.first())
    portfolio_objects = portfolio_object_schema.dump(
        obj=(
            models.PortfolioProject
            .query.order_by(models.PortfolioProject.position)
            .all()
        ),
        many=True
    )

    education_items = education_section_item_schema.dump(
        obj=(
            models.EducationSectionItem
            .query.order_by(models.EducationSectionItem.position)
            .all()
        ), many=True
    )
    job_items = job_section_item_schema.dump(
        obj=(
            models.JobSectionItem
            .query.order_by(models.JobSectionItem.order_number)
            .all()
        ), many=True
    )
    social_links = social_link_schema.dump(obj=models.SocialLink.query.all(), many=True)
    website_info.update(
        portfolio=portfolio_objects,
        education=education_items,
        work=job_items,
        social_links=social_links,
    )
    return website_info


if backend_application.debug:

    @backend_application.route("/data/<path:filename>", methods=["GET"])
    def data(filename):
        return send_from_directory(BackendSettings.DATA_DIR, filename)
else:
    @backend_application.route("/data/<path:filename>", methods=["GET"])
    def data(filename):
        pass
