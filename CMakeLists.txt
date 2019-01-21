cmake_minimum_required(VERSION 2.8.12)
set(CMAKE_BUILD_TYPE Release)
project(nb_cpp)

file(GLOB_RECURSE NB_CPP_SOURCES "nb_cpp/src/*.cpp")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/eigen)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/nb_cpp/include)

set(PYBIND11_CPP_STANDARD -std=c++14)
add_subdirectory(pybind11)
pybind11_add_module(nb_cpp "${NB_CPP_SOURCES}")
