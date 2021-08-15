from django.db.models import manager
from django.test import TestCase
from django.contrib.auth.models import User

from assets.models import Department,Asset,Profile, EmployeeAssetRequest,ManagerRequest, Email

# Create your tests here.

class TestDepartment(TestCase):
    def setUp(self):
        self.name = Department(name='IT')
        self.name.save()

    def TearDown(self):
        Department.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.name, Department))

    def test_saveDepartment(self):
        self.name.save()
        department = Department.objects.all()
        self.assertTrue(len(department)>0)

    def test_deleteDepartment(self):
        self.name.save()
        self.name.delete()
        department = Department.objects.all()
        self.assertTrue(len(department)==0)

# Creating a test case for asset setup,saving,updating and deleting and asset

class TestAsset(TestCase):
    def setUp(self):
        self.name = Asset(name='laptop')
        self.name.save()

    def TearDown(self):
        Asset.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.name, Asset))

    def test_saveAsset(self):
        self.name.save()
        asset = Asset.objects.all()
        self.assertTrue(len(asset)>0)

    def test_deleteAsset(self):
        self.name.save()
        self.name.delete()
        asset = Asset.objects.all()
        self.assertTrue(len(asset)==0)

# employeeAssetRequest

class TestEmployeeAssetRequest(TestCase):
    def setUp(self):
        self.type = EmployeeAssetRequest(type='stationery')
        self.type.save()

    def TearDown(self):
        EmployeeAssetRequest.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.type, EmployeeAssetRequest))

    def test_saveEmployeeAssetRequest(self):
        self.type.save()
        employeeassetrequest = EmployeeAssetRequest.objects.all()
        self.assertTrue(len(employeeassetrequest)>0)

    def test_deleteEmployeeAssetRequest(self):
        self.type.save()
        self.type.delete()
        employeeassetrequest = EmployeeAssetRequest.objects.all()
        self.assertTrue(len(employeeassetrequest)==0)

# ManagerRequest

class TestManagerRequest(TestCase):
    def setUp(self):
        self.specs = ManagerRequest(specs='hp-laptop')
        self.specs.save()

    def TearDown(self):
        ManagerRequest.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.specs, ManagerRequest))

    def test_saveManagerRequest(self):
        self.specs.save()
        manager = ManagerRequest.objects.all()
        self.assertTrue(len(manager)>0)

    def test_deleteManagerRequest(self):
        self.specs.save()
        self.specs.delete()
        manager = ManagerRequest.objects.all()
        self.assertTrue(len(manager)==0)

# UEmail test

class TestEmail(TestCase):
    def setUp(self):
        self.full_name = Email(full_name='emasharon@moringastaff.com')
        self.full_name.save()

    def TearDown(self):
        Email.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.full_name, Email))

    def test_saveEmail(self):
        self.full_name.save()
        email = Email.objects.all()
        self.assertTrue(len(email)>0)

    def test_deleteEmail(self):
        self.full_name.save()
        self.full_name.delete()
        email = Email.objects.all()
        self.assertTrue(len(email)==0)

        

