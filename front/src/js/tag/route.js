app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/tag/:tagText', {
        templateUrl: 'views/tag/list.html',
        controller: 'TagCtrl'
      });
});