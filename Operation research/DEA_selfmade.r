library(dplyr)
library(readxl)
library(Benchmarking)

DEA_data <- read_excel("C:/Users/parkj/Desktop/DEA.xlsx")
DEA_data <- data.frame(DEA_data)

X <- DEA_data %>% select('임차료','재고자산','X20대고객수','X30대고객수', 'X40대고객수', 'X50대고객수', 'X60대고객수')
Y <- DEA_data %>% select('매출','고객수')

crs_input_result <- dea(X,Y,RTS='crs',ORIENTATION='in')
vrs_input_result <- dea(X,Y,RTS='vrs',ORIENTATION='in')
crs_output_result <- dea(X,Y,RTS='crs',ORIENTATION='out')
vrs_output_result <- dea(X,Y,RTS='vrs',ORIENTATION='out')

benchmark_crs_input <- get.peers.lambda(crs_input_result)
benchmark_crs_output <- get.peers.lambda(crs_output_result)
benchmark_vrs_input <- get.peers.lambda(vrs_input_result)
benchmark_vrs_output <- get.peers.lambda(vrs_output_result)

slack_crs_input <- slack(X,Y,crs_input_result)
slack_crs_output <- slack(X,Y,crs_output_result)
slack_vrs_input <-slack(X,Y,vrs_input_result)
slack_vrs_output <- slack(X,Y,vrs_output_result)