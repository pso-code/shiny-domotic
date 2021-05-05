import glob
import time
import datetime

def read_temperature_file (location) :
    # Opens the file containing the temperature
    temperature_file = open(location)
    # Reading the file...
    content = temperature_file.read()
    # Closing file after reading
    temperature_file.close()
    return content


def extract_temperature_from_content (content) :
    # We don't car about the first line, temperature is given on the second line of the file
    second_line = content.split("\n")[1]
    temperature = second_line.split("t=")[1]
    # Return the temperature in degree
    return (float(temperature) / 1000)


def save_temperature_into_file(temperature, date, file_location):
    file = open(file_location, "a")
    file.write(str(date) + "   ")
    file.write(str(temperature) + '\r\n')
    file.close()


# We retrieve all the temperature sensors plugged and detected
routes_sensors = glob.glob("/sys/bus/w1/devices/28*/w1_slave")


if len(routes_sensors) > 0 :
    c = 1
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for sensor in routes_sensors :
       	file_content = read_temperature_file(sensor)
       	temperature = extract_temperature_from_content(file_content)
	print ("[" + str(date) + "/" + sensor + "] Sensor's temperature #" + str(c) + " : " + str(temperature))
       	c += 1
#    	time.sleep(60)

else :
    print("Sensor not found. Please check your setup.")


#if len(routes_capteurs) > 0 :
#while True:
#    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    contenu_fichier = lire_fichier(routes_capteurs[0])
#    temperature = extraire_temperature(contenu_fichier)
#    sauvegarde(temperature, date, "Temperature.txt")
#    time.sleep(60)
