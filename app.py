from flask import Flask , render_template, request
import sqlite3
app=Flask(__name__)
@app.route('/')
def landing_page():
    return render_template('index.html')
@app.route('/guest')
def guest():
    conn=sqlite3.connect('News.db')
    h=conn.execute('select * from articles')
    articles=h.fetchall()
    return render_template('guest.html',articles=articles)
@app.route('/User')
def user():
    return render_template('user_landing.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if 'username' in request.form and 'password' in request.form:
        username=request.form.get('username')
        password=request.form.get('password')
        conn=sqlite3.connect('News.db')
        conn.execute('insert into users values(?,?)', (username,password))
        conn.commit()
        return 'Account created,go back!'
    else:
        return 'err'
@app.route('/userhomepage',methods=['GET','POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        # print('Hello')
        print(request.form.get('username'),request.form.get('password'))
        conn=sqlite3.connect('News.db')
        h=conn.execute('select * from users')
        o4=conn.execute('select * from articles')
        rows=h.fetchall()
        articles=o4.fetchall()
        # print(rows)
        c=0
        for i in rows:
            o1=request.form.get('username')
            o2=request.form.get('password')
            # print(i[0],i[1],o1,o2,len(i[0]),len(i[1]),len(o1),len(o2))
            if str(i[0])==str(request.form.get('username')) and str(i[1])==str(request.form.get('password')):
                c+=1
        if c==0:
            return 'Invalid Username/Password'
        else:
            return render_template('user_homepage.html',user=request.form.get('username'),articles=articles)
    return 'Done'
@app.route('/addnews',methods=['GET','POST'])
def add_news():
    o=request.form.get('submit').split()
    p=o[1]
    return render_template('add_news.html',user=p)
@app.route('/news_added',methods=['GET','POST'])
def post_article():
    title=request.form.get('Title')
    g=request.form.get('submit').split()
    author=g[1]
    content=request.form.get('Content')
    category=request.form.get('Category')
    conn=sqlite3.connect('News.db')
    conn.execute('insert into articles values(?,?,?,?)',(title,author,content,category))
    conn.commit()
    return 'Added Successfully'
@app.route('/home',methods=['GET','POST'])
def home():
    o=request.form.get('submit').split()
    p=o[1]
    return render_template('User_Home.html',user=p)
@app.route('/newsarticles',methods=['GET','POST'])
def news():
    o=request.form.get('submit').split()
    p=o[1]
    conn=sqlite3.connect('News.db')
    h=conn.execute('select * from articles')
    rows=h.fetchall()
    return render_template('user_homepage.html',user=p,articles=rows)
@app.route('/contact',methods=['GET','POST'])
def contact():
    o=request.form.get('submit').split()
    p=o[1]
    return render_template('User_Contact.html',user=p)
@app.route('/guesthome',methods=['GET','POST'])
def guest_home():
    return render_template('guest_home.html')
@app.route('/guestnews',methods=['GET','POST'])
def guest_news():
    conn=sqlite3.connect('News.db')
    h=conn.execute('select * from articles')
    rows=h.fetchall()
    return render_template('guest.html',articles=rows)
@app.route('/guestcontact',methods=['GET','POST'])
def guest_contact():
    return render_template('guest_contact.html')
@app.route('/logout',methods=['GET','POST'])
def logout():
    return render_template('index.html')
@app.route('/Admin',methods=['GET','POST'])
def admin():
    return render_template('admin_login.html')
@app.route('/adminhome',methods=['GET','POST'])
def admin_login():
    o=request.form.get('username')
    p=request.form.get('password')
    if str(o)=='Admin@123' and str(p)=='HelloAdmin':
        conn=sqlite3.connect('News.db')
        h=conn.execute('select * from articles')
        rows=h.fetchall()
        return render_template('admin_homepage.html',articles=rows)
    else:
        return 'Invalid username/password'
@app.route('/delete',methods=['GET','POST'])
def deletion():
    o=request.form.get('submit').split()
    p=o[1:]
    q=''
    for j in range(len(p)):
        q+=p[j]
        if j!=len(p)-1:
            q+=' '
    # print(p,q)
    conn=sqlite3.connect('News.db')
    #generated by gpt
    conn.execute('delete from articles where title = ?',(q,))
    conn.commit()
    return 'article deleted'
@app.route('/update',methods=['GET','POST'])
def updation():
    o=request.form.get('submit').split()
    q=''
    for i in range(1,len(o)):
        q+=o[i]
        if i!=len(o)-1:
            q+=' '
    return render_template('update_article.html',title=q)
@app.route('/updated',methods=['GET','POST'])
def updated():
    o=request.form.get('content')
    p1=request.form.get('submit').split()
    q=''
    for i in range(1,len(p1)):
        q+=p1[i]
        if i!=len(p1)-1:
            q+=' '
    print(q)
    conn=sqlite3.connect('News.db')
    conn.execute('update articles set Content=? where title=?',(o,q))
    conn.commit()
    return 'Updated Sucessfully!'