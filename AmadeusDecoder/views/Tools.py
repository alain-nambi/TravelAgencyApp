'''
Created on 8 Sep 2022

'''
import os

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from AmadeusDecoder.utilities.ProductImportParser import ProductParser, CustomerParser
from AmadeusDecoder.models.configuration.Configuration import Configuration

@login_required(login_url='index')
def tools(request):  
    return render(request,'tools.html')


def call_product_import(request):
    
    status = ''
    try:
        directory = '/opt/odoo/issoufali-addons/sync_products/data/exported/'
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                ProductParser.import_product(os.path.join(directory, file), directory)
        status = 'Product successfuly imported'
    except Exception as e:
        print(e)
        status = str(e)

    return JsonResponse({'return':status})


def call_customer_import(request):
    
    status = ''
    try:
        directory = '/opt/odoo/issoufali-addons/export_contacts/data/restore_csv/'
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                CustomerParser.import_customer(os.path.join(directory, file), directory)
        status = 'Customer successfuly imported'
    except Exception as e:
        print(e)
        status = str(e)


    return JsonResponse({'return':status})
