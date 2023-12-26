from django.shortcuts import render
from django.conf import settings
from .models import DepositOptions, DepositProduct
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status


# BASE_URL = "https://fss.or.kr/finlife/finlifeapi/"


@api_view(["GET"])
def list(request):
    api_key = settings.API_KEY
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    print(url)
    response = requests.get(url).json()

    return Response(response)


@api_view(["GET"])
def save_prdt(request):
    api_key = settings.API_KEY
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

    response = requests.get(url).json()


    for product in response.get("result").get("baseList"):
        save_data = {
            "fin_prdt_cd" : product.get("fin_prdt_cd"),
            "kor_co_nm" : product.get("kor_co_nm"),
            "fin_prdt_nm" : product.get("fin_prdt_nm"),
            "etc_note" : product.get("etc_note"),
            "join_deny" : product.get("join_deny"),
            "join_member" : product.get("join_member"),
            "join_way" : product.get("join_way"),
            "spcl_cnd" : product.get("spcl_cnd"),
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    for option in response.get("result").get("optionList"):
        fin_prdt_cd = option.get("fin_prdt_cd")
        intr_rate_type_nm = option.get("intr_rate_type_nm")
        intr_rate = option.get("intr_rate")
        intr_rate2 = option.get("intr_rate2")
        save_trm = option.get("save_trm")

        deposit_product = DepositProduct.objects.filter(fin_prdt_cd=fin_prdt_cd)[0]
        if DepositOptions.objects.filter(product=deposit_product.pk,
                                         intr_rate_type_nm=intr_rate_type_nm,
                                        intr_rate=intr_rate,
                                        intr_rate2=intr_rate2,
                                        save_trm=save_trm).exists():
            continue

        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=deposit_product)
        
    return JsonResponse({"message":"저장완료"})



@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = DepositProduct.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DepositProductsSerializer(data=request.data)
        message = {
            "fail" : "실패!!!"
        }
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(message)
    

@api_view(["GET"])
def option_list(request, fin_prdt_cd):
    product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
    deposit_options = product.options.all()
    serializer = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializer.data)
    


# @api_view(["GET"])
# def top_rate(request):
#     max_rate = 0
#     option_fin_prdt_cd = ""
#     db_options = DepositOptions.objects.all()
#     for option in db_options:
#         if max_rate < option.intr_rate:
#             max_rate =option.intr_rate
#             option_fin_prdt_cd = option.fin_prdt_cd

#     product = DepositProduct.objects.get(fin_prdt_cd=option_fin_prdt_cd)
#     option = DepositOptions.objects.get(fin_prdt_cd=option_fin_prdt_cd)
    

@api_view(["GET"])
def top_rate(request):
    # ORM 문법을 잘 찾아보자! 
    option = DepositOptions.objects.order_by('-intr_rate2').first()
    serializer_o = DepositOptionsSerializer(option)
    serializer_p = DepositProductsSerializer(option.product)

    serializer = {
        'deposit_product': serializer_p.data,
        'options': serializer_o.data
        }
    return Response(serializer)