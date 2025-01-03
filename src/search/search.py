from duckduckgo_search import DDGS
from pprint import pprint

ENGINE_RESULTS_MAX: int = 40
_engine = DDGS()

def _source_filter(results: list, sources: list[str]) -> list[dict[str, str]]:
    return [result for result in results if any(domain in result["href"] for domain in sources)]

def search(query: str, _topk: int = 5) -> list[dict[str, str]]:
    assert _topk <= ENGINE_RESULTS_MAX, "Can't exceed search query limit. (%d)" % ENGINE_RESULTS_MAX
    return _engine.text(query, max_results=_topk)

def search_sources(query: str, sources: list[str], _topk: int = ENGINE_RESULTS_MAX, _debug: bool = False) -> str:
    _r = _source_filter(search(query, _topk), sources)
    _r = ",".join(("[%s, %s]" % (i["title"], i["body"])) for i in _r)

    if _debug:
        pprint(_r)
        return None

    return _r

def summarize(query: str, model: str) -> str:
    return _engine.chat(query, model)


"""
input: liton das house lit on fire
sources: [{'title': 'No, Viral Pic Doesn’t Show People Setting Liton Das’ House on Fire in ...', 'href': 'https://www.thequint.com/news/webqoof/liton-das-house-set-on-fire-bangladesh-viral-image-mashrafe-mortaza-fact-check', 'body': "Amidst the political turmoil in Bangladesh, a set of images is being shared on social media platforms with a claim that they show Bangladeshi cricketer Liton Das' house being recently set on fire ..."}, {'title': "Cricketer Liton Das' house set afire in Bangladesh? No, viral image ...", 'href': 'https://www.altnews.in/cricketer-liton-das-house-set-afire-in-bangladesh-no-viral-image-shows-narail-residence-of-mashrafe-mortaza/', 'body': 'Therefore, the claim that Liton Das’ house has been set on fire and that the viral image showed Das’ house is false. The viral image showed the house of former cricketer and Awami League MP Mashrafe Bin Mortaza’s house. Donate to Alt News! Independent journalism that speaks truth to power and is free of corporate and political control is possible only when people start contributing towards the same. Please consider donating towards this endeavour to fight fake news and misinformation.'}]

determine if the input is correct based on the sources. explain yourself.
"""
