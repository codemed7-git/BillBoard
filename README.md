# BillBoard

Доска объявлений на Django + PostgreSQL. Деплой на Render по `render.yaml`.

## Один раз на Render

**New → Blueprint** → репозиторий `codemed7-git/BillBoard`, ветка `main`, файл `render.yaml`.

Дальше каждый **push в `main`** сам собирает проект, применяет миграции, создаёт пользователей и перезапускает сервис.

## После деплоя

- Сайт: `https://<ваш-сервис>.onrender.com/` (редirect на `/bboard/`)
- Вход: **Войти** на сайте или `/accounts/login/`

| Логин | Пароль | Назначение |
|-------|--------|------------|
| `admin` | `admin123` | админка `/admin/` и сайт |
| `user` | `27kafthebest` | только сайт (без панели администратора) |

**admin** — суперпользователь Django: после входа на `/accounts/login/` попадает в `/admin/`.  
**user** — обычный аккаунт: вход на сайт, «Добавить объявление», «Мои объявления»; в `/admin/` доступа нет.

При первом деплое создаются 4 демо-объявления (если база пустая).

## Локально

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py create_initial_data
python manage.py runserver
```
