cmake_minimum_required(VERSION 3.26)
project(counting)

set(CMAKE_CXX_STANDARD 14)

add_executable(counting
        countingsort/counting.txt
        countingsort/countmare.in
        countingsort/countmare.out
        countingsort/countmic.in
        countingsort/countmic.out
        countingsort/file_name.in
        countingsort/main.cpp)
