import datetime

from portfolio_backend.application import db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# from sqlalchemy_imageattach.entity import Image, image_attachment


class PortfolioProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    description = db.Column(db.String(2047), nullable=False)
    image_path = db.Column(db.String(1024), nullable=False)
    # image = image_attachment("ProjectPicture")

    __table_name__ = "portfolio_project"

    # __table_args__ = (
    #     db.UniqueConstraint(
    #         "country", "province", "created_at", name="country_province_uc"
    #     ),
    # )

    def __repr__(self):
        return self.name

# class ProjectPicture(db.Model, Image):
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
#     user = db.relationship("User")
#     __tablename__ = "project_picture"

# class VirusDailyStatRecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     cases_confirmed = db.Column(db.Integer, nullable=True)
#     cases_deaths = db.Column(db.Integer, nullable=True)
#     cases_recovered = db.Column(db.Integer, nullable=True)
#     cases_confirmed_new = db.Column(db.Integer, nullable=True)
#     cases_deaths_new = db.Column(db.Integer, nullable=True)
#     cases_recovered_new = db.Column(db.Integer, nullable=True)
#     created_at = db.Column(
#         db.DateTime, default=datetime.datetime.utcnow, nullable=False
#     )
#
#     __table_name__ = "virus_daily_stat_record"
#
#
# class VirusDayOneByCountry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     country = db.Column(db.String(120), nullable=False)
#     cases_confirmed = db.Column(db.Integer, nullable=True)
#     cases_deaths = db.Column(db.Integer, nullable=True)
#     cases_recovered = db.Column(db.Integer, nullable=True)
#     date = db.Column(db.Date, nullable=False)
#
#     __table_name__ = "virus_day_one_by_country"
#     __table_args__ = (
#         db.UniqueConstraint("country", "date", name="country_date_unique_constraint"),
#     )
