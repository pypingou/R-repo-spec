%global packname  zoo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.6
Release:          1%{?dist}
Summary:          S3 Infrastructure for Regular and Irregular Time Series (Z's ordered observations)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
An S3 class with methods for totally ordered indexed observations. It is
particularly aimed at irregular time series of numeric vectors/matrices
and factors. zoo's key design goals are independence of a particular
index/date/time class and consistency with ts and base R by providing
methods to extend standard generics.

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
%doc %{rlibdir}/zoo/html
%doc %{rlibdir}/zoo/DESCRIPTION
%doc %{rlibdir}/zoo/NEWS
%doc %{rlibdir}/zoo/CITATION
%doc %{rlibdir}/zoo/doc
%{rlibdir}/zoo/help
%{rlibdir}/zoo/R
%{rlibdir}/zoo/demo
%{rlibdir}/zoo/INDEX
%{rlibdir}/zoo/NAMESPACE
%{rlibdir}/zoo/Meta
%{rlibdir}/zoo/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.6-1
- initial package for Fedora