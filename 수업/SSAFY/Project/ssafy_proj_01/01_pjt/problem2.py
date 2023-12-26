import pprint
import requests



def get_deposit_products():
  api_key="8c440e5adde726eb5ec0b1d4e7540fd1"
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
  response = requests.get(url).json()
  return response['result']['baseList']

    
if __name__ == '__main__':

    result = get_deposit_products()
    pprint.pprint(result)