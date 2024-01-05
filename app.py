from flask import Flask, jsonify
import requests, os

app = Flask(__name__)

gh_token = os.environ["GH_TOKEN"]
url = "https://api.github.com/users"
headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {gh_token}",
    "Accept": "application/vnd.github+json",
}


# Validates request url, catch HTTP error if any.
def validate_request(user):
    try:
        r = requests.get(f"{url}/{user}/gists", headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error")
        return (r, err)
    return r, {"error": None}


# By default, github api returns 30 gists per page, response may came in many pages.
# this function calculates number of pages.
def get_last_page_number(response):
    try:
        if response.links != {}:
            last_page = response.links["last"]["url"].split("=")
            last_page = int(last_page[len(last_page) - 1])
        else:
            last_page = 1  # when only one page, response.links returns empty i.e. {}
        return last_page
    except Exception as e:
        print("Error while getting last page number ", e)


# gets gists data per page.
def get_data_per_page(user, page):
    try:
        r = requests.get(f"{url}/{user}/gists?page={page}")
        return [{"url": i["url"], "html_url": i["html_url"]} for i in r.json()]
    except Exception as e:
        print(f"Error while fetching gists data on page {page}", e)


# main function
@app.route("/users/<string:user>/", methods=["GET"])
def get_data_all_page(user):
    try:
        r, error = validate_request(user)
        if r.status_code != 200:
            print(r.status_code)
            return (str(error), r.status_code)

        l = []
        # loop over number of pages to get gists data for each page, aggregate all data in last.
        for page in range(1, get_last_page_number(r) + 1):
            l.extend(get_data_per_page(user, page))
        return jsonify(l), 200
    except Exception as e:
        print("Error while fetching gists data in main function", e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
