# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:39:56 2018

@author: Rishabh Batra
"""

cur.execute("CREATE TABLE dashboard_sn05 (id , Time, Temperature, Eac_Today, Vpv, Ipv, Ppv, Vac, Iac, Pac, Fac, Eac_Total);") # use your column names here

for row in DictReader(open('./5_final.csv')):
            sn05 = SN05()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn05.Time = row['Time']
            sn05.Temperature = int(row['Temperature'])
            sn05.Eac_Today = float(row['Eac_Today'])
            sn05.Vpv = float(row['Vpv'])
            sn05.Ipv = float(row['Ipv'])
            sn05.Ppv = float(row['Ppv'])
            sn05.Vac = float(row['Vac'])
            sn05.Iac = float(row['Iac'])
            sn05.Pac = float(row['Pac'])
            sn05.Fac = float(row['Fac'])
            sn05.Eac_Total = float(row['Eac_Total'])
            sn05.save()
            if row%10000 == 0:
                print(row)
            
        print("%s Data Parsed"%(sn05))
        print("10% of Job completed")
        
        if SN7B.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN7B CSV data")
        for row in DictReader(open('./7b_final.csv')):
            sn7 = SN7B()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn7.Time = row['Time']
            sn7.Temperature = int(row['Temperature'])
            sn7.Eac_Today = float(row['Eac_Today'])
            sn7.Vpv = float(row['Vpv'])
            sn7.Ipv = float(row['Ipv'])
            sn7.Ppv = float(row['Ppv'])
            sn7.Vac = float(row['Vac'])
            sn7.Iac = float(row['Iac'])
            sn7.Pac = float(row['Pac'])
            sn7.Fac = float(row['Fac'])
            sn7.Eac_Total = float(row['Eac_Total'])
            sn7.save()
            if row%10000 == 0:
                print(row)
        
        print("%s Data Parsed"%(sn7))
        print("20% Job complete")
        
        if SN13.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN13 data")
        for row in DictReader(open('./13_final.csv')):
            sn13 = SN13()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn.Time = row['Time']
            sn13.Temperature = int(row['Temperature'])
            sn13.Eac_Today = float(row['Eac_Today'])
            sn13.Vpv = float(row['Vpv'])
            sn13.Ipv = float(row['Ipv'])
            sn13.Ppv = float(row['Ppv'])
            sn13.Vac = float(row['Vac'])
            sn13.Iac = float(row['Iac'])
            sn13.Pac = float(row['Pac'])
            sn13.Fac = float(row['Fac'])
            sn13.Eac_Total = float(row['Eac_Total'])
            sn13.save()
            if row%10000 == 0:
                print(row)
                
        print("%s data parsed"%(sn13))
        
        if SN15.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN15 CSV data")
        for row in DictReader(open('./15_final.csv')):
            sn15 = SN15()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn15.Time = row['Time']
            sn15.Temperature = int(row['Temperature'])
            sn15.Eac_Today = float(row['Eac_Today'])
            sn15.Vpv = float(row['Vpv'])
            sn15.Ipv = float(row['Ipv'])
            sn15.Ppv = float(row['Ppv'])
            sn15.Vac = float(row['Vac'])
            sn15.Iac = float(row['Iac'])
            sn15.Pac = float(row['Pac'])
            sn15.Fac = float(row['Fac'])
            sn15.Eac_Total = float(row['Eac_Total'])
            sn15.save()
            if row%10000 == 0:
                print(row)
            if row == 400000:
                print("30% Job complete")
        print("%s Data Parsed"%(sn))
        
        if SN28.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN28 CSV data")
        for row in DictReader(open('./28_final.csv')):
            sn28 = SN28()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn28.Time = row['Time']
            sn28.Temperature = int(row['Temperature'])
            sn28.Eac_Today = float(row['Eac_Today'])
            sn28.Vpv = float(row['Vpv'])
            sn28.Ipv = float(row['Ipv'])
            sn28.Ppv = float(row['Ppv'])
            sn28.Vac = float(row['Vac'])
            sn28.Iac = float(row['Iac'])
            sn28.Pac = float(row['Pac'])
            sn28.Fac = float(row['Fac'])
            sn28.Eac_Total = float(row['Eac_Total'])
            sn28.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn28))
        print("40% Job complete")
        
        if SN33.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN33 CSV data")
        for row in DictReader(open('./33_final.csv')):
            sn33 = SN33()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn33.Time = row['Time']
            sn33.Temperature = int(row['Temperature'])
            sn33.Eac_Today = float(row['Eac_Today'])
            sn33.Vpv = float(row['Vpv'])
            sn33.Ipv = float(row['Ipv'])
            sn33.Ppv = float(row['Ppv'])
            sn33.Vac = float(row['Vac'])
            sn33.Iac = float(row['Iac'])
            sn33.Pac = float(row['Pac'])
            sn33.Fac = float(row['Fac'])
            sn33.Eac_Total = float(row['Eac_Total'])
            sn33.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn))
        
        if SN34.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN34 CSV data")
        for row in DictReader(open('./34_final.csv')):
            sn34 = SN34()
            if row['Time'] == "Time":
                continue
            acquired_Time = row['Time']
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn34.Time = t
            sn34.Temperature = int(row['Temperature'])
            sn34.Eac_Today = float(row['Eac_Today'])
            sn34.Vpv = float(row['Vpv'])
            sn34.Ipv = float(row['Ipv'])
            sn34.Ppv = float(row['Ppv'])
            sn34.Vac = float(row['Vac'])
            sn34.Iac = float(row['Iac'])
            sn34.Pac = float(row['Pac'])
            sn34.Fac = float(row['Fac'])
            sn34.Eac_Total = float(row['Eac_Total'])
            sn34.save()
            if row%10000 == 0:
                print(row)
            if row == 400000:
                print("50% Job complete")
        print("%s Data Parsed"%(sn34))
        
        if SN44.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN44 CSV data")
        for row in DictReader(open('./44_final.csv')):
            sn44 = SN44()
            if row['Time'] == "Time":
                continue
            acquired_Time = row['Time']
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn44.Time = t
            sn44.Temperature = int(row['Temperature'])
            sn44.Eac_Today = float(row['Eac_Today'])
            sn44.Vpv = float(row['Vpv'])
            sn44.Ipv = float(row['Ipv'])
            sn44.Ppv = float(row['Ppv'])
            sn44.Vac = float(row['Vac'])
            sn44.Iac = float(row['Iac'])
            sn44.Pac = float(row['Pac'])
            sn44.Fac = float(row['Fac'])
            sn44.Eac_Total = float(row['Eac_Total'])
            sn44.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn))
        print("60% Job complete")
        
        if SN48.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN48 CSV data")
        for row in DictReader(open('./48_final.csv')):
            sn48 = SN48()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn48.Time = row['Time']
            sn48.Temperature = int(row['Temperature'])
            sn48.Eac_Today = float(row['Eac_Today'])
            sn48.Vpv = float(row['Vpv'])
            sn48.Ipv = float(row['Ipv'])
            sn48.Ppv = float(row['Ppv'])
            sn48.Vac = float(row['Vac'])
            sn48.Iac = float(row['Iac'])
            sn48.Pac = float(row['Pac'])
            sn48.Fac = float(row['Fac'])
            sn48.Eac_Total = float(row['Eac_Total'])
            sn48.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn48))
        print("70% Job complete")
        if SN66.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN66 CSV data")
        for row in DictReader(open('./66_final.csv')):
            sn66 = SN66()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn66.Time = row['Time']
            sn66.Temperature = int(row['Temperature'])
            sn66.Eac_Today = float(row['Eac_Today'])
            sn66.Vpv = float(row['Vpv'])
            sn66.Ipv = float(row['Ipv'])
            sn66.Ppv = float(row['Ppv'])
            sn66.Vac = float(row['Vac'])
            sn66.Iac = float(row['Iac'])
            sn66.Pac = float(row['Pac'])
            sn66.Fac = float(row['Fac'])
            sn66.Eac_Total = float(row['Eac_Total'])
            sn66.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn66))
        print("80% Job complete")
        
        if SN83.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN83 CSV data")
        for row in DictReader(open('./83_final.csv')):
            sn83 = SN83()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn83.Time = row['Time']
            sn83.Temperature = int(row['Temperature'])
            sn83.Eac_Today = float(row['Eac_Today'])
            sn83.Vpv = float(row['Vpv'])
            sn83.Ipv = float(row['Ipv'])
            sn83.Ppv = float(row['Ppv'])
            sn83.Vac = float(row['Vac'])
            sn83.Iac = float(row['Iac'])
            sn83.Pac = float(row['Pac'])
            sn83.Fac = float(row['Fac'])
            sn83.Eac_Total = float(row['Eac_Total'])
            sn83.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn83))
        print("90% Job complete")
        
        if SN89.objects.exists():
            print('Pet data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Parsing the SN89 CSV data")
        for row in DictReader(open('./89_final.csv')):
            sn89 = SN89()
            if row['Time'] == "Time":
                continue
            acquired_Time = t
            t = india.localize(datetime.strptime(acquired_Time, DATETIME_FORMAT))
            sn89.Time = row['Time']
            sn89.Temperature = int(row['Temperature'])
            sn89.Eac_Today = float(row['Eac_Today'])
            sn89.Vpv = float(row['Vpv'])
            sn89.Ipv = float(row['Ipv'])
            sn89.Ppv = float(row['Ppv'])
            sn89.Vac = float(row['Vac'])
            sn89.Iac = float(row['Iac'])
            sn89.Pac = float(row['Pac'])
            sn89.Fac = float(row['Fac'])
            sn89.Eac_Total = float(row['Eac_Total'])
            sn89.save()
            if row%10000 == 0:
                print(row)
        print("%s Data Parsed"%(sn89))
        print("100% Job complete")