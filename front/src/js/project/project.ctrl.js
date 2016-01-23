app.controller('ProjectCtrl', function ($scope, $rootScope, ProjectSvc, CaruselSvc, AppConst) {
	$scope.ProjectSvc=ProjectSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

	ProjectSvc.init();
});