from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
def defineRoutes(app,db):

    @app.route('/')
    def show_entries():
        #cur = db.execute('select title, text from entries order by id desc')
        #entries = cur.fetchall()
        return render_template('show_entries.html', entries=[])

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != app.config['USERNAME']:
                error = 'Invalid username'
            elif request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)


    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))