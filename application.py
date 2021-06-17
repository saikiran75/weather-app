from flask import Flask,render_template,request
import requests
import json

application=Flask(__name__)
@application.route("/")
def home():
    return render_template('index.html',flag=0)

@application.route("/information",methods=["POST"])
def information():
    city=request.form['city']
    city=city.strip()
    city=city.lower()
    r=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=05541db09d3829e5172ff0675ebd8946')
    if(r.status_code==404):
        return render_template('index.html',flag=1)
    k=r.content
    s=json.loads(k)
    print(r.status_code,k,s)
    a=s['name']
    b=s['weather'][0]['main']
    l1=s['coord']['lon']
    l2=s['coord']['lat']
    t=round(s['main']['temp']-273,2)  #converting to celsius
    h=s['main']['humidity']
    p=s['main']['pressure']
    w=int(s['wind']['speed']*3.6)  #converting to km/h
    return render_template('result.html',a1=a,b1=b,l11=l1,l21=l2,t1=t,h1=h,p1=p,w1=w)

if __name__=='__main__':
    application.run(debug=True,use_reloader=False)
