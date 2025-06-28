# 🌸 FLOSUN - Flower Shop Management System

A comprehensive Django-based flower shop management system with unified login, role-based access control, and integrated admin interfaces.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Database Configuration](#database-configuration)
- [Admin System](#admin-system)
- [Unified Login System](#unified-login-system)
- [User Management](#user-management)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

FLOSUN is a modern flower shop management system built with Django that provides:

- **Unified Login System**: Single login page with automatic role-based routing
- **Multi-Role Support**: Admin, Staff, and Customer dashboards
- **Integrated Admin Interfaces**: Django admin + custom admin interfaces
- **Product Management**: Complete product lifecycle management
- **User Management**: Registration, approval, and status tracking
- **Responsive Design**: Works seamlessly on all devices

## ✨ Features

### Core Features
- 🌸 **Product Catalog**: Browse and manage flower products
- 👥 **User Management**: Multi-role user system with approval workflow
- 🛒 **Shopping Cart**: Customer shopping experience
- 📊 **Dashboard Analytics**: Real-time statistics and insights
- 🔐 **Security**: Role-based access control and session management
- 📱 **Responsive Design**: Mobile-friendly interface

### Admin Features
- **Django Admin Integration**: Full CRUD operations
- **Custom Admin Interface**: Branded admin experience
- **Bulk Operations**: Mass approve/reject users
- **Statistics Dashboard**: System overview and metrics
- **User Approval System**: Manage user registrations

### User Roles & Access

| Role | Access Level | Dashboard | Features |
|------|-------------|-----------|----------|
| **Admin** | Full Access | `/adminhome` | System management, user approval, product management |
| **Staff** | Management | `/staff-dashboard` | Product management, user viewing, staff operations |
| **Customer** | Shopping | `/customer-dashboard` | Product browsing, cart, account management |

## 🛠️ Technologies Used

- **Backend**: Python 3.11+, Django 5.2.3
- **Database**: MySQL (with SQLite fallback)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Fonts**: Google Fonts (Montserrat, Roboto)
- **Icons**: Font Awesome
- **Server**: XAMPP (for local MySQL)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- MySQL (optional - SQLite fallback available)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/vishnu1100/django_FLOWERSHOP_APP.git
cd django_FLOWERSHOP_APP
```

### Step 2: Install Dependencies
```bash
pip install django mysqlclient
```

### Step 3: Database Setup
The system automatically detects and uses the best available database:

- **MySQL** (if available): Uses your existing `flowershop2` database
- **SQLite** (fallback): Automatically creates `db.sqlite3`

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 6: Start Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
- **Main Site**: http://127.0.0.1:8000/
- **Login Page**: http://127.0.0.1:8000/login
- **Django Admin**: http://127.0.0.1:8000/admin/
- **Custom Admin**: http://127.0.0.1:8000/flower-admin/

## 🗄️ Database Configuration

### MySQL Configuration (Recommended)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flowershop2',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### SQLite Configuration (Fallback)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## 🔧 Admin System

### Available Admin Interfaces

1. **Django Default Admin** (`/admin/`)
   - Full CRUD operations
   - Advanced filtering and search
   - Bulk actions (approve/reject users)
   - Image preview for products

2. **Custom Flower Admin** (`/flower-admin/`)
   - Customized branding with flower theme
   - Same functionality as Django admin
   - Better visual integration

3. **Custom Admin Home** (`/adminhome`)
   - Your existing custom admin interface
   - Traditional admin experience

4. **Enhanced Dashboard** (`/dashboard`)
   - Real-time statistics
   - Quick access to all admin interfaces
   - Modern, responsive design

### Admin Features

#### User Management
- View all users with their status
- Bulk approve/reject users
- Search and filter functionality
- Link to login credentials

#### Staff Management
- View all staff members
- Bulk approve/reject staff
- Aadhar number tracking
- Status management

#### Product Management
- Product listing with images
- Category filtering
- Search functionality
- Image preview in admin

## 🔐 Unified Login System

### How It Works

The system features a **single unified login page** that automatically routes users based on their role:

1. **Single Login Page**: `/login` - Entry point for all users
2. **Automatic Validation**: Credentials checked against database
3. **Role Detection**: System identifies user role (admin/staff/customer)
4. **Status Verification**: Checks if account is approved
5. **Smart Routing**: Redirects to appropriate dashboard

### Login Flow

```
User enters credentials
        ↓
System validates login
        ↓
Check user role & status
        ↓
┌─────────────────┬─────────────────┬─────────────────┐
│     Admin       │     Staff       │    Customer     │
│   (Approved)    │   (Approved)    │   (Approved)    │
│        ↓        │        ↓        │        ↓        │
│   /adminhome    │ /staff-dashboard│/customer-dashboard│
└─────────────────┴─────────────────┴─────────────────┘
```

### Role-Based Destinations

| Role | Status | Destination | Access Level |
|------|--------|-------------|--------------|
| **Admin** | Approved | `/adminhome` | Full admin access |
| **Staff** | Approved | `/staff-dashboard` | Staff management access |
| **Staff** | Waiting/Rejected | Login page with error message | No access |
| **Customer** | Approved | `/customer-dashboard` | Customer shopping access |
| **Customer** | Waiting/Rejected | Login page with error message | No access |

### Error Handling

Common error messages and their meanings:

- **"Invalid username or password"** - Credentials don't match
- **"Your staff account is pending approval"** - Staff needs admin approval
- **"Your account is pending approval"** - Customer needs admin approval
- **"Staff profile not found"** - Login exists but no staff record
- **"User profile not found"** - Login exists but no customer record

## 👥 User Management

### User Registration

#### Staff Registration (`/staff`)
- Creates login record + staff record
- Default status: "waiting"
- Requires admin approval

#### Customer Registration (`/customer`)
- Creates login record + user record
- Default status: "waiting"
- Requires admin approval

### Approving Users

#### Method 1: Django Admin (Recommended)
1. Access `/admin/`
2. Navigate to "Staff" or "Users" section
3. Find pending users
4. Change status from "waiting" to "approved"
5. Save changes

#### Method 2: Bulk Actions
1. Select multiple users
2. Use "Approve selected users" action
3. Confirm the action

### User Status Management

- **Waiting**: New registrations awaiting approval
- **Approved**: Active users with full access
- **Rejected**: Denied access (can be changed to approved)

## 📡 API Endpoints

### Core URLs
- `/` - Home page
- `/login` - Unified login page
- `/logout` - User logout
- `/admin/` - Django admin interface
- `/flower-admin/` - Custom admin interface
- `/adminhome` - Custom admin home
- `/dashboard` - Enhanced statistics dashboard

### User Dashboards
- `/staff-dashboard` - Staff management dashboard
- `/customer-dashboard` - Customer shopping dashboard

### Registration
- `/staff` - Staff registration page
- `/customer` - Customer registration page

### Product Management
- `/addproduct` - Add new products
- `/productdata` - View all products
- `/shop` - Product catalog

### User Management
- `/data` - View all users
- `/staffdata` - View all staff

## 📸 Screenshots

![Screenshot 1](/screenshots/1.png)
![Screenshot 2](/screenshots/2.png)
![Screenshot 3](/screenshots/3.png)
![Screenshot 4](/screenshots/4.png)

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Connection Issues
```bash
# Check if MySQL is running
# Verify database credentials in settings.py
# Try SQLite fallback if MySQL unavailable
```

#### 2. Migration Errors
```bash
python manage.py migrate --fake-initial
```

#### 3. Static Files Not Loading
```bash
python manage.py collectstatic
```

#### 4. "View didn't return HttpResponse"
- Check that all code paths in `adminlogin` return a response
- Ensure proper exception handling

#### 5. Session Issues
- Verify session middleware is enabled
- Check session configuration in settings

### Debug Mode
- Enable `DEBUG = True` in settings for detailed error messages
- Check Django logs for specific error information
- Use browser developer tools for frontend issues

### Getting Help
1. Check Django logs for error messages
2. Verify database connectivity
3. Ensure all migrations are applied
4. Check file permissions

## 🚀 Production Deployment

### Pre-deployment Checklist
1. Set `DEBUG = False` in settings
2. Configure proper database settings
3. Set up static file serving
4. Use HTTPS for admin interfaces
5. Configure proper logging
6. Set up backup procedures

### Security Considerations
1. **Django Admin Security**: Uses Django's built-in security features
2. **Session Management**: Proper session handling
3. **CSRF Protection**: Built-in CSRF protection
4. **Input Validation**: Required field validation
5. **SQL Injection Prevention**: Django ORM protection

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes with clear commit messages
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Create** a Pull Request explaining your changes

### Development Guidelines
- Follow Django best practices
- Add proper error handling
- Include documentation for new features
- Test thoroughly before submitting

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author

- **Vishnu Santhosh** - [@forzayt](https://github.com/forzayt)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive design framework
- Font Awesome for the beautiful icons
- Google Fonts for the typography

---

**Happy coding! 🌸** If you have any questions or need assistance, feel free to reach out!
