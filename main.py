from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1: {
        "name": "luke",
        "age": 18,
        "class": "year 12",
    },
    2: {
        "name": "adam",
        "age": 14,
        "class": "year 9",
    },
    3: {
        "name": "david",
        "age": 16,
        "class": "year 11",
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get('/get-all')
def get_all():
    return students


@app.get("/get-student/{student_id")
def get_student(student_id: int):
    return students


@app.get("/get-by-name/{student_id")
def get_by_name(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not Found"}


# Con un segundo parametro que será obligatorio al hacer GET
@app.get("/get-by-name-and-id/{student_id")
def get_by_name_id(student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not Found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Students already exists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
# La variable student viene de la clase UpdateStudent
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name is not None:
        students[student_id].name = student.name
    if student.age is not None:
        students[student_id].age = student.age
    if student.age is not None:
        students[student_id].year = student.year
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student delete successfully"}
