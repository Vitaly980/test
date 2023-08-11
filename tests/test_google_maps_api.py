import json
from requests import Response
from utils.api import Google_maps_api
from utils.cheking import Cheking

# Створення, змінення, видалення нової локації

class Test_create_place():


    def test_create_new_place(self):
        

        print("\nMethod post")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')
        print(result_post)
        

        print("\nMethod GET POST")
        result_get: Response= Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'accuracy', '50')
        print(result_get)

        print("\nMethod PUT")
        result_put: Response= Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put,['msg'])
        Cheking.check_json_value(result_put,'msg', 'Address successfully updated')



        print("\nMethod GET PUT")
        result_get: Response= Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'accuracy', '50')
        print(result_get)

        print("\nMethod DELETE")
        result_delete: Response= Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete,['status'])
        Cheking.check_json_value(result_delete,'status','OK')
        print(result_delete)



        print("\nMethod GET DELETE")
        result_get: Response= Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get,['msg'])
        # token = json.loads(result_get.text) Перевірка які токени мають бути наявні в  методі!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # print(list(token))
        print(result_get)
        # Cheking.check_json_value(result_put,'msg', "Get operation failed, looks like place_id  doesn't exists")
        Cheking.check_json_search_word_in_value(result_get,'msg','failed')
        print("\nТестування завершилоcь успішно")