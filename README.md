
# 🏍️ SuperBike Showroom - Django Web App

A web-based bike showroom management application built using Django. It supports browsing bikes, adding new entries with images, managing stock and status through the admin panel, and includes a visually styled home page with contact and navigation features.

---

## 📦 Features

- Home page with logo, navigation bar, contact info, and quick links.
- Browse all available bikes.
- Detailed view of each bike including image, price, description, and stock.
- Add new bikes via a form (with image upload).
- Admin panel access to manage bikes and their statuses:
  - `Available`
  - `Sold`
  - `On Hold`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bike-showroom.git
cd bike-showroom
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist, create one using:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Access the App

- 🌐 Home Page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 🔐 Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- 🚲 Browse Bikes: [http://127.0.0.1:8000/bikes/](http://127.0.0.1:8000/bikes/)
- ➕ Add Bike: [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/)

---

## 🖼️ Media and Static Files

- Images are stored under: `/media/bike_images/`
- Static files (CSS, logo) under: `/static/showroom/`

To serve media files in development, make sure `settings.py` has:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧾 Admin Capabilities

In the admin panel, you can:

- View all bikes.
- Add, update, or delete bike records.
- Change bike status: `Available`, `Sold`, `On Hold`.

---

## 📁 Project Structure

```
bike-showroom/
│
├── bikeshowroom/         # Django project settings
├── showroom/             # Django app
│   ├── models.py         # Bike model
│   ├── views.py          # Views for home, bike list, detail, add
│   ├── forms.py          # Form for adding bikes
│   ├── templates/
│   │   └── showroom/
│   │       ├── home.html
│   │       ├── bike_list.html
│   │       ├── bike_detail.html
│   │       └── add_bike.html
│   └── static/
│       └── showroom/
│           ├── style.css
│           └── images/
│               └── logo.png
├── media/                # Uploaded images
└── manage.py
```

---

## 💡 Future Enhancements

- Add filtering/sorting by price, brand, or status.
- Add user authentication and order history.
- Add charts for sold/stock bikes.

---

## 📬 Contact

For questions or feedback, contact:  
📧 **support@superbike.com**  
📞 **+91-9876543210**

---

## 📄 License

This project is open source under the MIT License.
