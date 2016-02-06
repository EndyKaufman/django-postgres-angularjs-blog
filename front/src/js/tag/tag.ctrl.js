app.controller('TagCtrl', function ($scope, TagSvc, AccountSvc) {
    $scope.AccountSvc=AccountSvc;
	$scope.TagSvc=TagSvc;

	TagSvc.init();
});