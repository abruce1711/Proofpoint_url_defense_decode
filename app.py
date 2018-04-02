from flask import Flask, render_template, flash

import models, forms

app = Flask(__name__)
app.secret_key = "svadagsnbbadgndgn"


@app.route('/', methods=('GET', 'POST'))
def index():
    form = forms.DecodeURL()
    url = ''
    if form.validate_on_submit():
        url = form.url.data
        if "https://urldefense.proofpoint.com/v2/url?u=" in url:
            url = models.decode(url)
            form.url.data = url
            flash("Decoded", "success")
        else:
            url = "fail"
            flash("Please enter a valid Proofpoint URL", "error")
    return render_template('index.html', form=form, url=url)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
