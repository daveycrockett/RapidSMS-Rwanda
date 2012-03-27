Reporters and Groups
========================
I'm getting the following error when I try to access this view.  Help?::

    Traceback (most recent call last):
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/core/servers/basehttp.py", line 280, in run
        self.result = application(self.environ, self.start_response)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/core/servers/basehttp.py", line 674, in __call__
        return self.application(environ, start_response)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/core/handlers/wsgi.py", line 241, in __call__
        response = self.get_response(request)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/core/handlers/base.py", line 141, in get_response
        return self.handle_uncaught_exception(request, resolver, sys.exc_info())
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/core/handlers/base.py", line 180, in handle_uncaught_exception
        return callback(request, **param_dict)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/views/defaults.py", line 24, in server_error
        return http.HttpResponseServerError(t.render(Context({})))
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/__init__.py", line 173, in render
        return self._render(context)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/__init__.py", line 167, in _render
        return self.nodelist.render(context)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
        bits.append(self.render_node(node, context))
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/__init__.py", line 809, in render_node
        return node.render(context)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/loader_tags.py", line 103, in render
        compiled_parent = self.get_parent(context)
    
      File "/home/david/Projects/PythonEnv/rwanda/lib/python2.6/site-packages/django/template/loader_tags.py", line 97, in get_parent
        raise TemplateSyntaxError(error_msg)
    
    TemplateSyntaxError: Invalid template name in 'extends' tag: ''. Got this from the 'base_template' variable.

.. toctree::
   :maxdepth: 2

   reminders
   triggers
   statistics
