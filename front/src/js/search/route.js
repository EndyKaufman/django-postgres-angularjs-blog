app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/search/:searchText', {
        templateUrl: 'views/search/list.html',
        controller: 'SearchCtrl'
      });
});