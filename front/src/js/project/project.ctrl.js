app.controller('ProjectCtrl', function ($scope, $rootScope, UtilsSvc, ProjectSvc, CaruselSvc, AppConst) {
    $scope.UtilsSvc=UtilsSvc;
	$scope.ProjectSvc=ProjectSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

	ProjectSvc.init();
});