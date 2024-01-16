from flask import Flask, render_template, request
from sympy import symbols, integrate, diff

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get the input function from the form
            input_function = request.form["input_function"]

            # Define the symbolic variable
            x = symbols("x")

            # Perform integration
            result = diff(input_function, x)

            # Convert the result to a string for direct display
            result_str = str(result)
        except Exception as e:
            result_str = f"Error: {str(e)}"
    else:
        result_str = None

    return render_template("index.html", result=result_str)


if __name__ == "__main__":
    app.run(debug=True)
