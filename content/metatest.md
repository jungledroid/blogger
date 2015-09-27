Title: Meta data test
Date: 2015-9-17 23:00
Modified: 2015-9-17 23:30
Category: test
Tags: pelican,test,metadata
Slug:my-super-post
Authors:Joe Zhang,Jerry Li
Summary: summary of metadata test
Status: published

This is an metadata test markdown blog
It is possible to translate articles. To do so, you need to add a lang meta attribute to your articles/pages and set a DEFAULT_LANG setting (which is English [en] by default). With those settings in place, only articles with the default language will be listed, and each article will be accompanied by a list of available translations for that article
[a link to test file]({filename}cat/test.md)
[a link to static file]({filename}images/favicon.ico)



There are two ways to specify the identifier:

    :::java
    System.out.print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!java
    System.out.print("The path-less shebang syntax *will* show line numbers.")