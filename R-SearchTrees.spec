%global packname  SearchTrees
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Spatial Search Trees

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package provides an implementation of the QuadTree data structure. It
uses this to implement fast k-Nearest Neighbor and Rectangular range
lookups in 2 dimenions. The primary target is high performance interactive

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
%doc %{rlibdir}/SearchTrees/html
%doc %{rlibdir}/SearchTrees/DESCRIPTION
%{rlibdir}/SearchTrees/Meta
%{rlibdir}/SearchTrees/NAMESPACE
%{rlibdir}/SearchTrees/libs
%{rlibdir}/SearchTrees/INDEX
RPM build errors:
%{rlibdir}/SearchTrees/help
%{rlibdir}/SearchTrees/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora