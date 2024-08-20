# app.py
from flask import Flask, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import io
import pdf2image
import transformers
import torch
import torch.nn.functional as F
import numpy as np
import random
device = "cpu"
model_name ="TrustSafeAI/RADAR-Vicuna-7B"
detector = transformers.AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
detector.eval()
detector.to(device)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/proctored')
def proctored():
    return render_template('proctored.html')
@app.route('/onlineproctored')
def live_proctoring():
    import audio
    import head_pose
    import detection
    import threading as th


    if __name__ == "__main__":
        # main()
        head_pose_thread = th.Thread(target=head_pose.pose)
        audio_thread = th.Thread(target=audio.sound)
        detection_thread = th.Thread(target=detection.run_detection)

        head_pose_thread.start()
        audio_thread.start()
        detection_thread.start()

        head_pose_thread.join()
        audio_thread.join()
        detection_thread.join()
    return render_template('proctored.html')

    

@app.route('/assignments')
def assignments():
    return render_template('assignment.html')

@app.route('/creative_writing')
def creative_writing():
    return render_template('creative_writing.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')
@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    
    if 'text-input' in request.form:
        text_input = request.form['text-input']
        Text_input =text_input
        with torch.no_grad():
            inputs = tokenizer(Text_input, padding=True, truncation=True, max_length=512, return_tensors="pt")
            inputs = {k:v.to(device) for k,v in inputs.items()}
            output_probs = F.log_softmax(detector(**inputs).logits,-1)[:,0].exp().tolist()
            print("There are",len(Text_input),"input instances")
        print("Probability of AI-generated texts is",output_probs)
        # Here you would integrate plagiarism checking logic
        # For demonstration, we'll just display the text input
        return render_template('assignment.html', result=output_probs)
    
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
