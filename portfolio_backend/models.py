from portfolio_backend.application import db


class OrderableMixin:
    position = db.Column(db.Integer)


class WebSiteInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=127), nullable=False)
    avatar_image_path = db.Column(db.String(length=1024), nullable=True)
    role = db.Column(db.String(length=511), nullable=False)
    role_description = db.Column(db.String(length=2047), nullable=False)
    about_me = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(length=127), nullable=False)
    website = db.Column(db.String(length=255), nullable=False)

    __table_name__ = "major_info"


class PortfolioLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=127), nullable=False)
    url = db.Column(db.String(length=511), nullable=False)

    portfolio_project_id = db.Column(db.Integer, db.ForeignKey("portfolio_project.id"))
    portfolio_project = db.relationship("PortfolioProject", back_populates="links")

    __table_name__ = "portfolio_project__link"


class PortfolioProject(OrderableMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Header info:
    name = db.Column(db.String(length=127), nullable=False)
    short_description = db.Column(db.Text, default="description")
    description = db.Column(db.Text, nullable=False)
    # Files:
    image_path = db.Column(db.String(length=1024), nullable=False)
    notebook_path = db.Column(db.String(length=1024), nullable=True)
    # Links:
    links = db.relationship("PortfolioLink", back_populates="portfolio_project")

    __table_name__ = "portfolio_project"
    __table_args__ = (
        db.UniqueConstraint("id", "image_path", name="project_image_uc"),
        db.UniqueConstraint("id", "name", name="project_name_uc"),
    )

    def __repr__(self):
        return self.name


class SocialLink(OrderableMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=127), nullable=False)
    url = db.Column(db.String(length=511), nullable=False)
    class_name = db.Column(db.String(length=127), nullable=False)

    __table_name__ = "social_link"
    __table_args__ = (db.UniqueConstraint("id", "name", name="id_name_uc"),)


class EducationSectionItem(OrderableMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(length=127), nullable=False)
    major = db.Column(db.String(length=127), nullable=False)
    graduation_month_year = db.Column(db.String(length=127), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    __table_name__ = "education_info"
    __table_args__ = (
        db.UniqueConstraint("id", "school_name", name="id_school_name_uc"),
    )


class JobSectionItem(OrderableMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(length=127), nullable=False)
    position = db.Column(db.String(length=127), nullable=False)
    order_number = db.Column(db.Integer)
    period_of_working = db.Column(db.String(length=511), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    __table_name__ = "job_info"
    __table_args__ = (
        db.UniqueConstraint("id", "company_name", name="id_company_name_uc"),
    )
