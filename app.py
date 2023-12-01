import subprocess
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Replace 'your_template_name.html' with your actual template filename

@app.route('/messenger_integration')
def messenger_integration():
    # Replace 'path_to_your_exe.exe' with the actual path to your executable file
    exe_path = 'C:/Users/shash/OneDrive/Desktop/NITK/main.exe'
    
    try:
        subprocess.Popen([exe_path], shell=True)  # Run the executable
    except Exception as e:
        print(f"Error running the executable: {e}")
    
    return redirect(url_for('index'))  # Redirect back to the main page after running the executable

if __name__ == '__main__':
    app.run(debug=True)
