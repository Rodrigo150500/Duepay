from .search_for_xml import SearchForXML

def test_search():


    #Input
    #if cpf: str or total: float
    repo = SearchForXML(10.10)
    repo.search()

    