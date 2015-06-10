angular.module('liveEditorApp', [])

	.controller('dataController', ['$scope', '$http', '$timeout', function($scope, $http, $timeout){
		

		// Here we initialize our data variable that we're sending to our view
		$scope.data = {};
		
		/*
		 * This method is called on ng-click on one of the buttons.
		 * This is how we're going to be sending our data to our view.
	 	 * Note that we use this method to both save the data and launch our rendering.
	 	 * The reason is that we save in either case, we add the launch flag to distinguish 
	 	 * between the two
	 	 */
		$scope.save = function(launch){
			
			$scope.data.html = window.html;
			$scope.data.css = window.css;
			
			// our flag to distinguish a save or a launch
			$scope.data.launch = launch;
			
			$http.post('/save', {html:html, css:css, launch:launch}).
			success(function(data) {
				console.log('success!!!');
				
				if (launch == 1){
					console.log('Rendering...');
					window.open('/render', '_blank');
				}
				else {
					$scope.showMessage = true;

				      
			        $timeout(function() {
			          $scope.showMessage = false;
			        }, 3000);

				}
				
			}).
			error(function(data) {
				console.log('failed' + data);
			});
		}
	}]);