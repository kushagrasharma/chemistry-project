from math import sqrt
from time import sleep	

def isFloat(n, positive = True):
	try:
		i = float(n)
	except ValueError, TypeError:
		return False
	if i < 0 and positive:
		return False
	return True

def ke():
    print "We will now solve for an unknown in the equation KE = m * v^2.\n"
    unknown = raw_input("What is your unknown? ('ke', 'm', or 'v'):")
    if unknown not in ['ke', 'm', 'v']:
        print "Invalid input"
        return
    if unknown == 'm':
        ke = raw_input('Please enter the kinetic energy in Joules: ')
        v = raw_input('Please enter the velocity in meters per second: ')
        if not isFloat(ke) or not isFloat(v):
            print "Invalid input for either ke or v.\n"
            return
        mass = float(ke) / (float(v)**2)
        print "The mass is %.3fkg" % mass
        return
    if unknown == 'v':
        ke = raw_input('Please enter the kinetic energy in Joules: ')
        m = raw_input('Please enter the mass in kilograms: ')
        if not isFloat(ke) or not isFloat(m):
            print "Invalid input for either KE or mass.\n"
            return
        v = float(ke) / float(m)
        print "The velocity is %.3f meters per second" % mass
        return
    else:
        m = raw_input('Please enter the mass in kilograms: ')
        v = raw_input('Please enter the velocity in meters per second: ')
        if not isFloat(m) or not isFloat(v):
            print "Invalid input for either m or v.\n"
            return
        ke = float(m) * (float(v)**2)
        print "The kinetic energy is %.3f Joules" % ke
        return

def distance(start, end, value):
    x = [start, end]
    if [start, end] == ['mm', 'm']:
        return value / 1000.0
    if [start, end] == ['m', 'km']:
        return value / 1000.0
    if [start, end] == ['mm', 'km']:
        return value / 1000000.0
    if [start, end] == ['km', 'm']:
        return value * 1000
    if [start, end] == ['m', 'mm']:
        return value * 1000
    if [start, end] == ['km', 'mm']:
        return value * 1000000.0

def mass(start, end, value):
    x = [start, end]
    if [start, end] == ['mg', 'g']:
        return value / 1000.0
    if [start, end] == ['g', 'kg']:
        return value / 1000.0
    if [start, end] == ['mg', 'kg']:
        return value / 1000000.0
    if [start, end] == ['kg', 'g']:
        return value * 1000
    if [start, end] == ['g', 'mg']:
        return value * 1000
    if [start, end] == ['kg', 'mg']:
        return value * 1000000.0

def volume(start, end, value):
    x = [start, end]
    if [start, end] == ['mL', 'L']:
        return value / 1000.0
    if [start, end] == ['L', 'kL']:
        return value / 1000.0
    if [start, end] == ['mL', 'kL']:
        return value / 1000000.0
    if [start, end] == ['kL', 'L']:
        return value * 1000
    if [start, end] == ['L', 'mL']:
        return value * 1000
    if [start, end] == ['kL', 'mL']:
        return value * 1000000.0

print "This is Kushagra Sharma's AS Chemistry Research Project.\nIf at any time you need help, simply type 'help'.\n"
def help():
	print "For unit to unit calculations, type 'units'.\n"
	print "For density calculations, type 'density'.\n"
	print "For kinetic energy calculations, type 'ke'.\n"
	print "For gravitational potential energy calculations, type 'gpe'.\n"
	print "For specific heat, type 'cp'.\n"
	#print "For stochiometry, type 'sto'.\n"
	print "To quit, type 'quit'.\n"

def density():
	print "We will now be calculating density, mass, or volume!\n"
	d = None
	m = None
	v = None
	print "We will be using the equation d = m / v\n"
	print "We are only able to solve for one unknown. Please enter your unknown ('d', 'm', or 'v'):\n"
	unknown = raw_input('Unknown:')
	if unknown == 'd':
		m = raw_input("Please enter the mass in kg: ")
		v = raw_input("Please enter the volume in m^3: ")
		if isFloat(m) and isFloat(v):
			print "The density is %.3f kg / m^3" % (float(m) / float(v))
		else:
			print "Invalid input, please enter 'density' once more and try again.\n"
	elif unknown == 'm':
		d = raw_input("Please enter the density in kg / m^3: ")
		v = raw_input("Please enter the volume in m^3: ")
		if isFloat(d) and isFloat(v):
			print "The mass is %.3f kg" % (float(d) * float(v))
		else:
			print "Invalid input, please enter 'density' once more and try again.\n"
	elif unknown == 'v':
		m = raw_input("Please enter the mass in kg: ")
		d = raw_input("Please enter the density in kg / m^3: ")
		if isFloat(m) and isFloat(d):
			print "The volume is %.3f m^3" % (float(m) / float(d))
		else:
			print "Invalid input, please enter 'density' once more and try again.\n"
	else:
		print "Sorry, the unknown entered must be either 'd', 'm', or 'v'. Please enter 'density' once more and try again.\n"

def units():
	print "We will now be converting between units, precise to 3 decimal places.\n"
	print "Supported units:\nMass: mg, g, and kg.\nVolume: mL, L, and kL.\nDistance: mm, m, and km.\n"
	print "Please enter whether you would like to convert mass units ('m'), volume units ('v'), or distance units ('d').\n"
	typeOfUnit = raw_input('Which type of unit: ')
	if typeOfUnit == 'm':
		first = raw_input("What is the known unit? ('mg', 'g', or 'kg'): ")
		if first in ['mg', 'g', 'kg']:
			givjf = 'How many %ss: ' % first
			amount = raw_input(givjf)
			if isFloat(amount):
				amount = float(amount)
				second = raw_input('What unit would you like to convert to?: ')
				a = ['mg', 'g', 'kg']
				a.remove(first)
				if second in a:
					print "%.3f %s to %s = %.3f %s" % (amount, first, second, mass(first, second, amount), second)

				else:
					print "Sorry, either invalid input or same unit to same unit."
					return
		else:
			print "Sorry, invalid input."
			return
	elif typeOfUnit == 'v':
		first = raw_input("What is the known unit? ('mL', 'L', or 'kL'): ")
		if first in ['mL', 'L', 'kL']:
			givjf = 'How many %ss: ' % first
			amount = raw_input(givjf)
			if isFloat(amount):
				amount = float(amount)
				second = raw_input('What unit would you like to convert to?: ')
				a = ['mL', 'L', 'kL']
				a.remove(first)
				if second in a:
					print "%.3f %s to %s = %.3f %s" % (amount, first, second, volume(first, second, amount), second)

				else:
					print "Sorry, either invalid input or same unit to same unit."
					return
		else:
			print "Sorry, invalid input."
			return
		
	elif typeOfUnit == 'd':
		first = raw_input("What is the known unit? ('mm', 'm', or 'km'): ")
		if first in ['mm', 'm', 'km']:
			givjf = 'How many %ss: ' % first
			amount = raw_input(givjf)
			if isFloat(amount):
				amount = float(amount)
				second = raw_input('What unit would you like to convert to?: ')
				a = ['mm', 'm', 'km']
				a.remove(first)
				if second in a:
					print "%.3f %s to %s = %.3f %s" % (amount, first, second, distance(first, second, amount), second)

				else:
					print "Sorry, either invalid input or same unit to same unit."
					return
		else:
			print "Sorry, invalid input."
			return
	else:
		print "Sorry, invalid input."
		return

help()
time.sleep(2)
typeOfCalc = raw_input('Enter your command: ')
while typeOfCalc != 'quit':
	if typeOfCalc == 'units':
		units()
	elif typeOfCalc == 'density':
		density()
	elif typeOfCalc == 'ke':
		ke()
	elif typeOfCalc == 'gpe':
		gpe()
	elif typeOfCalc == 'cp':
		cp()
	#elif typeOfCalc == 'sto':
	#	sto()
	elif typeOfCalc == 'help':
		help()
	elif typeOfCalc == 'quit':
		break
	else:
		print "Sorry, that is an invalid command. Please use one of the following:\n"
		help()
	typeOfCalc = raw_input('Enter your next command: ')

print "Thank you very much for using Kushagra Sharma's AS Chemistry Research Project!"