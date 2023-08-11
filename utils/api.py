from utils.http_methods import Http_methods
# Методи для тестування Google maps api

base_url="https://rahulshettyacademy.com"  #базова url
key ="?key=qaclick123"   #Параметр для всех запросов

class Google_maps_api():
    # метод для створення нової локації
    @staticmethod
    def create_new_place():

        json_for_create_new_place= {
            "location":{
                "lat":-38.383494,
                "lng":33.427362
            },"accuracy":50,
            "name":"Frontlinehouse",
            "phone_number":"(+91)9838933937",
            "address":"29,sidelayout,cohen09",
            "types":[
                "shoepark",
                "shop"
            ],
            "website":"http://google.com",
            "language":"French-IN"

        }
        post_resours = "/maps/api/place/add/json" # ресурс мктода post
        post_url = base_url + post_resours + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post







    # метод для провірки нової локації
    @staticmethod
    def get_new_place(place_id):    

        get_resourse="/maps/api/place/get/json" # ресурс мeтода get
        get_url = base_url+ get_resourse + key +"&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get
        

    # метод для зміни нової локації
    @staticmethod
    def put_new_place(place_id):    

        put_resourse="/maps/api/place/update/json" # ресурс мeтода put
        put_url = base_url+put_resourse+key
        print(put_url)
        json_for_update_new_location= {
            "place_id":place_id,
            "address":"100 Lenina street, RU",
            "key":"qaclick123"

        }
        result_put = Http_methods.put(put_url,json_for_update_new_location)
        return result_put
    
        # метод для видалення нової локації
    @staticmethod
    def delete_new_place(place_id):    

        delete_resourse="/maps/api/place/delete/json" 
        delete_url = base_url+delete_resourse+key
        print(delete_url)
        json_for_delete_new_location= {
            "place_id":place_id

        }
        result_delete = Http_methods.delete(delete_url,json_for_delete_new_location)
        return result_delete