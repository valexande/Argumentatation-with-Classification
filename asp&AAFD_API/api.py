from flask import Flask, request, render_template, jsonify
from extension import *
from create import *

app = Flask(__name__)

def mainASP(argument, attack, extension, problem):

   final = ""
   flagCreate = arg().createFile(argument, attack)
   if str(problem) == "1":
       if extension in ['cf', 'a', 'co']:
           e = compute(problem, extension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("semantics.lp", "w")
           f.write("")
           f.close()
           f = open('framework.lp', 'w')
           f.write("")
           f.close()
       else:
           e = compute(problem, extension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("semantics.lp", "w")
           f.write("")
           f.close()
           f = open('framework.lp', 'w')
           f.write("")
           f.close()
   elif str(problem) == "2":
       if extension in ['cf', 'a', 'co']:
           e = compute(problem, extension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("semantics.lp", "w")
           f.write("")
           f.close()
           f = open('framework.lp', 'w')
           f.write("")
           f.close()
       else:
           e = compute(problem, extension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("semantics.lp", "w")
           f.write("")
           f.close()
           f = open('framework.lp', 'w')
           f.write("")
           f.close()

   else:
       final = "Unfortunately, this is not an option"
       f = open("semantics.lp", "w")
       f.write("")
       f.close()
       f = open('framework.lp', 'w')
       f.write("")
       f.close()

   return final

def mainASPRule(selfProblem, selfExtension):

   final = ""
   if str(selfProblem) == "1":
       if selfExtension in ['cf', 'a', 'co']:
           e = compute(selfProblem, selfExtension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("framework.lp", "w")
           f.write("")
           f.close()
           f = open('semantics.lp', 'w')
           f.write("")
           f.close()
       else:
           e = compute(selfProblem, selfExtension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("framework.lp", "w")
           f.write("")
           f.close()
           f = open('semantics.lp', 'w')
           f.write("")
           f.close()
   elif str(selfProblem) == "2":
       if selfExtension in ['cf', 'a', 'co']:
           e = compute(selfProblem, selfExtension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("framework.lp", "w")
           f.write("")
           f.close()
           f = open('semantics.lp', 'w')
           f.write("")
           f.close()
       else:
           e = compute(selfProblem, selfExtension)
           flagPaste = e.pasteExtension()
           final = e.query()
           f = open("framework.lp", "w")
           f.write("")
           f.close()
           f = open('semantics.lp', 'w')
           f.write("")
           f.close()
   else:
       f = open("framework.lp", "w")
       f.write("")
       f.close()
       f = open('semantics.lp', 'w')
       f.write("")
       f.close()

   return final

def selfCreateASP(self, selfProblem, selfExtension):
    f = open("framework.lp", 'a')
    f.write(str(self))
    f.close()
    pfinal = mainASPRule(selfProblem, selfExtension)

    return pfinal


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    ##give only details for the framework
    argument = request.form['text1']
    attack = request.form['text3']
    extension = request.form['text5']
    problem = request.form['text7']

    if extension == "1":
        extension = "cf"
    elif extension == "2":
        extension = "a"
    elif extension == "3":
        extension = "co"
    elif extension == "4":
        extension = "gr"
    elif extension == "5":
        extension = "pr"
    elif extension == "6":
        extension = "st"
    else:
        pass

    ####write my own rules###
    selfASP = request.form['text8']
    selfExtension = request.form['text9']##the desired extension when he writes the rules
    selfProblem = request.form['text11']##what problem to solve
    if selfExtension == "1":
        selfExtension = "cf"
    elif selfExtension == "2":
        selfExtension = "a"
    elif selfExtension == "3":
        selfExtension = "co"
    elif selfExtension == "4":
        selfExtension = "gr"
    elif selfExtension == "5":
        selfExtension = "pr"
    elif selfExtension == "6":
        selfExtension = "st"
    else:
        pass


    if selfASP == "":
        try:
            combine = mainASP(argument, attack, extension, problem)
            f = open("semantics.lp", "w")
            f.write("")
            f.close()
            f = open('framework.lp', 'w')
            f.write("")
            f.close()
        except Exception as e:
            combine = "Sorry, possibly I could not parse something. Please press the reset button."
            f = open("semantics.lp", "w")
            f.write("")
            f.close()
            f = open('framework.lp', 'w')
            f.write("")
            f.close()
    else:
        combine = "The ASP you want to write is" + str(selfASP)
        combine = selfCreateASP(selfASP, selfProblem, selfExtension)
        f = open("semantics.lp", "w")
        f.write("")
        f.close()
        f = open('framework.lp', 'w')
        f.write("")
        f.close()


    final = ""
    result = {}
    for sentence in combine.split('\n'):
        sentence = '<p>' + str(sentence).replace('\r', '') + '<p>'
        final = final + sentence

    result['output'] = final

    return jsonify(result=result)



if __name__ == '__main__':
    #app.run(debug=True)##comment for my local use - uncomment for lab use
    app.run(host='0.0.0.0')##they need to enter the address http://192.168.1.7:5000