@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    user_id = session.get("user_id")
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)
    buy_username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)
    total_cash = cash[0]['cash'] # 10000
    symboled = request.form.get("symbol")
    shares = request.form.get("shares") # no. of shares submitted by the user
    stock_name = lookup(symboled)["symbol"] # Stock name from the lookup function
    stock_price = lookup(symboled)["price"]
    total = stock_price * shares # total price of the stocks
    date_time = datetime.now()


    # The return of the Lookup function and ordered as listed in helpers.py
    quoted_stock = lookup(symboled)

    # Checking if the symbol input field is empty
    if request.method == 'POST':
        if not symboled:
            return apology("You have to enter a Stock's Symbol", 400)

        # Checking the return of the lookup function
        if quoted_stock == None:
            return apology("Sorry, the symbol doesn't exist!")

        while(shares <= 0):
            return apology("Please enter a positive number of Shares")

        if total > total_cash:
            return apology("Sorry, you don't have ENOUGH CASH to complete the transaction")

        db.execute("INSERT INTO buy (username, Symbol, Shares, Price, Total, DateTime) VALUES (?, ?, ?, ?, ?, ?)", buy_username, stock_name, shares, usd(stock_price), usd(total), date_time)

        remaining_cash = total_cash - total # 10000 - total price of the bought stocks

        db.execute("UPDATE users SET cash = :cash WHERE username = :username", cash-remaining_cash, username=buy_username) # updating the users table

        bought = db.execute("SELECT Symbol, Shares, Price, Total FROM buy WHERE username = :username", username=buy_username)

        return render_template("portfolio.html", bought=bought, remaining_cash=usd(remaining_cash), total_cash=usd(total_cash))

    else:
        return render_template("buy.html")



























    # @app.route("/")
# @login_required
# def index():
#     """Show portfolio of stocks"""

#     user_id = session.get("user_id")
#     buy_username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)[0]['username']
#     info = db.execute("SELECT Symbol, SUM(Shares) AS TotalShares FROM buy WHERE username = ? GROUP BY Symbol", (buy_username,))
#     cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]['cash']
#     total_cash = usd(10000.00)

#     for stock in info:

#         quoted_stock = lookup(stock["Symbol"])
#         stock["Price"] = quoted_stock["price"]
#         stock["Total"] = stock["Price"] * stock["TotalShares"]
#         stock["Price"] = usd(stock["Price"])
#         stock["Total"] = usd(stock["Total"])

#     # Retrieve the query parameters from the URL
#     bought = request.args.get('bought')

#     return render_template("index.html", stocks=info, cash=usd(cash), bought=bought, total_cash=total_cash)


# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell shares of stock"""

#     user_id = session.get("user_id")
#     sell_username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)[0]['username']
#     info = db.execute("SELECT Symbol, SUM(Shares) AS TotalShares FROM buy WHERE username = ? GROUP BY Symbol", (sell_username,))
#     cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]['cash']

#     if request.method == 'POST':
#         symbol = request.form.get("symbol")

#         # Validate symbol input
#         if not symbol:
#             return apology("You have to enter a Stock's Symbol", 400)

#         sold_shares = request.form.get("shares")

#         # Check if shares is a positive integer
#         try:
#             shares = int(shares)
#             if sold_shares <= 0:
#                 return apology("Please enter a positive number of Shares", 400)
#             for stock in info:
#                 if stock["Symbol"] == symbol:
#                     if sold_shares > stock["TotalShares"]:
#                         return apology("You don't have enough shares", 400)
#                     break
#         except ValueError:
#             return apology("Shares must be a whole number", 400)

#         quoted_stock = lookup(symbol)

#         stock_name = symbol
#         stock_price = quoted_stock["price"]
#         total = stock_price * float(sold_shares)
#         date_time = datetime.now()

#         db.execute("INSERT INTO sell (username, Symbol, Shares, Price, Total, DateTime) VALUES (?, ?, ?, ?, ?, ?)",
#                    sell_username, stock_name, sold_shares, usd(stock_price), usd(total), date_time)

#         remaining_cash = total + cash

#         db.execute("UPDATE users SET cash = :cash WHERE username = :username",
#                    cash=remaining_cash, username=sell_username)

#         db.execute("UPDATE portfolio SET Shares = Shares - shares WHERE user_id = :user_id AND Symbol = :stock_name",
#                    shares=sold_shares, user_id=user_id, Symbol=stock_name)
#         updated_shares_number = db.execute("SELECT COUNT(Shares) FROM portfolio WHERE user_id = :user_id",
#                                            user_id=user_id)

#         if updated_shares_number == 0:
#             db.execute("DELETE FROM portfolio WHERE user_id = :user_id AND Symbol = :symbol AND Shares = 0",
#                        user_id=user_id, Symbol=stock_name, Shares=sold_shares)

#         flash("Sold!")
#         #redirect_url = f"/?bought={bought}"

#         return redirect("/")
#     else:
#         return render_template("sell.html", info=info, cash=usd(cash))






































import os
from datetime import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    source = request.args.get('source')

    if source == 'buy':
        # Show buy table information
        user_id = session.get("user_id")
        info = db.execute("SELECT Symbol, SUM(Shares) AS TotalShares FROM portfolio WHERE user_id = ? GROUP BY Symbol", (user_id,))

    else:
        # Show sell table information
        user_id = session.get("user_id")
        info = db.execute("SELECT Symbol, SUM(Shares) AS TotalShares FROM portfolio WHERE user_id = ? GROUP BY Symbol", (user_id,))

    total_cash = 10000.00
    total_stock_value = 0

    for stock in info:
        quoted_stock = lookup(stock["Symbol"])
        stock["Price"] = quoted_stock["price"]
        stock["Total"] = stock["Price"] * stock["TotalShares"]
        total_stock_value += float(stock["Total"])

    cash = total_cash - total_stock_value

    # Format the values to dollar amounts after all calculations are done
    for stock in info:
        stock["Price"] = usd(stock["Price"])
        stock["Total"] = usd(stock["Total"])

    return render_template("portfolio.html", stocks=info, cash=usd(cash), total_cash=usd(total_cash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    user_id = session.get("user_id")
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]['cash']
    buy_username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)[0]['username']
    total_cash = cash

    if request.method == 'POST':
        symbol = request.form.get("symbol")

        # Validate symbol input
        if not symbol:
            return apology("You have to enter a Stock's Symbol", 400)

        shares = request.form.get("shares")

        # Check if shares is a positive integer
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Please enter a positive number of Shares", 400)
        except ValueError:
            return apology("Shares must be a whole number", 400)

        quoted_stock = lookup(symbol)
        if not quoted_stock:
            return apology("Sorry, the symbol doesn't exist!", 400)

        stock_name = quoted_stock["symbol"]
        stock_price = quoted_stock["price"]
        total = stock_price * float(shares)
        date_time = datetime.now()

        if total > total_cash:
            return apology("Sorry, you don't have ENOUGH CASH to complete the transaction")

        db.execute("INSERT INTO buy (username, Symbol, Shares, Price, Total, DateTime) VALUES (:username, :symbol, :shares, :price, :total, :date_time)",
                   username=buy_username, symbol=stock_name, shares=shares, price=stock_price, total=total, date_time=date_time)

        # Check if the symbol exists in the portfolio for the current user
        symbol_in_portfolio = db.execute("SELECT Symbol FROM portfolio WHERE user_id = :user_id AND Symbol = :symbol",
                                         user_id=user_id, symbol=stock_name)

        if symbol_in_portfolio:
            # If the symbol exists, update the number of shares
            db.execute("UPDATE portfolio SET Shares = Shares + :shares WHERE user_id = :user_id AND Symbol = :symbol",
                       shares=shares, user_id=user_id, symbol=stock_name)
        else:
            # If the symbol does not exist, insert the new Symbol and Shares
            db.execute("INSERT INTO portfolio (user_id, Symbol, Shares) VALUES (:user_id, :symbol, :shares)",
                       user_id=user_id, symbol=stock_name, shares=shares)

        remaining_cash = total_cash - total

        db.execute("UPDATE users SET cash = :cash WHERE username = :username",
                   cash=remaining_cash, username=buy_username)  # updating the users table

        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html", cash=usd(cash))


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)[0]['username']



    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == 'POST':
        symbol = request.form.get("symbol")

        # Validate symbol input
        if not symbol:
            return apology("You have to enter a Stock's Symbol", 400)

        # The return of the Lookup function and ordered as listed in helpers.py
        quoted_stock = lookup(symbol)

        # Checking the return of the lookup function
        if quoted_stock == None:
            return apology("Sorry, the symbol doesn't exist!", 400)
        return render_template("/quoted.html", quoted_stock=quoted_stock, symbol=quoted_stock["symbol"], price=usd(quoted_stock["price"]))

    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Clearing the session
    session.clear()

    reg_username = request.form.get("username")
    reg_password = request.form.get("password")
    reg_password_confirm = request.form.get("confirmation")

    # Username validation against blank or already existed username

    if request.method == 'POST':
        if not reg_username:
            return apology("Sorry, you have to Enter a username", 400)
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=reg_username)
        if len(rows) > 0:
            return apology("Sorry, this username is already taken", 400)

        # Password validation against blank password input in password and confirmation inputs and against mismatch.

        if not reg_password or not reg_password_confirm:
            return apology("Sorry, you have to Enter and/or confirm a password", 400)

        if reg_password != reg_password_confirm:
            return apology("Sorry, your passwords are not matched, please enter and confirm a valid password", 400)
        hashed = generate_password_hash(reg_password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", reg_username, hashed)

        return redirect("/login")

    else:

        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session.get("user_id")
    sell_username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=user_id)[0]['username']
    info = db.execute("SELECT Symbol, SUM(Shares) AS TotalShares FROM buy WHERE username = ? GROUP BY Symbol", (sell_username,))
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]['cash']

    if request.method == 'POST':
        symbol = request.form.get("symbol")

        # Validate symbol input
        if not symbol:
            return apology("You have to enter a Stock's Symbol", 400)

        sold_shares = request.form.get("shares")

        # Check if shares is a positive integer
        try:
            sold_shares = int(sold_shares)
            if sold_shares <= 0:
                return apology("Please enter a positive number of Shares", 400)
            for stock in info:
                if stock["Symbol"] == symbol:
                    if sold_shares > stock["TotalShares"]:
                        return apology("You don't have enough shares", 400)
                    break
        except ValueError:
            return apology("Shares must be a whole number", 400)

        quoted_stock = lookup(symbol)

        stock_name = symbol
        stock_price = quoted_stock["price"]
        total = stock_price * float(sold_shares)
        date_time = datetime.now()

        db.execute("INSERT INTO sell (username, Symbol, Shares, Price, Total, DateTime) VALUES (?, ?, ?, ?, ?, ?)",
                   sell_username, stock_name, sold_shares, usd(stock_price), usd(total), date_time)

        remaining_cash = total + cash

        db.execute("UPDATE users SET cash = :cash WHERE username = :username",
                   cash=remaining_cash, username=sell_username)

        symbol_in_portfolio = db.execute("SELECT Symbol FROM portfolio WHERE user_id = :user_id AND Symbol = :symbol",
                                         user_id=user_id, symbol=stock_name)

        if symbol_in_portfolio:
            # If the symbol exists, update the number of shares
            db.execute("UPDATE portfolio SET Shares = Shares - :shares WHERE user_id = :user_id AND Symbol = :symbol",
                       shares=sold_shares, user_id=user_id, symbol=stock_name)
        else:
            # If the symbol does not exist, insert the new Symbol and Shares
            db.execute("INSERT INTO portfolio (user_id, Symbol, Shares) VALUES (?, ?, ?)",
                       (user_id, stock_name, sold_shares))

        updated_shares_number = db.execute("SELECT COUNT(Shares) FROM portfolio WHERE user_id = :user_id AND Symbol = :symbol",
                                           user_id=user_id, symbol=stock_name)

        if updated_shares_number[0]["COUNT(Shares)"] == 0:
            db.execute("DELETE FROM portfolio WHERE user_id = :user_id AND Symbol = :symbol AND Shares = 0",
                       user_id=user_id, symbol=stock_name)

        flash("Sold!")
        return redirect("/")
    else:
        return render_template("sell.html", info=info, cash=usd(cash))
