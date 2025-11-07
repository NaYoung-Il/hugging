import os
import urllib.request

DATA_DIR = os.path.expanduser("~/.pytorch_datasets")
os.makedirs(DATA_DIR, exist_ok=True)

TRAIN_URL = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt"
TEST_URL = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt"

DATA_TRAIN_PATH = os.path.join(DATA_DIR, "ratings_train.txt")
DATA_TEST_PATH = os.path.join(DATA_DIR, "ratings_test.txt")
print("현재 작업 디렉토리:", os.getcwd())
print("파일 저장 경로:", DATA_TEST_PATH)

def download_if_not_exists(url: str, path: str):
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
        return f"{os.path.basename(path)} 다운로드 완료"
    return f" {os.path.basename(path)} 이미 존재함"


def download_nsmc():
    train_msg = download_if_not_exists(TRAIN_URL, DATA_TRAIN_PATH)
    test_msg = download_if_not_exists(TEST_URL, DATA_TEST_PATH)
    return {
        "train_status": train_msg,
        "test_status": test_msg,
        "train_path": DATA_TRAIN_PATH,
        "test_path": DATA_TEST_PATH,
    }