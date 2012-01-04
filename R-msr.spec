%global packname  msr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Morse-Smale approximation, regression and visualization

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-class R-glmnet R-stats4 R-e1071 R-rgl R-RColorBrewer R-colorspace 


BuildRequires:    R-devel tex(latex) R-stats R-class R-glmnet R-stats4 R-e1071 R-rgl R-RColorBrewer R-colorspace



%description
Package for discrete Morse-Smale complex approximation based on kNN graph.
The Morse-Smale complex provides a decomposition of the domain. This
package provides methods to compute a hierarchical sequence of Morse-Smale
complicies and tools that exploit this domain decomposition for regression
and visualization of scalar functions.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora