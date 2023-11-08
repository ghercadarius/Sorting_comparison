cmake_minimum_required(VERSION 3.26)
project(radix)

set(CMAKE_CXX_STANDARD 14)

add_executable(radix
        main.cpp
        rs.in
        rs_rez.txt
        rsmare.out
        rsmare.txt
        rsmic.out)
