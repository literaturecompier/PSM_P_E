from django.shortcuts import render


from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from django.conf import settings
import pandas as pd

data=pd.read_excel(r'meddra_events.xlsx')
data=data.astype(str)
drug_data=pd.read_csv(r'Products.csv')
drug_data=drug_data.astype(str)
lower_data=data.copy()
for t in lower_data.columns:
    lower_data[t]=lower_data[t].str.lower()

lower_drug_data=drug_data.copy()
for t in lower_drug_data.columns:
    lower_drug_data[t]=lower_drug_data[t].str.lower()


@ensure_csrf_cookie
@csrf_exempt
@api_view(['POST','OPTIONS','GET'])
def get_events(request):
    # print(request.method)
    if request.method == 'POST' or request.method == 'OPTIONS':
        word=str(request.data['search']).lower()
        print(word)
        if word[0]=='%' and word[-1]=='%':
            # print(word[1:-1])
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.contains(word[1:-1],case=False,na=False)
        elif word[0]=='%':
            # print(word[:-1])
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.endswith(word[1:],na=False)
        elif word[-1]=='%':
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.startswith(word[:-1],na=False)
        else:
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.startswith(word,na=False)
        new_data=data[temp_data]
        for t in range(len(new_data)):
            if new_data['LLT_CURRENCY'].iat[t]=='N':
                new_data['LLT_NAME_ENGLISH'].iat[t]='*'+new_data['LLT_NAME_ENGLISH'].iat[t]
        new_data=new_data[['SOC_CODE','SOC_NAME','HLGT_CODE','HLGT_NAME','HLT_CODE','HLT_NAME','PT_CODE','PT_NAME','LLT_CODE','LLT_NAME_ENGLISH']]
        new_data=new_data.set_index('SOC_CODE')
        new_data=new_data.reset_index()
        # print(new_data)
        return JsonResponse({'searched_data':[new_data.loc[_].to_dict() for _ in range(len(new_data))]})

    if request.method == 'GET':
        word=str(request.GET.get('search')).lower()
        print(word)
        print(word[0])
        print(word[-1])
        if word[0]=='%' and word[-1]=='%':
            # print('two ')
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.contains(word[1:-1],case=False,na=False)
        elif word[0]=='%':
            # print('ends')
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.endswith(word[1:],na=False)
        elif word[-1]=='%':
            # print('start')
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.startswith(word[:-1],na=False)
        else:
            # print('regular')
            temp_data=lower_data['LLT_NAME_ENGLISH'].str.startswith(word,na=False)
        new_data=data[temp_data]
        for t in range(len(new_data)):
            if new_data['LLT_CURRENCY'].iat[t]=='N':
                new_data['LLT_NAME_ENGLISH'].iat[t]='*'+new_data['LLT_NAME_ENGLISH'].iat[t]
        new_data=new_data[['SOC_CODE','SOC_NAME','HLGT_CODE','HLGT_NAME','HLT_CODE','HLT_NAME','PT_CODE','PT_NAME','LLT_CODE','LLT_NAME_ENGLISH']]
        new_data=new_data.set_index('SOC_CODE')
        new_data=new_data.reset_index()
        # print(new_data)
        return JsonResponse({'searched_data':[new_data.loc[_].to_dict() for _ in range(len(new_data))]})



@ensure_csrf_cookie
@csrf_exempt
@api_view(['POST','OPTIONS','GET'])
def get_products(request):
    # print(request.GET.get('search')) 
    if request.method == 'POST'  or request.method == 'OPTIONS':
        word=str(request.data['search']).lower()
        print(word)
        if word[0]=='%' and word[-1]=='%':
            # print(word[1:-1])
            temp_data=lower_drug_data['Drug_Name'].str.contains(word[1:-1],case=False,na=False)
        elif word[0]=='%':
            # print(word[:-1])
            temp_data=lower_drug_data['Drug_Name'].str.endswith(word[1:],na=False)
        elif word[-1]=='%':
            temp_data=lower_drug_data['Drug_Name'].str.startswith(word[:-1],na=False)
        else:
            temp_data=lower_drug_data['Drug_Name'].str.startswith(word,na=False)
        new_data=drug_data[temp_data]
        new_data=new_data[['id','Drug_Name']]
        new_data=new_data.set_index('id')
        new_data=new_data.reset_index()
        new_data=new_data[['Drug_Name']]
        return JsonResponse({'searched_data':new_data['Drug_Name'].tolist()})

    if request.method == 'GET':
        word=str(request.GET.get('search')).lower()
        print(word)
        if word[0]=='%' and word[-1]=='%':
            # print(word[1:-1])
            temp_data=lower_drug_data['Drug_Name'].str.contains(word[1:-1],case=False,na=False)
        elif word[0]=='%':
            # print(word[:-1])
            # print(word[:-1])
            temp_data=lower_drug_data['Drug_Name'].str.endswith(word[1:],na=False)
        elif word[-1]=='%':
            temp_data=lower_drug_data['Drug_Name'].str.startswith(word[:-1],na=False)
        else:
            temp_data=lower_drug_data['Drug_Name'].str.startswith(word,na=False)
        new_data=drug_data[temp_data]
        new_data=new_data[['id','Drug_Name']]
        new_data=new_data.set_index('id')
        new_data=new_data.reset_index()
        new_data=new_data[['Drug_Name']]
        return JsonResponse({'searched_data':new_data['Drug_Name'].tolist()})



