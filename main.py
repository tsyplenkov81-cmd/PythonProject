# Создайте словарь api_response, который имитирует ответ от API при запросе данных пользователя.
#
# Словарь должен содержать: user_id, email, full_name, is_verified (булево значение), last_login (может быть None),
# и список projects, в котором он участвует.
#
# Добавьте в профиль пользователя новый проект "Project Gamma".

projects = [1, 2, 3, 4, 5]

api_response = {
    "user_id": 789,
    "email": "rrr@rrr.rr",
    "full_name": "ddd fff ggg",
    "is_verified": True,
    "last_login": "23.04.2025",
    "projects": projects.copy()
}


api_response["projects"].append("Project Gamma")


print(api_response)
print(projects)