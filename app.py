from fastapi import FastAPI

app = FastAPI()
students = [
	{'NIM': 18220059, 'Nama': 'Faiza Aqiela Zuma'},
	{'NIM': 18220085, 'Nama': 'Haje Noorjamani'},
	{'NIM': 18220005, 'Nama': 'Muhammad Rifqi Riyansah'}
]

@app.get("/")
def user_list() -> dict:
	return students
