import requests

def send_whatsapp_message(phone_number, message, phone_gateway):
    url = f'https://graph.facebook.com/v20.0/{phone_gateway}/messages'
    headers = {
        'Authorization': 'Bearer EAAIO4cetZBcQBO2yT7J7w1KoUGYw039InZBgGRdJhNw189EZBeBpJYFCSQWYtyv0aIsj4Uid54Vixez2GWzjtHlgIORXJ15o6llSZAZA9YXFCVZA47ZAqd091fKU3cweeYVt3ALnWSOAeMdtFxK77WYsuyqRSOVT6MF3nEpJrw1ncZAEZBJyPrKgLMmilq3DZACdxfe2CDy39YW4s2Nd9ZCARXVsKbzIEEKmwrWZBaLzmrSnkG8ZD',
        'Content-Type': 'application/json'
        
    }
    payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": "alerta2",
                "language": {
                    "code": "pt_BR"
                }
            }
        }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Exemplo de uso
message = 'Envio de Alerta!'
phone_gateway = '22222222222222222222'
phone_number = '55999999999'
response = send_whatsapp_message(phone_number, message, phone_gateway)
 

 