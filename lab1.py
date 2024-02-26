import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

# url = 'http://eclass.upatras.gr/'  # προσδιορισμός του url
url = input("Enter the URL: ")
with requests.get(url) as response:  # το αντικείμενο response
    # html = response.text
    # more(html)
    print(response.headers)
    
    server = response.headers.get('Server')
    print(f"The server is {server}")
    
    cookies = response.cookies.get_dict()
    print(f"The cookies are{cookies}")