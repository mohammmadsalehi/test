import requests

base_url = "https://demo-seller.digikala.com/api/v2/"
modules_url = "modules"
profile_mini_url = "profile?mini=true"
namespaces_url = "files/namespaces"
admin_page_url = "products/admin?page=1&size=10&order=desc"
admin_search_url = "products/admin?page=1&size=10&search%5Bmulti_search%5D=%D8%AA%D8%B3%D8%AA&order=desc"


def modules(cookies):
    url = f"{base_url}{modules_url}"
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.json()
        else:
            print("failed to get response")
            return None
    except requests.RequestException as e:
        print(f"{e}")
        return None


def profile_mini(cookies):
    url = f"{base_url}{profile_mini_url}"
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.json()
        else:
            print("failed to get response")
            return None
    except requests.RequestException as e:
        print(f"{e}")
        return None


def namespaces(cookies):
    url = f"{base_url}{namespaces_url}"
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.json()
        else:
            print("failed to get response")
            return None
    except requests.RequestException as e:
        print(f"{e}")
        return None


def admin_page(cookies):
    url = f"{base_url}{admin_page_url}"
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.json()
        else:
            print("failed to get response")
            return None
    except requests.RequestException as e:
        print(f"{e}")
        return None


def admin_search(cookies):
    url = f"{base_url}{admin_search_url}"
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.json()
        else:
            print("failed to get response")
            return None
    except requests.RequestException as e:
        print(f"{e}")
        return None


cookies = {
    'seller_api_access_token_demo': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJ0b2tlbl9pZCI6MTAzNjM2NzIsInNlbGxlcl9pZCI6MSwicGF5bG9hZCI6eyJ1c2VybmFtZSI6Ijk4OTM1ODgxNDgxMiIsImVtYWlsIjoiaC5tYXJrYXJpYW5AZGlnaWthbGEuY29tIiwiYnVzaW5lc3NfbmFtZSI6Ilx1MDYyZlx1MDZjY1x1MDYyY1x1MDZjY1x1MjAwY1x1MDZhOVx1MDYyN1x1MDY0NFx1MDYyNyIsImZpcnN0X25hbWUiOm51bGwsImxhc3RfbmFtZSI6bnVsbCwiY29tcGFueV9uYW1lIjoiXHUwNjQ2XHUwNjQ4XHUwNjIyXHUwNjQ4XHUwNjMxXHUwNjI3XHUwNjQ2IFx1MDY0MVx1MDY0Nlx1MjAwY1x1MDYyMlx1MDY0OFx1MDYyN1x1MDYzMlx1MDY0NyAoXHUwNjJmXHUwNmNjXHUwNjJjXHUwNmNjXHUyMDBjXHUwNmE5XHUwNjI3XHUwNjQ0XHUwNjI3KSIsImlzX2FkbWluIjp0cnVlLCJhZG1pbl9pZCI6MjYyMjkzMjIsImlzX2NvbnRlbnRfdXNlciI6dHJ1ZSwiaXNfbW9kZXJhdG9yIjpmYWxzZSwiaXNfbWFya2V0cGxhY2VfbW9kZXJhdG9yIjpmYWxzZX0sImV4cCI6MTcxNDI0Nzg4OX0.pyf1y-PleLpDsM4AL0Rv6JtHc8MxISL0XwvfQDSNYR4gFOBvwSnxwBDfoMTUcsFW'}

print(modules(cookies))
print((profile_mini(cookies)))
print(namespaces(cookies))
print(admin_page(cookies))
print(admin_search(cookies))
