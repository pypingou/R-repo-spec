%global packname  pracma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Practical Numerical Math Functions

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides R implementations of functions in numerical
analysis, with a special view on on optimization and time series routines.
Uses Matlab/Octave function names where appropriate to simplify porting.

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
%doc %{rlibdir}/pracma/html
%doc %{rlibdir}/pracma/DESCRIPTION
%doc %{rlibdir}/pracma/NEWS
%doc %{rlibdir}/pracma/doc
%{rlibdir}/pracma/demo
%{rlibdir}/pracma/R
%{rlibdir}/pracma/help
%{rlibdir}/pracma/NAMESPACE
%{rlibdir}/pracma/INDEX
RPM build errors:
%{rlibdir}/pracma/data
%{rlibdir}/pracma/Meta
%{rlibdir}/pracma/NEWS.Rd

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora