# Mpesa Daraja App

This is a Django-based application that integrates with the M-Pesa Daraja API to facilitate STK Push payments. The application allows users to initiate payments, handle callbacks, and provides a user-friendly interface for managing transactions.

---

## Features

- **STK Push Integration**: Users can initiate M-Pesa payments via STK Push.
- **Callback Handling**: The app processes M-Pesa API callbacks to confirm payment status.
- **Customizable Amount**: Users can manually enter the amount to be charged.
- **User Interface**: A simple and appealing UI for initiating payments and viewing results.

---

## Requirements

- Python 3.8+
- Django 4.x
- Ngrok (for exposing local server to the internet)
- M-Pesa Daraja API credentials

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/mpesa_daraja_app.git
   cd mpesa_daraja_app
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   ```bash
   export MPESA_CONSUMER_KEY=your_consumer_key
   export MPESA_CONSUMER_SECRET=your_consumer_secret
   export MPESA_SHORTCODE=your_shortcode
   export MPESA_PASSKEY=your_passkey
   ```

3. **Create a New Branch**
   ```bash
   git checkout -b feature-name
   ```

4. **Commit Changes**
   ```bash
   git commit -m "Description of changes"
   ```

5. **Push Changes**
   ```bash
   git push origin feature-name
   ```

6. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

8. **Expose Local Server**
   ```bash
   ngrok http 8000
   ```

---

## Project Structure

mpesa_daraja_app/
├── mpesa_daraja_app/
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
├── mpesa/
│   ├── views.py          # Views for STK Push and callback handling
│   ├── urls.py           # App-specific URL routing
│   ├── templates/        # HTML templates for the UI
├── manage.py             # Django management script
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies