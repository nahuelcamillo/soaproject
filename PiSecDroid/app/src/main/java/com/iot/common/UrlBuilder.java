package com.iot.common;

public class UrlBuilder {
    private static final String BASE_URL = "http://192.168.1.75:5000/alarm/";

    public static String build(String path) {
        return BASE_URL + path;
    }
}
