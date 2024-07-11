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
    except urllib.error.HTTPError as http_error:
        print(utils.Color.format_error(http_error))
        exit(1)
    except urllib.error.URLError as url_error:
        print(utils.Color.format_error(url_error))
        exit(1)
    except Exception as error:
        print(utils.Color.format_error(error))
        exit(1)
