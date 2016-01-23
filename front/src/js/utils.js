app.filter('unsafe', function($sce) { return $sce.trustAsHtml; })
.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });
                element[0].blur();
                event.preventDefault();
            }
        });
    };
})
.factory('UtilsSvc', function ($http, $q, $timeout) {
    var service={};

    service.capitalise = function (string) {
      if (string.length>0)
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
      else
        return '';
    }
    //Numbers 1, 3 и 5.
    //Sample: decOfNum(5, ['секунда', 'секунды', 'секунд'])
    service.declOfNum = function(number, titles)
    {
        cases = [2, 0, 1, 1, 1, 2];
        return titles[ (number%100>4 && number%100<20)? 2 : cases[(number%10<5)?number%10:5] ];
    }
    return service;
});
