%global packname  sampling
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Survey Sampling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-lpSolve 
Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-MASS R-lpSolve
BuildRequires:    R-lpSolve 


%description
Functions for drawing and calibrating samples.

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
%doc %{rlibdir}/sampling/doc
%doc %{rlibdir}/sampling/DESCRIPTION
%doc %{rlibdir}/sampling/html
%{rlibdir}/sampling/data
%{rlibdir}/sampling/libs
%{rlibdir}/sampling/R
%{rlibdir}/sampling/NAMESPACE
%{rlibdir}/sampling/INDEX
%{rlibdir}/sampling/help
%{rlibdir}/sampling/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4-1
- initial package for Fedora