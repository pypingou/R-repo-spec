%global packname  waterfall
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.9.20110424
Release:          1%{?dist}
Summary:          Waterfall Charts in R

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
This package provides both traditional and lattice graphics
implementations of waterfall charts.

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
%doc %{rlibdir}/waterfall/doc
%doc %{rlibdir}/waterfall/html
%doc %{rlibdir}/waterfall/CITATION
%doc %{rlibdir}/waterfall/DESCRIPTION
%{rlibdir}/waterfall/data
%{rlibdir}/waterfall/demo
%{rlibdir}/waterfall/R
%{rlibdir}/waterfall/help
%{rlibdir}/waterfall/LICENSE
%{rlibdir}/waterfall/Meta
%{rlibdir}/waterfall/NAMESPACE
%{rlibdir}/waterfall/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.9.20110424-1
- initial package for Fedora