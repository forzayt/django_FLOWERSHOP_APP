# Unified Login System Guide

## Overview

The Flower Shop application now features a **single unified login page** that automatically routes users to different dashboards based on their role. This provides a seamless user experience while maintaining proper access control.

## How It Works

### 1. Single Login Page
- **URL**: `/login` or `/`
- **Form Action**: `/adminlogin`
- **Purpose**: Single entry point for all users (Admin, Staff, Customer)

### 2. Automatic Role-Based Routing

When a user logs in, the system automatically:

1. **Validates credentials** against the `login` table
2. **Checks user role** (admin, staff, customer)
3. **Verifies account status** (approved, waiting, rejected)
4. **Redirects to appropriate dashboard** based on role and status

### 3. Role-Based Destinations

| Role | Status | Destination | Access Level |
|------|--------|-------------|--------------|
| **Admin** | Approved | `/adminhome` | Full admin access |
| **Staff** | Approved | `/staff-dashboard` | Staff management access |
| **Staff** | Waiting/Rejected | Login page with error message | No access |
| **Customer** | Approved | `/customer-dashboard` | Customer shopping access |
| **Customer** | Waiting/Rejected | Login page with error message | No access |

## Dashboard Features

### Admin Dashboard (`/adminhome`)
- **Access**: Only admin users
- **Features**: 
  - Full system management
  - User/staff approval
  - Product management
  - System statistics
- **Navigation**: Custom admin interface

### Staff Dashboard (`/staff-dashboard`)
- **Access**: Approved staff members
- **Features**:
  - Product management
  - User viewing
  - Staff information
  - Quick actions
- **Navigation**: Staff-specific interface

### Customer Dashboard (`/customer-dashboard`)
- **Access**: Approved customers
- **Features**:
  - Product browsing
  - Shopping cart
  - Account information
  - Quick navigation
- **Navigation**: Customer-friendly interface

## Login Flow

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

## Error Handling

### Common Error Messages

1. **"Invalid username or password"**
   - User credentials don't match any record

2. **"Your staff account is pending approval"**
   - Staff account exists but not yet approved

3. **"Your account is pending approval"**
   - Customer account exists but not yet approved

4. **"Staff profile not found"**
   - Login exists but no corresponding staff record

5. **"User profile not found"**
   - Login exists but no corresponding customer record

## Security Features

### Session Management
- Session data stored for logged-in users
- Automatic session cleanup on logout
- Role-based access control

### Status Verification
- All users must be approved before access
- Pending/rejected accounts cannot access dashboards
- Clear error messages for status issues

### Input Validation
- CSRF protection on all forms
- Required field validation
- SQL injection prevention

## User Registration

### Staff Registration
- **URL**: `/staff`
- **Creates**: Login record + Staff record
- **Default Status**: "waiting"
- **Approval Required**: Yes (by admin)

### Customer Registration
- **URL**: `/customer`
- **Creates**: Login record + User record
- **Default Status**: "waiting"
- **Approval Required**: Yes (by admin)

## Admin Management

### Approving Users
1. Access Django Admin: `/admin/`
2. Navigate to Users or Staff section
3. Select users to approve
4. Use bulk actions: "Approve selected users"

### Viewing User Status
- All user statuses visible in admin interface
- Filter by status (waiting, approved, rejected)
- Search functionality available

## Testing the System

### Test Scenarios

1. **Admin Login**
   ```
   Username: admin
   Password: admin123
   Expected: Redirect to /adminhome
   ```

2. **Staff Login (Approved)**
   ```
   Username: staff1
   Password: staff123
   Expected: Redirect to /staff-dashboard
   ```

3. **Staff Login (Pending)**
   ```
   Username: newstaff
   Password: staff123
   Expected: Error message about pending approval
   ```

4. **Customer Login (Approved)**
   ```
   Username: customer1
   Password: customer123
   Expected: Redirect to /customer-dashboard
   ```

5. **Invalid Credentials**
   ```
   Username: wrong
   Password: wrong
   Expected: "Invalid username or password"
   ```

## Customization

### Adding New Roles
1. Update the `role` choices in `models.py`
2. Add role-specific logic in `adminlogin` view
3. Create corresponding dashboard view and template
4. Add URL pattern for new dashboard

### Modifying Redirects
- Edit the `adminlogin` function in `views.py`
- Update redirect URLs as needed
- Ensure proper error handling

### Styling Changes
- Modify `login.html` for login page styling
- Update individual dashboard templates
- Customize error message styling

## Troubleshooting

### Common Issues

1. **"View didn't return HttpResponse"**
   - Check that all code paths in `adminlogin` return a response
   - Ensure proper exception handling

2. **Session not working**
   - Verify session middleware is enabled
   - Check session configuration in settings

3. **Database connection issues**
   - Ensure database is running
   - Check database credentials in settings

4. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check static file configuration

### Debug Mode
- Enable `DEBUG = True` in settings for detailed error messages
- Check Django logs for specific error information
- Use browser developer tools for frontend issues

## Best Practices

1. **Always validate user status** before granting access
2. **Use clear error messages** for better user experience
3. **Implement proper session management**
4. **Regular security audits** of user permissions
5. **Backup user data** regularly
6. **Monitor login attempts** for security

This unified login system provides a clean, secure, and user-friendly experience while maintaining proper access control and role-based functionality. 