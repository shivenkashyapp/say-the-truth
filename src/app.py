from flask import Flask, request
from inference.infer import infer
from search.search import search_sources

_source_list: list[str] = [
    "altnews.in",
    "thequint.com",
    "m.thewire.in",
    "boomlive.in",
    "dfrac.org"
] 

app = Flask(__name__)

@app.route('', methods=['POST'])
def send_output():
    query: str = request.json.get('input', '')

    output: str = infer(query, search_sources(query, _source_list))

    return output[0]["response"]

if __name__ == '__main__':
    app.run(debug = True)
