cmake_minimum_required(VERSION 3.26)
project(radix)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_EXE_LINKER_FLAGS "-static")

add_executable(radix main.cpp)
