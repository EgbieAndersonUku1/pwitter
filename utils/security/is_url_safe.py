from urllib.parse import urlparse, urljoin

from flask import request, abort
from werkzeug.utils import redirect


def is_safe_url(target):

    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def if_url_is_safe_redirect(url):

    if not is_safe_url(url):
        abort(404)
    return redirect(url)