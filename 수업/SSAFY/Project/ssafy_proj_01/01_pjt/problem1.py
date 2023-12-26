import pprint
import requests



def get_deposit_products():
  api_key="8c440e5adde726eb5ec0b1d4e7540fd1"
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
  response_full = requests.get(url).json()
  response=[]
  response.append(response_full['result'])
  response=dict(*response)
  dict_keys = list(response.keys())
  result = f'dict_keys({dict_keys})'
  return result


    
if __name__ == '__main__':

    result = get_deposit_products()
    pprint.pprint(result)