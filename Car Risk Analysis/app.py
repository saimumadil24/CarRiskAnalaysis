from flask import Flask,request, render_template
import pickle as pk

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def risk_pred():
    if request.method=='POST':
        model=pk.load(open(r'C:\Users\Saimum Adil Khan\OneDrive\Desktop\Flask\Car Risk Analysis\Car_Driving_Risk_pickle.pkl','rb'))
        speed=float(request.form.get('speed'))
        prediction=model.predict([[speed]])

    else:
        prediction=''
    
    return render_template('home.html',output=prediction)

if __name__=='__main__':
    app.run(debug=True)