

class SearchPageResultDto:
    def __init__(self, **kwargs):
        self.page_size = kwargs.get('page_size', 0)
        self.page_number = kwargs.get('page_number', 0)
        self.total_elements = kwargs.get('total_elements', 0)
        self.elements = kwargs.get('elements', [])
