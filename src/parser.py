import re
import codecs


def parse_ids():

    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_ids_sample.ttl', 'r', encoding='utf-8')
    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_ids.csv', 'w', encoding='utf-8')

    lines = ttl_file.readlines()

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)?\> \<.*\> \"(.*)\"\^\^\<.*\> .", line)
            csv_file.write(pattern.group(1) + "\t" + pattern.group(2) + "\n")
            # print(pattern.group(1), pattern.group(2))
        except:
            continue

    ttl_file.close()
    csv_file.close()


def parse_labels():

    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/labels_sample.ttl', 'r', encoding='utf-8')
    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/labels.csv', 'w', encoding='utf-8')

    lines = ttl_file.readlines()

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)?\> \<.*\> \"(.*)\"\@sk .", line)
            csv_file.write(pattern.group(1) + "\t" + pattern.group(2) + "\n")
            # print(pattern.group(1), pattern.group(2))
        except:
            continue

    ttl_file.close()
    csv_file.close()


def parse_categories():

    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/article_categories_sample.ttl',
                           'r',
                           encoding='utf-8')

    lines = ttl_file.readlines()
    categories = {}

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)?\> \<.*\> \<.*\/Kategória\:(.*)\> .", line)
            # print(pattern.group(1), pattern.group(2))

            if pattern.group(1) in categories.keys():
                if pattern.group(2) not in categories[pattern.group(1)]:
                    categories[pattern.group(1)].append(pattern.group(2))
            else:
                categories[pattern.group(1)] = [pattern.group(2)]
        except:
            continue

    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/article_categories.csv',
                           'w',
                           encoding='utf-8')

    for label, category in categories.items():
        tostr = ' '.join(map(str, category))
        csv_file.write(label + "\t" + tostr + "\n")

    ttl_file.close()
    csv_file.close()


def parse_links():

    ttl_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_links_sample.ttl',
                           'r',
                           encoding='utf-8')

    lines = ttl_file.readlines()
    links = {}

    for line in lines:
        try:
            pattern = re.match(r"^\<.*resource\/(.*)?\> \<.*\> \<(.*)\> .", line)
            # print(pattern.group(1), pattern.group(2))

            if pattern.group(1) in links.keys():
                if pattern.group(2) not in links[pattern.group(1)]:
                    links[pattern.group(1)].append(pattern.group(2))
            else:
                links[pattern.group(1)] = [pattern.group(2)]
        except:
            continue

    csv_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/page_links.csv', 'w', encoding='utf-8')

    for label, link in links.items():
        tostr = ' '.join(map(str, link))
        csv_file.write(label + "\t" + tostr + "\n")

    ttl_file.close()
    csv_file.close()


def merge_together():

    files = ['page_ids.csv', 'labels.csv', 'article_categories.csv', 'page_links.csv']
    labels = ['ID', 'Značka', 'Kategórie', 'Linky']
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

    output_file = codecs.open('D:/Jakub/FIIT/ING/2/VINF/vinf_project/vinf/data/dictionaries.csv',
                              'w',
                              encoding='utf-8')

    for upper_label, lower_label in output.items():
        output_file.write(upper_label + ":" + "\n")
        for label, value in lower_label.items():
            output_file.write("  " + label + ": " + value[0] + "\n")

    output_file.close()


if __name__ == '__main__':

    print("Starting parsing...")

    parse_ids()
    parse_labels()
    parse_categories()
    parse_links()

    merge_together()

    print("Parsing_done")

