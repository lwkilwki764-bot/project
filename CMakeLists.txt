cmake_minimum_required(VERSION 3.10)
project(BaqiyatSalihatNativeEngine CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(include)

file(GLOB SOURCES
    "src/DatabaseManager.cpp"
    "src/AuthManager.cpp"
    "src/SubscriptionEngine.cpp"
    "src/ServicesManager.cpp"
)

# Build Shared Library for Android NDK & Desktop integration
add_library(baqiyat_cpp_engine SHARED ${SOURCES})

# Build Executable for testing
add_executable(baqiyat_app_test src/main.cpp ${SOURCES})

target_link_libraries(baqiyat_app_test PRIVATE)
