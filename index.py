from bottle import route, static_file, run, error


@route('/')
@route('/About')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> About </title>
                    <meta charset="utf-8">
                </head>

                <header>
                    <ul>
                        <li><a href="">About</a></li>
                        <li><a href="biography">Biography</a></li>
                        <li><a href="pictures">Pictures</a></li>
                    </ul>
                </header>

                <body>
                    <h1> About Sida </h1>
                </body>
            </html>
        '''

@route('/biography')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> Biography </title>
                    <meta charset="utf-8">
                </head>

                <header>
                    <ul>
                        <li><a href="About">About</a></li>
                        <li><a href="#">Biography</a></li>
                        <li><a href="pictures">Pictures</a></li>
                    </ul>
                </header>

                <body>
                    <h2> Biography Sida </h2>
                </body>
            </html>
        '''

@route('/pictures')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> Biography </title>
                    <meta charset="utf-8">
                </head>

                <header>
                    <ul>
                        <li><a href="About">About</a></li>
                        <li><a href="biography">Biography</a></li>
                        <li><a href="#">Pictures</a></li>
                    </ul>
                </header>

                <body>
                    <h2> Pictures Sida </h2>
                </body>
            </html>
        '''

@error(404)
def error404(error):
    return "Error! Shit's Fooked mate"

run(host='localhost', port=8080, debug=True)