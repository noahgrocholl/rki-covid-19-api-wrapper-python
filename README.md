# rki-covid-19-api-wrapper-python
Wrapps up german corona virus data via python. Software uses data from Robert Koch Institut in Berlin.

###############################
# RKI Wrapper by noahgrocholl #
###############################


NOTE: The rki_corona_api.py file and the "content" folder have to be in
the same directory.


I used the official RKI api to make the wrapper.

To use it just import the .py file to your project and create a Rki object
and safe it in a variable:

api = Rki(0)

The number in the brackets represent you LK_ID, an id wich is connected to 
your Landkreis, your Bundesland or the whole Bundesrepublik.
To find out wich id your area has, lockup what the spreadsheet (csv)in 
content/Liste LKs.csv says.

If you dont know the id, but the exact(!) name of you area as in the csv
you can use like:

api.change_target_id_by_name_csv("Berlin")


To finally get the data you want use:

print(api.get_target_results("type of data you want"))


Possible types of data are: 
"AdmUnitId" 
"BundeslandId" 
"AnzFall" 
"AnzTodesfall" 
"AnzFallNeu" 
"AnzTodesfallNeu" 
"AnzFall7T" 
"AnzGenesen" 
"AnzGenesenNeu" 
"AnzAktiv" 
"AnzAktivNeu" 
"Inz7T" 
"ObjectId"

Data you can get:
lk_id -> api.lk_id
lk_name -> api.lk_name
results -> api.list_results
