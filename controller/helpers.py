from flask import jsonify

get_urls = ['compDesc', 'highlights', 'testing', 'cutAndRender',
            'cutAndRender.canCut', 'cutAndRender.canRender',
            'cutAndRender.cutProgress', 'cutAndRender.renderProgress']


def check_url(function):
    def wrapper(ID, key):
        if key in get_urls:
            return function(ID, key)
        return jsonify({'status': 'error'})
    return wrapper
