# script for statistics, elasticsearch indexing and searching

from elasticsearch import Elasticsearch, helpers
import sys
import json
import os


# output file to be precessed
fileName = 'D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/output'


# function for creating statistics from output file
def create_stats(input_file):

    # define variables
    counter = 0
    empty_ID = 0
    empty_label = 0
    empty_cats = 0
    empty_links = 0

    max_cats = 0
    max_cats_page = ""
    max_cats2 = 0
    max_cats2_page = ""
    max_cats3 = 0
    max_cats3_page = ""
    max_links = 0
    max_links_page = ""
    max_links2 = 0
    max_links2_page = ""
    max_links3 = 0
    max_links3_page = ""

    # process file by lines
    for lineText in input_file:
        counter += 1
        lineText.strip()

        try:
            json_file = json.loads(lineText)
        except:
            continue


        try:
            # count empty ids, should be empty
            if json_file['ID'] == "":
                empty_ID += 1
            # count empty labels, should be empty
            if json_file['Label'] == "":
                empty_label += 1
            # count empty categories and pages with maximum number of categories
            if not json_file['Categories']:
                empty_cats += 1
            elif len(json_file['Categories']) > max_cats:
                if max_cats > max_cats2:
                    max_cats2 = max_cats
                    max_cats2_page = max_cats_page
                elif max_cats > max_cats3:
                    max_cats3 = max_cats
                    max_cats3_page = max_cats_page
                max_cats = len(json_file['Categories'])
                max_cats_page = json_file['Label']
            elif len(json_file['Categories']) > max_cats2:
                if max_cats2 > max_cats3:
                    max_cats3 = max_cats2
                    max_cats3_page = max_cats2_page
                max_cats2 = len(json_file['Categories'])
                max_cats2_page = json_file['Label']
            elif len(json_file['Categories']) > max_cats3:
                max_cats3 = len(json_file['Categories'])
                max_cats3_page = json_file['Label']
            # count empty links and pages with maximum number of links
            if not json_file['Links']:
                empty_links += 1
            elif len(json_file['Links']) > max_links:
                if max_links > max_links2:
                    max_links2 = max_links
                    max_links2_page = max_links_page
                elif max_links > max_links3:
                    max_links3 = max_links
                    max_links3_page = max_links_page
                max_links = len(json_file['Links'])
                max_links_page = json_file['Label']
            elif len(json_file['Links']) > max_links2:
                if max_links2 > max_cats3:
                    max_links3 = max_links2
                    max_links3_page = max_links2_page
                max_links2 = len(json_file['Links'])
                max_links2_page = json_file['Label']
            elif len(json_file['Links']) > max_links3:
                max_links3 = len(json_file['Links'])
                max_links3_page = json_file['Label']

        except:
            continue

    # print results
    print("")
    print("Celkovy pocet stranok: " + str(counter))

    print("")
    print("Pocet stranok bez id: " + str(empty_ID) + " Podiel: " + str(empty_ID/counter) + "%")
    print("Pocet stranok bez labelu: " + str(empty_label) + " Podiel: " + str(empty_label/counter) + "%")
    print("Pocet stranok bez kategorii: " + str(empty_cats) + " Podiel: " + str(empty_cats/counter) + "%")
    print("Pocet stranok bez linkov: " + str(empty_links) + " Podiel: " + str(empty_links/counter) + "%")

    print("")
    print("Stranka s najvacsim poctom kategorii je: " + max_cats_page + " so " + str(max_cats) + " kategoriami")
    print("Stranka s druhym najvacsim poctom kategorii je: " + max_cats2_page + " so " + str(max_cats2) + " kategoriami")
    print("Stranka s tretim najvacsim poctom kategorii je: " + max_cats3_page + " so " + str(max_cats3) + " kategoriami")
    print("Stranka s najvacsim poctom linkov je: " + max_links_page + " s " + str(max_links) + " linkami")
    print("Stranka s druhym najvacsim poctom linkov je: " + max_links2_page + " s " + str(max_links2) + " linkami")
    print("Stranka s tretim najvacsim poctom linkov je: " + max_links3_page + " s " + str(max_links3) + " linkami")


# function to get data from output file
def get_data_from_text_file(self):

    return [l.strip() for l in open(str(self), encoding="utf8", errors='ignore')]


if __name__ == '__main__':

    json_data = open(fileName, encoding="utf8")

    # create statistics from output file, this should be commented out since it should be ran only once
    # uncomment line bellow to run stats again
    # create_stats(json_data)


    # read data
    docs = get_data_from_text_file("D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/output")

    # check elasticsearch connection
    es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)

    if not es.ping():
        raise ValueError("Connection failed")

    # index data with elasticsearch, this is commented out as it should be ran only once
    ''' uncomment this part to create index again
    for num in range(len(docs)):

        try:
            es.index(index='docs', id=num, body=docs[num], request_timeout=50)

        except json.decoder.JSONDecodeError as err:
            print("ERROR for num:", num, "-- JSONDecodeError:", err, "for doc:", docs[num])'''


    finder = ""

    # search for label with elasticsearch
    while finder != "end":

        # enter label input
        finder = input("Enter label to search for:")

        # if end is entered, searching is ended
        if finder == "end":
            print("Ending...")
            break

        # enter number of pages input
        number = input("Enter number of pages:")

        # check different cases of number imputs
        if number == "all":
            num = 10000
            print("Searching for all: " + finder + "pages...")
        else:
            num = int(number)
            print("Searching for: " + finder + " " + number + " pages...")


        # create query
        query_all = {
            'size': num,
            'query': {
                'match_phrase': {
                    'Label': finder
                }
            }
        }

        # search query
        resp = es.search(
            index="docs",
            body=query_all,
            request_timeout=30
        )

        # check if there are any results
        if resp['hits']['total']['value'] == 0:
            # no results for label
            print("Nothing found! Try something different...")
        else:
            # print results
            print("Results:")
            iterator = len(resp['hits']['hits'])
            for it in range(iterator):
                print(json.dumps(resp['hits']['hits'][it]['_source'], indent=4, ensure_ascii=False))


    json_data.close()
