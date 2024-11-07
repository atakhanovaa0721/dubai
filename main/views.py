from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
def Index(request):
    context={
        'home':Home.objects.first(),
        'servic':Services.objects.first(),
        'card':Card.objects.all(),
        'legal':Legal.objects.first(),
        'card1':Card.objects.all(),
        'boshqsmi':Boshqsmi.objects.first(),
        "header":Header.objects.first(),
        "portfoilo":Portfolio.objects.all(),
    }
    return render(request,"index.html",context)

def Contact(request):
    return render(request,"contact.html")

def SMS(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        SMS.objects.create(name=name,email=email,text=text)
        messages.success(request,"SMS keldi szga")
        return redirect('/')
    
def Project(request):
    a={
        'projecti_Home':Projecti_Home.objects.first(),
        'projectkard':Project_Kard.objects.all(),
        'header_Project':Header_Project.objects.first(),
        'project_Matn':Project_Matn.objects.first(),
        'project_Matn1':Project_Matn1.objects.first(),
    }
    return render(request,"project.html",a)

def News(request):
    b={
        'header_News':Header_News.objects.first(),
        'newsdagi_rasm':Newsdagi_rasm.objects.first(),
        'newsdagi_rasmdi_tagdagi_sozlar':Newsdagi_rasmdi_tagdagi_sozlar.objects.first(),
        'newsdagi_Categ':Newsdagi_Categ.objects.first(),
        'newsdi_button':Newsdi_button.objects.all(),
        'newsdagi_malumot_ongtomondagi':Newsdagi_malumot_ongtomondagi.objects.first(),
        'newsdagiDeta':NewsdagiDeta.objects.all(),
        'words_News':Words_News.objects.first(),
        'news_Butondi_Tepasdagi_matn':News_Butondi_Tepasdagi_matn.objects.first(),
    }
    return render(request,"news.html",b)

#def News2(request):
    # context={
        # 'news2_home':News2_Home.objects.first(),
    # }
    #return render(request,"news2.html",)


def Pdf6(request):
    context = {
        'PdfHome':PdfHome.objects.first(),
        'PdfHome2':PdfHome2.objects.first(),
        'pdfburj':PdfBurj.objects.first(),
        'pdftxt':PdfTxt.objects.first(),
        'pdfimg':PdfImg.objects.first(),
        'pdfcard':PdfCard.objects.all(),
        'pdfcard7':PdfCard7.objects.all(),
        'pdfcard8':PdfCard8.objects.all(),
        'pdfpast':PdfPast.objects.first(),
    }
    return render(request,"pdf6.html",context)


def Pdf8(request):
    context={
        "pdf8home":Pdf8Home.objects.first(),
        "pdfhome8":PdfHome8.objects.first(),
        'pdfburj8':PdfBurj8.objects.first(),
        'pdftxt8':PdfTxt8.objects.first(),
        "pdfimg8":PdfImg8.objects.first(),
        "rasm8pdf":Rasm8Pdf.objects.first(),
        "pdfcard9":PdfCard9.objects.all(),
        "pdfcard0":PdfCard0.objects.all(),
        "pdfpast0":PdfPast0.objects.first(),
    }
    return render(request,"pdf8.html",context)

def Pdf3(request):
    context={
        "pdf3home":Pdf3Home.objects.first(),
        "pdfhome3":PdfHome3.objects.first(),
        "pdfburj3":PdfBurj3.objects.first(),
        "pdftxt3":PdfTxt3.objects.first(),
        "rasm3pdf":Rasm3Pdf.objects.first(),
        "pdfimg3":PdfImg3.objects.first(),
        "Rasm33Pdf":Rasm33Pdf.objects.first(),
        "pdfcard3":PdfCard3.objects.all(),
        "pdfcard03":PdfCard03.objects.all(),
        "pdfpast03":PdfPast03.objects.first(),
    }
    return render(request,"pdf3.html",context)


def Pdf4(request):
    context={
        "pdf4home":Pdf4Home.objects.first(),
        "pdfhome4":PdfHome4.objects.first(),
        "pdfburj4":PdfBurj4.objects.first(),
        "pdftxt4":PdfTxt4.objects.first(),
        "rasm4pdf":Rasm4Pdf.objects.first(),
        "img44pdf":Img44Pdf.objects.first(),
        "pdfimg04":PdfImg04.objects.first(),
        "pdfcard4":PdfCard4.objects.all(),
        "pdfcard04":PdfCard04.objects.all(),
        "pdfpast04":PdfPast04.objects.first(),
    }
    return render(request,"pdf4.html",context)


def Pdf5(request):
    context={
        "pdf5home":Pdf5Home.objects.first(),
        "Pdfooo545":Pdfooo545.objects.first(),
        "pdfburj5":PdfBurj5.objects.first(),
        "pdftxt5":PdfTxt5.objects.first(),
        "pdfimg05":PdfImg05.objects.first(),
        "rasm5pdf":Rasm5Pdf.objects.first(),
        "pdfcard05":PdfCard05.objects.all(),
        "pdfcard005":PdfCard005.objects.all(),
        "pdfpast005":PdfPast005.objects.first(),
    }
    return render(request,"pdf5.html",context)


def Pdf9(request):
    context={
        "pdf9homes":PDF9HOMES.objects.first(),
        "pdf9homes2":PDF9HOMES2.objects.first(),
        "pdfburj9":PdfBurj9.objects.first(),
        "pdftxt9":PdfTxt9.objects.first(),
        "pdfimg09":PdfImg09.objects.first(),
        "pdfcard009":PdfCard009.objects.all(),
        "pdfcacrd9":PdFCaCrd9.objects.all(),
        "pdfpast009":PdfPast009.objects.first()
    }
    return render(request,"pdf9.html",context)