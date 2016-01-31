#!/usr/bin/env python
import os
import sys
import subprocess
import re

def read_env():
    """Pulled from Honcho code with minor updates, reads local default
    environment variables from a .env file located in the project root
    directory.

    """
    try:
        with open('.env') as f:
            content = f.read()
    except IOError:
        content = ''

    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            os.environ.setdefault(key, val)

def shell_command():
    command_text = 'cd front && gulp dev'
    print 'begin command: %s' % command_text
    print subprocess.Popen(command_text, shell=True, stdout=subprocess.PIPE).stdout.read()
    # print os.popen(command_text).read()
    print 'end command: %s' % command_text


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line
    read_env()

    if 'livereload' in sys.argv:
        from django.core.wsgi import get_wsgi_application
        from livereload import Server

        application = get_wsgi_application()
        server = Server(application)

        # Add your watch
        server.watch('front/src/assets', shell_command, 'forever')
        server.watch('front/src/js', shell_command, 'forever')
        server.watch('front/src/scss', shell_command, 'forever')
        server.watch('front/src/views', shell_command, 'forever')
        server.serve(port=5000, host='0.0.0.0')
    else:
        execute_from_command_line(sys.argv)
