%global packname  tensorA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.36
Release:          1%{?dist}
Summary:          Advanced tensors arithmetic with named indices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
The package provides convenience functions for advance linear algebra with
tensors and computation with datasets of tensors on a higher level
abstraction. It includes Einstein and Riemann summing conventions,
dragging, co- and contravariate indices, parallel computations on
sequences of tensors.

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
%doc %{rlibdir}/tensorA/DESCRIPTION
%doc %{rlibdir}/tensorA/html
%{rlibdir}/tensorA/INDEX
%{rlibdir}/tensorA/R
%{rlibdir}/tensorA/NAMESPACE
%{rlibdir}/tensorA/libs
%{rlibdir}/tensorA/help
%{rlibdir}/tensorA/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.36-1
- initial package for Fedora