import azure.functions as functions
import random
import string

application = functions.FunctionApp()
@application.function_name(name = "createDog")
@application.route(route = "createDog", auth_level = functions.AuthLevel.ANONYMOUS)
@application.cosmos_db_output(arg_name = "documentForDog", database_name = "waqqly_web_app_database", container_name = "waqqly_web_app_container", connection = "CosmosDbConnectionSetting")
def create_dog(req: functions.HttpRequest, documentForDog: functions.Out[functions.Document]) -> functions.HttpResponse:
    id_for_dog = ''.join(random.sample(string.ascii_letters+string.digits, 10))
    dog_name = req.params.get('dogname')
    dog_breed = req.params.get('dogbreed')
    owners_name = req.params.get('ownersname')
    owners_address = req.params.get('ownersaddress')
    if dog_name and dog_breed and owners_name and owners_address:
        documentForDog.set(functions.Document.from_dict({"id": id_for_dog, "dog_name": dog_name, "dog_breed": dog_breed, "owners_name": owners_name, "owners_address": owners_address}))
        return functions.HttpResponse(status_code = 204)
    else: 
        return functions.HttpResponse(status_code = 400)
    





@application.function_name(name = "createWalker")
@application.route(route = "createWalker", auth_level = functions.AuthLevel.ANONYMOUS)
@application.cosmos_db_output(arg_name = "documentForWalker", database_name = "waqqly_web_app_database", container_name = "waqqly_web_app_container", connection = "CosmosDbConnectionSetting")
def create_walker(req: functions.HttpRequest, documentForWalker: functions.Out[functions.Document]) -> functions.HttpResponse:
    id_for_walker = ''.join(random.sample(string.ascii_letters+string.digits, 10))
    walkers_name = req.params.get('walkersname')
    walkers_location = req.params.get('walkerslocation')
    walkers_phone_number = req.params.get('walkersphonenumber')
    if walkers_name and walkers_location and walkers_phone_number:
        documentForWalker.set(functions.Document.from_dict({"id": id_for_walker, "walkers_name": walkers_name, "walkers_location": walkers_location, "walkers_phone_number": walkers_phone_number}))
        return functions.HttpResponse(status_code = 204)
    else: 
        return functions.HttpResponse(status_code = 400)


    

