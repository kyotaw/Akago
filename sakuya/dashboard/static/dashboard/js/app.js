app = angular.module('DashboardApp', ['ui.bootstrap'])
	.config(function($httpProvider) {
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	});

