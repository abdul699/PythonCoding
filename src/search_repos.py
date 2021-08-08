from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_links(param, url):
    req = Request(url)

    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    # links will store all the links matched
    links = []
    for link in soup.find_all('a', href=True):
        # if the input string is in the current link and the link has a github url(i.e, a valid github repository then append it to the links)
        if(param in str(link) and "https://github.com/" in str(link)): 
            links.append(link.get('href'))

    if(links):
        print(links)
    else:
        print("No Link found with " +  param)
    

def main():
    # taking input parameter
    print("Query ?", end= ' ')
    param = input();

    # Given github url
    url = "https://github.com/vinta/awesome-python" 

    get_links(param, url)

if __name__ == "__main__":     
    main()