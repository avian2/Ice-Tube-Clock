import datetime

# edit these

# First measurement

#ref_1 = datetime.datetime(2013, 9, 13, 23, 26, 0)
#clk_1 = datetime.datetime(2013, 9, 13, 23, 26, 0)

#ref_2 = datetime.datetime(2013, 9, 16, 20, 18, 30)
#clk_2 = datetime.datetime(2013, 9, 16, 20, 18, 21)

#ref_2 = datetime.datetime(2013, 9, 17, 18, 37, 00)
#clk_2 = datetime.datetime(2013, 9, 17, 18, 36, 48)

# Second measurement

ref_1 = clk_1 = datetime.datetime(2013, 9, 17, 19, 42, 0)

ref_2 = datetime.datetime(2013, 9, 21, 19, 45, 50)
clk_2 = datetime.datetime(2013, 9, 21, 19, 45, 51)

def total_seconds(td):
	return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

ref_d = total_seconds(ref_2 - ref_1)
clk_d = total_seconds(clk_2 - clk_1)

print "Measurement time: %.1f h" % (ref_d/3600.0)
print "Difference      : %d s" % (clk_d-ref_d)
print

k = float(clk_d - ref_d)/clk_d
N = 256

print "current error"
print "    %.1f ppm" % (k*1e6)
print "    %.2f s/h" % (k*3600)
print "    %.1f counter digits" % (k*3600*N)
print

e = 1./clk_d

print "max error after calibratio"
print "    %.1f ppm" % (e*1e6)
print "    %.2f s/month" % (e*3600*24*30)
print "    %.1f counter digits" % (e*3600*N)
