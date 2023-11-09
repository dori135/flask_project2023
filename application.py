from flask import Flask, render_template, request
from database import DBhandler
import sys

application = Flask(__name__)

DB = DBhandler()

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/list")
def view_list():
    return render_template("list.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")


@application.route("/submit_item")
def reg_item_submit():
    name = request.args.get("name")
    seller = request.args.get("seller")
    addr = request.args.get("addr")
    money = request.args.get("money")
    category = request.args.get("category")
    status = request.args.get("status")
    intro = request.args.get("intro")

    print(name, seller, addr, money, category, card, status, intro)
    #return render_template("reg_item.html")

@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post():
    image_file = request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    DB.insert_item(data['name'], data, image_file.filename)
    
    return render_template("submit_item_result.html", data=data, img_path=
                           "static/images/{}".format(image_file.filename))

if __name__ == "__main__":
    application.run(host='0.0.0.0')
