import urllib.error
import urllib.request
import utils


def download_url(url, filepath):
    headers = {"User-Agent": "Python urllib"}
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response, open(
            filepath, "wb"
        ) as output:
            data = response.read()
            output.write(data)
        print(f" downloaded file: {filepath}")
    except urllib.error.HTTPError as http_error:
        print(f"{utils.Color.make_red("error downloading file")}: {http_error}")
        exit(1)
    except urllib.error.URLError as url_error:
        print(f"{utils.Color.make_red("error downloading file")}: {url_error}")
        exit(1)
    except Exception as error:
        print(f"{utils.Color.make_red("error downloading file")}: {error}")
        exit(1)
