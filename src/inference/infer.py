import requests
import json

MODEL_DEFAULT: str = "llama3.2:1b"
LLM_ENDPOINT: str = "http://localhost:11434/api/generate"

GEN_REQ_DATA: dict[str, str | bool] = {
    "model": MODEL_DEFAULT,
    "prompt": "",
    "stream": False
}

HEADER_DEFAULT: dict[str, str] = {
    "Content-Type": "application/json"
}

def _llm_get(query: str) -> dict | str:
    _data = GEN_REQ_DATA
    _data["prompt"] = query

    r = requests.post(url=LLM_ENDPOINT, data=json.dumps(_data), headers=HEADER_DEFAULT)
    # if r.status_code != 200:
    #     raise requests.RequestException("Received status code: %d" % r.status_code)

    # return json.loads(r.text)
    return r.text

def _prompt(query: str, sources: str) -> str:
    return \
    """
    input: %s

    sources: %s

    evaluate the sources' claim and analyze the validity of the input.
    """ % (query, sources)


def infer(_input: str, sources: str) -> tuple[object, str]:
    llm_out: dict = _llm_get(_prompt(_input, sources))
    ddg_sum: str = ""

    return llm_out, ddg_sum
