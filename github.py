################model#####################
class Bank(models.Model):
    ifsc=models.CharField(max_length=50)
    bank_id=models.IntegerField(max_length=10)
    branch=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)

    bank_name=models.CharField(max_length=50)

######################views#################################
@csrf_exempt
def banks(request):
   if request.method =='POST':
        result=json.loads(request.body)
        print("result",result)
        ifsc=result["ifsc"]
        bank_id=result["bank_id"]
        branch=result["branch"]
        address=result["address"]
        city=result["city"]
        bank_name=result["bank_name"]
        pp=Bank(ifsc=result["ifsc"],bank_id=result["bank_id"],branch=result["branch"],address=result["address"],city=result["city"],bank_name=result["bank_name"])
        pp.save()
        return JsonResponse({"message":"create"})
@csrf_exempt
def new_up(request):
    if request.method =='GET':
         pf=banks.objects.filter(ifsc="ANDB001").view('branch')
         print(pf)
         pe=banks.objects.filter(bank_name="sbi",city="hyderabad").view('branch')
         print(pe)
         return JsonResponse({"message": "create"})
############################### urls  #######################################
urlpatterns=[path('banked',banks) ,
             path("new",new_up)]
