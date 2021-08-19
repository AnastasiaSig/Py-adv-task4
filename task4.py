import json
import requests

class Countries:
    def __init__(self):
        with open('countries.json', 'r', encoding='UTF-8') as f:
            self.data = json.load(f)

    URL = 'https://en.wikipedia.org/wiki'
    def get_link(self, country):
        l = country.split()
        sl = '_'.join(l)
        response = requests.get(f'{self.URL}/{sl}')
        if response.ok:
            link = f'{self.URL}/{sl}'
            return link

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > len(self.data) - 1:
            raise StopIteration
        else:
            country = self.data[self.index]['name']['common']
            link = self.get_link(country)
            result = f'{country} - {link}\n'
            with open('countries_wikipedia.txt', "a", encoding='UTF-8') as file:
                file.write(result)
            self.index += 1

for country in Countries():
    country