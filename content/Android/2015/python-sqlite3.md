Title: Android Sqlite3 数据库调试

###前言

   最近做一个项目，数据逻辑比较复杂， 我建了一些表，然后写了些接口给同事调用， 关于数据逻辑在提供的接口里完成， 实现过程中需要解决这样的问题：

   1. 需要很多情形的数据，数据本身存在逻辑关系。
   2. Android中没有数据输入， 可以将数据库导入电脑直接操作，由于数据要做些换算，调试一次要换算很久。
    
###解决方式 
   可以写test或者脚本实现。这里用python脚本的方式比较方便。

###步骤：
   写python脚本

   adb pull导入db，然后写好python脚本。python有库直接支持sqlite3,使用起来很简单，下面是个示例:

	
	import sqlite3
	con = sqlite3.connect("C:/Users/dell/Desktop/db/sh-db")
	cur = con.cursor()
	cur.execute('SELECT * FROM CY')
	print (cur.fetchall())
	cur.execute('delete from CY')
	con.commit()

   使用起来是不是很简单。然后需要做得就是写好数据逻辑和日志：
   
    def generateDatetimeBefore(start,endDelta,cyLength):
	    endDatetime = start - timedelta(days = endDelta)
	    startDatetime =  endDatetime - timedelta(days = cycleLength - 1)
	    startMsg = millionsPattern%(realDateTimeStr(startDatetime),dateToMillions(startDatetime))
	    endMsg = millionsPattern%(realDateTimeStr(endDatetime),dateToMillions(endDatetime))
	    print("| %s | %s | %s | %d | %d |"%(startMsg, endMsg, membershipId, cyLength, peLength))
	    data = [dateToMillions(startDatetime), dateToMillions(endDatetime), id,cyLength,peLength]
	    cur.execute(insertSql,data)
	    con.commit()
	    return startDatetime
  我这里把日志打成markdown格式，方便观察和分析：

	  
	lastCycleStart = dateToday + timedelta(days = 1);
	lastCycleEnd = lastCyStart + timedelta(days=cyleLength-1)
	print("cyle dateToday:")
	print("	",dateToday.strftime("%Y-%m-%d"))
	print("============================")
	print("| xxx | xxx | xx | xxxx | xxxx|")
	print("|-----------|---------|----------|--------------|-------------|")
	generateCurrentPredict(lastCyStart)
	
	start = generateDatetimeBefore(lastCyStart,1,cyLength)
	start = generateDatetimeBefore(start,1,cyLength)
	start = generateDatetimeBefore(start,1,cyLength)
	start = generateDatetimeBefore(start,1,cyLength)
	
	
	print (cur.fetchall())
	con.close()

  这样根据特定逻辑生成了我想要的数据，下一步使用adb push 推入虚拟机就可以进行验证。
  文章很简单，紧紧是一个思路，即使用脚本语言来实现，往往可以节约大量的时间，而且准确率也会有所提高。