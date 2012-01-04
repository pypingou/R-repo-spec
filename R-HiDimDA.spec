%global packname  HiDimDA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          High Dimensional Discriminant Analysis

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-locfdr R-splines 

BuildRequires:    R-devel tex(latex) R-locfdr R-splines 

%description
Performs Linear Discriminant Analysis in High Dimensional problems based
on covariance estimators derived from low dimensional factor models.
Includes routines for classifier training, prediction, cross-validation
and variable selection.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/HiDimDA/html
%doc %{rlibdir}/HiDimDA/DESCRIPTION
%{rlibdir}/HiDimDA/NAMESPACE
%{rlibdir}/HiDimDA/Meta
%{rlibdir}/HiDimDA/libs
%{rlibdir}/HiDimDA/help
%{rlibdir}/HiDimDA/R
%{rlibdir}/HiDimDA/data
%{rlibdir}/HiDimDA/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora