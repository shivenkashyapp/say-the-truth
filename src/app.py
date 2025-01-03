from flask import Flask, request
from inference.infer import infer
from search.search import search_sources
from flask_cors import CORS

_source_list: list[str] = [
    "altnews.in",
    "thequint.com",
    "m.thewire.in",
    "boomlive.in",
    "dfrac.org"
] 

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/', methods=['POST'])
def send_output():
    query: str = request.json.get('input', '')
    # output: str = infer(query, search_sources(query, _source_list))
    return [{'title': 'No, Viral Pic Doesn’t Show People Setting Liton Das’ House on Fire in ...', 'href': 'https://www.thequint.com/news/webqoof/liton-das-house-set-on-fire-bangladesh-viral-image-mashrafe-mortaza-fact-check', 'body': "Amidst the political turmoil in Bangladesh, a set of images is being shared on social media platforms with a claim that they show Bangladeshi cricketer Liton Das' house being recently set on fire ..."}, {'title': "Cricketer Liton Das' house set afire in Bangladesh? No, viral image ...", 'href': 'https://www.altnews.in/cricketer-liton-das-house-set-afire-in-bangladesh-no-viral-image-shows-narail-residence-of-mashrafe-mortaza/', 'body': 'Therefore, the claim that Liton Das’ house has been set on fire and that the viral image showed Das’ house is false. The viral image showed the house of former cricketer and Awami League MP Mashrafe Bin Mortaza’s house. Donate to Alt News! Independent journalism that speaks truth to power and is free of corporate and political control is possible only when people start contributing towards the same. Please consider donating towards this endeavour to fight fake news and misinformation.'}]

if __name__ == '__main__':
    app.run(debug = True)
