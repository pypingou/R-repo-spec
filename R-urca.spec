%global packname  urca
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Unit root and cointegration tests for time series data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Unit root and cointegration tests encountered in applied econometric
analysis are implemented.

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
%doc %{rlibdir}/urca/CITATION
%doc %{rlibdir}/urca/html
%doc %{rlibdir}/urca/DESCRIPTION
%{rlibdir}/urca/book-ex
%{rlibdir}/urca/Meta
%{rlibdir}/urca/NAMESPACE
%{rlibdir}/urca/MacKinnonLicense.txt
RPM build errors:
%{rlibdir}/urca/libs
%{rlibdir}/urca/data
%{rlibdir}/urca/INDEX
%{rlibdir}/urca/Rcmdr
%{rlibdir}/urca/R
%{rlibdir}/urca/help
%{rlibdir}/urca/ChangeLog

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora