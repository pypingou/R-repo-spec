%global packname  gpclib
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          General Polygon Clipping Library for R

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
General polygon clipping routines for R based on Alan Murta's C library

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
%doc %{rlibdir}/gpclib/DESCRIPTION
%doc %{rlibdir}/gpclib/html
%{rlibdir}/gpclib/README
%{rlibdir}/gpclib/libs
%{rlibdir}/gpclib/LICENSE
%{rlibdir}/gpclib/Meta
%{rlibdir}/gpclib/NAMESPACE
%{rlibdir}/gpclib/R
%{rlibdir}/gpclib/INDEX
%{rlibdir}/gpclib/poly-ex
%{rlibdir}/gpclib/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.1-1
- initial package for Fedora