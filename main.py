import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_jobs():
    for url in file_to_set(QUEUE_FILE):
        if DOMAIN_NAME in str(url) and 'http' in str(url):
            queue.put(url)
    queue.join()
    crawl()


def crawl():
    queue_urls = file_to_set(QUEUE_FILE)
    if len(queue_urls) > 0:
        print(str(len(queue_urls)) + ' urls in the queue')
        create_jobs()


PROJECT_NAME = 'Test'
HOMEPAGE = 'http://www.hkbu.edu.hk/eng/main/index.jsp'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
create_workers()
crawl()
