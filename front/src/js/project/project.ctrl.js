app.controller('ProjectCtrl', function ($scope, $timeout, UtilsSvc, ProjectSvc, CaruselSvc, AppConst, AuthSvc) {
    $scope.UtilsSvc=UtilsSvc;
	$scope.ProjectSvc=ProjectSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;
	$scope.AuthSvc=AuthSvc;

	ProjectSvc.init();
});