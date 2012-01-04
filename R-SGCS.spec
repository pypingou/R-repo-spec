%global packname  SGCS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Spatial Graph based Clustering Summaries for spatial point patterns

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-spatstat 

BuildRequires:    R-devel tex(latex) R-spatstat 

%description
Graph based clustering summaries for spatial point patterns. Includes
Connectivity function, Cumulative connectivity function and clustering
function, plus the triplet intensity function T.

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
%doc %{rlibdir}/SGCS/DESCRIPTION
%doc %{rlibdir}/SGCS/html
%{rlibdir}/SGCS/help
%{rlibdir}/SGCS/libs
%{rlibdir}/SGCS/Meta
%{rlibdir}/SGCS/data
%{rlibdir}/SGCS/R
%{rlibdir}/SGCS/NAMESPACE
%{rlibdir}/SGCS/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora