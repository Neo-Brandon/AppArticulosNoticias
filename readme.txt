#INSTALAR SDK DE PayPal
pip install paypalrestsdk

#CODIGO QUE SE UTILIZA EN CUALQUIER VIEWS
from .paypal_config import paypalrestsdk
from django.http import JsonResponse

def paypal_payment_view(request):
    # Crear un pago
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute",
            "cancel_url": "http://localhost:8000/payment/cancel",
        },
        "transactions": [{
            "item_list": {"items": [{
                "name": "Producto",
                "sku": "001",
                "price": "20.00",
                "currency": "USD",
                "quantity": 1
            }]},
            "amount": {"total": "20.00", "currency": "USD"},
            "description": "Pago con PayPal."
        }]
    })

    if payment.create():
        return JsonResponse({'paymentID': payment.id})
    else:
        return JsonResponse({'error': payment.error}, status=500)
