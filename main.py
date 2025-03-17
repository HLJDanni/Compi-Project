import ply.lex as lex

# Definimos los tokens
tokens = (
    'KEYWORD', 'IDENTIFIER', 'NUMBER', 'OP', 'SYMBOL'
)

# Palabras clave
keywords = {
    'int': 'KEYWORD',
    'float': 'KEYWORD',
    'return': 'KEYWORD',
    'if': 'KEYWORD',
    'else': 'KEYWORD'
}

# Expresiones regulares para tokens
literals = "=+-*/(){};"



def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()


def analyze_code(code):
    lexer.input(code)
    tokens_list = [(tok.type, tok.value) for tok in lexer]
    return tokens_list


def generate_html_report(tokens, filename="tokens.html"):
    html = """
    <html>
    <head><title>Reporte de Tokens</title></head>
    <body>
        <h2>Lista de Tokens</h2>
        <table border='1'>
            <tr><th>Token</th><th>Tipo</th></tr>
    """

    for token_type, token_value in tokens:
        html += f"<tr><td>{token_value}</td><td>{token_type}</td></tr>"

    html += """
        </table>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)
    print(f"Reporte generado: {filename}")


sample_code = """
int x = 10;
float y = 5.5;
return x + y;
"""
tokens = analyze_code(sample_code)
generate_html_report(tokens)
