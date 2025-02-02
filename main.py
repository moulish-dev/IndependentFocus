import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import requests
import os
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

gemini_api_key = os.environ.get('API_KEY')

# API Key debugging
if gemini_api_key:
    print("API Key:", gemini_api_key)
else:
    print("API Key not found. Please set the environment variable.")

print(gemini_api_key)
class IndependentFocus(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Print debug message for start
        print(f"Requested path: {self.path}")
        
        # Check if the requested path is root "/"
        if self.path == '/':
            file_path = 'home.html'
            self.serve_html_page(file_path)
        elif self.path == '/results':
            file_path = 'dasboard.html'
            self.serve_html_page(file_path)
        elif self.path.startswith('/assets/'):
            asset_path = self.path[1:]  # Remove the leading '/'
            try:
                with open(asset_path, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/svg+xml+jpg+png')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "File not found.")
        elif self.path == '/styles.css':
            css_file_path = "styles.css"
            try:
                with open(css_file_path, 'r') as file:
                    css_content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(css_content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found.")
        elif self.path == '/results-styles.css':
            css_file_path = "results-styles.css"
            try:
                with open(css_file_path, 'r') as file:
                    css_content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(css_content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found.")
        elif self.path == '/app.js':
            js_file_path = "app.js"
            try:
                with open(js_file_path, 'r') as file:
                    js_content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'application/javascript')
                    self.end_headers()
                    self.wfile.write(js_content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found.")
        else:
            # Handle paths that are not "/"
            self.send_error(404, "Page not found")
    
    #serving html pages
    def serve_html_page(self, file_path):
        try:
            # Open and read the HTML file
            with open(file_path, 'r') as file:
                html_content = file.read()
            # Send a 200 OK response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Write the HTML content to the response
            self.wfile.write(html_content.encode('utf-8'))
        # Handle file not found error
        except FileNotFoundError:
            self.send_error(404, "File not found")


    def format_combined_ideas(self, combined_ideas):
        # Splitting the ideas by new lines
        ideas_list = combined_ideas.split('\n')
        formatted_ideas = '<ul class="ideas-list">'  # Start an unordered list with a class
        for idea in ideas_list:
            if idea.strip():  # Check if the idea is not just whitespace
                # Replace Markdown with HTML tags
                idea = self.convert_markdown_to_html(idea.strip())
                formatted_ideas += f'<li class="idea-item">{idea}</li>'  # Add each idea as a list item with a class
        formatted_ideas += '</ul>'  # End the unordered list
        return formatted_ideas

    def convert_markdown_to_html(self, text):
        # Convert headings with classes
        text = text.replace('## ', '<h2 class="heading1">').replace('\n##', '</h2>')  # Convert to <h2>
        text = text.replace('# ', '<h1 class="heading2">').replace('\n#', '</h1>')  # Convert to <h1>
        
        # Replace closing tags correctly
        text = text.replace('</h1>', '</h1>\n').replace('</h2>', '</h2>\n')

        #adding paragraph tags and classes to be styled in styles.css
        text = text.replace('***', '<span class="heading3">').replace('***', '</span></strong>')  # ***text***
        text = text.replace('**', '<span class="heading4">').replace('**', '</span>')  # **text**
        text = text.replace('*', '<span class="heading5">').replace('*', '</span>')  # *text*

        
        text = text.replace('</span></span>', '</span>').replace('</span></span>', '</span>')

        # Ensure proper formatting by removing excess tags
        # text = text.replace('<p></p>', '').replace('<p></p>', '')  # Remove empty tags

        return text

    
    #updating results.html with the parameter given
    def update_results(self, combined_ideas):
        with open('results.html','w') as f:
            f.write(f'''
                <!DOCTYPE html>
                <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
                <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
                <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
                <!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
                <html>
                    <head>
                        <meta charset="utf-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <title></title>
                        <meta name="description" content="">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="stylesheet" href="results-styles.css">
                    
                    </head>
                    <body style="background-size: no-repeat;">
                        <!--[if lt IE 7]>
                            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
                        <![endif]-->
                        <div class='background-mask'></div>
                        <h1>Results</h1>
                        {self.format_combined_ideas(combined_ideas)}
                        <h5>Model Used: Google Gemini 1.5 Flash</h5>
                        <script src="" async defer></script>
                    </body>
                </html>
            ''') 


    #get ideas list and combine them using ai and send combined ideas
    def combine_ideas_usingAI(self,ideas):
        api_endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={gemini_api_key}'
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"Here are the following ideas:\n{ideas}\nPlease summarize them into three distinct ideas."
                        }
                    ]
                }
            ]
        }
        

        try:
            #posting to the gemini ai
            prompt = f"""
                    Based on the following ideas, generate three new, creative ideas that are inspired by the input concepts. Each idea should be unique and combine elements from the provided ideas:
                    {ideas}Return the ideas in a clear format, highlighting their potential benefits and functionalities.
                """
            response = model.generate_content(prompt)
            
            #getting the json response
            # combined_ideas = response.json()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return "Error in api call"

    

    def do_POST(self):
        if self.path=='/idea-submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            ideas = parsed_data.get('idea', [])
            idea_list = [idea for idea in ideas]
            print(idea_list)
            
            #send ideas to gemini ai
            combined_ideas = self.combine_ideas_usingAI(idea_list)

            if combined_ideas:
                print(f"Combined Ideas: {combined_ideas}")
                # Directly access the candidates from the response object
                if combined_ideas.candidates:
                    # Extract the text content from the first candidate
                    generated_ideas = combined_ideas.candidates[0].content.parts[0].text
                else:
                    print("No content generated.")
                    generated_ideas = "No content generated."
                # Update results.html with the combined ideas
                self.update_results(generated_ideas)  # Assuming combined_ideas is a list
                self.send_response(302)  # Redirect after POST
                self.send_header('Location', '/results')  # Redirect to results
                self.end_headers()
            else:
                # Handle error case and inform the user
                self.send_response(500)  # Internal Server Error
                self.end_headers()




def runserver(server_class=HTTPServer, handler_class=IdeaGeneration, port=8070):
    # Set up the server address and port
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    # Open the browser to localhost and specified port
    webbrowser.open(f'http://localhost:{port}/')
    
    print(f"Server starting on port {port}...")
    httpd.serve_forever()


# Run the server if this script is executed
if __name__ == '__main__':
    runserver()

