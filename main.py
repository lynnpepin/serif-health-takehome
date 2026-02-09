import json
import os, sys
import json_stream
import httpx
import gzip
import time

url_set = set()
url_list = []



def tst( ts_json_object):
    # Utility function since I'll be using this a lot
    return json_stream.to_standard_types(ts_json_object)

def ein_lookup(ein):
    req = httpx.get(f"https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/{ein}.json")
    if req.status_code == 200:
        return json.loads(req.text)

def _get_json_gz(url):
    return json.loads(gzip.decompress(httpx.get(url).content))

def _collapse(string: str):
    return string.lower().strip().replace(' ','')


def _strip_url(url):
    if "?" in url:
        return url.split("?")[0]
    else:
        return url

def _add_url(url):
    stripped = _strip_url(url)
    if not stripped in url_set:
        url_set.add(stripped)
        url_list.append(url)

def _is_ein_anthem(ein):
    'anthem' in _collapse(str(ein_lookup(ein)))

def is_plan_anthem(plan):
    # check first for 'anthem' in plan name, issuer name, etc
    for key in ['plan_name', 'issuer_name', 'plan_sponsor_name']:
        if 'anthem' in _collapse(plan.get(key, '')):
            return True
    
    # failing that, look up the EIN and check for references there
    if plan.get('plan_id_type', '') == 'EIN':
        return _is_ein_anthem(plan.get('plan_id',0))
    
    return False

def collect_urls_from_one_reporting_structure(reporting_structure):
    is_anthem = False
    
    for plan in reporting_structure['reporting_plans']:
        if is_plan_anthem(plan):
            is_anthem = True
            break
    
    if is_anthem:
        # one of the entries are anthem, so let's add all of them
        for entry in reporting_structure['in_network_files']:
            _add_url(entry.get('location',''))


def main():
    ff = open("anthem_index.json", "r")
    index = json_stream.load(ff)
    url_set = set()
    url_list = []
    start = time.time()

    for ii, reporting_structure in enumerate(index['reporting_structure']):
        if ii % 1000 == 0:
            print(f"index {ii:> 4}")
        collect_urls_from_one_reporting_structure(tst(reporting_structure))
    
    end = time.time()
    with open("url_list.txt", "w") as ff:
        for url in url_list:
            ff.write(url)
            ff.write("\n")
    with open("url_set.txt", "w") as ff:
        for url in url_set:
            ff.write(url)
            ff.write("\n")        
    print(f"Done in {round(end-start)} seconds")


if __name__ == "__main__":
    main()
