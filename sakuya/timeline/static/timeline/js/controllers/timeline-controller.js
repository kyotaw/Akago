app = angular.module('TimelineApp');

app.controller('TimelineController', ['$scope', '$timeout', '$location', 'Photo', 'Util', function($scope, $timeout, $location, Photo, Util) {
	$scope.photo = new Photo();

	var imageArea = angular.element(document.getElementById('user-drop-image'));
	imageArea.on('dragenter', Util.stopEvent);
	imageArea.on('dragover', Util.stopEvent);
	
	$scope.frameHeight = '150px';
	$scope.catchImage = function(e) {
		var imageFile = null;
		var files = e.originalEvent.dataTransfer.files;
		for (var i = 0; i < files.length; ++i) {
			if (files[i].type.indexOf('image') == 0) {
				imageFile = files[i];
				break
			}
		}
		if (imageFile == null) {
			return;
		}
		imageArea.off('drop');
		
		$scope.photo.loadImage(imageFile, function(){
			$timeout(function(){});
		});
		return Util.stopEvent(e);
	}
	imageArea.on('drop', $scope.catchImage);

	$scope.showPhotoEditor = function() {
		$('#timeline-photo-editor').show('fast');
	}

	$scope.hidePhotoEditor = function() {
		$('#timeline-photo-editor').hide('fast');
	}

	$scope.save = function() {
		if ($scope.photo.imageFile == null) {
			return;
		}
		content = $('#photo-comment-input>.photo-comment-placeholder');
		$scope.photo.comment = content.val();
		$scope.photo.save(function(data){
			location.href = '/timeline';
		});
	}

	$scope.delete = function(id) {
		return;
	}
}]);
