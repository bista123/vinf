# coding=utf-8
import re
import codecs
import json


class Page:

    def __init__(self, name):
        self.name = name
        self.ID = ""
        self.Label = ""
        self.Categories = []
        self.Links = []

    def save_file(self):
        # filename = self.name + '.txt'
        #
        # with open(filename, 'w') as outfile:
        #     json.dump(self.__dict__, outfile)
        # y = y.encode().decode('utf8')
        # x = y.encode('utf8')
        y = json.dumps(self.__dict__, ensure_ascii=False).encode('utf8')
        print(y.decode())


# Function to parse page ids
def parse_ids():
    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/page_ids_sk.ttl', 'r', encoding='utf-8')
    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_ids.csv', 'w', encoding='utf-8')
    lines = ttl_file.readlines()

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\^\^\<.*\> .", line)
            if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                    or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                    or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
                continue
            elif pattern.group(1).__contains__(':'):
                csv_file.write(pattern.group(1) + "\t" + "ID: " + pattern.group(2) + "\n")
            else:
                continue
            # print(pattern.group(1), pattern.group(2))
        except:
            continue

    ttl_file.close()
    csv_file.close()


# Function to parse labels
def parse_labels():
    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/labels_sk.ttl', 'r', encoding='utf-8')
    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/labels.csv', 'w', encoding='utf-8')
    lines = ttl_file.readlines()

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\@sk .", line)
            if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                    or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                    or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
                continue
            elif pattern.group(1).__contains__(':'):
                csv_file.write(pattern.group(1) + "\t" + "Label: " + pattern.group(2) + "\n")
            else:
                continue
            # print(pattern.group(1), pattern.group(2))
        except:
            continue

    ttl_file.close()
    csv_file.close()


# Function to parse article categories
def parse_categories():
    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/article_categories_sk.ttl',
                           'r',
                           encoding='utf-8')
    lines = ttl_file.readlines()
    categories = {}

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \<.*\/Kategória\:(.*)\> .", line)
            # print(pattern.group(1), pattern.group(2))
            if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                    or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                    or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
                continue
            elif pattern.group(1).__contains__(':'):
                if pattern.group(1) in categories.keys():
                    if pattern.group(2) not in categories[pattern.group(1)]:
                        categories[pattern.group(1)].append(pattern.group(2))
                else:
                    categories[pattern.group(1)] = [pattern.group(2)]
            else:
                continue
        except:
            continue

    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/article_categories.csv',
                           'w',
                           encoding='utf-8')

    for label, category in categories.items():
        tostr = ' '.join(map(str, category))
        csv_file.write(label + "\t" + "Kategorie: " + tostr + "\n")

    ttl_file.close()
    csv_file.close()


# Function to parse page links
def parse_links():
    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/page_links_sk.ttl',
                           'r',
                           encoding='utf-8')
    lines = ttl_file.readlines()
    links = {}

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \<(.*)\> .", line)
            # print(pattern.group(1), pattern.group(2))
            if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                    or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                    or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
                continue
            elif pattern.group(1).__contains__(':'):
                if pattern.group(1) in links.keys():
                    if pattern.group(2) not in links[pattern.group(1)]:
                        links[pattern.group(1)].append(pattern.group(2))
                else:
                    links[pattern.group(1)] = [pattern.group(2)]
            else:
                continue
        except:
            continue

    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_links.csv', 'w', encoding='utf-8')

    for label, link in links.items():
        tostr = ' '.join(map(str, link))
        csv_file.write(label + "\t" + "Linky: " + tostr + "\n")

    ttl_file.close()
    csv_file.close()


# Function to parse and merge together all previously created temporary csv files
def merge_together():
    files = ['page_ids.csv', 'labels.csv', 'article_categories.csv', 'page_links.csv']
    labels = ['ID', 'Label', 'Kategorie', 'Linky']
    output = {}

    for file, label in zip(files, labels):

        parse_file = codecs.open(f'D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/{file}', 'r', encoding='utf-8')
        lines = parse_file.readlines()

        for line in lines:
            try:
                pattern = re.match(r"^(.+)\t(.*)$", line)
                # print(pattern.group(1), pattern.group(2))

                if pattern.group(1) in output.keys():
                    output[pattern.group(1)][label] = [pattern.group(2)]
                else:
                    output[pattern.group(1)] = {}
                    output[pattern.group(1)][label] = [pattern.group(2)]
            except:
                continue

        parse_file.close()

    # output_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/dictionaries.csv',
    #                           'w',
    #                           encoding='utf-8')
    #
    # for upper_label, lower_label in output.items():
    #     output_file.write(upper_label + ":" + "\n")
    #     for label, value in lower_label.items():
    #         output_file.write("  " + label + ": " + value[0] + "\n")
    #
    # output_file.close()

    for upper_label, lower_label in output.items():
        # output_file.write(upper_label + ":" + "\n")
        name = upper_label
        obj = Page(name)
        for label, value in lower_label.items():
            if label == "ID":
                obj.idd = value
            elif label == "Label":
                obj.label = value
            elif label == "Kategorie":
                obj.categories = value
            elif label == "Linky":
                obj.links = value

        obj.save_file()


if __name__ == '__main__':
    print("Starting parsing...")

    # parse_ids()
    # parse_labels()
    # parse_categories()
    parse_links()
    #
    # merge_together()

    print("Parsing done!")
