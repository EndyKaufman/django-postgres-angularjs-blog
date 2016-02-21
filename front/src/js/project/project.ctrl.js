app.controller('ProjectCtrl', function ($scope, $timeout, ProjectSvc, AccountSvc, TagSvc) {
    $scope.AccountSvc=AccountSvc;
	$scope.ProjectSvc=ProjectSvc;
	$scope.TagSvc=TagSvc;

	ProjectSvc.init();
});