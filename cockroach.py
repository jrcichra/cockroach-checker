def was_cockroach_updated():
    import requests
    from datetime import datetime
    from lxml import html
    COCKROACH_URL = f"https://www.cockroachlabs.com/docs/releases/index.html"
    FILE = "last.dat"

    page = requests.get(COCKROACH_URL)
    tree = html.fromstring(page.content)
    releases = tree.xpath(
        '/html/body/div[2]/div/main/div[3]/table[1]/tbody/tr')

    versions = []

    for release in releases:
        i = 0
        record = {}
        for columns in release.getchildren():
            if i == 0:
                record['version'] = str(
                    columns.text_content()).strip().split(' ')[0].strip()
            if i == 1:
                date = str(columns.text_content()).strip()
                record['date'] = datetime.strptime(
                    date, '%b %d, %Y').strftime("%c")
            i += 1
        versions.append(record)

    last = f"{versions[0]['version']},{versions[0]['date']}"

    # check if the last one matches what's on disk (prev)
    prev = ""
    try:
        with open(FILE, "r") as f:
            prev = f.read()
    except FileNotFoundError as e:
        pass

    ret = "NO"
    if last != prev:
        ret = last
        with open(FILE, "w") as f:
            f.write(last)
    return ret
