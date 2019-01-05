# mlbPlayers = read.table(file=file.choose(),
#                         header=T, sep=" ",
#                         na.strings="`",
#                         stringsAsFactors=F)
# 
# # Grab just RBIs and Avg for each player
# # playerData is known as a data frame (Table of Data)
# # We get the stats we want by passing that list in a vector
# playerData = mlbPlayers[,c("RBI","AVG")]
# 
# # Create the file
# png(file="player_rbi_avg.png")
# 
# # Create the plot
# plot(x=playerData$RBI, y=playerData$AVG,
#      xlab="RBI", ylab="AVG", main="RBIs and Average")
# 
# # Create the file
# dev.off()
# myNum=c(1:20)
# mnumber=myNum[myNum+2 > 10]
# mnumber
# print(myNum)
# myNum_2=c(1,2,3,4,5,6)
# print(myNum_2)
# evens=seq(from=myNum_2[1],to=myNum_2[length(myNum_2)],by=2)
# print(evens)
# evens_2=rep(myNum_2,times=2,each=3)
# print(evens_2)
# if(evens_2[2]<2){
#   print("No")
# }else if(evens_2[2]==1){
#   print("yes")
# }
# str1="go to lahore"
# sub(pattern="go",replacement=1,x=str1)
# a=strsplit(x=str1," ")
# # a
# custData=data.frame(name=c("Ali","Mohtashim","Taqir"),
#                     age=c("12","13","14"),
#                     stringsAsFactors = F)
# matrix_try=matrix(data=c(1,2,3,4,5,6),nrow=3,ncol=2,byrow=T)
# matrix_try[1,1:2]
# array1=array(data=1:8,dim=c(2,2,3))
# array1
# fib=function(n){
#   if(n==0||n==1){
#     return(1)
#   }
#   else{
#     result=fib(n-1)+fib(n-2)
#     return(result)
#   }
# }
# fib(7)
exp=function(exp){
  function(x){
    return (x^exp)
  }
}
# num_list=(1:10)
# dbllist=(function(x)(x*2))(num_list)
# dbllist
# list_function=list(add_3=function(x){
#   
#                   x+3},
#                   add_4=function(x){x+4
#                     })
# list_function$add_3(3)
# divide=function(num1,num2){
#   tryCatch(
#     num1/num2,
#     error=function(e){
#       if(is.character(num1)||is.character(num2)){
#         print("Error Value")
#       }
#     }
#   )
# }
# divide(2,3)
# x1=c(1,2,3,4,5,6,7)
# y1=c(1,2,3,4,5,6,7)
# plot(x1,y1,type="l",xlab="x-axis",ylab = "y-axis",main = "graph",col="red")
# abline(h=c(2,4),col='blue')
# segments(x0=c(2,4),y0=c(2,2),x1=c(2,4),y1=c(4,4),col = "black")
# arrows(x0=3.1,y0=1.24,x1=5.5,y1=5.1)
# text(x=1.1,y=2.1,labels = "Graph")
# plot(faithful)
# eruptions=with(faithful,faithful[eruptions>4,])
# points(eruptions,col="red",pch="3")
# print(faithful[eruptions>0,])
# library(plotrix)
# company_name=c("Nike","Addidas","Reebok","Puma")
# company_share=c(15,40,30,15)
# png(file="plot_Pie_char.png")
# colors=rainbow(length(company_name))
# barplot(company_share,names.arg =company_name,main="Company Market Share",
#         xlab = "company name",
#         ylab = "company share",col = colors)
# legend("topright",c("Nike","Addidas","Reebok","Puma"),fill =colors,cex = 0.8)
# dev.off()
# mlbPlayers = read.table(file=file.choose(),
#                             header=T, sep=" ",
#                             na.strings="`",
#                             stringsAsFactors=F)
# playersData=mlbPlayers[,c("RBI","AVG")]
# png("regression_model_mlbplayer.png")
# plot(playersData$AVG,playersData$RBI,main = "Regression Model",xlab = "AVG",
#      ylab="RBI",abline(lm(playersData$RBI~playersData$AVG)))
# dev.off()
#################################################\
