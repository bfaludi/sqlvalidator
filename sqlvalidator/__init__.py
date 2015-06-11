
import sys, io, re, os

def remove_comments(content):
    content = re.sub(ur'(--|\\)[^\n]*\n', u'', content)
    content = re.sub(ur'/\*((.|\n|\r)*?)\*/', u'', content)
    return content

def get_content():
    if len(sys.argv) == 1:
        content = sys.stdin.read().decode('utf-8')
    
    elif len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        content = io.open(sys.argv[1], 'r', encoding = 'utf-8').read()
    
    else:
        print "Usage: generate-validate-sql [FILE]"
        sys.exit(1)

    return remove_comments(content)

def main():
    for stmt in map(unicode.strip, re.split(ur'\;[ ]*(\n|$)', get_content())):
        if stmt.upper().startswith( (u'SELECT', u'UPDATE', u'INSERT', u'DELETE', u'WITH') ):
            exec_stmt = u'EXPLAIN {};\n'.format(stmt)
            print exec_stmt
