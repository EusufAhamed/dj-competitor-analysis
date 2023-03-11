from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.client import RestClient

# local finder
@api_view(['POST'])
def post_local_finder(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    
    post_data = dict()
    post_data[len(post_data)] = dict(
        language_code = request.data.get('language_code'),
        location_coordinate = request.data.get('location_coordinate'),
        keyword = request.data.get('keyword'),
        min_rating = request.data.get('min_rating'),
        time_filter = request.data.get('time_filter')
    )

    # print(post_data)

    responses = client.post("/v3/serp/google/local_finder/task_post", post_data)

    if responses["status_code"] == 20000:
        return Response(responses, status=status.HTTP_200_OK)
        # return Response(data=response, status=status.HTTP_201_CREATED)
    else:
        print("error. Code: %d Message: %s" % (responses["status_code"], responses["status_message"]))
    
    # return Response(data='hello', status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_local_finder(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    
    post_data = dict()
    post_data[len(post_data)] = dict(
        language_code = "en",
        location_coordinate = "-37.7155669,144,10z",
        keyword = "Physiotherapists",
        min_rating = 4.5,
        time_filter = "monday"
    )

    response = client.post("/v3/serp/google/local_finder/task_post", post_data)

    if response["status_code"] == 20000:
        print("Hello")
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
    
    
    data = client.get("/v3/serp/google/local_finder/tasks_ready")

    if data["status_code"] == 20000:
        results = []
        for task in data['tasks']:
            if (task['result'] and (len(task['result']) > 0)):
                for resultTaskInfo in task['result']:
                    if(resultTaskInfo['endpoint_advanced']):
                        results.append(client.get(resultTaskInfo['endpoint_advanced']))
                        
        # final_data = data["tasks"][0]["result"][0]["endpoint_advanced"]
        # items = results[0]['tasks'][0]['result'][0]['items']
        
        return Response(data=results, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))


# my business info
@api_view(['POST'])
def post_business_info(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    post_data = dict()

    post_data[len(post_data)] = dict(
        location_name = request.data.get('location_name'),
        language_code = request.data.get('language_code'),
        keyword = request.data.get('keyword'),
    )

    response = client.post("/v3/business_data/google/my_business_info/task_post", post_data)

    if response["status_code"] == 20000:
        return Response(response, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))


@api_view(['GET'])
def get_business_info(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    post_data = dict()

    post_data[len(post_data)] = dict(
        location_name = "New York,New York,United States",
        language_code = "en",
        keyword = "RustyBrick, Inc."
    )

    response = client.post("/v3/business_data/google/my_business_info/task_post", post_data)

    if response["status_code"] == 20000:
        print(response)
        # pass
        # return Response(response, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

    data = client.get("/v3/business_data/google/my_business_info/tasks_ready")

    if data['status_code'] == 20000:
        results = []
        for task in data['tasks']:
            if (task['result'] and (len(task['result']) > 0)):
                for resultTaskInfo in task['result']:
                    if(resultTaskInfo['endpoint']):
                        results.append(client.get(resultTaskInfo['endpoint']))
                    
        return Response(data=results, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))


# reviews
@api_view(['POST'])
def post_reviews(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    post_data = dict()

    post_data[len(post_data)] = dict(
        location_name = request.data.get('location_name'),
        language_code = request.data.get('language_code'),
        keyword = request.data.get('keyword'),
        depth = request.data.get('depth'),
    )

    response = client.post("/v3/business_data/google/my_business_info/task_post", post_data)

    if response["status_code"] == 20000:
        return Response(response, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))


@api_view(['GET'])
def get_reviews(request: Request) -> Response:
    client = RestClient('shuvodewan.sky@gmail.com', '1fb82e99bedf0ed3')
    post_data = dict()

    post_data[len(post_data)] = dict(
        location_name = "London,England,United Kingdom",
        language_code = "en",
        keyword = "hedonism wines",
        depth =  50
    )

    response = client.post("/v3/business_data/google/reviews/task_post", post_data)

    if response["status_code"] == 20000:
        pass
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

    data = client.get("/v3/business_data/google/reviews/tasks_ready")

    if data['status_code'] == 20000:
        results = []
        for task in data['tasks']:
            if (task['result'] and (len(task['result']) > 0)):
                for resultTaskInfo in task['result']:
                    if(resultTaskInfo['endpoint']):
                        results.append(client.get(resultTaskInfo['endpoint']))
                    
        return Response(data=results, status=status.HTTP_200_OK)
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))



