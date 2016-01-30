app.config(function ($selectProvider, showErrorsConfigProvider, $carouselProvider) {
    showErrorsConfigProvider.showSuccess(true);

    var mydefaults = {
        outerWidth:'100%',
        //innerHeight:'350px',
        interval:15000,
    }
    angular.extend($carouselProvider.defaults, mydefaults)
});