# script for testing regexes

import re
import sys

if __name__ == '__main__':

    # regex for label
    label = '<http://sk.dbpedia.org/resource/Main_Page> <http://www.w3.org/2000/01/rdf-schema#label> "Main Page"@sk .'
    label_pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\@sk .", label)

    # regex for id
    id = '<http://sk.dbpedia.org/resource/Egon_Gál> <http://dbpedia.org/ontology/wikiPageID> "1676"^^<http://www.w3.org/2001/XMLSchema#integer> .'
    id_pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\^\^\<.*\> .", id)

    # regex for link
    link = '<http://sk.dbpedia.org/resource/Main_Page> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://sk.dbpedia.org/resource/Hlavná_stránka> .'
    link_pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \<(.*)\> .", link)

    # regex for category
    category = '<http://sk.dbpedia.org/resource/Isaac_Newton> <http://purl.org/dc/terms/subject> <http://sk.dbpedia.org/resource/Kategória:Narodenia_v_1643> .'
    category_pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \<.*\/Kategória\:(.*)\> .", category)

    # test all regexes one by one
    if label_pattern.group(1) == "Main_Page" and label_pattern.group(2) == 'Main Page':
        if id_pattern.group(1) == "Egon_Gál" and id_pattern.group(2) == '1676':
            if link_pattern.group(1) == "Main_Page" and link_pattern.group(2) == 'http://sk.dbpedia.org/resource/Hlavná_stránka':
                if category_pattern.group(1) == "Isaac_Newton" and category_pattern.group(2) == 'Narodenia_v_1643':
                    # all regexes have passed the test
                    print('All tests passed!')
                else:
                    sys.exit("Category regex not passed!")
            else:
                sys.exit("Link regex not passed!")
        else:
            sys.exit("ID regex not passed!")
    else:
        sys.exit("Label regex not passed!")
