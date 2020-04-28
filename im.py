from flask import Flask


app = Flask(__name__)


@app.route('/im') 
def im():
  return '''<!doctype html>
              <html lang="en">
                <head>
                  <!-- Required meta tags -->
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                  <!-- Bootstrap CSS -->
                  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                  <title>Hello, world!</title>
                </head>
                <body>
                    <nav class="navbar navbar-expand-lg navbar-light bg-light">
                        <a class="frost" href="#">Navbar</a>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul class="navbar-nav mr-auto">
                                    <li class="nav-item active">
                                        <a class="nav-link" href="#">музыка <span class="sr-only">(current)</span></a>
                                    </li>
                                    <li class="nav-item dropdown">
                                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        name
                                        </a>
                                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                                        <a class="dropdown-item" href="#">Action</a>
                                        <a class="dropdown-item" href="#">Another action</a>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="#">Something else here</a>
                                        </div>
                                    </li>
                                </ul>
                                <form class="form-inline my-2 my-lg-0">
                                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                                </form>
                        </div>
                    </nav>
                    <div class="container">
                    <div class="row">
                        <div class="col-sm">
                            <div class="btn-group-vertical" role="group" aria-label="Basic example">
                            <a href="http://127.0.0.1:8080/im" type="button" class="btn btn-secondary">моя страница</a>
                            <button href="http://127.0.0.1:8080/new" type="button" class="btn btn-secondary">новости</button>
                            <button href="http://127.0.0.1:8080/posts" type="button" class="btn btn-secondary">сообщения</button>
                            <button href="http://127.0.0.1:8080/friends" type="button" class="btn btn-secondary">друзья</button>
                            <button href="http://127.0.0.1:8080/community" type="button" class="btn btn-secondary">сообщества</button>
                            <button href="http://127.0.0.1:8080/photos" type="button" class="btn btn-secondary">фотографии</button>
                            </div>
                        </div>
                        <div class="col-sm">
                        <img src="/static/img/my.jpg" class="rounded mx-auto d-block" alt="...">
                        </div>
                        <div class="col-sm">
                            <h1> name surname </h1>
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th> день рождения </th>
                                        <th> 01.01.2001 </th>
                                    </tr>
                                    <tr>
                                        <th> город </th>
                                        <th> city </th>
                                    </tr>                                    
                                    <tr>
                                        <th> место учебы </th>
                                        <th> school </th>
                                    </tr>
                                </thead>
                        </div>
                    </div>
                </body>
              </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)