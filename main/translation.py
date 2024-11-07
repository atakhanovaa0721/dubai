from modeltranslation.translator import register,TranslationOptions,translator
from .models import *

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields=("nomi1","nomi2","text")
    
@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields=("nom1","nom2","text","button")
    
@register(Card)
class CardTranslationOptions(TranslationOptions):
    fields=("emad","estate","text","cap")
    
@register(Legal)
class LegalTranslationOptions(TranslationOptions):
    fields=("nomi","nom1","nom2","nom3","text1","text2","text3")

@register(Newsdagi_malumot_ongtomondagi)
class Newsdagi_malumot_ongtomondagiTranslationOptions(TranslationOptions):
    fields=("nomi","text")

@register(Newsdagi_Categ)
class Newsdagi_CategTranslationOptions(TranslationOptions):
    fields=("title","nomi1","raqam1","nomi2","raqam2","nomi3","raqam3","nomi4","raqam4","nomi5","raqam5")

@register(Newsdagi_rasmdi_tagdagi_sozlar)
class Newsdagi_rasmdi_tagdagi_sozlarTranslationOptions(TranslationOptions):
    fields=("title","title_small","text","button_nomi")

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields=("title1","title2","title3","title4")

@register(Header_Project)
class Header_ProjectTranslationOptions(TranslationOptions):
    fields=("title1","title2","title3","title4")


@register(Project_Kard)
class Project_KardTranslationOptions(TranslationOptions):
    fields=('rnomi1','rnomi2','nomi1','nomi2')

@register(Project_Matn)
class Project_MatnTranslationOptions(TranslationOptions):
    fields=('title','text')

@register(Project_Matn1)
class Project_Matn1TranslationOptions(TranslationOptions):
    fields=('title','text')

@register(Header_News)
class Header_NewsTranslationOptions(TranslationOptions):
    fields=('title1','title2','title3','title4')

@register(Words_News)
class Words_NewsTranslationOptions(TranslationOptions):
    fields=('title1','text1','title2','text2','title3','text3')

@register(News_Butondi_Tepasdagi_matn)
class News_Butondi_Tepasdagi_matnTranslationOptions(TranslationOptions):
    fields=('title1','title2','title3')

@register(NewsdagiDeta)
class NewsdagiDetaTranslationOptions(TranslationOptions):
    fields=('title','titlesmal','nomi','nomi1','ong1','nomi2','ong2','nomi3','button_nomi')







