import requests

headers = {'Authorization': 'token %s' % "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
           'per_page': 100,
           'state': 'all'}
r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', params=headers)


def get_pulls(state):
    ls = []

    def add_pulls(j):
        pulls = {
            "num": j["number"],
            "title": j["title"],
            "link": j["html_url"]
        }
        return ls.append(pulls)
    for i in r.json():
        if i["labels"]:
            if state == "open":
                if i["state"] == 'open':
                    add_pulls(i)
            elif state == "closed":
                if i["state"] == "closed":
                    add_pulls(i)
            elif state == "accepted":
                if i["labels"][0]["name"] == "accepted":
                    add_pulls(i)
            elif state == "needs work":
                if i["labels"][0]["name"] == "needs work":
                    add_pulls(i)
    return ls
