import ply.lex as lex

# tokens
tokens = (
    'INT',
    'ID',
    'FUNCTION',
    'OPENPAREN',
    'CLOSEPAREN',
    'OPENBRACE',
    'CLOSEBRACE',
    'COMMA',
    'SEMICOLON',
    'EQ',
    'WHILE',
    'IF',
    'FOR',
    'PRINT',
    'OPENBRACKET',
    'CLOSEBRACKET',
    'PROGRAM'
)

# Expressões regulares
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_OPENBRACE = r'\{'
t_CLOSEBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQ = r'='
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_FUNCTION = r'function'
t_WHILE = r'while'
t_IF = r'if'
t_FOR = r'for'
t_PRINT = r'print'
t_PROGRAM = r'program'
t_INT = r'int'

# Ignorar comentário de linha
def t_comment_line(t):
    r'\/\/+'
    pass

# Ignorar comentário de multiplas linhas
def t_comment_multilines(t):
    r'\/\*.*?\*\/'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignorar espaços em branco e tabs
t_ignore = ' \n\t'

# Contar número de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    #dou apenas skip aos tokens inválidos
    t.lexer.skip(1)

# Fazer a execução do compilador:
lexer = lex.lex()
data1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

data2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

print("\n------------------- Data 1 -------------------")
lexer.input(data1)
while token := lexer.token():
    print(token)

print("\n\n------------------- Data 2 -------------------")
lexer.input(data2)
while token := lexer.token():
    print(token)