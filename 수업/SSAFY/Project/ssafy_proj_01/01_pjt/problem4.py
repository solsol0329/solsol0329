import pprint
import requests

# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():

    api_key="8c440e5adde726eb5ec0b1d4e7540fd1"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    result_full=response['result']
    option_info_full = result_full['optionList']
    base_info_full = result_full['baseList']
    finace_code_list=[]
    option_list=[]
    

    for i in range(len(base_info_full)):
        finace_code={}
        for j in range(len(base_info_full)):
            if base_info_full[j]['fin_prdt_cd'] == base_info_full[i]['fin_prdt_cd']:
                option_info={}
                option_info['저축 기간'] = option_info_full[j]['save_trm']
                option_info['저축금리유형'] = option_info_full[j]['intr_rate_type']
                option_info['저축금리유형명'] = option_info_full[j]['intr_rate_type_nm']
                option_info['최고 우대금리'] = option_info_full[j]['intr_rate2']  
                option_list.append(option_info)
                finace_code['금리정보']=option_list
        finace_code['금융상품명']=base_info_full[i]['fin_prdt_nm']
        finace_code['금융회사명']=base_info_full[i]['kor_co_nm']
        finace_code_list.append(finace_code)
               
    return(finace_code_list)
       
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)       
