%global packname  svcm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          2d and 3d Space-Varying Coefficient Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-splines 

BuildRequires:    R-devel tex(latex) R-Matrix R-splines 

%description
2d and 3d space-varying coefficient models are fitted to regular grid data
using either a full B-spline tensor product approach or a sequential
approximation. The latter one is computationally more efficient.
Resolution increment is enabled.

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
%doc %{rlibdir}/svcm/CITATION
%doc %{rlibdir}/svcm/html
%doc %{rlibdir}/svcm/doc
%doc %{rlibdir}/svcm/DESCRIPTION
%{rlibdir}/svcm/INDEX
%{rlibdir}/svcm/Meta
%{rlibdir}/svcm/NAMESPACE
%{rlibdir}/svcm/libs
%{rlibdir}/svcm/R
%{rlibdir}/svcm/data
%{rlibdir}/svcm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora