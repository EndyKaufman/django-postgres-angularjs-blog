app.controller('ProjectCtrl', function ($scope, $rootScope, UtilsSvc, ProjectSvc, CaruselSvc, AppConst) {
    $scope.UtilsSvc=UtilsSvc;
	$scope.ProjectSvc=ProjectSvc;
	$scope.CaruselSvc=CaruselSvc;
	$scope.AppConst=AppConst;

    $rootScope.$on('project.delete',function(item){
        ProjectSvc.goList();
	});

	ProjectSvc.init();
});