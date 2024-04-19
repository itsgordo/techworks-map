import json


# RUN THIS FILE TO UPDATE COUNTIES'S PROPERTIES (WEBSITE, ADDRESS, PHONE, ETC.) TO COUNTIES.JSON FROM COUNTIES_ORIGINAL.JSON

# Read the JSON file
with open('counties_original.json', 'r') as file:
    data = json.load(file)

# Function to add properties for a specific location
def add_properties(location_name, new_properties):
    for feature in data['features']:
        if 'properties' in feature and 'name' in feature['properties'] and feature['properties']['name'] == location_name:
            if 'properties' not in feature:
                feature['properties'] = {}
            feature['properties'].update(new_properties)

# Call the function to add properties for each counties
'''
add_properties("", 
               {"active": True,
                "website": "", 
                "address": "", 
                "phone": "",
                "image": ""})
'''
add_properties("Broome", 
               {"active": True,
                "website": "https://www.broomehistory.org/", 
                "address": "185 Court Street, Binghamton, NY 13901", 
                "phone": "(607) 778-3572",
                "image": "https://wicz.images.worldnow.com/images/20274342_G.jpeg?auto=webp&disable=upscale&height=560&fit=bounds&lastEditedDate=1611186652000"})

add_properties("Chemung", 
               {"active": True,
                "website": "https://chemungvalleymuseum.org/", 
                "address": "415 E. Water Street, Elmira, NY 14901", 
                "phone": "(607) 734-4167",
                "image": "https://upload.wikimedia.org/wikipedia/commons/5/53/Exterior_of_the_Chemung_County_Historical_Society_-_2014.jpg"})

add_properties("Cayuga", 
               {"active": True,
                "website": "http://www.colhs.org/", 
                "address": "14 W Cayuga St, Moravia, NY 13118", 
                "phone": "(315) 497-3906",
                "image": "http://4.bp.blogspot.com/_qTiQYZhnBQc/TUBIrya62PI/AAAAAAAAACU/qFZ3qc6BOLY/s190/IMG_7609S.JPG"})
add_properties("Chenango", 
               {"active": True,
                "website": "https://chenangohistorical.org/", 
                "address": "45 Rexford St, Norwich, NY 13815", 
                "phone": "(607) 334-9227",
                "image": "https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/crm/newyorkstate/CCHS-Day_5B969B3B-9162-9604-9385790B02EE1FE7-5b9699ca9d5f5fa_5b969bbc-dfb7-7834-471b7219211f651e.jpg"})
add_properties("Cortland", 
               {"active": True,
                "website": "https://cortlandhistory.org/", 
                "address": "25 Homer Ave, Cortland, NY 13045", 
                "phone": "(607) 756-6071",
                "image": "https://img.geocaching.com/waymarking/display/fcfc3902-b257-4150-8d01-8658aaba96d4.jpg"})
add_properties("Delaware", 
               {"active": True,
                "website": "https://www.dcha-ny.org/", 
                "address": "46549 State Hwy 10, Delhi, NY 13753 ", 
                "phone": "(607) 746-3849",
                "image": "https://www.dcha-ny.org/dcha3.jpg"})
add_properties("Livingston", 
               {"active": True,
                "website": "https://www.livingstoncountyhistoricalsociety.com/", 
                "address": "30 Center Street, Geneseo, NY 14454", 
                "phone": "(585) 243-9147",
                "image": "https://images.squarespace-cdn.com/content/v1/52dd58cbe4b0f48cdba72311/1394299449445-T0MBRRQ4K3NDJPRVYT1R/Museum-current.jpg?format=1000w"})
add_properties("Madison", 
               {"active": True,
                "website": "https://mchs1900.org/", 
                "address": "435 Main Street, Oneida, NY 13421", 
                "phone": "(315) 363-4136",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSilPme2VJRGg28wwsGvx6OC-OfJmnLERtQW2WFovQ6aA&s"})
add_properties("Onondaga", 
               {"active": True,
                "website": "https://www.cnyhistory.org/", 
                "address": "321 Montgomery Street, Syracuse, NY 13202 ", 
                "phone": "(315) 428-1864",
                "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/7e/06/ec/onondaga-historical-associatio.jpg?w=1200&h=1200&s=1"})
add_properties("Ontario", 
               {"active": True,
                "website": "https://www.ochs.org/", 
                "address": "55 N. Main Street, Canandaigua, NY 14424", 
                "phone": "(585) 394-4975",
                "image": "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_692,q_75,w_970/v1/crm/fingerlakesny/Ontario-County-Historical-Museum-Canandaigua-exterior0_d5fcb484-5056-a36a-09fc9590a9ff90a4.jpg"})
add_properties("Otsego", 
               {"active": True,
                "website": "https://mohawkvalleymuseums.us/museums/otsego-county-historical-association/", 
                "address": "3140 CR-11, Hartwick, NY 13348", 
                "phone": "(607) 547-8070",
                "image": "https://mohawkvalleymuseums.us/wp-content/uploads/2022/04/Otsego-County-Historical-Association-Hartwick-NY.jpg"})
add_properties("Schuyler", 
               {"active": True,
                "website": "https://schuylerhistory.org/", 
                "address": "108 N. Catharine St. / Route 14, Montour Falls, NY 14865", 
                "phone": "(607) 535-9741",
                "image": "https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/crm/newyorkstate/IMG_3847_C73B52EC-2A8C-4006-AF765EADF4A4EB01_b87272cd-f783-422f-9b1b30099096bee3.jpg"})
add_properties("Seneca", 
               {"active": True,
                "website": "https://westsenecahistory.com/wp/", 
                "address": "919 Mill Road, West Seneca, NY 14224", 
                "phone": "(716) 674-4283",
                "image": "https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,q_75,w_1200/v1/crm/senecacountyny/sfhs-2_E3E223B2-5056-B365-AB365D15341DFBEF-e3e222b95056b36_e3e22405-5056-b365-ab14a18c8d4cc839.jpg"})
add_properties("Steuben", 
               {"active": True,
                "website": "https://steubenhistoricalsociety.org/", 
                "address": "1 Cohocton St, Bath, NY 14810", 
                "phone": "(607) 776-9930",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9MuxMUpnK3c06f4Fp7bi5pWqhLlyqKGqFiyCi8r2J6Q&s"})
add_properties("Tioga", 
               {"active": True,
                "website": "https://tiogahistory.org/", 
                "address": "110 Front Street, Owego, NY 13827", 
                "phone": "(607) 687-2460",
                "image": "https://tiogahistory.org/wp-content/uploads/2015/04/Museum-Stairs-1024x878.jpg?x72180"})
add_properties("Tompkins", 
               {"active": True,
                "website": "https://thehistorycenter.net/", 
                "address": "110 North Tioga Street, Ithaca, NY, 14850", 
                "phone": "(607) 273-8284",
                "image": "https://lh4.googleusercontent.com/proxy/QeGXgeDuGVBB9PCuz-JNTBP7LzmoLaBrIfd3TcbI_VMHX5edDYNDyKG6bBwoColxrRZNShiBxjNhfXEOEVw4N-DfF2dC4tv8PV5w9e2b7IeCnacxIA"})
add_properties("Yates", 
               {"active": True,
                "website": "http://www.yatespast.org/", 
                "address": "107 Chapel Street, Penn Yan, NY 14527", 
                "phone": "(315) 536-7318",
                "image": "https://lh5.googleusercontent.com/proxy/kvorupuGndhRoXztBBjWapfkXh7s6geI7ED9BZl_-JCo8mbs7EuA86OIlNK0i58FcDplXk8CvuOVhcPO"})

# Write the modified data back to the JSON file
with open('counties.json', 'w') as file:
    json.dump(data, file, indent=2)
