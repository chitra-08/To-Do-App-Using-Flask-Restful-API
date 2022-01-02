# pip install flask-restful
from flask import Flask, request, render_template, jsonify, Response, redirect, url_for
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDoUsingRest.db'
db = SQLAlchemy(app)


class Items(db.Model):
    itemid = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    status = db.Column(db.String(50))
    itemDate = db.Column(db.String(20))


class Home(Resource):
    def get(self):
        return Response(response=render_template('ToDoApp.html'))
        '''
        #headers = {'Content-Type': 'text/html'}
        #return make_response(render_template('login.html'), 200, headers)
        # or just                                                                                        
        return make_response(render_template('index.html'))
        '''


class addItem(Resource):
    def post(self):
        item = Items(item=request.form['searchText'], status='Not Completed', itemDate=datetime.now())
        db.session.add(item)
        db.session.commit()
        return Response(response=render_template('ToDoApp.html'))


class Show(Resource):
    def get(self):
        return Response(response=render_template('ShowList.html', todoitems=Items.query.all()))


class delete(Resource):
    def get(self, sno):
        item = Items.query.filter_by(itemid=sno).first()
        db.session.delete(item)
        db.session.commit()
        return Response(response=render_template('ToDoApp.html'))


class edit(Resource):
    '''
    When the edit btn is clicked from the home page , the get method is called. It fetches the data from db
    and pass it on to the EditList.html.
    When person edits the details on EditList.html page and clicks edit btn, the call goes to post method and
    the value edited are captured and passed to Items model class to commit and then the home page template
    is rendered.

    Step 1:  http://127.0.0.1:5000/Show :Edit btn on home page
    Step 2:  http://127.0.0.1:5000/edit/6: Click on Edit on show page : Get method is called
    Step 3: http://127.0.0.1:5000/edit/6: On EditList page: edit the details and click on Edit btn
    Step 4: Post method is called and values edited are saved in table and redirected to home page
    '''
    def post(self, sno):
        edit_item = request.form.get('searchText')
        edit_status = request.form.get('itmStat')
        item = Items.query.filter_by(itemid=sno).first()
        item.item = edit_item
        item.status = edit_status
        db.session.commit()
        return Response(response=render_template('ToDoApp.html'))

    def get(self, sno):
        item = Items.query.filter_by(itemid=sno).first()
        return Response(response=render_template('EditList.html', todoitems=item))




api.add_resource(Home, '/')
api.add_resource(addItem, '/add')
api.add_resource(delete, '/delete/<int:sno>')
api.add_resource(edit, '/edit/<int:sno>')
api.add_resource(Show, '/Show')
app.run(debug=True)
