from typing import List, Optional, Any

from fastapi import FastAPI, Form, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI()

# In-memory storage for students
students = ['jose']

@app.get("/students")
async def list_students():
    """
    Retrieve the list of students.
    """
    return {
        "status": "success",
        "message": "Students retrieved successfully.",
        "data": students
    }

@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int):
    """
    Retrieve a student by their ID.
    """
    for student in students:
        if student["id"] == student_id:
            return {
                "status": "success",
                "message": "Student retrieved successfully.",
                "data": student
            }
    raise HTTPException(status_code=404, detail="Student not found.")

@app.get("/students_search")
async def search_students_by_name(name: str = Query(...)):
    """
    Search students by name.
    """
    matching_students = [student for student in students if name.lower() in student["name"].lower()]
    if matching_students:
        return {
            "status": "success",
            "message": "Students retrieved successfully.",
            "data": matching_students
        }
    raise HTTPException(status_code=404, detail="No students found with the given name.")

@app.post("/students")
async def create_student(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...)
):
    """
    Add a new student to the list.
    """
    student = {
        "id": len(students) + 1,  # Generate a simple ID
        "name": name,
        "email": email,
        "phone": phone
    }
    students.append(student)
    return {
        "status": "success",
        "message": "Student added successfully.",
        "data": student
    }

@app.put("/students/{student_id}")
async def update_student(
    student_id: int,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...)
):
    """
    Update a student's details by their ID.
    """
    for student in students:
        if student["id"] == student_id:
            student.update({"name": name, "email": email, "phone": phone})
            return {
                "status": "success",
                "message": "Student updated successfully.",
                "data": student
            }
    raise HTTPException(status_code=404, detail="Student not found.")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Delete a student by their ID.
    """
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return {
                "status": "success",
                "message": "Student deleted successfully.",
                "data": deleted_student
            }
    raise HTTPException(status_code=404, detail="Student not found.")


@app.post("/login")
async def create_student(
    email: str = Form(...),
    senha: str = Form(...)
):
    return True

#########################3
## TELAS

@app.get("/")
def root(request: Request) -> dict:  # 2
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "students": students},
    )

@app.get("/tela_login")
def tela_login(request: Request) -> dict:  # 2
    return TEMPLATES.TemplateResponse(
        "login.html",
        {"request": request},
    )

@app.get("/tela_form")
def tela_form(request: Request) -> dict:  # 2
    return TEMPLATES.TemplateResponse(
        "form.html",
        {"request": request},
    )