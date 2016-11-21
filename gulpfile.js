var gulp = require('gulp');
var rename = require('gulp-rename');
var concat = require('gulp-concat');

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