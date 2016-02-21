var gulp = require('gulp');
var change = require('gulp-change');
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
var minimist = require('minimist');
var Xvfb = require('xvfb');

var gutil = require('gulp-util');

var options = minimist(process.argv.slice(2));

if (options.isvagrant==undefined)
	options.isvagrant=(process.env.USER=='vagrant')?true:false;
if (options.env==undefined)
	options.env=process.env.ENV || 'development';
if (options.host==undefined)
	options.host=process.env.HOST || 'http://127.0.0.1:5000';
if (options.static_dir==undefined)
	options.static_dir=process.env.STATIC_DIR || '../project/static/';

//source
var scss_source=['src/scss/**/*.scss'];
var less_source=['src/less/**/*.less'];

var css_source=[
    'bower_components/normalize-css/normalize.css',
    'bower_components/google-code-prettify/bin/prettify.min.css',
    'bower_components/angular-ui-tree/dist/angular-ui-tree.min.css',
    'bower_components/ng-tags-input/ng-tags-input.css',
    'bower_components/ng-tags-input/ng-tags-input.bootstrap.css',
    'bower_components/quantumui/dist/css/addon/effect-light.min.css',
    'bower_components/quantumui/dist/css/quantumui.css',
    'src/temp/css/**/*.css',
    'src/**/css/*.css',
    'src/**/*.css',];
var js_source=[
    'src/js/**/tools.js',
    'bower_components/sprintf/dist/sprintf.min.js',
    'bower_components/chance/chance.js',
    'bower_components/google-code-prettify/src/run_prettify.js',
    //'bower_components/element-queries/dist/element-queries.min.js',
    'bower_components/angular/angular.js',
    'bower_components/angular-route/angular-route.js',
    'bower_components/angular-cookies/angular-cookies.js',
    'bower_components/angular-animate/angular-animate.js',
    'bower_components/angular-resource/angular-resource.js',
    'bower_components/angular-sanitize/angular-sanitize.js',
    'bower_components/angular-ui-tree/dist/angular-ui-tree.js',
    'bower_components/quantumui/dist/js/quantumui.js',
    'bower_components/angular-strap/dist/angular-strap.js',
    'bower_components/angular-strap/dist/angular-strap.tpl.js',
    'bower_components/ng-tags-input/ng-tags-input.js',
    'bower_components/angular-bootstrap-show-errors/src/showErrors.js',
    'bower_components/showdown/src/showdown.js',
    'bower_components/showdown/src/ng-showdown.js',
    'bower_components/showdown/src/extensions/github.js',
    'bower_components/showdown/src/extensions/prettify.js',
    'bower_components/showdown/src/extensions/table.js',
    'bower_components/showdown/src/extensions/twitter.js',
    'bower_components/angular-markdown/angular.markdown.js',
    'src/js/app.init.js',
    'src/js/app.skin.js',

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

    'src/js/**/**/**/*.res.js',
    'src/js/**/**/*.res.js',
    'src/js/**/*.res.js',
    'src/js/app.res.js',

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
    '!tests/**/helpers.js',
    '!tests/helpers.js'
];
if (options['_']=='test' && options.file!==undefined)
    tests_source=[
        'tests/'+options.file,
        '!tests/**/helpers.js',
        '!tests/helpers.js'
    ];

//dest
var dest_path=options.static_dir;

// Downloads the selenium webdriver
gulp.task('webdriver_update', webdriver_update);

// Runs the selenium webdriver
gulp.task('webdriver_standalone', webdriver_standalone);

//source modifi function
function sourceChange(content) {
    return content
    .replace(new RegExp("../../bower_components/bootstrap/fonts/glyphicons-halflings-regular","ig"),
    '//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/fonts/glyphicons-halflings-regular')
    .replace(new RegExp("# sourceMappingURL=","ig"),'')
    .replace(new RegExp("../../images/scrollbar/resizer.png","ig"),'')
    .replace(new RegExp("../../images/scrollbar/arrow-up.png","ig"),'')
    .replace(new RegExp("../../images/scrollbar/arrow-down.png","ig"),'')
    .replace(new RegExp("../../images/scrollbar/arrow-left.png","ig"),'')
    .replace(new RegExp("../../images/scrollbar/arrow-right.png","ig"),'');
}

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

//build css
gulp.task('build:css', function () {
  if (options.env=='production')
	  return gulp.src(css_source)
		.pipe(sourcemaps.init({loadMaps:true}))
		.pipe(minifyCSS({compatibility: 'ie8'}))
		.pipe(change(sourceChange))
		.pipe(concat(dest_path+'app.css'))
		.pipe(sourcemaps.write({addComment: false}))
		.pipe(gulp.dest('.'));
  else
	  return gulp.src(css_source)
		.pipe(change(sourceChange))
		.pipe(concat(dest_path+'app.css'))
		.pipe(gulp.dest('.'));
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

//build js
gulp.task('build:js', function () {
  if (options.env=='production')
	  return gulp.src(js_source)
		.pipe(sourcemaps.init())
		.pipe(ngAnnotate())
		.pipe(uglify())
		.pipe(change(sourceChange))
		.pipe(concat(dest_path+'app.js'))
		.pipe(sourcemaps.write({addComment: false}))
		.pipe(gulp.dest('.'));
  else
	  return gulp.src(js_source)
		.pipe(sourcemaps.init())
		.pipe(change(sourceChange))
		.pipe(concat(dest_path+'app.js'))
		.pipe(sourcemaps.write({addComment: false}))
		.pipe(gulp.dest('.'));
});

//build
gulp.task('build', gulp.series('clear','template:js','scss','less','build:css',
              'build:js'));

// Tests
gulp.task('test', function (done) {
	if (options.isvagrant){
		var xvfb = new Xvfb({displayNum:10, timeout: 15000});
		xvfb.start(function(err, xvfbProcess) {
			var stream = gulp.src(tests_source)
			.pipe(protractor({
				configFile: "protractor.config.js",
				args: ['--baseUrl', options.host]
			}));
			stream.on('end', function() {
				xvfb.stop(function() {
					done();
				});
			});
			stream.on('error', function(err) {
				xvfb.stop(function(err) {
					done(err);
				});
			});
		});
	}else{
		var stream = gulp.src(tests_source)
		.pipe(protractor({
			configFile: "protractor.config.js",
			args: ['--baseUrl', options.host]
		}));
		stream.on('end', function() {
			done();
		});
		stream.on('error', function(err) {
			done(err);
		});
	}
});