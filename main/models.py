from django.db import models
# Create your models here.

class Home(models.Model):
    nomi1 = models.CharField(max_length=100)
    nomi2 = models.CharField(max_length=100)
    text = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.nomi1
    
class Services(models.Model):
    nom1 = models.CharField(max_length=100)
    nom2 = models.CharField(max_length=150) 
    text = models.TextField()
    button = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom1
#verbose_name = ""
class Card(models.Model):
    emad = models.CharField(max_length=200 )
    estate = models.CharField(max_length=200)
    text = models.TextField()
    cap = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.emad

class Legal(models.Model):
    nomi = models.CharField(max_length=200)
    nom1 = models.CharField(max_length=100)
    nom2= models.CharField(max_length=100)
    nom3 = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi
    

class Boshqsmi(models.Model):
    rasm = models.ImageField(upload_to='media/')


class SMS(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Projecti_Home(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    

class Project_Kard(models.Model):
    rnomi1 = models.CharField(max_length=300)
    rnomi2 = models.CharField(max_length=400)
    rasm = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=500)
    nomi2 = models.CharField(max_length=600)
    url = models.CharField(max_length=300)
    
    def __str__(self):
        return self.rnomi1
    
    
class Newsdagi_rasm(models.Model):
    rasm = models.ImageField(upload_to='media/',verbose_name = "newsdagi headerdi tagidagi rasmni krting:")
    
class Newsdagi_rasmdi_tagdagi_sozlar(models.Model):
    title = models.CharField(max_length=300)
    title_small = models.CharField(max_length=400)
    text = models.TextField()
    button_nomi = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title
      
class Newsdagi_Categ(models.Model):
    title = models.CharField(max_length=200)
    nomi1 = models.CharField(max_length=200)
    raqam1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=200)
    raqam2 = models.CharField(max_length=200)
    nomi3 = models.CharField(max_length=200)
    raqam3 = models.CharField(max_length=200)
    nomi4= models.CharField(max_length=200)
    raqam4 = models.CharField(max_length=200)
    nomi5 = models.CharField(max_length=200)
    raqam5 = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
        
class Newsdi_button(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=200)
    def __str__(self):
        return self.nomi1
    
class Newsdagi_malumot_ongtomondagi(models.Model):
    nomi = models.CharField(max_length=200)
    text = models.TextField()
    


class NewsdagiDeta(models.Model):
    title = models.CharField(max_length=200)
    titlesmal = models.CharField(max_length=200)
    icon =  models.ImageField(upload_to='media/')
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=200)
    nomi1 = models.CharField(max_length=200)
    ong1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=200)
    ong2 = models.CharField(max_length=200)
    nomi3 = models.CharField(max_length=200)
    button_nomi = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class Header(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title1


class Header_Project(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title1

class Project_Matn(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Project_Matn1(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Header_News(models.Model):
    title1 = models.CharField(max_length=300)
    title2 = models.CharField(max_length=300)
    title3 = models.CharField(max_length=300)
    title4 = models.CharField(max_length=300)

    def __str__(self):
        return self.title1

class Words_News(models.Model):
    title1 = models.CharField(max_length=300)
    text1 = models.TextField()
    title2 = models.CharField(max_length=300)
    text2 = models.TextField()
    title3 = models.CharField(max_length=300)
    text3 = models.TextField()

class News_Butondi_Tepasdagi_matn(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)


class Portfolio(models.Model):
    rasm = models.ImageField(upload_to='media/')

class PdfHome(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PdfHome2(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class PdfTxt(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    
    
    def __str__(self):
        return self.text1

class PdfImg(models.Model):
    img = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    img9 = models.ImageField(upload_to="media/")
    img10 = models.ImageField(upload_to="media/")
    
class PdfCard(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard7(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
class PdfCard8(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
class PdfPast(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")
    
# pdf10 html modeli
class Pdf8Home(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PdfHome8(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj8(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class PdfTxt8(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    text7 = models.TextField()
    text8 = models.TextField()
    text9 = models.TextField()
    
    
    def __str__(self):
        return self.text1

class PdfImg8(models.Model):
    img1 = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    
    
class Rasm8Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
    
class PdfCard9(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard0(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
  
  
class PdfPast0(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")
    
# pdf3
class Pdf3Home(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PdfHome3(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj3(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    nomi7 = models.CharField(max_length=300)
    nomi8 = models.CharField(max_length=300)
    nomi9 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class PdfTxt3(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    
    
    def __str__(self):
        return self.text1

class PdfImg3(models.Model):
    img1 = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    
    
class Rasm3Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
class Rasm33Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
    
class PdfCard3(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard03(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
  
  
class PdfPast03(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")
    
    
#pdf4
class Pdf4Home(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PdfHome4(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj4(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    nomi7 = models.CharField(max_length=300)
    nomi8 = models.CharField(max_length=300)
    nomi9 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class PdfTxt4(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    
    
    def __str__(self):
        return self.text1

class PdfImg04(models.Model):
    img1 = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    
    
class Rasm4Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
class Img44Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
    
class PdfCard4(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard04(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
  
  
class PdfPast04(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")
    
# pdf5
class Pdf5Home(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class Pdfooo545(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj5(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    nomi7 = models.CharField(max_length=300)
    nomi8 = models.CharField(max_length=300)
    nomi9 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class PdfTxt5(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    
    
    def __str__(self):
        return self.text1

class PdfImg05(models.Model):
    img1 = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    
    
class Rasm5Pdf(models.Model):
    rasm = models.ImageField(upload_to="media/")
 
class PdfCard05(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard005(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
  
  
class PdfPast005(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")
    
    
# pdf9 model
class PDF9HOMES(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PDF9HOMES2(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    
class PdfBurj9(models.Model):
    title = models.CharField(max_length=300)
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    nomi7 = models.CharField(max_length=300)
    def __str__(self):
        return self.title
    
class PdfTxt9(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    nomi1 = models.CharField(max_length=300)
    text3 = models.TextField()
    nomi2 = models.CharField(max_length=300)
    nomi3 = models.CharField(max_length=300)
    nomi4 = models.CharField(max_length=300)
    nomi5 = models.CharField(max_length=300)
    nomi6 = models.CharField(max_length=300)
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    text7 = models.TextField()
    text8 = models.TextField()
    text9 = models.TextField()
    text10 = models.TextField()
    
    def __str__(self):
        return self.text1

class PdfImg09(models.Model):
    img1 = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    

class PdfCard009(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdFCaCrd9(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
  
  
class PdfPast009(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")