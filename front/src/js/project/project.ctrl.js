app.controller('ProjectCtrl', function ($scope, $timeout, ProjectSvc, AccountSvc) {
    $scope.AccountSvc=AccountSvc;
	$scope.ProjectSvc=ProjectSvc;

	ProjectSvc.init();
});