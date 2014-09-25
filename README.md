sqlii
=====

A web fuzzer to find sites vulnerable to Union based SQL injection. It uses page comparison to find a large set of sites, allowing for a better detection rate of the pages. The search scanner was created by a third party, and due to Google cutting support for the API, means that the user can only get upto 64 search results at a time. Hope is to transfer to another search engine of find a permanent work-around for this.

Reason for version 0.1 and not version 1 is that sqlii is currently a command-line program. The hope is to include a GUI before offically calling it version 1.

Version 0.1 - Allows user to search Google for vulnerable websites and test them
            - Saves list from Google to file to allow user to check later
            - User can test sites by entering URL into the application
            - Uses page comparison to check vulnerables on the site
            - Opens user's default web browser with vulnerable URL in it
