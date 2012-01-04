%global packname  Hmisc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.9.0
Release:          1%{?dist}
Summary:          Harrell Miscellaneous

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.9-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival 

BuildRequires:    R-devel tex(latex) R-methods R-survival 

%description
The Hmisc library contains many functions useful for data analysis,
high-level graphics, utility operations, functions for computing sample
size and power, importing datasets, imputing missing values, advanced
table making, variable clustering, character string manipulation,
conversion of S objects to LaTeX code, and recoding variables.  Please
submit bug reports to 'http://biostat.mc.vanderbilt.edu/trac/Hmisc'.

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
%doc %{rlibdir}/Hmisc/DESCRIPTION
%doc %{rlibdir}/Hmisc/NEWS
%doc %{rlibdir}/Hmisc/html
%{rlibdir}/Hmisc/CHANGELOG
%{rlibdir}/Hmisc/libs
%{rlibdir}/Hmisc/help
%{rlibdir}/Hmisc/WISHLIST
%{rlibdir}/Hmisc/INDEX
%{rlibdir}/Hmisc/NAMESPACE
%{rlibdir}/Hmisc/THANKS
%{rlibdir}/Hmisc/todo
%{rlibdir}/Hmisc/Meta
RPM build errors:
%{rlibdir}/Hmisc/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.9.0-1
- initial package for Fedora