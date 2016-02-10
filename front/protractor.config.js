// An example configuration file.
// https://raw.github.com/angular/protractor/master/example/conf.js
exports.config = {
    framework: 'jasmine2',
    // The address of a running selenium server.
    seleniumServerJar: './node_modules/protractor/selenium/selenium-server-standalone-2.48.2.jar', // Make use you check the version in the folder
    //seleniumAddress: 'http://localhost:4444/wd/hub',
    // Capabilities to be passed to the webdriver instance.
    capabilities: {
        'browserName': 'firefox'
        //'browserName': 'phantomjs'
        //'browserName': 'chrome'
    },
    // Options to be passed to Jasmine-node.
    jasmineNodeOpts: {
        isVerbose: true,
        showColors: true,
        includeStackTrace: true,
        defaultTimeoutInterval: 60000
    },
    onPrepare: function() {
        var jasmineReporters = require('jasmine-reporters');
        jasmine.getEnv().addReporter(new jasmineReporters.JUnitXmlReporter({
            consolidateAll: true,
            savePath: 'tests',
            filePrefix: 'result'
        }));
    }
};