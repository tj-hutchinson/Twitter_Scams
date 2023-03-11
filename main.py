import readline
# import datetime
from urlextract import URLExtract
import urlexpander
import requests
from requests.exceptions import HTTPError
import urllib
from urllib.parse import urlparse
import csv
import urlexpander
import numpy as np
import datetime


class List_Info:
    def __init__(self, url, list_id, name, description, owner_id, created_at, follower_count, status_code, content_type,
                 date_time, strict_transport_security, age, content_security_policy, x_content_type_options,
                 request_history, error, error_code):
        self.url = url
        self.list_id = list_id
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.created_at = created_at
        self.follower_count = follower_count
        self.status_code = status_code
        self.content_type = content_type
        self.date_time = date_time
        self.strict_transport_security = strict_transport_security
        self.age = age
        self.content_security_policy = content_security_policy
        self.x_content_type_options = x_content_type_options
        self.request_history = request_history
        self.error = error
        self.error_code = error_code


# def request_url(url):
#     request = requests.get(url)
#     # request_code = str(request.status_code)
#     if request.status_code == requests.codes.ok:
#         # print(request.headers['content-type'])
#         request_code = request.headers['content-type']
#     # request_code = request.text
#     return request_code


extractor = URLExtract()

list_info = []
known_urls = []
expanded_known_urls = []
req_codes = []
good_links = []
bad_links = []

status_code = ""
content_type = ""
date_time = ""
strict_transport_security = ""
age = ""
content_security_policy = ""
x_content_type_options = ""
request_history = ""
error = ""
error_code = ""

f = 'all_lists.txt'
filename = 'twitter_list_info.csv'

with open(f) as file:
    while line := file.readline().rstrip():
        items = line.split("\t")
        list_id = items[0]
        name = items[1]
        description = items[2]
        owner_id = items[3]
        created_at = items[4]
        follower_count = items[5]
        if description != "":
            if extractor.find_urls(description):
                urls = extractor.find_urls(description)
                if len(urls) == 1:
                    u = urlparse(urls[0])
                    if u.scheme == 'https':
                        url = u._replace(fragment="").geturl()
                    elif u.scheme == 'http':
                        url = u._replace(fragment="").geturl()
                    else:
                        add_scheme = "https://" + urls[0]
                        u = urlparse(add_scheme)
                        u = u._replace(fragment="")._replace(scheme='https')
                        url = u.geturl()
                elif len(urls) > 1:
                    for i in urls:
                        u = urlparse(i)
                        if u.scheme == 'https':
                            url = u._replace(fragment="").geturl()

                        elif u.scheme == 'http':
                            url = u._replace(fragment="").geturl()

                        else:
                            add_scheme = "https://" + i
                            u = urlparse(add_scheme)
                            u = u._replace(fragment="")._replace(scheme='https')
                            url = u.geturl()

                # print(url)
                # try:
                #     request = requests.get(url)
                #     print(request)
                #     print(request.headers['date'])
                # except HTTPError as http_err:
                #     print(f'Other error occurred: {err}')  # Python 3.6
                # except Exception as err:
                #     print(f'Other error occurred: {err}')  # Python 3.6

                try:
                    # url = urlexpander.expand(url)
                    request = requests.get(url)
                    print("Normal")
                    if request.status_code == requests.codes.ok:

                        response_header = request.headers
                        status_code = str(request.status_code)
                        content_type = request.headers['content-type']
                        try:
                            date_time = request.headers['date']
                        except:
                            date_time = datetime.datetime.now()
                        try:
                            strict_transport_security = request.headers['strict-transport-security']
                        except:
                            strict_transport_security = ""
                        try:
                            age = request.headers['age']
                        except:
                            age = ""
                        try:
                            content_security_policy = request.headers['content-security-policy']
                        except:
                            content_security_policy = ""
                        try:
                            x_content_type_options = request.headers['x-content-type-options']
                        except:
                            x_content_type_options = ""
                        try:
                            request_history = str(request.history)
                        except:
                            request_history = ""
                        error = "No"
                        error_code = ""

                        print(url)
                        print(request.headers)
                        print(request.status_code)
                        print(request.headers['content-type'])
                        print(date_time)
                        print(request.headers['strict-transport-security'])
                        print(request.headers['age'])
                        print(request.headers['content-security-policy'])
                        print(request.headers['x-content-type-options'])
                        print(request.history)
                        request_code = request.headers['content-type']

                    # If the response was successful, no Exception will be raised
                    request.raise_for_status()

                except HTTPError as http_err:
                    response_header = request.headers
                    status_code = str(request.status_code)
                    content_type = request.headers['content-type']
                    try:
                        date_time = request.headers['date']
                    except:
                        date_time = datetime.datetime.now()
                    try:
                        strict_transport_security = request.headers['strict-transport-security']
                    except:
                        strict_transport_security = ""
                    try:
                        age = request.headers['age']
                    except:
                        age = ""
                    try:
                        content_security_policy = request.headers['content-security-policy']
                    except:
                        content_security_policy = ""
                    try:
                        x_content_type_options = request.headers['x-content-type-options']
                    except:
                        x_content_type_options = ""
                    try:
                        request_history = str(request.history)
                    except:
                        request_history = ""
                    print("ERROR WITH THIS LINK: " + url)
                    print(f'HTTP error occurred: {http_err}')  # Python 3.6
                    error = "Yes"
                    error_code = http_err

                except Exception as err:
                    response_header = request.headers
                    status_code = str(request.status_code)
                    content_type = request.headers['content-type']
                    try:
                        date_time = request.headers['date']
                    except:
                        date_time = datetime.datetime.now()
                    try:
                        strict_transport_security = request.headers['strict-transport-security']
                    except:
                        strict_transport_security = ""
                    try:
                        age = request.headers['age']
                    except:
                        age = ""
                    try:
                        content_security_policy = request.headers['content-security-policy']
                    except:
                        content_security_policy = ""
                    try:
                        x_content_type_options = request.headers['x-content-type-options']
                    except:
                        x_content_type_options = ""
                    try:
                        request_history = str(request.history)
                    except:
                        request_history = ""
                    print(f'Other error occurred: {err}')  # Python 3.6
                    error = "Yes"
                    error_code = err

                else:
                    print('Success!')

                print(url)
                print(list_id)
                print(name)
                print(description)
                print(owner_id)
                print(created_at)
                print(follower_count)
                print(response_header)
                print(status_code)
                print(content_type)
                print(date_time)
                print(strict_transport_security)
                print(age)
                print(content_security_policy)
                print(x_content_type_options)
                print(request_history)
                print(error)
                print(error_code)


                list_info.append(List_Info(url, list_id, name, description, owner_id, created_at, follower_count,
                                           status_code, content_type, date_time, strict_transport_security, age,
                                           content_security_policy, x_content_type_options, request_history, error,
                                           error_code))


try:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "LIST ID", "LIST NAME", "LIST DESCRIPTION", "OWNER ID", "CREATION DATE",
                         "FOLLOWER COUNT", "STATUS CODE", "CONTENT TYPE", "DATE/TIME OF REQUEST",
                         "STRICT TRANSPORT SECURITY", "AGE", "CONTENT SECURITY POLICY", "X CONTENT TYPE OPTIONS",
                         "REQUEST HISTORY", "ERROR", "ERROR CODE"])
        for twitter_list in list_info:
            writer.writerow([twitter_list.url, twitter_list.list_id, twitter_list.name, twitter_list.description,
                             twitter_list.owner_id, twitter_list.created_at, twitter_list.follower_count,
                             twitter_list.status_code, twitter_list.content_type, twitter_list.date_time,
                             twitter_list.strict_transport_security, twitter_list.age,
                             twitter_list.content_security_policy, twitter_list.x_content_type_options,
                             twitter_list.request_history, twitter_list.error, twitter_list.error_code])
except BaseException as e:
    print('BaseException:', filename)
else:
    print('Data has been loaded successfully !')

# print(len(list_info))
# # print(list(list_info))
#
# for twitter_list in list_info:
#     print("URL:", twitter_list.url, "List ID:", twitter_list.list_id, "NAME:",
#           twitter_list.name, "DESCRIPTION: ", twitter_list.description,
#           "OWNER ID:", twitter_list.owner_id, "CREATED AT:", twitter_list.created_at,
#           "FOLLOWER COUNT:", twitter_list.follower_count, "STATUS CODE:", twitter_list.status_code, "CONTENT TYPE:",
#           twitter_list.content_type, "DATE/TIME:", twitter_list.date_time,
#           "STRICT TRANSPORT SECURITY:", twitter_list.strict_transport_security, "AGE:", twitter_list.age,
#           "CONTENT SECURITY POLICY:", twitter_list.content_security_policy,
#           "X CONTENT TYPE OPTIONS:", twitter_list.x_content_type_options,
#           "REQUEST HISTORY:", twitter_list.request_history, "ERROR:", twitter_list.error,
#           "ERROR CODE:", twitter_list.error_code,
#           "\n", "-------------------------------------------", "\n")
