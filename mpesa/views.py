from django.http import JsonResponse, HttpResponse
import requests
from datetime import datetime
import base64
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def get_access_token():
    """
    Fetches the access token from the Mpesa API.
    """
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(api_url, auth=(consumer_key, consumer_secret))
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return access_token
    else:
        raise Exception("Failed to fetch access token: " + response.text)

def initiate_stk_push(request):
    access_token = get_access_token()
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()).decode()

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "5",  # Amount to charge
        "PartyA": "254719299900",  # Phone number paying
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": "254719299900",  # Phone number paying
        "CallBackURL": "https://839c-2c0f-fe38-2022-9c57-cccd-2120-c4bd-1bac.ngrok-free.app/",  # Callback URL
        "AccountReference": "TestPay",
        "TransactionDesc": "Payment for service"
    }

    response = requests.post(url, json=payload, headers=headers)
    return JsonResponse(response.json())

@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        # Process the callback data here
        print(data)
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def home(request):
    return HttpResponse("Welcome to the Mpesa Daraja App!")