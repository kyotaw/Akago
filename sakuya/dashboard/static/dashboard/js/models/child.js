app = angular.module('DashboardApp');

app.factory('Child', ['$http', function($http) {

	var VOCABURARY_URL = '/vocaburary/';
	
	var constructor = function(id) {
		this.id = id;
	}

	constructor.prototype = {
		words: function(success, error)	{
			$http.get(
				VOCABURARY_URL + this.id
			).success(function(data) {
				if (success) {
					success(data);
				}
			}).error(function(data) {
				if (error) {
					error(data);
				}
			});
		},
	}
	
	return constructor;
}]);
