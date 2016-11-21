var gulp = require('gulp');

/* Bower components are hardcoded just beacause this is a small thing */

gulp.task('bower-css', function () {
    return gulp.src('./bower_components/bootstrap/dist/css/bootstrap.min.css')
        .pipe(gulp.dest('./public/css/vendor.css'))
});