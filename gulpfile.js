var gulp = require('gulp');
var rename = require('gulp-rename');
var concat = require('gulp-concat');
var cleanCss = require('gulp-clean-css');
var uglify = require('gulp-uglify');

/* Bower components are hardcoded just beacause this is a small thing */


gulp.task('bower-css', function () {
    return gulp.src('./bower_components/bootstrap/dist/css/bootstrap.min.css')
        .pipe(rename('vendor.css'))
        .pipe(gulp.dest('./public/css/'))
});

gulp.task('bower-fonts', function () {
    return gulp.src('./bower_components/bootstrap/fonts/*')
        .pipe(gulp.dest('./public/fonts/'))
});

gulp.task('bower-js', function () {
    return gulp.src(['./bower_components/jquery/dist/jquery.min.js',
        './bower_components/bootstrap/dist/js/bootstrap.min.js',
        './bower_components/jQuery.dotdotdot/src/jquery.dotdotdot.min.js'])
        .pipe(concat('vendor.js', {newLine: ';'}))
        .pipe(gulp.dest('./public/js/'))
});

gulp.task('app-css', function () {
    return gulp.src('./resources/css/*.css')
        .pipe(concat('app.css'))
        .pipe(cleanCss())
        .pipe(gulp.dest('./public/css/'))
});

gulp.task('app-js', function () {
    return gulp.src('./resources/js/*.js')
        .pipe(concat('app.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./public/js/'))
});

gulp.task('watch', function () {
    gulp.watch('./bower_components/**/*', ['bower-all']);
    gulp.watch('./resources/**/*', ['app-all']);
});

gulp.task('bower-all', ['bower-css', 'bower-fonts', 'bower-js']);
gulp.task('app-all', ['app-css', 'app-js']);
gulp.task('build', ['bower-all', 'app-all']);
gulp.task('default', ['build', 'watch']);