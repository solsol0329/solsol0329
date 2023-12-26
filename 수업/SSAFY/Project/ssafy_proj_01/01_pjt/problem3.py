import pprint
import requests


def get_deposit_products():
  api_key="8c440e5adde726eb5ec0b1d4e7540fd1"
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
  response = requests.get(url).json()
  result_full=response['result']['optionList']
  
  result=[]

  for i in range(len(result_full)):
    result_dict={}
    result_dict['금융상품코드'] = result_full[i]['fin_prdt_cd']
    result_dict['저축 금리'] = result_full[i]['intr_rate']
    result_dict['저축 기간'] = result_full[i]['save_trm']
    result_dict['저축금리유형'] = result_full[i]['intr_rate_type']
    result_dict['저축금리유형명'] = result_full[i]['intr_rate_type_nm']
    result_dict['최고 우대금리'] = result_full[i]['intr_rate2']
  
    result.append(result_dict)

  return result


if __name__ == '__main__':

    result = get_deposit_products()
    pprint.pprint(result)