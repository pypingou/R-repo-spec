%global packname  peperr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Parallelised Estimation of Prediction Error

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-snowfall R-survival 

BuildRequires:    R-devel tex(latex) R-snowfall R-survival 

%description
Package peperr is designed for prediction error estimation through
resampling techniques, possibly accelerated by parallel execution on a
compute cluster. Newly developed model fitting routines can be easily

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora