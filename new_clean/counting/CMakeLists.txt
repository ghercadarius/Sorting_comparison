cmake_minimum_required(VERSION 3.26)
project(counting)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_EXE_LINKER_FLAGS "-static")

add_executable(counting main.cpp)
