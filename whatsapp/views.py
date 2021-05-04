# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return render(request, 'home.html')

# # def whatsappDATA(ph,message):
# #     import time
# #     import webbrowser as web
# #     import pyautogui as pg  
# #     Phone = "+91" + ph
# #     web.open('https://web.whatsapp.com/send?'+ Phone + '&text'+Message)
# #     time.sleep(40)
# #     pg.press('enter')

# def WhatsappData(Ph, Message):
#     import time
#     import webbrowser as web
#     import pyautogui
#     Phone = "+91"+Ph
#     web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
#     time.sleep(30)

#     pyautogui.press('enter')

# def send_data(request):
#     if request.method == 'POST':
#         ph = request.POST['Phone']
#         message = request.POST['Message']
#         # print(ph, message)    
#         whatsappDATA(ph,message)        
#         msg = "Message has sent successfully!!"
#         return render(request, 'whatsapp/home.html', {'msg': msg})
#     else:
#         return HttpResponse("<h1> 404 Not Found</h1>")    



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def WhatsappData(Ph, Message):
    import time
    import webbrowser as web
    import pyautogui
    Phone = "+91"+Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)

    pyautogui.press('enter')


    
def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        # print(Ph,Message)
        WhatsappData(Ph,Message)
        msg = "Message has successfully sent.."
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404- Not Found :)</h1>")