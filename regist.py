from flask import Flask


app = Flask(__name__)


@app.route('/regist')
def regi():
  return '''<!doctype html>
              <html lang="en">
                <head>
                  <!-- Required meta tags -->
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                  <!-- Bootstrap CSS -->
                  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                  <title>reg frost</title>
                </head>
                <body>
                    <h2> Пожалуйста укажите ваше имя и фамилию. </h2>
                    <h3> это облегчит поиск и общение с вашими друзьями </h3>
                    <form>
                        <div class="form-row align-items-center">
                            <div class="col-auto">
                            <label class="sr-only" for="inlineFormInput">Name</label>
                            <input type="text" class="form-control mb-2" id="inlineFormInput" placeholder="Jane Doe">
                            </div>
                            <div class="col-auto">
                            <label class="sr-only" for="inlineFormInputGroup">Username</label>
                            <div class="input-group mb-2">
                                <div class="input-group-prepend">
                                <div class="input-group-text">@</div>
                                </div>
                                <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Username">
                            </div>
                            <div class="col-sm-10">
                            <input type="password" class="form-control" id="inputPassword">
                            </div>
                            </div>
                            <div class="col-auto">
                            <button type="submit" class="btn btn-primary mb-2">Submit</button>
                            </div>
                        </div>
                    </form>
                </body>
              </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)