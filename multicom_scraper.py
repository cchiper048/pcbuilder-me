from bs4 import BeautifulSoup
import requests
import re

def parse_multicom(file, url, page_end, page_start=1, start_text = '', min_price=0, max_price=9999):
    data_to_write = start_text

    for page_number in range(page_start, page_end + 1):
        page_url = re.sub('page-replace', str(page_number), url)
        multicom_scrape = requests.get(page_url).text

        soup = BeautifulSoup(multicom_scrape, 'lxml')
        artikli = soup.find_all('div', class_ = 'artikal-n d-flex flex-column col-4 mb-2 p-3')

        for artikal in artikli:
            ime = artikal.find('h2').text
            cijena = "".join(artikal.find('p', class_ = 'cijenaGotovina').text.split())
            artikal_data = " ".join((ime + ' - ' + cijena).split())
            data_to_write += artikal_data + '\n'

    file_open = open(file, 'w')
    file_open.write(data_to_write)
    file_open.close()


# parse_multicom(
#     start_text='Graficke kartice: \n',
#     file='./data/graficke.txt', 
#     url='https://www.multicom.me/racunari-i-oprema/graficke-kartice/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=3,
#     page_end=6
#     )

# parse_multicom(
#     start_text='Maticne ploce: \n',
#     file='./data/maticne_ploce.txt', 
#     url='https://www.multicom.me/racunari-i-oprema/maticne-ploce/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=3,
#     page_end=6,
#     )

# parse_multicom(
#     start_text='Napajanja: \n',
#     file='./data/napajanje.txt', 
#     url='https://www.multicom.me/racunari-i-oprema/napajanje/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=2,
#     page_end=5
#     )

# parse_multicom(
#     start_text='Ram memorije: \n',
#     file='./data/ram.txt', 
#     url='https://www.multicom.me/racunari-i-oprema/memorija/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=3,
#     page_end=7
#     )

# parse_multicom(
#     start_text='Ssd diskovi: \n',
#     file='./data/ssd.txt',
#     url='https://www.multicom.me/racunari-i-oprema/ssd-disk/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=2,
#     page_end=5
#     )

# parse_multicom(
#     start_text='Procesori: \n',
#     file='./data/procesori.txt',
#     url='https://www.multicom.me/racunari-i-oprema/procesori/svi.html?page=page-replace&vrstaprikaza=kocka',
#     page_start=2,
#     page_end=5
#     )

# parse_multicom(
#     start_text='Kuleri za procesor: \n',
#     file='./data/kuleri.txt',
#     url='https://www.multicom.me/racunari-i-oprema/kuler-za-procesor/svi.html?page=page-replace&pretraga=hladjenje&vrstaprikaza=kocka',
#     page_end=2
#     )

# parse_multicom(
#     start_text='Kucista: \n',
#     file='./data/kucista.txt',
#     url='https://www.multicom.me/racunari-i-oprema/kucista/svi.html?page=page-replace&pretraga=kuciste&vrstaprikaza=kocka',
#     page_start=2,
#     page_end=5
#     )

