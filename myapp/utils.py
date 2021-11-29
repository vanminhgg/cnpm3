import hashlib

from myapp import db
from myapp.models import Users, DanhSachKham, Patients, HoaDon


def add_user(Name, Username, Password, Birth, Phonenumber):
    user = Users(Name=Name,
                 Username=Username,
                 Password=Password,
                 Birth=Birth,
                 Phonenumber=Phonenumber
                 )
    db.session.add(user)

    try:
        db.session.commit()
        return True
    except:
        return False


def get_list_kham(date=None):
    danhsachkham = DanhSachKham.query

    if date:
        danhsachkham= danhsachkham.filter(DanhSachKham.Ngaykham==date)

    return danhsachkham.all()

def add_list_kham(PatientName, Sex, Birth, Address):
    ds = DanhSachKham(PatientName=PatientName,
                 Sex=Sex,
                 Birth=Birth,
                 Address=Address
                 )
    db.session.add(ds)

    try:
        db.session.commit()
        return True
    except:
        return False


def add_phieu_kham(Name, TrieuChung, Loaibenh, Drug, Donvi, Soluong, Use):
    patients = Patients(Name=Name,
                 TrieuChung=TrieuChung,
                 Loaibenh=Loaibenh,
                 Drug=Drug,
                 Donvi=Donvi,
                 Soluong=Soluong,
                 Use=Use

                 )
    db.session.add(patients)

    try:
        db.session.commit()
        return True
    except:
        return False

def get_patient():
    patient = Patients.query



    return patient.all()


def add_hoadon(PatientName, drug_name, Soluong, Dongia, Tongtien):
    hoadon = HoaDon(PatientName=PatientName,
                 drug_name=drug_name,
                 Soluong=Soluong,
                 Dongia=Dongia,
                 Tongtien=Tongtien


                 )
    db.session.add(hoadon)

    try:
        db.session.commit()
        return True
    except:
        return False


def product_stats(from_date=None, to_date=None):
    stats = HoaDon.query
    if from_date:
        stats = stats.filter(HoaDon.Date.__ge__(from_date))

    if to_date:
        stats = stats.filter(HoaDon.Date.__le__(to_date))

    return stats.all()

def product_stats_sum( from_date=None, to_date=None):
    stats = HoaDon.query
    if from_date:
        stats = stats.filter(HoaDon.Date.__ge__(from_date))

    if to_date:
        stats = stats.filter(HoaDon.Date.__le__(to_date))

    return stats.all()

