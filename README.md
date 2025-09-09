# Online Kirana Store

An online grocery store web application built with Django and Django REST Framework.

## Features

- User registration, authentication (JWT-based), and profile management.
- Product catalog with categories.
- Shopping cart and order management.
- Delivery addresses for users.
- Admin panel for store management.
- RESTful API endpoints for frontend integration.

## Tech Stack

- **Backend:** Django 5.x, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (development), can be configured for PostgreSQL/MySQL in production.
- **Static/Media:** Handled with Django static and media settings.
- **Frontend:** HTML templates, custom CSS/JS for admin.

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Kalpeshlokhande/Online-Kirana-Store.git
   cd Online-Kirana-Store
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements/local.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit:**  
   - Frontend: `http://localhost:8000/`
   - Admin: `http://localhost:8000/admin/`

## Project Structure

- `apps/` — Django apps: users, products, cart, orders, addresses, admin_panel
- `config/` — Django settings and configuration files
- `static/` — Static files (CSS, JS)
- `templates/` — HTML templates
- `requirements/` — Dependency lists for different environments

## Environment Variables

Create a `.env` file in the root with settings like:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
```

## Deployment

- Set up environment variables and production settings (`config/settings/production.py`).


## License

This project is licensed under the MIT License.
