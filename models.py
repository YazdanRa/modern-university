from datetime import datetime

from peewee import *


database = SqliteDatabase(None)


class BaseModel(Model):
    id = PrimaryKeyField()
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class User(BaseModel):
    first_name = CharField(max_length=128, null=True)
    last_name = CharField(max_length=128, null=True)
    student_number = CharField(max_length=128, unique=True)
    password = CharField(max_length=128)
    is_active = BooleanField(default=False)
    is_student = BooleanField(default=False)
    is_teacher = BooleanField(default=False)
    is_admin = BooleanField(default=False)

    # Extra Field
    national_id = CharField(max_length=32, null=True)
    birthday = DateField(null=True)
    hometown = CharField(max_length=128, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.student_number)


class Course(BaseModel):
    title = CharField(max_length=128, null=True)
    teacher = ForeignKeyField(User, backref='courses')
    students = ManyToManyField(User, backref='courses')
    rate = IntegerField(default=3)
    is_active = BooleanField(default=False)


class Mark(BaseModel):
    student = ForeignKeyField(User, backref='marks')
    course = ForeignKeyField(Course, backref='marks')
    mark = IntegerField(null=True)
    rate = IntegerField(null=True)


StudentCourse = Course.students.get_through_model()

