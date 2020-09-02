from flask import Flask, request, render_template 
import flask

app = Flask('revival')

@app.route('/')

def main():
    return render_template('welcome.htm')

@app.route('/yourPharmacies', methods=['GET', 'POST'])

def yourPharmacies():
	return render_template('yourPharmacies.htm')

if __name__ == '__main__':   # means 'if script is running from terminal'
	app.run(debug=True)