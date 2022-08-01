import pytest

import src.data.countries


class TestCountries:

    @pytest.fixture()
    def countries(self):

        return src.data.countries.Countries()

    def test_exc(self, countries):

        message = countries.exc()
        assert message.startswith('The countries gazetteer')
