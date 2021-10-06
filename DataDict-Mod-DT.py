# WB Datadict Mod- Modified MySQL Workbench plugin to generate data dictionaries.
#
# Public domain 2021 LIGJ. All rights waived.

import os
import datetime
import webbrowser

from wb import *
import grt
import mforms as gui

# CONSTANTS
# =========

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="ISO-8859-1">
  <meta name="author" content="WB Datadict">
  <meta name="description" content="[PROJECTNAME] Data Dictionary.">
  
  <title>[PROJECTNAME] Data Dictionary</title>
  
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.4/jspdf.min.js"></script>
  <script src="http://cdn.jsdelivr.net/g/filesaver.js"></script>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Quantico:ital,wght@1,700&display=swap" rel="stylesheet">
  <link href="https://unpkg.com/pattern.css" rel="stylesheet">
  <script>
    // Highlight table corresponding to the current fragment in the URL.
    $(document).ready(function(){
      $("a").click(function() {
        var elem = $(this);
        // Remove all classes from tables.
        $("table").removeClass( "focused" )
        // Get a.href value and extract its fragment id.
        var id = elem.attr("href");
        // Highlight table using fragment id.
        $(id).addClass( "focused" );
      });
    });
  </script>

<style type="text/css">
    .pattern-dots-sm {
        background-image: radial-gradient(#ffffff59 .5px, #ffffff00 .5px);
        background-size: calc(10 * 1.5px) calc(10 * 1.5px);
    }
    
    h1 {
        text-shadow: 4px 3px #5450509e;
    }
    
    html {
        background-image: radial-gradient(#061f37d9, #040018);
    }

    ul {
        -webkit-column-count: 4;
        -webkit-column-gap: 20px;
        column-count: 4;
        column-gap: 20px;
        padding-bottom: 1rem;
        padding-right: 1rem;
        font-family: Arial;
        font-style: italic;
        margin-top: 0;
    }
    
    a {
        text-decoration: none;
    }

    a:link {
      color: #d0dbff;
    }

    /* visited link */
    a:visited {
        color: #3a89c5;
    }

    /* mouse over link */
    a:hover {
      color: #9fb5fa;;
    }

    header {
        color: white;
        text-align: center;
        font-family: 'Quantico', sans-serif;
        font-size: large;
    }
    
    table {
        border-top: none;
        border-collapse: collapse;
        margin: 0 0.5rem 0.5rem 0.5rem;
        width: 98%;
        border: 2px solid black;
    }

    td, th {
        padding: 0.4em;
        border-color: black;
        border-style: solid;
        border-width: 1px;
    }

    caption {
        padding: 7px;
        background-color: #6a6a6a7a;
	    border: solid 2px black;
	    border-bottom: none;
        font-family: Arial;
        font-size: 120%;
        font-weight: bold;
    }

    tr:hover {
        color: #333;
        background-color: white;
    }

    td:hover {
        color: #333;
        background-color: #cfdeff94;
    }

    th { //Table Headers
        padding: 2.5px; 
        background: #c8c8c8a8;
    }

    td {
        background: #ffffffc2;
        background-color: #ffffffeb;
    }

    .centered {
        text-align: center;
    }

    .field {
        font-family: Arial;
        color: #4C4C4C;
        font-weight: bold;
    }

    .focused {
        outline-color: aqua;
        outline-style: solid;
        outline-width: thin;
    }

    .editable {
        font-size: small;
        padding: 1px;
        max-width: 30ch;
        max-height: 4ch;
        overflow: auto;
        outline: none;
    }

    .indexwrapper {
        margin: auto;
        display: flex;
        width: 53%;
        background-color: rgb(214 213 255 / 31%);
        border-radius: 5px;
        backdrop-filter: blur(1px);
    }

    .tablewrapper {
        padding: 10px;
        border-radius: 5px;
        background-color: rgb(173 190 251 / 52%);
        margin: 1.5rem auto 0 auto;
        width: 49%;
        outline: none;
        display: table;
        box-shadow: 2px 6px 8px 0px #00000026;
        backdrop-filter: blur(1px);
    }

    .dropdownindex {
        font-family: Arial;
        color: #ffffffcc;
    }

    .dropdowntables {
        font-family: Arial;
        display: flex;
        justify-content: center;
        outline: none;
    }

    .indexsummary {
        font-family: Arial;
        font-weight: bold;
        padding: 10px;
    }

    .tablesummary {
        font-family: Arial;
        font-weight: bold;
        padding: 0px 0px 10px 0px;
        color: #ffffffcc;
    }

    button:hover {
        padding: 5px;
        border: none;
        border-radius: 3px;
        font-size: 16px;
        background-color: #dbe0ffe0;
        background-image: radial-gradient(#dbe0ffe0, #050f491c);
    }

    .button {
        box-shadow: 2px 3px #5450509e;
        padding: 5px;
        border: none;
        border-radius: 3px;
        font-size: 16px;
        background-color: #ffffffe0;
    }

    body::-webkit-scrollbar {
        width: 15px; 
    }

    body::-webkit-scrollbar-track {
        background: #f1f1f1cc;
    }

    body::-webkit-scrollbar-thumb {
        background-color: #757575;
        border-radius: 20px;
        border: 1px solid white;
    }

    .editable::-webkit-scrollbar {
        width: 5px; 
    }

    .editable::-webkit-scrollbar-track {
        background: #d9d9d9cc;
    }

    .editable::-webkit-scrollbar-thumb {
        background-color: #757575;
        border-radius: 20px;
        border: none;
    }    

</style>

</head>

<body><div id="font" class="flex flex-column pattern-dots-sm gray-darker br-16 py-l5">
    <header>
        <h1>[PROJECTNAME] - Data Dictionary</h1>
        
         <p>
            <em>[EDITION]</em>
        </p>
        
        <p align="center">
            <em>[DESCRIPTION]</em>
        </p>

        <p>
            <button id="save" class='button'>Salvar <i class="fa fa-save"></i></button>
        </p>
    </header>

    <div class='indexwrapper'>
        [INDEX]
    </div>
    <div>
        [MAIN]
    </div>
</div></body>

  <script type="text/javascript">
    $("#save").click(function() {
        var blob = new Blob([$("html").html()], {type: "text/html;charset=utf-8"});
        saveAs(blob, "DataDict.html");
    });
  </script>
</html>
"""


# PLUGIN
# ======

ModuleInfo = DefineModule(name="WB Datadict Dark Theme",
                          author="LIGJ",
                          version="1.4.0")


@ModuleInfo.plugin("wb.data_dict.dark",
                   caption="Gerar Dicionário de Dados (Dark)",
                   input=[wbinputs.currentCatalog()],
                   pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)

def create_datadict(catalog):
    # Get default schema
    schema = catalog.defaultSchema

    # Get table objects and sort them alphabetically
    tables = sorted(schema.tables, key=lambda table: table.name)

    # Fill HTML template
    markup = HTML_TEMPLATE
    markup = markup.replace("[PROJECTNAME]", schema.name)
    markup = markup.replace("[DESCRIPTION]", escape(schema.comment))
    markup = markup.replace("[EDITION]", str(datetime.date.today()))
    markup = markup.replace("[INDEX]", html_index(tables))
    markup = markup.replace("[MAIN]", html_main(tables))

    # Write the HTML file to disk (GUI Dialog)
    doc_path = os.path.dirname(grt.root.wb.docPath)
    dialog = gui.FileChooser(gui.SaveFile)
    dialog.set_title("Salve em um arquivo .html")
    dialog.set_directory(doc_path)
    response = dialog.run_modal()
    file_path = dialog.get_path()

    if response:
        save(markup, file_path)

    return 0


# HELPER FUNCTIONS
# ================

def column_as_html(column, table):
    """Return column as an HTML row."""
    markup = "<tr>"
    markup += "<td class='field'>{0}</td>".format(column.name)
    markup += "<td>{0}</td>".format(column.formattedType)

    # Check for Primary Key
    if table.isPrimaryKeyColumn(column):
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Foreign Key
    if table.isForeignKeyColumn(column):
        markup += "<td class='centered'><a>&#10004;</a></td>".format(
            column.name.replace("_id", ""))
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Not Null attribute
    if column.isNotNull == 1:
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Check for Auto Increment attribute
    if column.autoIncrement == 1:
        markup += "<td class='centered'>&#10004;</td>"
    else:
        markup += "<td class='centered'>&nbsp;</td>"

    # Comment
    markup += "<td><div class='editable' contenteditable>{0}</div></td>".format(escape(column.comment))
    markup += "</tr>"

    return markup


def escape(text):
    """Return text as an HTML-safe sequence."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")
    return text


def html_index(tables):
    """Return index of tables as HTML nav."""
    markup = "<nav>"
    markup += "<details class='dropdownindex'>"
    markup += "<summary class='indexsummary'>Índice</summary>"
    markup += "<ul>"
    for table in tables:
        markup += "<li><a href='#{0}'>{0}</a></li>".format(table.name)
    markup += "</ul></details></nav>"

    return markup


def html_main(tables):
    """Return the main content of the HTML document."""
    markup = "<div>"

    for table in tables:
        markup += table_as_html(table)

    markup += "</div>"

    return markup


def html_table_header():
    """Return the HTML row with header cells used in all tables."""
    markup = ("<tr>" +
              "<th>Coluna</th>" +
              "<th>DataType</th>" +
              "<th>Primary Key</th>" +
              "<th>Foreign Key</th>" +
              "<th>Not Null</th>" +
              "<th>Auto Increment</th>" +
              "<th>Descrição</th>" +
              "</tr>")
    return markup


def save(html, path):
    """Save HTML to the given file system path."""
    try:
        html_file = open(path, "w")
    except IOError:
        text = "Erro ao abrir {0}.".format(path)
        gui.Utilities.show_error("Erro ao salvar arquivo.", text, "Ok", "", "")
    else:
        html_file.write(html)
        html_file.close()

        # Display success dialog
        text = "O Dicionário de Dados foi gerado com sucesso!"
        gui.Utilities.show_message("DataDict", text, "Ok", "", "")

        # Open HTML file in the Web browser
        try:
            webbrowser.open_new(path)
        except webbrowser.Error:
            print("Aviso: Não foi possivel iniciar o navegador " +
                  "para exibir o Dicionário de Dados.")
            print(path)


def table_as_html(table):
    """Return table as an HTML table."""
    markup = "<div class='tablewrapper'><details open class='dropdowntables' id='{0}'><table id='{0}'>".format(table.name)
    markup += "<summary class='tablesummary'>{0}</summary>".format(table.name)
    markup += "<caption>{0}</caption>".format(table.name)
    markup += html_table_header()

    # Format column objects in HTML
    for column in table.columns:
        markup += column_as_html(column, table)

    markup += "</table></details></div>"

    return markup
