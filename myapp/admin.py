from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from myapp.models import Users, Category, Drugs, Rules
from myapp import db, admin, utils
from flask import redirect, request
from flask_login import logout_user, current_user


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedViewBV(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class TableModelView(AuthenticatedView):
    can_export = True


class StatsView(BaseView):
    @expose("/")
    def index(self):
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        stats = utils.product_stats(from_date=from_date, to_date=to_date)
        return self.render("admin/stats.html", stats=stats)

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedViewBV):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect('/admin')


admin.add_view(TableModelView(Users, db.session, name="Nhân Viên"))
admin.add_view(TableModelView(Category, db.session, name="Chức năng"))
admin.add_view(TableModelView(Drugs, db.session, name="Thuốc"))
admin.add_view(TableModelView(Rules, db.session, name="Quy Định"))
admin.add_view(LogoutView(name="đăng xuất"))
admin.add_view(StatsView(name="Thong ke doanh thu"))