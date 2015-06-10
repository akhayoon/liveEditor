angular.module('liveEditorApp', [])

	.controller('dataController', ['$scope', '$http', function($scope, $http){
		
		$scope.data = {};
		
		
		$scope.save = function(launch){
			
			$scope.data.html = window.html;
			$scope.data.css = window.css;
			$scope.data.launch = launch;
			

			$http.post('/save', {html:html, css:css, launch:launch}).
			success(function(data) {
				console.log('success!!!');
				
				if (launch == 1){
					console.log('Rendering...');
					window.open('/render', '_blank');
				}
				
			}).
			error(function(data) {
				console.log('failed' + data);
			});
		}
	}]);