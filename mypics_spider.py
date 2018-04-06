from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup


spider_queue = MogoQueue('mypics_db', 'crawl_queue')
def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')
    all_div = Soup.find_all('div', class_='item masonry_brick masonry-brick')
    for div in all_div:
        a = div.find_all('a')
        title = a[0]['href'][-10:-1] #a[1].get_text()
        url = a[0]['href']
        spider_queue.push(url, title)
    """上面这个调用就是把URL写入MongoDB的队列了"""

if __name__ == "__main__":
    start('http://www.mmonly.cc/gqbz/mnbz/')
    #spider_queue.clear()

"""这一段儿就不解释了哦！超级简单的"""