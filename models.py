from google.appengine.ext import db
import rest
#Domain models go here

#EXAMPLES:
#class Restaurant(db.Model):
#    name = db.StringProperty()
#    image_background = db.ReferenceProperty(RestaurantImage)
#    num_employees = db.IntegerProperty()
#    is_open = db.BooleanProperty();

#Expose domain models as REST here

#EXAMPLES:

#Add all models from the current module, and/or...
#rest.Dispatcher.add_models_from_module(__name__)

#Add all models from some other module, and/or...
#rest.Dispatcher.add_models_from_module(my_model_module)
# add specific models
#rest.Dispatcher.add_models({
#        "foo": FooModel,
#        "bar": BarModel})

#Add specific models (with given names) and restrict the supported methods
#rest.Dispatcher.add_models({
#      'foo' : (FooModel, rest.READ_ONLY_MODEL_METHODS),
#      'bar' : (BarModel, ['GET_METADATA', 'GET', 'POST', 'PUT'],
#      'cache' : (CacheModel, ['GET', 'DELETE'] })
