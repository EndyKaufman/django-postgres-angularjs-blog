#!/usr/bin/env python
import os
import sys
import subprocess


def shell_command():
    command_text = 'cd front && gulp dev'
    print 'begin command: %s' % command_text
    print subprocess.Popen(command_text, shell=True, stdout=subprocess.PIPE).stdout.read()
    # print os.popen(command_text).read()
    print 'end command: %s' % command_text


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

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
