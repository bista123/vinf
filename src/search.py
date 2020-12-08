from elasticsearch import Elasticsearch, helpers
import sys, json
import os

# get filename, author, title, from command line
fileName = 'D:/Jakub/FIIT/ING/2/VINF/part-00000'


def create_stats(input_file):

    counter = 0
    empty_ID = 0
    empty_label = 0
    empty_cats = 0
    empty_links = 0

    max_cats = 0
    max_cats_page = ""
    max_links = 0
    max_links_page = ""

    for lineText in input_file:
        counter += 1
        lineText.strip()

        try:
            json_file = json.loads(lineText)
        except:
            continue


        try:
            if json_file['ID'] == "":
                empty_ID += 1
            if json_file['Label'] == "":
                empty_label += 1

            if len(json_file['Categories']) == 0:
                empty_cats += 1
            elif len(list(json_file['Categories'].split(" "))) > max_cats:
                max_cats = len(list(json_file['Categories'].split(" ")))
                if json_file['Label'] != "":
                    max_cats_page = json_file['Label']
                elif json_file['ID'] != "":
                    max_cats_page = json_file['ID']

            if not json_file['Links']:
                empty_links += 1
            elif len(list(json_file['Links'].split(" "))) > max_links:
                max_links = len(list(json_file['Links'].split(" ")))
                if json_file['Label'] != "":
                    max_links_page = json_file['Label']
                elif json_file['ID'] != "":
                    max_links_page = json_file['ID']
        except:
            continue

    print("")
    print("Celkovy pocet stranok: " + str(counter))

    print("")
    print("Pocet stranok bez id: " + str(empty_ID) + " Podiel: " + str(empty_ID/counter) + "%")
    print("Pocet stranok bez labelu: " + str(empty_label) + " Podiel: " + str(empty_label/counter) + "%")
    print("Pocet stranok bez kategorii: " + str(empty_cats) + " Podiel: " + str(empty_cats/counter) + "%")
    print("Pocet stranok bez linkov: " + str(empty_links) + " Podiel: " + str(empty_links/counter) + "%")

    print("")
    print("Stranka s najvacsim poctom kategorii je: " + max_cats_page + " so " + str(max_cats) + " kategoriami")
    print("Stranka s najvacsim poctom linkov je: " + max_links_page + " s " + str(max_links) + " linkami")

if __name__ == '__main__':

    json_data = open(fileName, encoding="utf8")

    create_stats(json_data)

    # es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
    #
    # if not es.ping():
    #     raise ValueError("Connection failed")



    # es = Elasticsearch()
    #
    # filedata = open(fileName)
    # lineNum = 0  # line number including empty lines
    # txtNum = 0  # line number of non-empty lines
    #
    # try:
    #     for lineText in filedata:
    #         lineText.strip()
    #         lineText = lineText[:-1]
    #         lineNum += 1
    #         json_file = json.loads(lineText)
    #
    #         helpers.bulk(es, json_file, index='Label')
    # except UnicodeDecodeError as e:
    #     print("Decode error at: " + str(lineNum) + ':' + str(txtNum))
    #     print(e)


    json_data.close()

