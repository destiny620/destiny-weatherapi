import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# def get_client_city(ip):
#     try:
#         response = requests.get(f'http://ipinfo.io/{ip}/json')
#         response.raise_for_status()
#         location_data = response.json()
#         return location_data.get('city', 'Unknown')
#     except requests.RequestException:
#         return 'Unknown'