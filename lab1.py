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

def get_url_info(url):
    with requests.get(url) as response:  # το αντικείμενο response
    
        # print("\nHeaders of the website:",response.headers)
        print("\033[1mWebsite Headers: \033[0m") #bold
        for key, values in response.headers.items():
            print(f"{key}:{values}")
            
        server = response.headers.get('Server')
        print(f"\nThe server is {server}\n")
    
        cookies = response.cookies.get_dict()
        if cookies: 
            print(f"The cookies are: {cookies}\n")
        else:
            print("No cookies found")
        
# url = 'http://eclass.upatras.gr/'  # προσδιορισμός του url
url = input("\nEnter the URL: \n")
get_url_info(url)
