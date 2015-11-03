app = angular.module('DashboardApp');

app.factory('Child', ['$http', function($http) {

	var VOCABURARY_URL = '/vocaburary/';
	var MOTIONS_URL = '/motions/';

	var constructor = function(id) {
		this.id = id;
	}

	constructor.prototype = {
		words: function(range, posList, success, error)	{
			var url = VOCABURARY_URL + this.id + '?';
			if (range != null) {
				url += ('start_month=' + range[0] + '&' + 'end_month=' + range[1]);
			}
			for (var i = 0; i < posList.length; ++i) {
				url += ('&' + posList[i]);
			}

			$http.get(
				url
			).success(function(data, status) {
				if (success) {
					success(data);
				}
			}).error(function(data) {
				if (error) {
					error(data);
				}
			});
		},

		motions: function(motionList, success, error) {
			var url = MOTIONS_URL + this.id + '?';
			for (var i = 0; i < motionList.length; ++i) {
				url += ('&' + motionList[i]);
			}
			$http.get(
				url
			).success(function(data, status) {
				if (success) {
					success(data);
				}
			}).error(function(data) {
				if (error) {
					error(data);
				}
			});
		}
	}
	
	return constructor;
}]);
