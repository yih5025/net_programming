import requests, time
import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.Pool(processes=5, initializer=set_global_session) as pool:
        pool.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr/iot",
        "https://home.sch.ac.kr/bigdata"
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time

    print(f"Download {len(sites)} in {duration} seconds")