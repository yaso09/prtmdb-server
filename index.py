from flask import *
import requests, os, json, base64

api = "https://script.google.com/macros/s/" + "AKfycbzdM9K9BO3CLVK2Wyd-AJCMTpil1VLPbukygTABw32rUdJtifoghZhcBsr_iqiOyEo7UA" + "/exec"

app = Flask(__name__)


def decomp(arr):
    if not arr:
        return []
    keys = list(arr[0].keys())
    res = [keys, *(list(obj.values()) for obj in arr)]
    return res

def toDataURI(txt: str, type="text/plain"):
    # Text to base64
    txtToBase64 = base64.b64encode(txt.encode()).decode("utf-8")
    data_uri = f"data:{type};base64,{txtToBase64}"
    return data_uri

# Web Site

def getReadme(lang):
    readme_path = os.path.join(
        os.path.dirname(__file__), f"README.{lang}.md"
    )
    with open(readme_path, "r", encoding="utf-8") as file:
        if file.readable():
            return toDataURI(file.read())
        else:
            with open(readme_path.replace(f"README.{lang}.md", "404.md"), "r") as f404:
                return toDataURI(f404.read())


@app.route("/")
def master():
    return """
        <script>window.location.href = navigator.language.split("-")[0];</script>
    """

@app.route("/<lang>")
def master2(lang):
    return render_template("index.html", readme=getReadme(lang), lang=lang)

@app.errorhandler(404)
def not_found(err):
    return err



# API

@app.route("/api/<req>", methods=["GET", "POST"])
def api_req(req):
    if request.method == "POST":
        if param == "insertsheet":
            pass
        
        res = requests.post(
            f"{api}?id={req}&type=create",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps(decomp(request.get_json())[1:])
        )
        return json.loads(res.content)
    if request.method == "PATCH":
        row = request.get_json()
        row = row[0]
        column = decomp(request.get_json()[1:])[1]
        
        res = requests.post(
            f"{api}?id={req}&type=update&row={row}&column={column}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps(decomp(request.get_json()[1:])[1:])
        )
        return json.loads(res.content)
    if request.method == "DELETE":
        dat = request.get_json()
        dat = dat[0]
        res = requests.post(
            f"{api}?id={req}&type=delete&row={dat}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data="empty"
        )
        return json.loads(res.content)
    res = requests.get(f"{api}?id={req}")
    try:
        return json.loads(res.content)
    except: pass
    return json.loads('{"error": 1}')

@app.route("/api/<req>/<param>", methods=["GET", "POST", "DELETE", "PATCH"])
def api_req_param(req, param):
    if request.method == "POST":
        if param == "insertsheet":
            pass
        res = requests.post(
            f"{api}?id={req}&sheet={param}&type=create",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps(decomp(request.get_json())[1:])
        )
        return json.loads(res.content)
    if request.method == "PATCH":
        row = request.get_json()
        row = row[0]
        column = decomp(request.get_json()[1:])[1]
        res = requests.post(
            f"{api}?id={req}&sheet={param}&type=update&row={row}&column={column}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps(decomp(request.get_json()[1:])[1:])
        )
        return json.loads(res.content)
    if request.method == "DELETE":
        dat = request.get_json()
        dat = dat[0]
        
        res = requests.post(
            f"{api}?id={req}&sheet={param}&type=delete&row={dat}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data="empty"
        )
        return json.loads(res.content)
    res = requests.get(f"{api}?id={req}&sheet={param}")
    try:
        return json.loads(res.content)
    except: pass
    return json.loads('{"error": 1}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)