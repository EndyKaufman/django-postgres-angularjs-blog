app.controller('SearchCtrl', function ($scope, SearchSvc, AccountSvc, TagSvc) {
    $scope.AccountSvc=AccountSvc;
	$scope.SearchSvc=SearchSvc;
	$scope.TagSvc=TagSvc;

	SearchSvc.init();
});