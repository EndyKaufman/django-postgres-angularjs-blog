app.controller('SearchCtrl', function ($scope, SearchSvc, AuthSvc, TagSvc) {
    $scope.AuthSvc=AuthSvc;
	$scope.SearchSvc=SearchSvc;
	$scope.TagSvc=TagSvc;

	SearchSvc.init();
});