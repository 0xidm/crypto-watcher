import requests


class Subgraph(object):
    def __init__(self, url, debug=False):
        self.url = url
        self.debug = debug

    # function to use requests.post to make an API call to the subgraph url
    def run_query(self, query):
        request = requests.post(self.url, '', json={'query': query})

        if request.status_code == 200:
            return request.json()
        else:
            raise Exception('Query failed. return code is {}'.format(request.status_code))
