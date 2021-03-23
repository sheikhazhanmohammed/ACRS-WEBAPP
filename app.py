from typing import final
from flask import Flask, render_template, url_for
from wordList import hindiWordsList, tamilWordsList, wordGenerator, G2R
from forms import EntropyToWordsAndKeys

app = Flask(__name__)
app.config['SECRET_KEY']= '3445ff020d9e96783e6747f9f8b49b77'



@app.route('/', methods=['GET','POST'])
def home():
    form = EntropyToWordsAndKeys()
    if form.validate_on_submit():
        wordList, finalList = wordGenerator(form.entropy.data, form.language.data)
        rootSeed, masterPrivateKey, masterChainCode = G2R(finalList)
        return render_template('generatedEntropy.html', wordList=wordList, entropy=form.entropy.data, rootSeed =rootSeed,
        masterChainCode = masterChainCode, masterPrivateKey = masterPrivateKey, title='Generated Entropy')
    return render_template('home.html', form = form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hindiWordsList')
def hindiWords():
    return render_template('hindiWordList.html', hindiWords=hindiWordsList, title='Hindi Words List')

@app.route('/tamilWordsList')
def tamilWords():
    return render_template('tamilWordList.html', tamilWords=tamilWordsList, title='Tamil Word List')

if __name__ == "__main__":
    app.run(debug=True)