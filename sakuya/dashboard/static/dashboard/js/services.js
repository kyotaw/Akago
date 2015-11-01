app = angular.module('TimelineApp');

app.service('FileUpload', ['$http', function($http) {
	this.upload = function(file, url, success, error) {
		var fd = new FormData();
		fd.append('file', file);
		$http.post(
			url,
			fd,
			{
				transformRequest: angular.identity,
				headers: {'Content-Type': undefined}
			}
		).success(function(data){
			success(data);
		}).error(function(){
			error();
		})
	}
}]);
