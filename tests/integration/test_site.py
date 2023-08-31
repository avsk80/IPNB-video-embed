from IPNBvideoembed.site import embed_site
from IPNBvideoembed.custom_exception import InvalidURLException
from IPNBvideoembed.logger import logger
import pytest

class TestEmbedSite:
    URL_test_good_data = [
    ("http://pytorch.org", "success"),
    ("https://pytorch.org", "success"),
    ]
    
    URL_test_bad_data = [
    ("http://pytorch"),
    ("http//pytorch"),
    ("http:/pytorch"),
    ("http/pytorch"),
    ("http/pytorch"),
    ("pytorch.org"),
    ("http://asyef/"),
    ]
    
    @pytest.mark.parametrize("url, expected", URL_test_good_data)
    def test_embed_site_good_data(self, url, expected):
        assert embed_site(url) == expected
        
    @pytest.mark.parametrize("url", URL_test_bad_data)
    def test_embed_site_bad_data(self, url):
        with pytest.raises(InvalidURLException):
            embed_site(url)
                
    
    