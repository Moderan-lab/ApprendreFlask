from flask import Flask
from flask import render_template

list_post= [
	{"id":1, "title":'TOYOTA NISSAN', "content":"Tout terrain blinde"},
	{"id":2, "title":'Range Over', "content":"Couleur noir"},
	{"id":3, "title":'4*4', "content":"Tout terrain silencieux h"} ]


app= Flask(__name__)

@app.route('/')

def Home():
	return render_template('pages/home.html')

@app.route('/contact')
def contact():
	return render_template('pages/contact.html')


@app.route('/blog')
def Blog():
	return render_template('posts/index.html', moderan=list_post )


@app.route('/blog/posts/<int:a>')
def show(a):
	post= list_post[a - 1]
	return render_template('posts/show.html', mode=post)

@app.errorhandler(404)
def page_erreur(error):
	return render_template('ERROR/404.html'), 404

if __name__ == '__main__':
	app.run(debug=True, port=5000)