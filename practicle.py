import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdp_path,restaurant_fc_name)
crime_fc_path = os.path.join(gdp_path,crime_fc_name)

arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_lyr")
arcpy.management.MakeFeatureLayer(crime_fc_path,"crime_lyr")

# getting count of all the features before selection
pre_count1=arcpy.GetCount_management("restaurant_lyr")
pre_count3=arcpy.GetCount_management("crime_lyr")

arcpy.management.SelectLayerByLocation("crime_lyr","WITHIN_A_DISTANCE","restaurant_lyr","500 meters")
post_count3 =arcpy.GetCount_management("crime_lyr")
print('crime near 500 meters of restaurant = {}'.format(post_count3))






