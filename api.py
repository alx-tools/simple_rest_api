from flask import Flask, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def all_routes(path):
    print "New request:"
    print "\t-path: /%s" % path
    print "\t-verb: %s" % request.method
    
    print "\t-headers: "
    for k,v in request.headers:
        print "\t\t%s = %s" % (k, v)
    
    print "\t-query parameters: "
    for qp in request.args:
        print "\t\t%s = %s" % (qp, request.args.get(qp))
    
    print "\t-raw body: "
    print "\t\t%s" % request.data

    print "\t-form body: "
    for fb in request.form:
        print "\t\t%s = %s" % (fb, request.form.get(fb))

    print "\t-json body: "
    print "\t\t%s" % request.json
    
    return "OK"

if __name__ == '__main__':
    app.run(host='localhost', port=8989, debug=False)  

