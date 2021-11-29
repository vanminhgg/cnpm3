from datetime import datetime
from datetime import date

from sqlalchemy import Column, Integer, DateTime, String, Float, Boolean, ForeignKey

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from myapp import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Username = Column(String(20), unique=True, nullable=False)
    Password = Column(String(26), nullable=False)
    Birth = Column(DateTime)
    Phonenumber = Column(String(15), nullable=True)
    Roll = Column(String(10), nullable=False, default='nv')

    def __str__(self):
        return self.Name


class Category(db.Model):
    CateID = Column(Integer, primary_key=True, autoincrement=True)
    CateName = Column(String(50), nullable=False)

    def __str__(self):
        return self.CateName


class Rules(db.Model):
    RuleID = Column(Integer, primary_key=True, autoincrement=True)
    RuleName = Column(String(50), nullable=False)
    RuleContent = Column(String(200))

    def __str__(self):
        return self.RuleName


class Drugs(db.Model):
    DrugID = Column(Integer, primary_key=True, autoincrement=True)
    DrugName = Column(String(50), nullable=False)
    Price = Column(Float, nullable=False)
    Amount = Column(Integer)
    Unit = Column(String(20))
    Use = Column(Integer)

    def __str__(self):
        return self.DrugName


class Patients(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Ngaykham = Column(DateTime, default=date.today())
    TrieuChung = Column(String(100))
    Loaibenh = Column(String(100))
    Drug = Column(String(30))
    Donvi = Column(String(10))
    Soluong = Column(Integer)
    Use = Column(Integer)


# class ChiTietKhamNgay(db.Model):
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#     PatientID = Column(Integer, nullable=False)
#     Date = Column(DateTime, nullable=False)
#     Description = Column(String(50))


class DanhSachKham(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    PatientName = Column(String(50), nullable=False)
    Sex = Column(String(10), nullable=False)
    Birth = Column(DateTime)
    Address = Column(String(200))
    Ngaykham = Column(DateTime, default=date.today())

#
class HoaDon(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Date = Column(DateTime, nullable=False, default=date.today())
    PatientName = Column(String(50), nullable=False)
    drug_name= Column(String(50))
    Soluong = Column(Integer)
    Dongia = Column(Float)
    Tongtien = Column(Float, default=30000)



if __name__ == '__main__':
    db.create_all()
