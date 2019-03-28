from bs4 import BeautifulSoup
import requests
import sys

class nptel:

    url = ''
    tags = ''

    # Initialise the class variables
    def __init__(self, url):
        self.url = url
        self.getTags(url)

    # Stores the all the a tags in the instance variable tags
    def getTags(self, url):
        response = requests.get(url)
        data = response.text

        soup = BeautifulSoup(data, 'lxml')
        self.tags = soup.find_all('a')
    
    # Changes the instance variable url
    def update (self, url):
        self.url = url
        self.getTags(url)
    
    # Return the stack of download links
    def getLinks(self, format, module='courses'):
        Stack = []
        for tag in self.tags:
            if (tag.get('href').find(format) != -1) and (tag.get('href').find(module) != -1):
                Stack.append(tag.get('href'))
        return Stack
        
    # Dowloads the file
    def download(url, filename):
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')

            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50*downloaded/total)
                    sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                    sys.stdout.flush()
        sys.stdout.write('\n')

