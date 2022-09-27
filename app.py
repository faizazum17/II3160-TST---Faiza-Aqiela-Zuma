from fastapi import FastAPI

app = FastAPI()
students = [
	{'NIM': 18220059, 'Nama': 'Faiza Aqiela Zuma'},
	{'NIM': 18220085, 'Nama': 'Haje Noorjamani'},
	{'NIM': 18220005, 'Nama': 'Muhammad Rifqi Riyansah'},
	{'NIM': 18220063, 'Nama': 'I Nyoman Aditya Ariputra'}
]

@app.get("/")
def user_list() -> dict:
	return students
