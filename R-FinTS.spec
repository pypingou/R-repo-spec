%global packname  FinTS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Companion to Tsay (2005) Analysis of Financial Time Series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-zoo R-graphics 


BuildRequires:    R-devel tex(latex) R-zoo R-graphics



%description
R companion to Tsay (2005) Analysis of Financial Time Series, 2nd ed.
(Wiley). Includes data sets, functions and script files required to work
some of the examples.  Version 0.3-x includes R objects for all data files
used in the text and script files to recreate most of the analyses in
chapters 1-3 and 9 plus parts of chapters 4 and 11.

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
%doc %{rlibdir}/FinTS/NEWS
%doc %{rlibdir}/FinTS/html
%doc %{rlibdir}/FinTS/DESCRIPTION
%{rlibdir}/FinTS/scripts
%{rlibdir}/FinTS/data
%{rlibdir}/FinTS/R
%{rlibdir}/FinTS/NAMESPACE
%{rlibdir}/FinTS/INDEX
RPM build errors:
%{rlibdir}/FinTS/help
%{rlibdir}/FinTS/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.4-1
- initial package for Fedora