cmake_minimum_required(VERSION 3.26)
project(bubble)

set(CMAKE_CXX_STANDARD 14)

add_executable(bubble
        bubblesort/bubble.txt
        bubblesort/bubble_in.in
        bubblesort/bubble_out.txt
        bubblesort/countmic.in
        bubblesort/countmic.out
        bubblesort/file_name.in
        bubblesort/main.cpp)
