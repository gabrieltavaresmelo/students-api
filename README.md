# Student Management API 🎓

This is a simple **FastAPI** project for managing a list of students. It provides basic CRUD functionality and search capabilities, making it a great starting point for learning FastAPI.

---

## Features ✨

- 📋 List all students.
- 🔍 Retrieve a student by ID.
- 📝 Search students by name.
- ➕ Add a new student.
- ✏️ Update an existing student's details.
- ❌ Delete a student.

---

## Endpoints 🌐

### 1. **List All Students** 📋
**GET** `/students`

Retrieve the list of all students.

**Response:**
```json
{
  "status": "success",
  "message": "Students retrieved successfully.",
  "data": [...]
}
```

---

### 2. **Retrieve Student by ID** 🔍
**GET** `/students/{student_id}`

Retrieve the details of a student using their unique ID.

**Response (if found):**
```json
{
  "status": "success",
  "message": "Student retrieved successfully.",
  "data": {...}
}
```

---

### 3. **Search Students by Name** 🔎
**GET** `/students/search?name={name}`

Search for students whose names contain the given query string (case-insensitive).

**Response:**
```json
{
  "status": "success",
  "message": "Students retrieved successfully.",
  "data": [...]
}
```

---

### 4. **Add a New Student** ➕
**POST** `/students`

**Form Data:**
- `name` (string, required)
- `email` (string, required)
- `phone` (string, required)

**Response:**
```json
{
  "status": "success",
  "message": "Student added successfully.",
  "data": {...}
}
```

---

### 5. **Update a Student** ✏️
**PUT** `/students/{student_id}`

Update an existing student's details using their ID.

**Response:**
```json
{
  "status": "success",
  "message": "Student updated successfully.",
  "data": {...}
}
```

---

### 6. **Delete a Student** ❌
**DELETE** `/students/{student_id}`

Delete a student by their ID.

**Response:**
```json
{
  "status": "success",
  "message": "Student deleted successfully.",
  "data": {...}
}
```

---

## Conda Environment Commands ⚙️

Here are some useful commands to manage your Conda environments:

- 🌱 **View created environments**:
  ```bash
  conda info --envs
  ```

- ❌ **Remove an environment**:
  ```bash
  conda env remove --name pweb1
  ```

- 🆕 **Create a new environment**:
  ```bash
  conda create --name pweb1 pip python=3.10
  ```

- 🔄 **Activate an environment**:
  ```bash
  conda activate pweb1
  ```

- 🚪 **Deactivate an environment**:
  ```bash
  conda deactivate
  ```

---

## How to Run 🚀

### Prerequisites

- 🐍 Python 3.9 or higher installed.
- 🛠 Install dependencies.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
