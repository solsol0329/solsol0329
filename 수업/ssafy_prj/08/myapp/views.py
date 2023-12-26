from django.http import JsonResponse
import csv
import pandas as pd

def readcsv(request):
    df = pd.read_csv("data/test_data.CSV", encoding='utf-8')
    data = df.to_dict('records')
    return JsonResponse({'data':data})


def process(request):
    df = pd.read_csv("data/test_data.CSV",encoding='utf-8')
    df.fillna("NULL",  inplace=True)
    data = df.to_dict("records")
    return JsonResponse({'data':data})

def avg(request):
    df = pd.read_csv("data/test_data.CSV",encoding='utf-8')
    
    avg = df["나이"].mean(numeric_only=True)

    df["close_avg"] = abs(df["나이"]-avg)
    data = df.nsmallest(10,"close_avg").to_dict("records")
    
    return JsonResponse({"data":data})

