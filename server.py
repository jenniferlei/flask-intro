"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

def return_dropdown(options):
  html_strings_list = []
  for option in options:
    html_strings_list.append(f'<option value="{option}">{option.capitalize()}</option>')
  all_html_strings = """
""".join(html_strings_list)
  return all_html_strings

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = ['bad', 'not very good', 'just okay', 'slovenly', 'delinquent',
    'terrible', 'shameful', 'clumsy']

return_dropdown(AWESOMENESS)
return_dropdown(DISSES)

@app.route('/')
def start_here():
    """Home page."""
  
    return """
    <!doctype html><html>Hi! This is the home page.
    <p>
    <a href="http://localhost:5000/hello">Hello</a>
    </p>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          <br>
          Choose your compliment
          <select name="compliment">
            <option value="blank"></option>
            {return_dropdown(AWESOMENESS)}
          </select>
          <br>OR
          <br>
          Choose your diss
          <select name="diss">
            <option value="blank"></option>
            {return_dropdown(DISSES)}
          </select>
          <br><input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")

    compliment = request.args.get("compliment")

    diss = request.args.get("diss")

    if compliment != "blank":
      description = compliment
    elif diss != "blank":
      description = diss

    #if they chose an item from the insult form, "
    #then return this:
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {description}!
        <br><a href="http://localhost:5000/">Home</a>
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
