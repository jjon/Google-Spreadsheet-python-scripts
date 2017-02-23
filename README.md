# Use Python to Parse Published Google Spreadsheet Data.

It's not easy to determine what URL parameters Google makes available for a Google Spreadsheet that has been 'published'. Here is a (not exhaustive) list of some of the URLs that a Google spreadsheet will respond to.

* this URL will take you to the published spreadsheet:
[https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0](https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0)

* Here's some dope:
[http://stackoverflow.com/questions/23446449/google-sheet-embed-url-documentation](http://stackoverflow.com/questions/23446449/google-sheet-embed-url-documentation).

* Here's some more useful dope:
[http://acrl.ala.org/techconnect/post/query-a-google-spreadsheet-like-a-database-with-google-visualization-api-query-language](http://acrl.ala.org/techconnect/post/query-a-google-spreadsheet-like-a-database-with-google-visualization-api-query-language)

* You can get a plain html representation here:
[https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml](https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml)

* You can also get jsonp (json with padding) from a URL that looks like this:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?alt=json-in-script](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?alt=json-in-script)

* You can also get some sort of xml, like this:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?format=xml](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?format=xml)

* inexplicably, you get the same result if you specify format=csv or just:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic)

* for our purposes here, some prettyprinted json is easiest to work with:
[https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true&alt=json](https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true&alt=json)


our sample spreadsheet looks like this:
Sample Spreadsheet : Sheet1 Table:

| name        | city          | state | zip   |
| ----------- | ------------- | ----- | ----- |
| bob         | Seattle       | Wa    | 98116 |
| carol       | San Francisco | Ca    | 62742 |
| ted         | Detroit       | Mi    | 48104 |
| alice       | Denver        | Co    | 54321 |

The JSON representation seems to me bizarre and opaque. The actual data of the spreadsheet cells has to be parsed from a string. The relevant portion of the JSON representation is the `list` of `entry` objects that each have a `title` and a `content` property. The `entry` object for the first row of our spreadsheet looks like this:<code>
<pre>
    {
    "id": {
        "$t": "https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic/cokwr"
    },
    "updated": {
        "$t": "2017-02-22T00:46:48.404Z"
    },
    "category": [
         {
          "scheme": "http://schemas.google.com/spreadsheets/2006",
          "term": "http://schemas.google.com/spreadsheets/2006#list"
         }
    ],
    "title": {
        "type": "text",
        "$t": "bob"
    },
    "content": {
        "type": "text",
        "$t": "city: Seattle, state: Wa, zip: 98116"
    },
    "link": [
         {
          "rel": "self",
          "type": "application/atom+xml",
          "href": "https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic/cokwr"
         }
    ]
    },
</pre>
</code>

The script does only the most rudimentary parsing of the payload string. I an envision all sorts of cases in which ambiguous data in the string would defeat this script; so, use at your own risk.
