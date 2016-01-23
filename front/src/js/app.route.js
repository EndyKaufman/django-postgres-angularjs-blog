app.config(['$resourceProvider','$httpProvider', function($resourceProvider,$httpProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])
.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/content.html',
      })
      .when('/:navId', {
        templateUrl: 'views/home/content.html'
      })
      .otherwise({
        redirectTo: '/'
      });

    $locationProvider.html5Mode({
      requireBase: false
    });
});