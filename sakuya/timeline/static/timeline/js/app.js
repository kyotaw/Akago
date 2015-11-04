app = angular.module('TimelineApp', [])
	.config(function($httpProvider) {
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.directive('audioTag', function($sce) {
	return {
    	restrict: 'A',
    	scope: { src: '=' },
    	replace: true,
    	template: '<audio class="timeline-photo-audio" ng-src="{{url}}" controls></audio>',
     	link: function (scope) {
	    	scope.$watch('src', function(newVal, oldVal) {
				if (newVal !== undefined) {
					scope.url = $sce.trustAsResourceUrl("media/" + newVal);
				}
			});
		}
	};
});
