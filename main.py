from urllib.request import Request, urlopen

def fetch_random_dad_joke() -> str:
    """
    This will give a conflict.

    Made in the master branch.
    """
    req = Request(
        url="https://icanhazdadjoke.com/",
        headers={
            "Accept": "text/plain",
            "User-Agent": "Workshop"
        }
    )
    return urlopen(req).read().decode("utf-8")

print(fetch_random_dad_joke())