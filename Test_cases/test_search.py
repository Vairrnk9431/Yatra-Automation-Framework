
import pytest
from Pages.yatra_launch_pages import Launchpage
from Utilities.Utils import Utils



@pytest.mark.usefixtures("setup")
class Test_searchandverify():
    def test_search(self):

        yatralp = Launchpage(self.driver)
        search_flight_results=yatralp.searchflight("Mumbai","New Delhi")
        
        yatralp.page_scroll()

        # Search result actions
        # yatrasf = SearchFlightResult(self.driver)
        search_flight_results.get_filter_flights_by_stops("2 stop")

        all_flights= search_flight_results.get_filter_search_result()
        yatrautil=Utils()
        yatrautil.assertListItem( all_flights,"2")






       
        



