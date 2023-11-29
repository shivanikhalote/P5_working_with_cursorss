# three types of cursors
# 1 SearchCursor - reading the attribute data
# 2 UpdateCursor - updating the attribute data
# 3 InsertCursor - creating new row in the attribute data

import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Cursors\ProProject_Cursors\ProProject_Cursors.gdb"

fc_name = "MajorAttractions"
fc_path = os.path.join(gdp_path,fc_name)

field_list = ["ESTAB","NAME","ZIP",]

# using search cursors - gives only read only access
#s_cursors = arcpy.da.SearchCursor(fc_path,field_list)

#for row in s_cursors:
    # since "NAME" at zero position in list
    #print("{}, {}, {}".format(row[0], row[1], row[2]))

#del s_cursors

with arcpy.da.SearchCursor(fc_path,field_list,"ESTAB > 2000") as s_cursor:
    for row in s_cursor:
        print("Name:{}, Estabishment:{}".format(row[1], row[0]))
        #if row[0]>2000:




