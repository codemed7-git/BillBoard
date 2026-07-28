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
| `user` | `27kafthebest` | сайт (объявления) |

Учётки создаются командой `create_initial_data` при каждом старте сервиса (см. `start.sh`).

## Локально

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py create_initial_data
python manage.py runserver
```
