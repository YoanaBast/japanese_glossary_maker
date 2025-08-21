I want to make glossaries fast and with minimal effort, but ChatGPT (at least the free version) does not extract text well. So I spent a few hours and lots of effort to make this console program! :)

You can choose to add words to 2 json files:
1. db.json: this holds the words in the glossary, they are also accessible in result.txt in a clean form, ready for export. 
2. common.json: here I move words I don't want to see in my glossary. It is used for validation. 

- A custom input func allows dumping text in any format and the inout will not submit unless 'END' is typed on a new line. Any format can be dumped directly. 
- From there the program takes only Japanese words, removes duplicates, excludes those who already exist in the glossary, as well as those in the unwanted (common) db, sorts and uploads. 

How to use:
the janome lib needs to be installed for this code to run, it's a console program, so run on terminal/IDE