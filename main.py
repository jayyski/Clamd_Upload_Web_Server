import clamd
from flask import Flask,render_template,request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/Malware'
cd = clamd.ClamdUnixSocket() # Connect to Clamd

def scan_file(file):    
    response = cd.scan(app.config['UPLOAD_FOLDER'] + file.filename)
    response = list(response.items())
    print('scsanning file')
    # Check if file is clean, infected or not found

    if (response[0][1][1]) == None:
        
        return('File clean')
        
    elif (response[0][1][1]) == 'No such file or directory.':
        
        return('File not found')
        
    else:
        
        return('File infected:  ' + response[0][1][1])    


@app.route('/', methods=['GET'])
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file:
            file.save(app.config['UPLOAD_FOLDER'] + file.filename)
            return scan_file(file)
    
    return 'File not uploaded'
    

if __name__ == '__main__':
    
    
    try:
        
        cd.ping() # Test Clamd
        cd.reload() # Reload Clamd Database
        app.run('0.0.0.0', port=8000) # Run Flask app
        
    except:
        
        print('Clamd not running or flask app not running')
        