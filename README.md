It's not easy to determine what URL parameters Google makes available for a
Google Spreadsheet that has been 'published'.

this URL will take you to the published spreadsheet:
[https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0](https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0)

Here's some dope:
[http://stackoverflow.com/questions/23446449/google-sheet-embed-url-documentation](http://stackoverflow.com/questions/23446449/google-sheet-embed-url-documentation).

Here's some more useful dope:
[http://acrl.ala.org/techconnect/post/query-a-google-spreadsheet-like-a-database-with-google-visualization-api-query-language](http://acrl.ala.org/techconnect/post/query-a-google-spreadsheet-like-a-database-with-google-visualization-api-query-language)

this URL will take you to the published spreadsheet:
[https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0](https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0)

You can get a plain html representation here:
[https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml](https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml)

You can also get jsonp (json with padding) from a URL that looks like this:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?alt=json-in-script](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?alt=json-in-script)

You can also get some sort of xml, like this:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?format=xml](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?format=xml)

inexplicably, you get the same result if you specify format=csv or just:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic)

for our purposes here, some prettyprinted json is easiest to work with:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true)
&alt=json

our sample spreadsheet looks like this:
Sample Spreadsheet : Sheet1 Table:

        | name        | city          | state | zip   |
        |:------------|:-------------:|:----- |:----- |
        | bob         | Seattle       | Wa    | 98116 |
        | carol       | San Francisco | Ca    | 62742 |
        | ted         | Detroit       | Mi    | 48104 |
        | alice       | Denver        | Co    | 54321 |

