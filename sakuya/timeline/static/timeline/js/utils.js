app = angular.module('TimelineApp');

app.factory('Util', [function() {
	var utils = {};

	utils.stopEvent = function(e) {
		e.preventDefault();
		e.stopPropagation();
		return false;	
	}
	
	return utils;
}]);

