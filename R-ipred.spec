%global packname  ipred
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.11
Release:          1%{?dist}
Summary:          Improved Predictors

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rpart R-MASS R-mlbench R-survival R-nnet R-class 

BuildRequires:    R-devel tex(latex) R-rpart R-MASS R-mlbench R-survival R-nnet R-class 

%description
Improved predictive models by indirect classification and bagging for
classification, regression and survival problems as well as resampling
based estimators of prediction error.

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
%doc %{rlibdir}/ipred/doc
%doc %{rlibdir}/ipred/html
%doc %{rlibdir}/ipred/DESCRIPTION
%{rlibdir}/ipred/libs
%{rlibdir}/ipred/help
%{rlibdir}/ipred/data
%{rlibdir}/ipred/INDEX
%{rlibdir}/ipred/NAMESPACE
%{rlibdir}/ipred/Meta
RPM build errors:
%{rlibdir}/ipred/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.11-1
- initial package for Fedora