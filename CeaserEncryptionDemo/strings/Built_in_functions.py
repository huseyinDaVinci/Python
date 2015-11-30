__author__ = 'barin.huseyin'



#help  function get the object and return the help related to it.
#ord()  gets a charachter and returns its ASCII CODE
S="Hello"
help(S.replace)
print ord("\n")

#-------------------------------------------------------------
#PATTERN MATCHING (SO SWEET)
import re

#pattern matching  first we are creating our pattern then search it in the whole string  should "import re"  as a built in function


nbaPlayers="Kobe is the         mamba**Jordan is the goat**Oscar is the mr triple man***mamba"

#we are looking for line should include "is the"  end space and mamba at the end

deneme="Hello Python world"

denemePattern="Hello[ \t]*(.*)world"

print re.match(denemePattern,deneme).group(1)

pattern="(.*)is the[ \t]*(.*)mamba"
who=re.match(pattern,nbaPlayers)  #returns null if the pattern is not found

print(who.group(1))
print who.groups()


directoryPath="/home/makaveli/documents"
directoryPattern="/(.*)/(.*)/(.*)"

print re.match(directoryPath,directoryPath).group(0)
#-------------------------------------------------------------