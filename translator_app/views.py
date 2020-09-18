from  googletrans import Translator
from django.shortcuts import render

def translator(request):
  
  return render(request,'translator.html',{})

def translated(request):
  text = request.GET.get('text')
  lang = request.GET.get('lang')
  print(f'text :{text} , lang: {lang}')

  in_translator = Translator()

  # detect the langauge
  dt = in_translator.detect(text)
  dt2 = dt.lang
  # translate the text
  in_trnslated = in_translator.translate(text,lang)
  tr = in_trnslated.text
  return render(request,'translated.html',{
    'trnslated':tr,'u_lang':dt2,'t_lang':lang
  })


def profile(request):
  return render(request,'translator.html',{})


def home(request):
  pass

def add(request):
  return render(request,'translator.html',{})
