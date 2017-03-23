import crawl_core
import mariaDB
import crawl_source
from multiprocessing import Process,Queue
import json

def run(start,end,result): # get url and save in DB
    links = crawl_core.goal_com(start,end)
    result.put(links)


def run_db(list): # get data from url
    for k in list:
        json_data = crawl_core.get_data(k[0])
        crawl_source.mariadb_json(json_data)

if __name__ == '__main__':
    '''
    str = "select url from url_dat where date>'2015-07-01' && date<'2016-07-01' "
    url_value = mariaDB.load_db_table(str,'Soccer')
    db_process = list()
    for sect in range(5):
        indexing = sect * 76
        url_list = url_value[indexing:indexing+76]
        db_process.append(Process(target=run_db, args=(url_list,)))
    for sta in range(5):
        db_process[sta].start()
    for jin in range(5):
        db_process[jin].join()
    '''
    #get data url source

    date_list = crawl_source.time_calc()
    result = Queue()
    pr = []
    for i in date_list:
        pr.append(Process(target=run, args=(i,date_list[i],result,)))
    for k in pr:
        k.start()
    for m in pr:
        m.join()

    field_data = dict()
    for keyword in range(result.qsize()):
        dictionary = result.get()
        for k in dictionary:
            for i in dictionary[k]:
                order_string = """insert into url_dat(date, url) values(""" + "'" + str(k) + "'," + str(i) + ");"
                mariaDB.create_db_table(order_string)
