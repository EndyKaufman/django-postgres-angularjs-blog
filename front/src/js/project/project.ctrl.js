app.controller('ProjectCtrl', function ($scope, $timeout, ProjectSvc, AuthSvc) {
    $scope.AuthSvc=AuthSvc;
	$scope.ProjectSvc=ProjectSvc;

	ProjectSvc.init();
});