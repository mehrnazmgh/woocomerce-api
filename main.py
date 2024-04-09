import requests
import pandas as pd




customer_key = 'ck_2c4c25a0514d3d5127c193ce4200edf25297e227'
customer_secret = 'cs_5dd191584bb521d989d65113293cafaf0f290fc3'


#response from list of all users api
url_user = "https://emersun.com//wp-json/wc/v3/customers?per_page=100&page=1&role=all&role=irib&role=irib&consumer_key="+ customer_key +"&consumer_secret=" + customer_secret

payload = {}
headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

users_data = requests.request("GET", url_user, headers=headers, data=payload)
# print(users_data[0]["meta_data"])
total_pages = int(users_data.headers['X-WP-TotalPages'])
# print(total_pages)
users_data_total_list = []
for page in range(1,total_pages + 1):
    url_user_total = "https://emersun.com//wp-json/wc/v3/customers?per_page=100&page=" + str(page) + "&role=all&role=irib&role=irib&consumer_key="+ customer_key +"&consumer_secret=" + customer_secret
    payload = {}
    headers = {
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    users_data_total = requests.request("GET", url_user_total , headers=headers, data=payload).json()
    # print(users_data_total)
    users_data_total_list.append(users_data_total)
merge_total_user_data = []
for item in users_data_total_list :
    merge_total_user_data += item
    
# print(merge_total_user_data)

#response from list of all orders api
url_orders = "https://emersun.com//wp-json/wc/v3/orders?status=completed&page=1&per_page=100&orderby=date&consumer_key="+ customer_key +"&consumer_secret=" + customer_secret

payload = {}
headers = {
  # 'Cookie': 'shop_per_page=100; wfwaf-authcookie-143a2bc064b8ec5f8c7b3eb608e65817=684%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%7Cf43507187ebf34a7ee1f83191b39f54fd157070a2b5b37dcb2f9034ffdd83d4d; wp-wpml_current_admin_language_d41d8cd98f00b204e9800998ecf8427e=fa' ,
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

response_all_orders = requests.request("GET", url_orders, headers=headers, data=payload)


mainDf = pd.read_excel(r'./users.xlsx')
phones = mainDf['phone']
for phone in phones:
  for user_data in merge_total_user_data:
    user_phone = user_data["username"]
    if int(phone) == int(user_phone) :
      print('ok')
