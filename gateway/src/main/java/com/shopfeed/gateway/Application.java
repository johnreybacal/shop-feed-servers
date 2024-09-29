package com.shopfeed.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Bean
	public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
		return builder.routes()
				.route(r -> r.path("/users/**")
						.filters(f -> f
								.prefixPath("/api"))
						.uri("http://localhost:8001"))
				.route(r -> r.path("/shops/**")
						.filters(f -> f
								.prefixPath("/api"))
						.uri("http://localhost:8002"))
				.build();
	}
}
