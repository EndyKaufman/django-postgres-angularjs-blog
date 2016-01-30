app.controller('TagCtrl', function ($scope, TagSvc, AuthSvc) {
    $scope.AuthSvc=AuthSvc;
	$scope.TagSvc=TagSvc;

	TagSvc.init();
});