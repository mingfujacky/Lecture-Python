import requests
from bs4 import BeautifulSoup

def get_latest_invoice_numbers():
    url = "https://invoice.etax.nat.gov.tw/"
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    # 期別
    period = soup.find(title="114年03-04月中獎號碼單")
    print("最新一期：", period.text.strip() if period else "未知")

    # 找到最新一期的號碼區塊
    latest = soup.find("div", class_="container-fluid etw-bgbox mb-4")
    if not latest:
        print("找不到最新一期發票資訊")
        return

# class="font-weight-bold etw-color-red"

    # 特別獎 & 特獎
    special = latest.find_all("span", class_="font-weight-bold etw-color-red")
    print("特別獎：", special[0].text.strip() if special else "未知")
    print("特獎：\t", special[1].text.strip() if special else "未知")

    # 頭獎
    print("頭獎：")
    # 找到標題為"頭獎"的<td>
    td = latest.find("td", class_="text-center", string="頭獎")
    if td:
        # 找到同一列的下一個<td>
        prize_td = td.find_next_sibling("td")
        # 找到所有頭獎號碼的 <p>
        ps = prize_td.find_all("p", class_="etw-tbiggest mb-md-4")
        for p in ps:
            # 合併同一 p 內所有粗體號碼
            bolds = p.find_all("span", class_="font-weight-bold")
            number = ''.join([b.text.strip() for b in bolds])
            print("\t", number)
    else:
        print("頭獎：未知")

if __name__ == "__main__":
    get_latest_invoice_numbers()