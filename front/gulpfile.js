var gulp = require('gulp');
var clean = require('gulp-clean');
var sass = require('gulp-sass');
var less = require('gulp-less');
var concat = require('gulp-concat');
var minifyCSS = require('gulp-minify-css');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var ngAnnotate = require('gulp-ng-annotate');
var templateCache = require('gulp-templatecache');
var path = require('path');
var child_process = require('child_process');
var q = require('q');
var protractor = require("gulp-protractor").protractor;
// Download and update the selenium driver
var webdriver_update = require('gulp-protractor').webdriver_update;
var webdriver_standalone = require('gulp-protractor').webdriver_standalone;

var spawn = require('child_process').spawn;
var gutil = require('gulp-util');

//source
var scss_source=['src/scss/**/*.scss'];
var less_source=['src/less/**/*.less'];
var css_source=[
    'bower_components/normalize-css/normalize.css',
    'bower_components/Bootflat/bootflat/css/bootflat.css',
    'bower_components/angular-ui-tree/dist/angular-ui-tree.min.css',
    'src/temp/css/**/*.css',
    'src/**/css/*.css',
    'src/**/*.css',];
var js_source=[
    'src/js/**/tools.js',
    'bower_components/element-queries/dist/element-queries.min.js',
    'bower_components/angular/angular.js',
    'bower_components/Bootflat/bootflat/js/jquery.fs.selecter.min.js',
    'bower_components/Bootflat/bootflat/js/jquery.fs.stepper.min.js',
    'bower_components/angular-route/angular-route.js',
    'bower_components/angular-cookies/angular-cookies.js',
    'bower_components/angular-animate/angular-animate.js',
    'bower_components/angular-resource/angular-resource.js',
    'bower_components/angular-ui-tree/dist/angular-ui-tree.js',
    'src/js/app.init.js',

    'src/js/**/**/**/const.js',
    'src/js/**/**/const.js',
    'src/js/**/const.js',
    'src/js/app.const.js',

    'src/js/**/**/**/route.js',
    'src/js/**/**/route.js',
    'src/js/**/route.js',
    'src/js/app.route.js',

    'src/js/**/init.js',
    'src/temp/js/templates.js',
    'src/js/**/utils.js',

    'src/js/**/**/**/*.svc.js',
    'src/js/**/**/*.svc.js',
    'src/js/**/*.svc.js',
    'src/js/app.svc.js',

    'src/js/**/**/**/*.ctrl.js',
    'src/js/**/**/*.ctrl.js',
    'src/js/**/*.ctrl.js',
    'src/js/app.ctrl.js',

    'src/js/**/*.js'];

//test
var tests_source=[
    'tests/**/*.js',
    '!tests/tools.js'
];

//dest
var dest_path='../project/static/'

//clear temp folder
gulp.task('clear', function () {
  return gulp.src('src/temp').pipe(clean())
});

//compile sass
gulp.task('scss', function () {
  return gulp.src(scss_source)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./src/temp/css'));
});

//compile less
gulp.task('less', function () {
  return gulp.src(less_source)
    .pipe(less())
    .pipe(gulp.dest('./src/temp/css'));
});

//concat dev css
gulp.task('dev:css', function () {
  return gulp.src(css_source)
    .pipe(concat(dest_path+'app.css'))
    .pipe(gulp.dest('.'))
});

//concat public css
gulp.task('public:css', function () {
  return gulp.src(css_source)
    .pipe(sourcemaps.init({loadMaps:true}))
    .pipe(minifyCSS({compatibility: 'ie8'}))
    .pipe(concat(dest_path+'app.css'))
    .pipe(sourcemaps.write({addComment: false}))
    .pipe(gulp.dest('.'))
});

//concat templates js
gulp.task('template:js', function () {
  return gulp.src('src/views/**/*.html')
    .pipe(templateCache({
      output: 'src/temp/js/templates.js',
      moduleName: 'app',
      strip: 'src/views/',
      prepend: 'views/',
    }))
    .pipe(gulp.dest('./'))
});

//concat dev js
gulp.task('dev:js', function () {
  return gulp.src(js_source)
    .pipe(sourcemaps.init())
    .pipe(concat(dest_path+'app.js'))
    .pipe(sourcemaps.write({addComment: false}))
    .pipe(gulp.dest('.'))
});

//concat public js
gulp.task('public:js', function () {
  return gulp.src(js_source)
    .pipe(sourcemaps.init())
    .pipe(concat(dest_path+'app.js'))
    .pipe(ngAnnotate())
    .pipe(uglify())
    .pipe(sourcemaps.write({addComment: false}))
    .pipe(gulp.dest('.'))
});

//build to dev
gulp.task('dev', gulp.series('clear','template:js','scss','less','dev:css',
              'dev:js'));

//build to public
gulp.task('public', gulp.series('clear','template:js','scss','less','public:css',
              'public:js'));

//run silenium test (before run tests you must  run server on http://127.0.0.1:5000)
var cwd0={
	title: 'tests',
	configFile: 'protractor.config.js',
	args: ['--baseUrl', 'http://127.0.0.1:5000', '--waits', 500]
};
var cwd1={
	title: 'selenium-server-standalone',
	shell:'java',
	params: ['-jar','node_modules/protractor/selenium/selenium-server-standalone-2.48.2.jar', '-role',  'hub']
};
var cwd2={
	title: 'phantomjs webdriver',
	shell:'node_modules/phantomjs/bin/phantomjs',
	params: ['--webdriver=8084', '--webdriver-selenium-grid-hub=http://127.0.0.1:4444']
};

// Downloads the selenium webdriver
gulp.task('webdriver_update', webdriver_update);

// Runs the selenium webdriver
gulp.task('webdriver_standalone', webdriver_standalone);

gulp.task('test', function () {
    //prepare
    var runCwd1Spawn=null;
    var runCwd2Spawn=null;
    var def=null;
    var runTestRunned=null;


    function exitHandler(options, err) {
        //Stop reading input
        process.stdin.pause();

        if (runCwd1Spawn!=null && runCwd1!=null){
            runCwd1Spawn.kill();
            runCwd1=null;
        }

        if (runCwd2Spawn!=null&& runCwd2!=null){
            runCwd2Spawn.kill();
            runCwd2=null;
        }

        if (options.cleanup) {
            console.log('clean');
        }
        if (err) console.log(err.stack);
        if (options.exit){
            console.log('exit from process');
            if (def!=null && !options.err)
                def.resolve();

            if (def!=null && options.err)
                def.reject(options.err);
            //process.exit();
        }
    }

    //do something when app is closing
    process.on('exit', exitHandler.bind(null,{cleanup:true}));

    //catches ctrl+c event
    process.on('SIGINT', exitHandler.bind(null, {exit:true}));

    //catches uncaught exceptions
    process.on('uncaughtException', exitHandler.bind(null, {exit:true}));

    var runTest=function(){
        gutil.log(gutil.colors.yellow('['+cwd0.title+'] start'));
        var stream = gulp.src(tests_source)
            .pipe(protractor({
                configFile: cwd0.configFile,
                args: cwd0.args
            }));
        stream.on('end', function() {
            gutil.log(gutil.colors.yellow('['+cwd0.title+'] completed'));
            exitHandler({exit:true});
        });

        stream.on('error', function(err) {
            gutil.log(gutil.colors.yellow('['+cwd0.title+'] error'));
            exitHandler({exit:true});
        });
        return stream;
    }

    runCwd2=function(){
        gutil.log(gutil.colors.yellow('['+cwd2.title+'] start'));
        // Finally execute your script below - here "ls -lA"
        var child = spawn(cwd2.shell, cwd2.params, {cwd: process.cwd()}),
            stdout = '',
            stderr = '',
            prevData = '';

        child.stdout.setEncoding('utf8');

        child.stdout.on('data', function (data) {
            if (prevData!=data){
                prevData = data;
                stdout += data;
                gutil.log(gutil.colors.blue(data));
            }
            if (runTestRunned==null)
                runTestRunned=runTest();
        });

        child.stderr.setEncoding('utf8');
        child.stderr.on('data', function (data) {
            if (prevData!=data){
                prevData = data;
                stderr += data;
                gutil.log(gutil.colors.red(data));
            }
            gutil.beep();
        });

        child.on('close', function(code) {
            gutil.log(gutil.colors.yellow('['+cwd2.title+'] Done with exit code'), code);
            //gutil.log(gutil.colors.yellow('['+cwd2.title+'] You access complete stdout and stderr from here'));
        });

        return child;
    }

    runCwd1=function(){
        // Finally execute your script below - here "ls -lA"
        var child = spawn(cwd1.shell, cwd1.params, {cwd: process.cwd()}),
            stdout = '',
            stderr = '',
            prevData = '';

        child.stdout.setEncoding('utf8');
        gutil.log(gutil.colors.yellow('['+cwd1.title+'] start'));

        child.stdout.on('data', function (data) {
            if (prevData!=data){
                prevData = data;
                stdout += data;
                gutil.log(gutil.colors.blue(data));
            }

            if (data.indexOf('Selenium Grid hub is up and running')!=-1 && runCwd2Spawn==null)
                runCwd2Spawn=runCwd2();
        });

        child.stderr.setEncoding('utf8');
        child.stderr.on('data', function (data) {
            if (prevData!=data){
                prevData = data;
                stderr += data;
                gutil.log(gutil.colors.red(data));
                gutil.beep();
            }

            if (data.indexOf('Selenium Grid hub is up and running')!=-1 && runCwd2Spawn==null)
                runCwd2Spawn=runCwd2();
        });

        child.on('close', function(code) {
            gutil.log(gutil.colors.yellow('['+cwd1.title+'] Done with exit code'), code);
            //gutil.log(gutil.colors.yellow('['+cwd1.title+'] You access complete stdout and stderr from here'));
        });

        return child;
    }

    //test body

    def = q.defer();

    process.stdin.resume();//so the program will not close instantly

    runCwd1Spawn=runCwd1();

    return def.promise;
});


