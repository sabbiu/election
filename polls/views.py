from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import VoterInfo
from .models import Citizenship
from .models import Address
from .models import Disability
from django.utils import timezone



def index(request):
    voter_list = VoterInfo.objects.all()
    
    context = {'voter_list': voter_list}
    
    return render(request, 'polls/index.html', context)



def voter(request):
    
      
    

 





    check=2

    if request.method=='POST':
       check=0
       try:
          voter_id=request.POST['voter_id']
       except:
          check=1

       name=request.POST['name']
       try:

         gender=request.POST['gender']
       except: 
         check=1

       spousename=request.POST['spousename']
       fathername=request.POST['fathername']
       gfathername=request.POST['gfathername']
       mothertongue=request.POST['mothertongue']
       mobile=request.POST['mobile']
       email=request.POST['email']
       try:

         literacystatus=request.POST['literacystatus']
       except:
         check=1
       qualification=request.POST['qualification']
       district=request.POST['district']
       vdc_municipality=request.POST['vdc_municipality']
       try:
          ward_no=request.POST['ward_no']
       except:
          check=1


       try:
          disability=request.POST['disability']
       except:
          check=1
       citizenship=request.POST['citizenship']
       cdistrict=request.POST['cdistrict']
       cvdc_municipality=request.POST['cvdc_municipality']
       cward_no=request.POST['cward_no']
       citizenshiptype=request.POST['citizenshiptype']
       birthdistrict=request.POST['birthdistrict']
       issuedate=request.POST['issuedate']
       dob=request.POST['dob']    
 
       if name== ''   or  fathername=='' or gfathername=='' or mothertongue=='' or district=='' or vdc_municipality=='' or citizenship=='' :
          check=1
       if cdistrict=='' or cvdc_municipality=='' or citizenshiptype=='' or birthdistrict=='' or issuedate=='' or dob=='':
          check=1


       if check==0 :      
             

             dis=request.POST['disability']
             try:
                dis=1
                d=Disability.objects.get(disability_id=dis)
             except:
                dis=0

             

            
          


             
             x=request.POST['district']
             y=request.POST['vdc_municipality']
             z=request.POST['ward_no']
             
             #  If Address previously does  not exist , create new
             try:
                a=Address.objects.get(district=x , vdc_municipality=y , wardno=z)
             except:
                tot=Address.objects.all()
                l=len(tot)
                a=Address.objects.create(address_id=l+1,district=x,vdc_municipality=y,wardno=z)
                a.save()
             a=Address.objects.get(district=x , vdc_municipality=y , wardno=z) 

             c=Citizenship()
             c.citizenship_id=citizenship
             
             c.citizenshiptype=citizenshiptype
             c.birthdistrict=birthdistrict
             c.issuedate=issuedate;
             c.dob=dob
             c.issuedaddress=a
             c.save()
             
             v=VoterInfo()
             
           
             
             

             v.name=name
             v.voter_id=voter_id
             v.citizenship=c
             v.gender=gender
             v.spousename=spousename
             v.fathername=fathername
             v.gfathername=gfathername
             v.mothertongue=mothertongue
             v.mobile=mobile
             v.email=email
             v.literacystatus=literacystatus
             v.qualification=qualification

             v.address=a
             if dis==1 :  
                v.disability=d
             
              
             v.save()

    print('check')
    print(check) 
    return render(request, 'polls/voter.html',{'check':check})




