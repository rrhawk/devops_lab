def get_pulls(state, rj):
    ls = []

    def add_pulls(j):
        pulls = {
            "num": j["number"],
            "title": j["title"],
            "link": j["html_url"]
        }
        return ls.append(pulls)
    for i in rj:
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
