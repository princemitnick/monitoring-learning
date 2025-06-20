from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str

class Teacher(BaseModel):
    id: int
    name: str

class Subject(BaseModel):
    id: int
    name: str

class StudentTeacherMapping(BaseModel):
    student_id: int
    teacher_id: int


