from flask import Flask, request, render_template, jsonify
from flask_cors import CORS,cross_origin
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bs
from Logging.logger import logging
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        logging.info("Index page is succesfully rendered.")
        return render_template("index.html")
        
    except:
        logging.error("Something went weird.")


@app.route("/review",methods=['POST','GET'])
def search():
    if request.method=="POST":  
        try:            
            reviews=[]
            search = request.form['content']
            logging.info("Search query is successfully fetched.")
            search_rep = search.replace(" ","+")
            url = "https://flipkart.com/search?q="+search_rep
            url_open = urlopen(url)
            url_html = bs(url_open,"html.parser")
            prod = url_html.find_all("div",{"class" : "_1AtVbE col-12-12"})
            prod_url = "https://www.flipkart.com"+prod[2].div.a["href"]
            prod_html = bs(urlopen(prod_url),"html.parser")

            for i in range(10):
                try:
                    rev = (prod_html.find_all("div",{"class":"_16PBlm"}))[i].find("div",{"class":""}).div.text
                except:
                    pass

                try:    
                    name=((prod_html.find_all("div",{"class":"row _3n8db9"}))[i].div.p.text)
                except:
                    pass

                try:    
                    ratings=(prod_html.find_all("div",{"class":"_3LWZlK _1BLPMq"}))[i].text
                except:
                    pass

                try:
                    comment_head=(prod_html.find_all("p",{"class":"_2-N8zT"}))[i].text
                except:
                    pass

                    
                dict={"Product":search,'Name':(str(name).capitalize()),"Rating":ratings,"CommentHead":comment_head,"Comment":rev,"Comment":rev}
                
                reviews.append(dict)
                
                
            df = pd.DataFrame(reviews)  
            path_to_csv = os.path.join(os.getcwd(),'data',f'{(reviews[0]["Product"]).capitalize()}.csv')
            df.to_csv(path_to_csv)  
            logging.info("Succefully saved in csv format.")
            logging.info("Reviews are successfully fetched.")
            return render_template("result.html",reviews=reviews)    

        except Exception as e:
            logging.error(e)
            logging.error("Reviews are not displayed")
            return render_template('index.html')
            



    else:
        return render_template('index.html')    
    

if __name__=="__main__":
    app.run(debug=True)