from flask import Flask,jsonify
app = Flask(__name__)


courses = [ {'id':'0',
             'fname':'Nagesh',
            'lname':'bellala',
            'mobile':'9177601023',
            'company':'TCS'},
            {'id':'1',
             'fname':'sravani',
            'lname':'bandari',
            'mobile':'7659025923',
            'company':'omni hospitals'
             },
            {'id':'2',
            'fname':'pubg',
            'lname':'t',
            'mobile':'7702288397',
            'company':'sunera'},
            {'id':'3',
            'fname':'akhil',
            'lname':'m',
            'mobile':'7207751520',
            'company':'TechM'
             }]
@app.route('/')
def hello_world():
    return " hello nagesh"

@app.route('/courses',methods = ['GET'])
def get():
    return jsonify({'courses':courses})


@app.route('/courses/<int:id>',methods = ['GET'])

def get_id(id):
    return jsonify({'courses':courses[id]})

@app.route("/courses",methods = ['POST'])
def create():
    course = {'id':'4',
            'fname':'Maruti',
            'lname':'M',
            'mobile':'9603426077',
            'company':'POLICE'
              }
    courses.append(course)
    return jsonify({'created':course})

@app.route('/courses/<int:id>',methods = ['PUT'])
def course_update(id):
    courses[id]['company'] = "xyz"
    return jsonify({'course':courses[id]})
if __name__ == '__main__':
    app.run()