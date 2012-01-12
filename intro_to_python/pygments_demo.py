from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

if __name__ == '__main__':
    # get this file
    code = open("pygments_demo.py", "rw").read()
    
    # figure out the lexer
    lexer = get_lexer_by_name("python", stripall=True)
    
    # construct the formatter
    formatter = HtmlFormatter(linenos=False, cssclass="source")
    
    # style and formatting
    css = HtmlFormatter().get_style_defs('.source')
    highlighted_code = highlight(code, lexer, formatter)        
    page = """
        <html>
            <head><style>{css}</style></head>
            <body>{highlighted_code}</body>
        </html>
        """.format(css=css, highlighted_code=highlighted_code)
    print(page)